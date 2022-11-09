"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730570002"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, new_point: Point) -> int:
        """Calculates the distance bewteen previous point and new point."""
        distance: float = sqrt(((self.x - new_point.x)**2) + ((self.y - new_point.y)**2))
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
 
    def tick(self) -> None:
        """For every tick the position of the cell is updated."""
        self.location = self.location.add(self.direction)

        if self.is_infected() is True:
            self.sickness += 1

        if self.sickness >= constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable() is True:
            return "gray"
        if self.is_immune() is True:
            return "purple"
        if self.is_infected() is True:
            return "orange"

    def contract_disease(self) -> None:
        """Assigns INFECTED to sickness."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Returns true if sickness is equal to VULNERABLE and false if else."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Returns true if sickness is equal to INFECTED and false if else."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def contact_with(self, cell: Point) -> None:
        """When a non-infected cell comes into contact with an infected cell it becomes infected."""
        if self.is_infected() and cell.is_vulnerable() is True:
            self.contract_disease()
            cell.contract_disease()

        elif self.is_vulnerable() and cell.is_infected() is True:
            self.contract_disease()
            cell.contract_disease()

        elif self.is_immune() and cell.is_infected() is True:
            self.immunize()
        
        elif self.is_infected() and cell.is_immune() is True:
            cell.immunize()
        
        elif self.is_immune() and cell.is_vulnerable() is True:
            self.immunize()
        
        elif self.is_vulnerable() and cell.is_immune() is True:
            cell.immunize()

    def immunize(self) -> None:
        """Assigns IMMUNE to the sickness attribute."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Return True if a Cell's sickness is immune."""
        if self.sickness == constants.IMMUNE:
            return True


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, starting_infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        index: int = 0
        index: int = 0
        index1: int = 0

        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)

            if starting_infected >= cells or starting_infected <= 0:
                raise ValueError("Some number of the Cell objects must begin infected.")
            
            elif immune >= cells or immune < 0:
                raise ValueError("Some number of the Cell objects must begin infected.")

            elif immune + starting_infected > cells:
                raise ValueError("Some number of the Cell objects must begin infected.")

            elif index < starting_infected:
                cell.contract_disease()
                index += 1

            elif index1 < immune:
                cell.immunize()
                index1 += 1

            self.population.append(cell)

    def check_contacts(self) -> None:
        """Compares the distance between every two cell's location."""
        index: int = 0
        index1: int = 0

        for index in range(len(self.population)):
            for index1 in range(index + 1, len(self.population)):
                cell_one: Cell = self.population[index]
                cell_two: Cell = self.population[index1]

                if cell_one.location.distance(cell_two.location) < constants.CELL_RADIUS:
                    cell_one.contact_with(cell_two)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_WIDTH - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0

        if cell.location.x > constants.MAX_Y:
            cell.location.x = constants.MAX_Y
            cell.direction.x *= -1.0
        
        if cell.location.x < constants.MIN_Y:
            cell.location.x = constants.MIN_Y
            cell.direction.x *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        index: int = 0
        index1: int = 0

        for index1 in range(len(self.population)):
            if Cell.is_immune(self.population[index1]) is True:
                index += 1
            if Cell.is_vulnerable(self.population[index1]) is True:
                index += 1
        
        while index < len(self.population):
            return False
        else:
            return True