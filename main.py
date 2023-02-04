# See LICENSE.

import os
from utils.tools import Settings
from terminal.terminal import Terminal

settings = Settings("settings.json")

div = settings.load_data().get("profile", {}).get("div")
term = Terminal()
cmd = term.Commands()

# Extra commands that run the same thing are aliases
# Aliases are not listed inside the help command
# But can always be used

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
    'dir': cmd.ls,
    'run': cmd.run,
    'call': cmd.run,
    'exec': cmd.run,
    'echo': cmd.say,
    'back': cmd.say,
    'say': cmd.say,
    'findstr': cmd.findstr,
    'fstr': cmd.findstr,
    'cd': cmd.cd,
    'move': cmd.cd
}

def main():
    print(f"cmdX V2.0\nCopyright (c) 2023 Lapis Pheonix")
    while True:
        line = input(str(os.getcwd()) + str(div))   # User input
        arguments = []
        current_argument = ""
        in_quotes = False
        for char in line:
            if char == " " and not in_quotes:   # Check if its just a space
                if current_argument:    # Check if the current arg is True/not empty
                    arguments.append(current_argument)
                    current_argument = ""
            # Check if its inside quotes
            elif char == '"':
                in_quotes = not in_quotes
            elif char == "'":
                in_quotes = not in_quotes
            else:
                current_argument += char
        # Check again
        if current_argument:
            arguments.append(current_argument)
        # Check the command in lowercase while keeping the original arguments
        command = commands.get(arguments[0].lower())
        # Get the original Arguments with case kept
        # We do this extra check lower case check of the command
        # Because we need to check if the command is valid
        # While keeping the original case of the arugments
        # This also adds the plus side of having commands be case-insensitive
        arguments = arguments[1:]
        if command:
            command(*arguments)
        else:
            print("Invalid Command!\nTry: help")

if __name__ == "__main__":
    main()