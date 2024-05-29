import random

def generate_random_name():
    """
    Generate a random name from predefined lists of first and last names.

    Returns:
    str: A randomly generated full name.
    """
    first_names = [
        "James", "Mary", "John", "Patricia", "Robert", "Jennifer",
        "Michael", "Linda", "William", "Elizabeth", "David", "Barbara",
        "Richard", "Susan", "Joseph", "Jessica", "Charles", "Sarah",
        "Thomas", "Karen"
    ]

    last_names = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
        "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez",
        "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore",
        "Jackson", "Martin"
    ]

    # Randomly select a first name and a last name
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    return f"{first_name} {last_name}"

if __name__ == "__main__":
    # Generate a random name and print it
    random_name = generate_random_name()
    print(f"Generated random name: {random_name}")
