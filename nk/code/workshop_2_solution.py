"""
this porgram update helps to the user improving new activities verification 
and  a new structured menu, where the clients and the new users could move
as they want  with any requirements that they have.

Author: Nicolas Avendaño Barajas
"""



# Engine class definition
class Engine:
    """This class represents the behavior of a vehicle engine."""
    # Constructor and methods

# Other class definitions
class Vehicle:
    """
    This class represents the behavior of an abstract class
    to define vehicles.
    """
    # Constructor and methods

class Car(Vehicle):
    """This class is a concrete definition for a Car."""
    # Additional methods for Car

class Truck(Vehicle):
    """This class is a concrete definition for a truck."""
    # Additional methods for Truck

class Yatch(Vehicle):
    """This class is a concrete definition for a yatch."""
    # Additional methods for Yatch

class Motorcycle(Vehicle):
    """This class is a concrete definition for a motorcycle."""
    # Additional methods for Motorcycle

# Menu-related functions and variables
MESSAGE = """
    Please, choose an option:
    1. Create an engine
    2. Create a car
    3. Create a truck
    4. Create a yatch
    5. Create a motorcycle
    6. Show all engines
    7. Show all vehicles
    8. Exit
"""

enginees = {}
vehicles = []

# Authentication credentials
USERNAME = "user"
PASSWORD = "password"

# Menu function
def menu():
    """Display menu and handle user input."""
    while True:
        print(MESSAGE)
        option = input("Select an option: ")
        try:
            option = int(option)
            if option in MENU_OPTIONS:
                MENU_OPTIONS[option]()
            else:
                print("Invalid option. Please choose again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Authenticate user
def authenticate():
    """Authenticate user."""
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == USERNAME and password == PASSWORD:
        print("Authentication successful. Welcome!")
        menu()
    else:
        print("Invalid credentials. Access denied.")

# Main entry point
if __name__ == "__main__":
    authenticate()
