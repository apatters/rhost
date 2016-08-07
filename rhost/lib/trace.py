"""
Python program tracing.

Some code leveraged from:

   http://code.activestate.com/recipes/145297-grabbing-the-current-line-\
   number-easily/
"""

__author__ = 'Andrew Patterson'
__copyright__ = 'Copyright (C) 2016 Hewlett-Packard Corp'
__credits__ = ['Andrew Patterson']
__license__ = 'Proprietary'
__version__ = '1.4'
__maintainer__ = 'Andrew Patterson'
__email__ = 'andrew.patterson@hp.com'

__all__ = ['TRACE', 'HEADER']

import sys
import os
import inspect

HEADER = '[***] '

def TRACE(*msgs):
    """Print out header, file name and number and, optionally, one or
    more messages along with a header to stdout.  The header is used
    to make the the message standout amongst other program output."""

    lineno = inspect.currentframe().f_back.f_lineno
    sourcefile = inspect.currentframe().f_back.f_code.co_filename
    sourcefile = os.path.basename(sourcefile)
    print('%s%s:%d' % (HEADER, sourcefile, lineno)),
    if msgs:
        print(' -- '),
        for msg in msgs:
            print msg,
        print
    else:
        print
    sys.stdout.flush()