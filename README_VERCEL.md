# CSRR Faculty Tracker - Vercel Deployment

## Overview
This is a Flask-based web application for tracking faculty publications and media appearances at the Center for Security, Race and Rights (CSRR) at Rutgers Law School. The application is optimized for deployment on Vercel.

## Features
- AI-powered chatbot assistant
- Faculty publication tracking
- Content summarization
- Email subscription management
- Demo search functionality
- Responsive Rutgers-themed UI

## Vercel Deployment

### Prerequisites
- GitHub account
- Vercel account (free tier available)

### Files for Vercel Deployment
- `app.py` - Main Flask application
- `vercel.json` - Vercel configuration
- `requirements.txt` - Python dependencies

### Deployment Steps

1. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign in with your GitHub account
   - Click "New Project"
   - Import the `csrr-dashboard` repository

2. **Configure Deployment**
   - Framework Preset: **Other**
   - Root Directory: `./` (default)
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
   - Install Command: `pip install -r requirements.txt`

3. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete
   - Your app will be available at `https://your-project-name.vercel.app`

### Environment Variables
No special environment variables are required for the demo version.

### Configuration Files

#### vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
  "env": {
    "FLASK_ENV": "production"
  }
}
```

#### requirements.txt
```
Flask>=2.0.0
Werkzeug>=2.0.0
pandas>=1.5.0
requests>=2.25.0
beautifulsoup4>=4.9.0
openpyxl>=3.0.0
gunicorn>=20.0.0
lxml>=4.9.3
```

## Application Structure

### Main Components
- **CSRRFacultyTracker Class**: Manages faculty data
- **AIAssistant Class**: Handles chatbot responses
- **Flask Routes**: Web application endpoints
- **HTML Templates**: Embedded responsive UI

### Key Routes
- `/` - Main dashboard
- `/chat` - AI chatbot endpoint
- `/faculty` - Faculty directory
- `/subscribe` - Email subscription

## Local Development

### Setup
```bash
# Clone the repository
git clone https://github.com/azrabano23/csrr-dashboard.git
cd csrr-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Access
- Local: `http://localhost:5000`
- Vercel: `https://your-project-name.vercel.app`

## Features

### AI Chatbot
- Rule-based responses
- Faculty information queries
- System guidance
- Search assistance

### Faculty Tracking
- 70+ faculty members
- Publication monitoring
- Media appearance tracking
- Academic paper discovery

### Demo Functionality
- Sample publication data
- Simulated search results
- AI recommendations
- Content summarization

## Customization

### Adding Faculty
Edit the `faculty_names` list in the `CSRRFacultyTracker` class in `app.py`.

### Styling
Update the CSS in the HTML templates within `app.py` to customize the appearance.

### AI Responses
Modify the `AIAssistant.generate_response()` method to add new chatbot capabilities.

## Support
For issues or questions, please contact the CSRR development team.

## License
This project is developed for Rutgers Law School's Center for Security, Race and Rights.
