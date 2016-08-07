"""
A collection of generally useful utility functions and classes.
"""

__all__ = [
    'get_program_name',
    'get_default_logfile_name',
    'answer_yes_no',
    'contains_any',
    'Enum',
    'Color',
    ]

import abc
import os
import pwd
import sys
import tempfile


def get_program_name():
    """Return the name of the program suitable for printing."""

    return os.path.basename(sys.argv[0])

def get_default_logfile_name():
    """Return a default temporty logfile name."""

    prg_name = os.path.splitext(get_program_name())[0]
    user_name = pwd.getpwuid(os.getuid())[0]

    return os.path.join(tempfile.gettempdir(),  '%s-%s.log' % (prg_name, user_name))

def answer_yes_no(prompt):
    """Outputs a prompt and returns true if input is is 'y' or 'Y'."""

    prompt += ' (y/N)? '
    ans = raw_input(prompt)
    if ans and ans[0].upper() == 'Y':
        return True
    else:
        return False

def contains_any(str, contains):
    """Return True if 'str' contains any characters in 'contains'."""

    return True in [c in str for c in set(contains)]


class Enum(object):
    """Base clase for enumerations."""
    string_repr = []

    def __init__(self):
        pass

    @classmethod
    def str(cls, val):
        """Return a human-readable string of an enum."""
        if not cls.string_repr:
            return None
        if val in cls.string_repr:
            return cls.string_repr[val]
        else:
            return None

    @classmethod
    def val(cls, name):
        """Lookup up name and return corresponding enum."""
        if not cls.string_repr:
            return None
        for key in cls.string_repr:
            if cls.string_repr[key] == name:
                return key
        return None

class TextColor(object):
    """Handles coloring text."""

    __metaclass__ = abc.ABCMeta

    _COLOR_ASCSII_OFFSET = 29

    FOREGROUND = 0
    BLACK = 1
    RED = 2
    GREEN = 3
    YELLOW = 4

    def __new__(cls, *args, **kw):
        raise StaticClassError("%s is a static class and cannot be initiated."
                                % cls)

    @classmethod
    def color_text(cls, color, s):
        if color == cls.FOREGROUND:
            return  chr(0x1b) + "[0m" + s + chr(0x1b) + "[0m"
        else:
            return chr(0x1b) + "[" + str(color + cls._COLOR_ASCSII_OFFSET) + "m" + s + chr(0x1b) + "[0m"

