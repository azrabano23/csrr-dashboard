#!/bin/bash
# Setup cron job for monthly CSRR automation

echo "Setting up cron job for monthly CSRR automation..."

# Create a cron job that runs on the 30th of each month at 9:00 AM
CRON_JOB="0 9 30 * * cd /Users/azrabano/csrr-dashboard && python monthly_automation.py"

# Add to crontab
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo "Cron job added successfully!"
echo "Monthly automation will run on the 30th of each month at 9:00 AM"
echo ""
echo "To view current cron jobs: crontab -l"
echo "To remove the cron job: crontab -e (then delete the line)"
echo ""
echo "Note: Make sure the dashboard is running for the automation to work properly."
