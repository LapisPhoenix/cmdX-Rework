from utils.tools import OperatingSystem, Settings, progress_bar
from terminal.terminal import Terminal

settings = Settings("settings.json")    # Setup the json file
os = OperatingSystem()                  # Setup the os

div = settings.load_data()["profile"]["div"]
term = Terminal()
cmd = term.Commands()

commands = {
    'cls': os.cls,
    'clear': os.cls,
    'hello': cmd.hello,
    'help': cmd.help,
    '?': cmd.help,
    'exit': cmd.close,
    'close': cmd.close
}

def main():
    print("\nBETA TEST!\nRun: ? or help")
    while True:
        line = input(f"{os.current_working_directory() + div} ")

        if line in commands:
            commands[line.casefold()]()
        else:
            print("Invalid Command!")

main()