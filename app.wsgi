import sys
import os
from app import app as application

# Add the project directory to the Python path
sys.path.insert(0, '/home/aapo/appAll')

# Set up logging
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
