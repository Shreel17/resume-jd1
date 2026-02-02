import sys
import os

# Isse frontend folder ke andar ki files ek dusre ko pehchan lengi
sys.path.append(os.path.join(os.path.dirname(__file__), 'frontend'))

from frontend.app import *

# Session state initialize karein
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Agar user login nahi hai toh login page dikhao
if not st.session_state['authenticated']:
    # Yahan aapka login logic aayega
    # Login hone par st.session_state['authenticated'] = True set karein
    main_ui() 
else:
    # Login ke baad kya dikhana hai wo yahan likhein
    from frontend.dashboard import show_dashboard
    show_dashboard()
