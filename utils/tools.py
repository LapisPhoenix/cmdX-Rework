import os
import platform

from json import dump, load, JSONDecodeError
from os import stat
from os.path import exists
from utils.errors import FileNotJson, FailedToLoad

from colorama import Fore, init

class Settings:
    """Handles the settings file"""
    def __init__(self, settings_file: str):
        self._file = settings_file
        self.check_file()
    
    @property
    def file(self):
        return self._file


    def file_format(self):
        """Basic Settings Format"""
        return {
            "profile": {
                "div": ">>",
                "username": "",
            }
        }


    def write_file(self):
        """Write to the settings file the basic format ( file_format() )"""
        with open(self.file, "w") as f:
            dump(self.file_format(), f, indent=4)
    

    def check_file(self):
        """Checks the settings file for:\n
            existing\n
            ends with ".json"\n
            if its empty
        """
        if not exists(self.file):
            self.write_file()
            return

        if not self.file.endswith(".json"):
            raise FileNotJson(f"{self.file} is not a json file!")

        if stat(self.file).st_size == 0:
            self.write_file()
            return
    
    def load_data(self):
        """Tries to load the settings file"""
        self.check_file()
        try:
            with open(self.file, "r") as f:
                file_contents = load(f)
        except JSONDecodeError:
            raise FailedToLoad(f"Couldn't load {self.file}")
        else:
            return dict(file_contents)


class OperatingSystem:
    def __init__(self):
        self._system = platform.system()
    

    def cls(self) -> None:
        """Clears the console"""
        return os.system("cls" if self._system == "Windows" else "clear")
    

    def current_working_directory(self) -> str:
        return str(os.getcwd())
    
    def username(self) -> str:
        return os.getlogin()

def progress_bar(progress: int, total: float):
    """
    E.G: progress_bar(progress=i + 1, total=30)
    """
    init()
    percent = 100 * (progress / float(total))
    bar = f'{Fore.GREEN}█' * int(percent) + f'{Fore.RESET}░' * (100 - int(percent))
    print(f'{Fore.RESET}| {bar} {Fore.RESET}| {percent:.2f}%', end="\r")