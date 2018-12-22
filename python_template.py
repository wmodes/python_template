# -*- coding: utf-8 -*-
"""python_template - a basic python script template

This basic python script template demonstrates:

    * header docstring (this!)
    * header block metadata
    * using logging module
    * using a config json config config file
    * basic class template 
    * standard entry point using __name__ and main() function

"""

__author__ = "Wes Modes"
__copyright__ = "Copyright 2018, Wes Modes"
__credits__ = [""]
__license__ = "MIT"
__version__ = "0.9"
__maintainer__ = "Wes Modes"
__email__ = "wmodes@gmail.com"
__status__ = "Development"

# used for printing debug and other info
import logging
# used to read our config in JSON format
import json
# useful for pretty printing data
import pprint

# setup
pp = pprint.PrettyPrinter(indent=4)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s %(message)s',
)

#constants
config_filename = './config.json'

# read config
with open(config_filename, 'r') as f:
    config = json.load(f)

logging.info("Received configuration:\n" + json.dumps(config, indent=4))

# set logging level based on config
#   options: CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
logging.getLogger().setLevel(getattr(logging, config.log_level.upper()))

### Classes

class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg


### Functions

def your_function_here():
    logging.debug("Running your_function_here")


def main():
    """main function entry point"""
    logging.info("Starting")
    # calls to more functions

# this calls main() if the script is run, 
#   but not if it is imported as a module
if __name__ == '__main__':
    main()