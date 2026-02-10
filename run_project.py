import subprocess
import os
import sys
import webbrowser
import time
import signal

# --- CONFIGURATION ---
BACKEND_PORT = "8000"
FRONTEND_PORT = "8080" # Using 8080 to avoid conflict with Django
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, 'backend')
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')

def run_servers():
    print(f"🚀 Starting Project...")
    
    # 1. Start Django Backend
    # We use sys.executable to ensure we use the same python interpreter (venv friendly)
    print(f"--> Starting Django on port {BACKEND_PORT}")
    backend_process = subprocess.Popen(
        [sys.executable, 'manage.py', 'runserver', BACKEND_PORT],
        cwd=BACKEND_DIR,
        # stdout=subprocess.DEVNULL, # Uncomment these lines if you want to hide Django logs
        # stderr=subprocess.DEVNULL
    )

    # 2. Start Frontend HTTP Server
    print(f"--> Starting Frontend on port {FRONTEND_PORT}")
    frontend_process = subprocess.Popen(
        [sys.executable, '-m', 'http.server', FRONTEND_PORT],
        cwd=FRONTEND_DIR
    )

    # 3. Open Browser
    # Give servers a moment to spin up
    time.sleep(2)
    url = f"http://localhost:{FRONTEND_PORT}"
    print(f"--> Opening {url}")
    webbrowser.open(url)

    print("\n✅ Servers are running. Press Ctrl+C to stop.\n")

    try:
        # Keep the script running to monitor processes
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Stopping servers...")
        # Terminate processes nicely
        backend_process.terminate()
        frontend_process.terminate()
        print("Done.")

if __name__ == '__main__':
    run_servers()