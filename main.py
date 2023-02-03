# See LICENSE.

import os
from utils.tools import Settings
from terminal.terminal import Terminal

settings = Settings("settings.json")

div = settings.load_data().get("profile", {}).get("div")
term = Terminal()
cmd = term.Commands()

commands = {
    'cls': cmd.cls,
    'clear': cmd.cls,
    'hello': cmd.hello,
    'hi': cmd.hello,
    'help': cmd.help,
    '?': cmd.help,
    'exit': cmd.close,
    'close': cmd.close,
    'test': cmd.test,
    'cat': cmd.cat,
    'read': cmd.cat,
    'ls': cmd.ls,
    'dir': cmd.ls
}

def main():
    print(f"cmdX V2.0\nCopyright (c) 2023 Lapis Pheonix")
    while True:
        line = input(f"{os.getcwd() + div} ").casefold() #type: ignore
        parts = line.split(" ", maxsplit=1)
        command = commands.get(parts[0])
        arguments = parts[1] if len(parts) > 1 else None
        if command:
            if arguments:
                command(arguments)
            else:
                command()
        else:
            print("Invalid Command!\nTry: help")

if __name__ == "__main__":
    main()