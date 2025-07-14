# CSRR Faculty Tracker - Setup Complete

## ✅ What's Been Created

1. **Web Dashboard** (`/Users/azrabano/csrr-dashboard/`)
   - Flask-based web interface
   - User registration and login system
   - Search history and reporting
   - Email subscription management

2. **Core Tracking System** (`/Users/azrabano/csrr_faculty_tracker.py`)
   - Automated search for 70+ faculty members
   - Searches op-eds, interviews, TV appearances
   - Generates Excel reports
   - Email delivery system

3. **Monthly Automation** (`/Users/azrabano/csrr-dashboard/monthly_automation.py`)
   - Scheduled monthly searches
   - Automatic email delivery
   - Health monitoring

## 🚀 How to Start

### Option 1: Simple Dashboard (Recommended for now)
```bash
cd /Users/azrabano/csrr-dashboard
python simple_app.py
```
Then open: http://127.0.0.1:9000

### Option 2: Full Dashboard (may need debugging)
```bash
cd /Users/azrabano/csrr-dashboard
python app.py
```

## 📧 Email Configuration

Edit `/Users/azrabano/config.json`:
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

## 🔄 Monthly Automation Setup

1. **Manual setup:**
   ```bash
   cd /Users/azrabano/csrr-dashboard
   python monthly_automation.py
   ```

2. **Automatic setup (cron job):**
   ```bash
   ./setup_cron.sh
   ```

## 📋 Default Login (Full Dashboard)
- Username: `admin`
- Password: `admin123`

## 🛠 Manual Search (Command Line)
```bash
cd /Users/azrabano
python csrr_faculty_tracker.py
```

## 📁 Key Files Created

- `/Users/azrabano/csrr_faculty_tracker.py` - Main tracking script
- `/Users/azrabano/csrr-dashboard/app.py` - Full web interface
- `/Users/azrabano/csrr-dashboard/simple_app.py` - Simple web interface
- `/Users/azrabano/csrr-dashboard/monthly_automation.py` - Automation script
- `/Users/azrabano/csrr-dashboard/templates/` - HTML templates
- `/Users/azrabano/config.json` - Configuration file

## 📊 What the System Does

1. **Searches** for recent publications by 70 CSRR faculty affiliates
2. **Finds** op-eds, interviews, TV appearances, articles
3. **Generates** Excel reports with all findings
4. **Emails** reports to subscribers automatically
5. **Runs** monthly on the 30th of each month

## 🔧 Troubleshooting

If the web interface isn't loading:
1. Try the simple_app.py version first
2. Check if ports are available (try different ports)
3. Use the command-line version to test functionality
4. Check logs in `/Users/azrabano/csrr-dashboard/flask_output.log`

## 📞 Next Steps

1. Test the simple dashboard first
2. Configure email settings
3. Run a test search
4. Set up monthly automation
5. Customize as needed

The core functionality is ready to use!
