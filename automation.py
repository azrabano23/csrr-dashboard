#!/usr/bin/env python3

import schedule
import time
import subprocess

# Function to run the dashboard
def run_dashboard():
    subprocess.Popen(["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "app:app"])  # Adjust workers and bind to suitable IP and port

# Schedule the dashboard to start every 30th of the month at midnight
schedule.every().month.at("00:00").do(run_dashboard)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)
