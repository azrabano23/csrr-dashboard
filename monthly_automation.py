#!/usr/bin/env python3
"""
Monthly Automation Script for CSRR Faculty Tracker
Runs monthly searches and sends email notifications automatically
"""

import schedule
import time
import sys
import os
import logging
from datetime import datetime, timedelta
from pathlib import Path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Add the parent directory to path to import modules
sys.path.append('/Users/azrabano')
sys.path.append('/Users/azrabano/csrr-dashboard')

from csrr_faculty_tracker import CSRRFacultyTracker
from app import app, db, EmailSubscriber, SearchRun, User

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/Users/azrabano/csrr-dashboard/automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class MonthlyAutomation:
    def __init__(self):
        self.tracker = CSRRFacultyTracker()
        
    def run_monthly_search(self):
        """Run the monthly search and send emails"""
        logger.info("Starting monthly automated search...")
        
        try:
            with app.app_context():
                # Create a new search run record
                search_run = SearchRun(user_id=1)  # Use admin user
                db.session.add(search_run)
                db.session.commit()
                
                # Run the actual search
                results_count = self.tracker.run_monthly_search()
                
                # Update search run record
                search_run.completed_at = datetime.utcnow()
                search_run.status = 'completed'
                search_run.results_count = results_count
                
                # Find the most recent report file
                reports_dir = Path(self.tracker.config['output']['reports_folder'])
                if reports_dir.exists():
                    report_files = list(reports_dir.glob('*.xlsx'))
                    if report_files:
                        latest_report = max(report_files, key=lambda f: f.stat().st_mtime)
                        search_run.report_path = str(latest_report)
                        
                        # Send emails to all subscribers
                        self.send_monthly_emails(latest_report)
                
                db.session.commit()
                logger.info(f"Monthly search completed. Found {results_count} results.")
                
        except Exception as e:
            logger.error(f"Monthly search failed: {e}")
            with app.app_context():
                search_run = SearchRun.query.filter_by(status='running').first()
                if search_run:
                    search_run.status = 'failed'
                    search_run.completed_at = datetime.utcnow()
                    db.session.commit()
    
    def send_monthly_emails(self, report_path):
        """Send monthly report emails to all subscribers"""
        try:
            with app.app_context():
                subscribers = EmailSubscriber.query.filter_by(is_active=True).all()
                
                if not subscribers:
                    logger.info("No active subscribers found.")
                    return
                
                logger.info(f"Sending monthly report to {len(subscribers)} subscribers...")
                
                for subscriber in subscribers:
                    try:
                        self.send_individual_email(subscriber.email, report_path)
                        logger.info(f"Email sent to {subscriber.email}")
                    except Exception as e:
                        logger.error(f"Failed to send email to {subscriber.email}: {e}")
                        
        except Exception as e:
            logger.error(f"Failed to send monthly emails: {e}")
    
    def send_individual_email(self, recipient_email, report_path):
        """Send email to individual subscriber"""
        if not self.tracker.config['email']['sender_email']:
            logger.warning("Email configuration not set up. Skipping email delivery.")
            return
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = self.tracker.config['email']['sender_email']
        msg['To'] = recipient_email
        msg['Subject'] = f"CSRR Faculty Publications Report - {datetime.now().strftime('%B %Y')}"
        
        # Email body with unsubscribe link
        body = f"""
        Dear CSRR Team Member,
        
        Please find attached the monthly faculty publications report for {datetime.now().strftime('%B %Y')}.
        
        This automated report includes:
        - Recent op-eds, interviews, and publications by CSRR faculty affiliates
        - Summary by faculty member and content type
        - Links to original sources
        
        Report generated on: {datetime.now().strftime('%Y-%m-%d at %H:%M')}
        
        To unsubscribe from these notifications, click here:
        http://localhost:5000/unsubscribe/{recipient_email}
        
        Best regards,
        CSRR Automated Tracking System
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach Excel file
        if report_path and os.path.exists(report_path):
            with open(report_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {os.path.basename(report_path)}'
            )
            msg.attach(part)
        
        # Send email
        server = smtplib.SMTP(self.tracker.config['email']['smtp_server'], self.tracker.config['email']['smtp_port'])
        server.starttls()
        server.login(self.tracker.config['email']['sender_email'], self.tracker.config['email']['sender_password'])
        
        text = msg.as_string()
        server.sendmail(self.tracker.config['email']['sender_email'], recipient_email, text)
        server.quit()
    
    def health_check(self):
        """Perform a health check of the system"""
        logger.info("Performing system health check...")
        
        try:
            with app.app_context():
                # Check database connectivity
                user_count = User.query.count()
                subscriber_count = EmailSubscriber.query.filter_by(is_active=True).count()
                
                logger.info(f"Health check passed. Users: {user_count}, Subscribers: {subscriber_count}")
                
        except Exception as e:
            logger.error(f"Health check failed: {e}")

def main():
    """Main automation function"""
    automation = MonthlyAutomation()
    
    # Schedule monthly search on the 30th of each month at 9:00 AM
    schedule.every().month.at("09:00").do(automation.run_monthly_search)
    
    # Daily health check at 8:00 AM
    schedule.every().day.at("08:00").do(automation.health_check)
    
    logger.info("Monthly automation started. Waiting for scheduled tasks...")
    logger.info("Next monthly search will run on the 30th of each month at 9:00 AM")
    
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
