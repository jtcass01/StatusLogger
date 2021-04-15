"""Logger.py: Python Logger tested on both Linux and Windows operating systems that provides file logging and console log
   operations."""
from __future__ import annotations

__author__ = "Jacob Taylor Casasdy"
__email__ = "jacobtaylorcassady@outlook.com"

from datetime import datetime
from enum import Enum
from platform import system
from typing import Union
from os import getcwd, makedirs
from os.path import sep, abspath


class Logger(object):
    """"""
    def __init__(self, file_log: bool = True, log_location: Union[str, None] = None, use_timestamp: bool = True) -> None:
        """Constructor.
        Args:
            file_log (bool, optional): [description]. Defaults to True.
            log_location (Union[str, None], optional): [description]. Defaults to None."""
        self.file_log: bool = file_log
        self.use_timestamp: bool = use_timestamp

        if file_log:
            if log_location is None:
                self.log_location = getcwd() + sep + ".." + sep + "Logs" + sep + datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')[:-3] + ".log"
            else:
                self.log_location = log_location

            # Ensure log directory exists
            makedirs(abspath(self.log_location), exist_ok=True)

    def log(self, message: str, message_type: MESSAGE_TYPE) -> None:
        """Logs a message to a file and to the console given a status.
        Args:
            message (str): [description]
            status (LogStatus): [description]"""
        if self.file_log:
            Logger.log_to_file(log_file_location=self.log_location,
                               message=message, message_type=message_type,
                               use_timestamp=self.use_timestamp)
        Logger.console_log(message=message, message_type=message_type, use_timestamp=self.use_timestamp)

    @staticmethod
    def log_to_file(log_file_location: str, message: str, message_type: MESSAGE_TYPE, use_timestamp: bool = True) -> None:
        """[summary]
        Args:
            log_file_location (str): [description]
            message (str): [description]
            status (LogStatus): [description]"""
        with open(log_file_location, 'a+') as log_file:
            if use_timestamp:
                log_file.write('{}: [{}] {}\n'.format(datetime.now().strftime('%H:%M:%S.%f')[:-3],
                                                      message_type,
                                                      message))
            else:
                log_file.write(message + '\n')

    def verbose_console_log(verbose: bool, message: str, message_type: MESSAGE_TYPE, use_timestamp: bool = True) -> None:
        """[summary]
        Args:
            verbose (bool): [description]
            message (str): [description]
            message_type (MESSAGE_TYPE): [description]"""
        if verbose:
            Logger.console_log(message=message, message_type=message_type, use_timestamp=use_timestamp)

    @staticmethod
    def console_log(message: str, message_type: MESSAGE_TYPE, use_timestamp: bool = True) -> None:
        """[summary]
        Args:
            message (str): [description]
            status (LogStatus): [description]"""
        system_platform = system()

        if use_timestamp:
            time_string = datetime.now().strftime('%H:%M:%S.%f')[:-3] + ":"
        else:
            time_string = ""

        if system_platform == 'Windows':
            from printy import printy

            try:
                if message_type == Logger.MESSAGE_TYPE.SUCCESS:
                    printy(time_string + '[n]' + ' ' + message + '@', predefined='w')  # SUCCESS
                elif message_type == Logger.MESSAGE_TYPE.FAIL:
                    printy(time_string + '[r]' + ' ' + message + '@', predefined='w')  # FAIL
                elif message_type == Logger.MESSAGE_TYPE.STATUS:
                    printy(time_string + '[c]' + ' ' + message + '@', predefined='w')
                elif message_type == Logger.MESSAGE_TYPE.MINOR_FAIL:
                    printy(time_string + '[r>]' + ' ' + message + '@', predefined='w') # Minor Fail
                elif message_type == Logger.MESSAGE_TYPE.WARNING:
                    printy(time_string + '[y]' + ' ' + message + '@', predefined='w')
                else:
                    printy(time_string + '[r]' + ' ' + 'INVALID LOG FORMAT. Please check int value.' + '@', predefined='w')
            except:
                printy(time_string + '[r]' + ' ' + 'Failed to understand log call. Wrong format when calling log.' + '@', predefined='w') # wrong format

        else:
            from colorama import Fore

            if message_type == Logger.MESSAGE_TYPE.SUCCESS:
                print(Fore.WHITE + time_string + Fore.GREEN + ' ' + message)  #SUCCESS
            elif message_type == Logger.MESSAGE_TYPE.FAIL:
                print(Fore.WHITE + time_string + Fore.RED + ' ' + message)   #FAIL
            elif message_type == Logger.MESSAGE_TYPE.STATUS:
                print(Fore.WHITE + time_string + Fore.CYAN + ' ' + message)
            elif message_type == Logger.MESSAGE_TYPE.MINOR_FAIL:
                print(Fore.WHITE + time_string + Fore.LIGHTRED_EX + ' ' + message)  #Minor fail
            elif message_type == Logger.MESSAGE_TYPE.WARNING:
                print(Fore.WHITE + time_string + Fore.YELLOW + ' ' + message)
            else:
                print(Fore.WHITE + time_string + Fore.RED + ' INVALID LOG FORMAT. Please check int value.')

    class MESSAGE_TYPE(Enum):
        """[summary]"""
        SUCCESS = "SUCCESS"
        FAIL = "FAIL"
        STATUS = "STATUS"
        MINOR_FAIL = "MINOR_FAIL"
        WARNING = "WARNING"

        def __str__(self) -> str:
            return self.value

if __name__ == "__main__":
    for message_type in list(Logger.MESSAGE_TYPE):
        Logger.console_log(message="[" + str(message_type) + "] Hello World.", message_type=message_type)
