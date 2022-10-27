

def love(subject: str):
    """Given a subject as a parameter, returns a loving string."""
    return f"I love you {subject}!!!"

print(love("Cam"))

def spread_love(to: str, n: int) -> str:
    """"Generates a str repeating a loving message n times"""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i += 1
        return love_note

print(spread_love("Cam", 5))
