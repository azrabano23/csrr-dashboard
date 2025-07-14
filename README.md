# CSRR Faculty Tracker Dashboard

An automated web-based system for tracking CSRR faculty affiliate publications, op-eds, and media appearances.

## Features

- **Web Dashboard**: User-friendly interface for managing searches
- **Automated Monthly Reports**: Scheduled searches on the 30th of each month
- **Email Notifications**: Automated email delivery to subscribers
- **Excel Report Generation**: Comprehensive reports in Excel format
- **User Management**: Registration, login, and admin controls
- **Search History**: Track all previous searches and results

## Quick Start

### 1. Setup

```bash
cd /Users/azrabano/csrr-dashboard
chmod +x start_dashboard.sh
./start_dashboard.sh
```

### 2. Access the Dashboard

Open your browser and navigate to: `http://localhost:8080`

**Default Admin Login:**
- Username: `admin`
- Password: `admin123`

### 3. Configure Email Settings

Edit the `config.json` file (created automatically on first run) to set up email notifications:

```json
{
    "email": {
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "sender_email": "your-email@gmail.com",
        "sender_password": "your-app-password",
        "recipient_emails": ["recipient@example.com"]
    }
}
```

## Monthly Automation

To enable monthly automated searches:

1. **Start the automation script:**
```bash
python monthly_automation.py
```

2. **Or run in the background:**
```bash
nohup python monthly_automation.py &
```

3. **Set up as a system service** (recommended for production)

## Dashboard Features

### Main Dashboard
- View system statistics
- Start new searches
- Download recent reports
- Subscribe to email notifications

### Search Management
- Manual search initiation
- Real-time progress tracking
- Search history with pagination
- Report downloads

### User Management
- User registration and login
- Admin privileges for settings
- Email subscription management

### Settings
- Configure search parameters
- Adjust email settings
- View system configuration

## File Structure

```
csrr-dashboard/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── monthly_automation.py  # Automated monthly searches
├── start_dashboard.sh     # Startup script
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── faculty_list.html
│   ├── search_history.html
│   └── settings.html
├── csrr_dashboard.db     # SQLite database (created automatically)
└── automation.log        # Automation logs
```

## Usage

### Starting a Search

1. Log in to the dashboard
2. Click "Start New Search" on the main page
3. The search runs in the background
4. Check the "Recent Search Runs" section for progress
5. Download the Excel report when complete

### Email Subscriptions

1. Enter your email in the "Email Notifications" section
2. Click "Subscribe"
3. You'll receive monthly reports automatically on the 30th

### Viewing Faculty List

Navigate to "Faculty List" to see all 70 CSRR faculty affiliates being tracked.

### Search History

View all previous searches with details including:
- Start and completion times
- Number of results found
- Search duration
- Download links for reports

## Configuration

### Search Settings (Admin Only)

- **Days Back**: Number of days to search backwards (default: 30)
- **Max Results per Faculty**: Maximum results per faculty member (default: 5)
- **Search Delay**: Delay between searches to avoid rate limiting (default: 2 seconds)

### Email Settings

Configure in `config.json`:
- SMTP server details
- Sender email credentials
- Recipient email lists

## Troubleshooting

### Common Issues

1. **Database errors**: Delete `csrr_dashboard.db` and restart the application
2. **Email not sending**: Check email configuration in `config.json`
3. **Search failures**: Check logs in `automation.log`
4. **Permission errors**: Ensure proper file permissions for the dashboard directory

### Logs

- Dashboard logs: Check terminal output
- Automation logs: `automation.log`
- Search logs: `/Users/azrabano/CSRR_Reports/logs/`

## Security Notes

- Change the default admin password after first login
- Use app-specific passwords for Gmail
- Consider using environment variables for sensitive configuration
- Restrict dashboard access to internal network only

## Support

For issues or questions, contact the CSRR technical team.

## License

Built for Center for Security, Race and Rights at Rutgers Law School.
