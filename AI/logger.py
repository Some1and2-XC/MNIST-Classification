#!/usr/bin/env python3
"""

Sets up Logger

Author	: @some1and2
Date	: 3/29/2023

"""

import sys
import logging

logger = logging.getLogger("main") # Sets up the main logger
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(FuncName)s - %(message)s")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)