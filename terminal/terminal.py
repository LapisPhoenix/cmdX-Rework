from utils.tools import OperatingSystem, progress_bar

os = OperatingSystem()

#TODO: Add a loop in the help command to automate the help command
#TODO: Transfer all commands into Commands class (E.G: os.cls)

class Terminal:
    def __init__(self):
        pass

    class Commands:
        def __init__(self):
            pass

        def hello(self):
            """Says hello to you."""
            print(f"Hi {os.username()}!")
        
        def help(self):
            print("Loading Help...")
            i = 0
            msg = f"""\n\nhelp
{'-' * 50}\n"""

            for callable in Terminal.Commands.__dict__:
                i += 1
                progress_bar(i, Terminal.Commands.__dict__.__len__())
                
                msg.join(f"{callable.lower()} {' ' * (50 - len(callable))}{callable.__doc__}")
            
            print(msg)

        def close(self):
            """Exits the console."""
            exit(0)