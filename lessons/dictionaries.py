"""Demonstrations of dictionary capabilities."""

# Declaring the type of a dictionary
from ast import Break

schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key value pair from a dictionary
# By its key
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 100

print(schools)

# Demonstration of dictionary literals


# Empty dictionary literal
schools = {} # Same as dict()
print(schools)

# Alternatively, intitialize key-value pairs
schools = {"UNC": 19400, "Dookie": 6717, "NCSU": 26150}
#print(schools["UNCC"])

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

print("")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")