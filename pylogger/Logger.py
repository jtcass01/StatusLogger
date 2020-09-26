from datetime import datetime
from enum import IntEnum
from platform import system
from typing import Union
from os import getcwd, makedirs
from os.path import sep, abspath


class Logger(object):
    """

    """
    def __init__(self, file_log: bool = True, log_location: Union[str, None] = None) -> None:
        """
        Constructor.

        :param file_log:
        :param log_location:
        """
        self.file_log = file_log

        if file_log:
            if log_location is None:
                self.log_location = getcwd() + sep + ".." + sep + "Logs" + sep + datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')[:-3] + ".log"
            else:
                self.log_location = log_location

            # Ensure log directory exists
            makedirs(abspath(self.log_location), exist_ok=True)

    def log(self, message: str, status: IntEnum) -> None:
        """

        :param message:
        :param status:
        :return:
        """
        if self.file_log:
            Logger.log_to_file(self.log_location, message, status)
        Logger.console_log(message, status)

    @staticmethod
    def log_to_file(log_file_location: str, message: str, status: IntEnum) -> None:
        """

        :param log_file_location:
        :param message:
        :param status:
        :return:
        """
        with open(log_file_location, 'a+') as log_file:
            log_file.write(datetime.now().strftime('%H:%M:%S.%f')[:-3] + ' - [{}]'.format(str(status)) + ' - ' + message + '\n')

    @staticmethod
    def console_log(message: str, status: IntEnum) -> None:
        """

        :param message:
        :param status:
        :return:
        """
        system_platform = system()

        if system_platform == 'Windows':
            from printy import printy

            if status == Logger.LogStatus.SUCCESS:
                printy((datetime.now().strftime('%H:%M:%S.%f')[:-3]) + '[n]' + ' ' + message + '@', predefined='w')  # SUCCESS
            elif status == Logger.LogStatus.FAIL:
                printy((datetime.now().strftime('%H:%M:%S.%f')[:-3]) + '[r]' + ' ' + message + '@', predefined='w')  # FAIL
            elif status == Logger.LogStatus.COMMUNICATION:
                printy((datetime.now().strftime('%H:%M:%S.%f')[:-3]) + '[c]' + ' ' + message + '@', predefined='w')
            elif status == Logger.LogStatus.MINOR_FAIL:
                printy((datetime.now().strftime('%H:%M:%S.%f')[:-3]) + '[r>]' + ' ' + message + '@', predefined='w') # Minor Fail
            elif status == Logger.LogStatus.EMPHASIS:
                printy((datetime.now().strftime('%H:%M:%S.%f')[:-3]) + '[y]' + ' ' + message + '@', predefined='w')
            else:
                printy((datetime.now().strftime('%H:%M:%S.%f')[:-3]) + '[r]' + ' ' + 'INVALID LOG FORMAT. Please check int value.' + '@', predefined='w')
        else:
            from colorama import Fore

            if status == Logger.LogStatus.SUCCESS:
                print(Fore.WHITE + datetime.now().strftime('%H:%M:%S.%f')[:-3] + Fore.GREEN + ' ' + message)  #SUCCESS
            elif status == Logger.LogStatus.FAIL:
                print(Fore.WHITE + datetime.now().strftime('%H:%M:%S.%f')[:-3] + Fore.RED + ' ' + message)   #FAIL
            elif status == Logger.LogStatus.COMMUNICATION:
                print(Fore.WHITE + datetime.now().strftime('%H:%M:%S.%f')[:-3] + Fore.CYAN + ' ' + message)
            elif status == Logger.LogStatus.MINOR_FAIL:
                print(Fore.WHITE + datetime.now().strftime('%H:%M:%S.%f')[:-3] + Fore.LIGHTRED_EX + ' ' + message)  #Minor fail
            elif status == Logger.LogStatus.EMPHASIS:
                print(Fore.WHITE + datetime.now().strftime('%H:%M:%S.%f')[:-3] + Fore.YELLOW + ' ' + message)
            else:
                print(Fore.WHITE + datetime.now().strftime('%H:%M:%S.%f')[:-3] + Fore.RED + ' INVALID LOG FORMAT. Please check int value.')

    class LogStatus(IntEnum):
        """

        """
        SUCCESS = 1
        FAIL = 2
        COMMUNICATION = 3
        MINOR_FAIL = 4
        EMPHASIS = 5


if __name__ == "__main__":
    Logger.console_log(message="Hello World.", status=Logger.LogStatus.SUCCESS)
