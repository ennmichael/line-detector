#!/usr/bin/env python3

import os

os.environ['PYSDL2_DLL_PATH'] = os.getcwd()

from .managed import *
from .eventloop import *
from .utils import *
from . import events
from . import colors
