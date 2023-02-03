from utils.tools import OperatingSystem, Settings, progress_bar
from terminal.terminal import Terminal
from colorama import Fore, init

settings = Settings("settings.json")
os = OperatingSystem()

div = settings.load_data().get("profile", {}).get("div", ">>")
term = Terminal()
cmd = term.Commands()

commands = {
    'cls': cmd.cls,
    'clear': cmd.cls,
    'hello': cmd.hello,
    'help': cmd.help,
    '?': cmd.help,
    'exit': cmd.close,
    'close': cmd.close,
    'test': cmd.test
}

def main():
    init()
    print(f"cmdX V2.0\nCopyright (c) 2023 Lapis Pheonix")
    while True:
        line = input(f"{os.current_working_directory() + div} ").casefold()
        command = commands.get(line)
        if command:
            command()
        else:
            print("Invalid Command!\nTry: help")

if __name__ == "__main__":
    main()