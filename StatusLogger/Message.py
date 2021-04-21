"""Message.py: """
from __future__ import annotations

__author__ = "Jacob Taylor Casasdy"
__email__ = "jacobtaylorcassady@outlook.com"

# Built-in Modules
from enum import Enum


class Message(object):
    def __init__(self, message: str, message_type: MESSAGE_TYPE, use_timestamp: bool = True):
        self.message = message
        self.message_type = message_type
        self.use_timestamp = use_timestamp

    class MESSAGE_TYPE(Enum):
        """[summary]"""
        SUCCESS = "SUCCESS"
        FAIL = "FAIL"
        STATUS = "STATUS"
        MINOR_FAIL = "MINOR_FAIL"
        WARNING = "WARNING"

        def __str__(self) -> str:
            return self.value


