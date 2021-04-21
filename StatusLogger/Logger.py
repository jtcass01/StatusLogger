"""Logger.py: Python Logger tested on both Linux and Windows operating systems that provides file logging and console log
   operations."""
from __future__ import annotations

__author__ = "Jacob Taylor Casasdy"
__email__ = "jacobtaylorcassady@outlook.com"

# Built-in Modules
from datetime import datetime
from platform import system
from typing import Union, List
from os import getcwd, makedirs, remove
from os.path import join, isfile
from threading import Thread, Lock
from time import sleep

# StatusLogger Modules
from StatusLogger import Message

class Logger(Thread):
    """"""
    def __init__(self, name: str, file_log: bool = False, log_directory: Union[str, None] = None, verbose: bool = False, 
                 rate: float = 1, overwrite: bool = False) -> None:
        """Constructor.
        Args:
            file_log (bool, optional): [description]. Defaults to True.
            log_location (Union[str, None], optional): [description]. Defaults to None."""
        Thread.__init__(self, name=name + "_log_thread")

        if file_log:
            if log_directory is None:
                log_directory = join(getcwd(), "logs")

            makedirs(log_directory, exist_ok=True)

            self.log_file_location = join(log_directory, name + ".log")

            if isfile(self.log_file_location) and overwrite:
                remove(self.log_file_location)

        self.file_log: bool = file_log
        self.verbose = verbose
        self.rate = rate
        self.queue: List[Message] = []
        self.lock = Lock()
        self.running = False

    def run(self) -> None:
        """[summary]"""
        self.running = True

        Logger.verbose_console_log(verbose=self.verbose,
                                    message="{} {} is running.".format(type(self), self.name),
                                    message_type=Message.MESSAGE_TYPE.STATUS)

        while self.running:
            self.lock.acquire()
            if len(self.queue) > 0:
                message_ready_to_log: Message = self.queue.pop(0)
                print(message_ready_to_log.message)
                self.lock.release()

                if self.file_log:
                    Logger.log_to_file(log_file_location=self.log_file_location,
                                       message=message_ready_to_log.message,
                                       message_type=message_ready_to_log.message_type,
                                       use_timestamp=message_ready_to_log.use_timestamp)

                if self.verbose:
                    Logger.verbose_console_log(verbose=self.verbose,
                                               message=message_ready_to_log.message,
                                               message_type=message_ready_to_log.message_type,
                                               use_timestamp=message_ready_to_log.use_timestamp)
            else:
                print("queue empty")
                self.lock.release()
                sleep(1/self.rate)
                continue

    def stop(self):
        """Waits for the queue to empty, then sets the running flag to false and console logs the status."""
        while len(self.queue) > 0:
            sleep(1/self.rate)
        self.running = False
        Logger.verbose_console_log(verbose=self.verbose,
                                   message="{} {} has stopped.".format(type(self), self.name),
                                   message_type=Message.MESSAGE_TYPE.STATUS)

    def _add_message_to_queue(self, message: Message):
        """[summary]

        Args:
            message (Message): [description]"""
        self.lock.acquire()
        self.queue.append(message)
        self.lock.release()
        print(self.queue)

    def log(self, message: str, message_type: Message.MESSAGE_TYPE, use_timestamp: bool) -> None:
        """Logs a message to a file and to the console given a status.
        Args:
            message (str): [description]
            status (LogStatus): [description]"""
        self._add_message_to_queue(message=Message(message=message, message_type=message_type, use_timestamp=use_timestamp))

    @staticmethod
    def log_to_file(log_file_location: str, message: str, message_type: Message.MESSAGE_TYPE, use_timestamp: bool = True) -> None:
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

    @staticmethod
    def verbose_console_log(verbose: bool, message: str, message_type: Message.MESSAGE_TYPE, use_timestamp: bool = True) -> None:
        """[summary]
        Args:
            verbose (bool): [description]
            message (str): [description]
            message_type (MESSAGE_TYPE): [description]"""
        if verbose:
            Logger.console_log(message=message, message_type=message_type, use_timestamp=use_timestamp)

    @staticmethod
    def console_log(message: str, message_type: Message.MESSAGE_TYPE, use_timestamp: bool = True) -> None:
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
                if message_type == Message.MESSAGE_TYPE.SUCCESS:
                    printy(time_string + '[n]' + ' ' + message + '@', predefined='w')  # SUCCESS
                elif message_type == Message.MESSAGE_TYPE.FAIL:
                    printy(time_string + '[r]' + ' ' + message + '@', predefined='w')  # FAIL
                elif message_type == Message.MESSAGE_TYPE.STATUS:
                    printy(time_string + '[c]' + ' ' + message + '@', predefined='w')
                elif message_type == Message.MESSAGE_TYPE.MINOR_FAIL:
                    printy(time_string + '[r>]' + ' ' + message + '@', predefined='w') # Minor Fail
                elif message_type == Message.MESSAGE_TYPE.WARNING:
                    printy(time_string + '[y]' + ' ' + message + '@', predefined='w')
                else:
                    printy(time_string + '[r]' + ' ' + 'INVALID LOG FORMAT. Please check int value.' + '@', predefined='w')
            except:
                printy(time_string + '[r]' + ' ' + 'Failed to understand log call. Wrong format when calling log.' + '@', predefined='w') # wrong format

        else:
            from colorama import Fore

            if message_type == Message.MESSAGE_TYPE.SUCCESS:
                print(Fore.WHITE + time_string + Fore.GREEN + ' ' + message)  #SUCCESS
            elif message_type == Message.MESSAGE_TYPE.FAIL:
                print(Fore.WHITE + time_string + Fore.RED + ' ' + message)   #FAIL
            elif message_type == Message.MESSAGE_TYPE.STATUS:
                print(Fore.WHITE + time_string + Fore.CYAN + ' ' + message)
            elif message_type == Message.MESSAGE_TYPE.MINOR_FAIL:
                print(Fore.WHITE + time_string + Fore.LIGHTRED_EX + ' ' + message)  #Minor fail
            elif message_type == Message.MESSAGE_TYPE.WARNING:
                print(Fore.WHITE + time_string + Fore.YELLOW + ' ' + message)
            else:
                print(Fore.WHITE + time_string + Fore.RED + ' INVALID LOG FORMAT. Please check int value.')


if __name__ == "__main__":
    test_logger = Logger(name="test", file_log=True, verbose=True, rate=10, overwrite=True)
    test_logger_2 = Logger(name="test2", file_log=True, verbose=True, rate=10)
    test_logger.start()
    test_logger_2.start()

    for message_type in list(Message.MESSAGE_TYPE):
        test_logger.log(message="Hello World. 1", message_type=message_type, use_timestamp=True)
        test_logger_2.log(message="Hello World. 2", message_type=message_type, use_timestamp=True)

    test_logger.stop()
    test_logger_2.stop()
