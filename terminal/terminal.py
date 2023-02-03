from utils.tools import System, progress_bar
import os
import CONSTANTS

sys = System()


class Terminal:
    def __init__(self):
        pass

    class Commands:
        def __init__(self):
            pass

        def __iter__(self):
            for command in self.__dir__:  # type:ignore
                yield command

        def help(self):
            """The basic help command!"""
            msg = f"""\n\nhelp
{'-' * 50}\n"""

            for callable in Terminal.Commands.__dict__:
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
            print(f"Hi {os.getlogin()}!")

        def test(self):
            """Test Command for text output"""
            print("Test")

        def cls(self):
            """Clears the console"""
            os.system("cls" if sys._system == "Windows" else "clear")

        def cat(self, file):
            """Reads a file."""
            with open(file, "r") as f:
                return print(f.read())

        def ls(self, directory=None):
            """List all items inside a directory."""
            msg = ""

            if directory is None:
                directory = os.getcwd()

            items = os.listdir(directory)
            max_item_len = max([len(item) for item in items])
            for item in items:
                item_path = os.path.join(directory, item)
                msg += f"{item}{' ' * (max_item_len - len(item) + CONSTANTS.spacer)}"

                try:
                    if os.path.isfile(item_path):
                        item_size = os.path.getsize(item_path)
                        if item_size > 0:
                            msg += f"{item_size}b\n"
                        else:
                            msg += "N/A\n"
                    elif os.path.isdir(item_path):
                        msg += "N/A\n"
                except Exception:
                    msg += "N/A\n"

            print(msg)

        def close(self):
            """Exits the console."""
            exit(0)
