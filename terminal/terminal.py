from utils.tools import OperatingSystem, progress_bar
import CONSTANTS

os = OperatingSystem()

#TODO: Transfer all commands into Commands class (E.G: os.cls)

class Terminal:
    def __init__(self):
        pass

    class Commands:
        def __init__(self):
            pass

        def __iter__(self):
            for command in self.__dir__:
                yield command

        def help(self):
            """The basic help command!"""
            print("Loading Help...")
            i = 0
            msg = f"""\n\nhelp
{'-' * 50}\n"""

            for callable in Terminal.Commands.__dict__:
                i += 1
                progress_bar(i, Terminal.Commands.__dict__.__len__())
                
                if callable.startswith("__"):
                    continue
                
                function = Terminal.Commands.__dict__[callable]
                doc = function.__doc__
                if doc:
                    msg += f"{callable.lower()}{' ' * (CONSTANTS.spacer - len(callable))}{doc}\n"
                else:
                    msg += f"{callable.lower()}{' '* (CONSTANTS.spacer - len(callable))}No documentation given.\n"
            
            print(msg)

        def hello(self):
            """Says hello to you."""
            print(f"Hi {os.username()}!")
        
        def test(self):
            """Test Command for text output"""
            print("Test")
        
        def cls(self):
            """Clears the console"""
            os.do_sys("cls" if os._system == "Windows" else "clear")

        def close(self):
            """Exits the console."""
            exit(0)