import sys
import os

# Isse frontend folder ke andar ki files ek dusre ko pehchan lengi
sys.path.append(os.path.join(os.path.dirname(__file__), 'frontend'))

from frontend.app import *

