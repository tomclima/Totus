import subprocess
import time

script_to_run = "backend/api.py"

while True:
    # Run the script
    process = subprocess.run(["python3", script_to_run])
    
    # Optionally add a small delay before restarting
    time.sleep(1)
