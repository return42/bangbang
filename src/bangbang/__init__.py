# pylint: disable=missing-module-docstring

import logging
from . import __pkginfo__

logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__   = __pkginfo__.version
__author__    = __pkginfo__.authors[0]
__license__   = __pkginfo__.license
__copyright__ = __pkginfo__.copyright
