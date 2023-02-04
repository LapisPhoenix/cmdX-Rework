import os
import CONSTANTS

from utils.tools import System

sys = System()


class Terminal:
    # Terminal class is to keep things neat

    def __init__(self):
        pass

    class Commands:
        def __init__(self):
            pass

        def help(self):
            """The basic help command!"""
            msg = f"""\n\nhelp
{'-' * 50}\n"""

            for callable in Terminal.Commands.__dict__:  # Check if the current method is callable
                if callable.startswith("__"):   # If it is, make sure it isnt a magic method
                    continue

                function = Terminal.Commands.__dict__[callable] # Grab the function/method
                doc = function.__doc__  # Grab the documentation
                if doc: # If there is documentation, add the docs
                    msg += f"{callable.lower()}{' ' * (CONSTANTS.spacer - len(callable))}{doc}\n"
                else:   # If not, then add boilerplate message
                    msg += f"{callable.lower()}{' '* (CONSTANTS.spacer - len(callable))}No documentation given.\n"

            print(msg)

        def hello(self):
            """Says hello to you."""
            try:
                print(f"Hi {os.getlogin()}!")
            except Exception:   # Sometimes messes up, usually with remote terminals
                print(f"Hi User!")

        def test(self):
            """Test Command for text output"""
            print("Test")

        def cls(self):
            """Clears the console"""
            os.system("cls" if sys._system == "Windows" else "clear")   # Windows and linux use different clear commands

        def cat(self, file = None):
            """Reads a file."""
            
            if file is None:
                print("You must specify an file to read!")
                return

            try:
                with open(file, "r") as f:
                    return print(f.read())
            except FileNotFoundError:
                print(f"'{file}' not found!")

        def ls(self, directory=None):
            """List all items inside a directory."""
            msg = ""

            if directory is None:
                directory = os.getcwd()

            items = os.listdir(directory)   # Grab everything within a directory
            max_item_len = max([len(item) for item in items])
            for item in items:  # For every item inside the directory
                item_path = os.path.join(directory, item)   # Get the item path
                # Add 40 spaces minus the length of the file name, this is so everything lines up nicely
                msg += f"{item}{' ' * (max_item_len - len(item) + CONSTANTS.spacer)}"

                try:
                    if os.path.isfile(item_path):   # If its an file
                        item_size = os.path.getsize(item_path)  # Get the size of the file
                        if item_size > 0:   # If the size of the file is more than 0
                            msg += f"{item_size}b\n"
                        else:
                            msg += "N/A\n"  # If not then just add N/A
                    elif os.path.isdir(item_path):  # Same but if its a directory
                        msg += "N/A\n"  # If its a directory dont try to grab the size
                except Exception:
                    msg += "N/A\n"  # If for whatever reason both fail then just N/A so it doesnt crash

            print(msg)
        
        def say(self, message):
            """Says back whatever you want"""
            print(message)

        def run(self, directory = None):
            """Runs/Opens a program."""

            if directory is None:
                print("You need to specify a file to run/open!")
                return

            try:
                os.startfile(directory)     # Run the file, if its not an binary open it with the preffered app.
            except FileNotFoundError:
                print(f"{directory} not found!")
            except OSError as e:
                print(e)
            
        def findstr(self, file = None, string = None):
            """Find a string of text inside a file"""
            if file == None:
                print("You need to specify a file!")
                return
            if string == None:
                print("You need to specify a string!")
                return
            
            try:
                with open(file, 'r') as f:
                    lines = f.readlines()   # Read all the files inside the file
            except FileNotFoundError:
                print(f"Could not find '{file}'")
                return
            except FileExistsError:
                print(f"'{file}' does not exist!")
                return
            
            for i, line in enumerate(lines):
                if string in line:
                    print(f"Line {i + 1}: {line.strip()}")  # If the string is found inside one of those lines, get the line number and line text
                    return

            print(f"'{string}' not found inside '{file}'")  # Finally, if it doesnt find the string then just say we didnt find it

        def cd(self, directory: str = None):  #type: ignore
            """Change the current directory"""
            if directory is None:
                print(os.getcwd())
                return
            if directory == "..":   # Go back easily
                os.chdir(os.getcwd().rsplit("\\", 1)[0])
            else:
                os.chdir(directory)

        def close(self):
            """Exits the console."""
            exit(0)
