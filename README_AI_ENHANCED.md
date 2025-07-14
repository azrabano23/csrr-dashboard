# 🤖 CSRR AI-Enhanced Faculty Tracker

An advanced, AI-powered web dashboard for tracking Rutgers Law School CSRR faculty publications, media appearances, and academic output.

## 🚀 Features

### Core Functionality
- **Automated Faculty Tracking**: Monitors 70+ CSRR faculty affiliates
- **Multi-Source Search**: Web scraping from news outlets, academic databases, and media platforms
- **Excel/Word Reports**: Automated generation of professional reports
- **Email System**: Monthly reports sent automatically on the 1st of each month
- **User Management**: Login/logout, email subscriptions

### 🧠 AI-Powered Features
- **ChatGPT-Style Assistant**: Interactive AI chatbot for queries about faculty and publications
- **Content Summarization**: AI-powered article and publication summarization
- **Smart Recommendations**: ML-based recommendations for "CSRR in the News" features
- **Timeline Visualization**: Interactive publication timelines per faculty member
- **Enhanced Web Scraping**: AI-guided scraping from Google Scholar and academic sources

### 🎨 UI/UX
- **Rutgers Law Branding**: Official colors, logos, and styling
- **Responsive Design**: Bootstrap-based mobile-friendly interface
- **Real-time Updates**: Live search status and progress indicators
- **Interactive Dashboard**: Statistics, analytics, and visual data representation

## 📋 Requirements

### System Requirements
- Python 3.8+
- macOS/Linux/Windows
- 4GB+ RAM recommended
- Internet connection for web scraping

### Python Dependencies
```
Flask>=2.0.0
pandas>=1.5.0
requests>=2.25.0
beautifulsoup4>=4.9.0
openai>=0.27.8          # For AI features
scholarly>=1.7.11       # Google Scholar integration
plotly>=5.15.0          # Timeline visualizations
python-docx>=0.8.11     # Enhanced reports
lxml>=4.9.3             # Web scraping
```

## 🛠️ Installation

### Quick Setup
```bash
cd /Users/azrabano/csrr-dashboard
python install_ai_features.py
```

### Manual Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Create directories
mkdir -p /Users/azrabano/CSRR_Reports
mkdir -p static templates

# Set up environment (optional)
cp .env.example .env
# Edit .env with your configuration
```

## ⚙️ Configuration

### Environment Variables (Optional)
Create a `.env` file for production use:

```bash
# OpenAI API Key (for full AI features)
OPENAI_API_KEY=your-openai-api-key-here

# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your-email@example.com
EMAIL_PASSWORD=your-app-password

# Flask Configuration
FLASK_SECRET_KEY=your-secret-key-here
FLASK_DEBUG=True
```

### Faculty List
Faculty members are automatically loaded from `csrr_faculty_tracker.py`. To modify:
1. Edit the `faculty_names` list in the tracker file
2. Restart the application

## 🚀 Usage

### Starting the Application
```bash
# Run the enhanced AI dashboard
python advanced_app.py

# Access the dashboard
open http://localhost:3000
```

### Alternative Ports
If port 3000 is busy, try:
```bash
# Try different ports
python -c "
import subprocess
for port in [3000, 8080, 9000, 5001]:
    try:
        subprocess.run(['python', 'advanced_app.py'], env={'PORT': str(port)})
        break
    except:
        continue
"
```

## 🤖 AI Features Guide

### 1. AI Chatbot Assistant
- **Access**: Click the robot icon in bottom-right corner
- **Capabilities**: 
  - Faculty information queries
  - Publication searches
  - System help and guidance
  - Real-time web scraping for faculty mentions

### 2. Content Summarization
- **Usage**: Click "AI Summarize" on any publication
- **Features**: Extracts key points from articles and op-eds
- **Sources**: Works with most news websites and academic papers

### 3. Smart Recommendations
- **Access**: Click "AI Recommend" on completed searches
- **Function**: Analyzes publications for CSRR website featuring
- **Criteria**: Impact, visibility, source credibility, timeliness

### 4. Timeline Visualization
- **Access**: Click "Timeline" next to faculty names
- **Display**: Interactive publication history over time
- **Data**: Academic papers, media appearances, op-eds

### 5. Enhanced Search
- **Sources**: Google Scholar, news outlets, academic databases
- **AI Analysis**: Automatic impact assessment and categorization
- **Reports**: Enhanced Word/Excel documents with AI insights

## 📊 Dashboard Components

### Main Dashboard
- **Search Control**: Start AI-enhanced searches
- **Statistics**: Faculty count, publications, subscribers
- **Recent Activity**: Latest publications and search results
- **AI Features Panel**: Quick access to AI tools

### Search Results
- **Status Tracking**: Real-time search progress
- **AI Actions**: Recommend, summarize, analyze
- **Downloads**: Excel and Word reports
- **Publication Details**: Source, type, impact metrics

### Faculty Management
- **Faculty List**: Complete CSRR affiliate directory
- **Publication History**: Per-faculty publication tracking
- **Timeline Views**: Visual publication timelines
- **Activity Metrics**: Publication frequency and impact

## 📧 Email System

### Monthly Reports
- **Schedule**: Automatically sent on the 1st of each month
- **Content**: AI-enhanced faculty publication summary
- **Recipients**: All email subscribers
- **Format**: Professional HTML emails with attachments

### Subscription Management
- **Sign-up**: Email form on dashboard
- **Unsubscribe**: Automatic links in emails
- **Management**: Admin interface for subscriber control

## 🔧 Troubleshooting

### Common Issues

#### Port Conflicts
```bash
# Error: Port already in use
# Solution: Try different ports
python advanced_app.py --port 8080
```

#### Missing Dependencies
```bash
# Error: Module not found
# Solution: Reinstall dependencies
pip install -r requirements.txt
```

#### AI Features Not Working
```bash
# Check OpenAI API key
export OPENAI_API_KEY=your-key-here

# Or edit .env file
echo "OPENAI_API_KEY=your-key-here" >> .env
```

#### Google Scholar Rate Limiting
- **Issue**: Scholarly library rate limited
- **Solution**: Automatic retry logic implemented
- **Alternative**: Manual faculty data entry

### Performance Optimization

#### Large Faculty Lists
- **Issue**: Slow searches with 70+ faculty
- **Solution**: Batch processing implemented
- **Limit**: Adjust `faculty_names[:10]` in search function

#### Memory Usage
- **Issue**: High memory with large datasets
- **Solution**: Pagination implemented
- **Cleanup**: Automatic cleanup of old search data

## 🔐 Security

### Data Protection
- **Local Storage**: All data stored locally
- **No Cloud Sync**: Faculty data remains on your machine
- **Secure Communication**: HTTPS recommendations for production

### API Keys
- **OpenAI**: Store in environment variables
- **Email**: Use app-specific passwords
- **Database**: SQLite with local file storage

## 🚀 Advanced Usage

### Custom Faculty Lists
```python
# Edit csrr_faculty_tracker.py
faculty_names = [
    "Your Faculty Name",
    "Another Faculty Member",
    # Add more faculty...
]
```

### Custom Search Sources
```python
# Add to WebScraper class
def scrape_custom_source(self, faculty_name):
    # Your custom scraping logic
    pass
```

### Enhanced AI Prompts
```python
# Modify AIAssistant._generate_simple_response()
# Add custom response logic
```

## 📈 Analytics and Reporting

### Built-in Analytics
- **Faculty Metrics**: Publication counts, citation tracking
- **Search Analytics**: Success rates, source effectiveness
- **Email Metrics**: Subscriber growth, engagement tracking
- **AI Usage**: Chatbot interactions, summarization requests

### Custom Reports
- **Export Options**: Excel, Word, CSV formats
- **Time Ranges**: Daily, weekly, monthly, custom
- **Faculty Filters**: Individual or group reporting
- **AI Insights**: Automated trend analysis

## 🤝 Contributing

### Development Setup
```bash
git clone /path/to/csrr-tracker
cd csrr-tracker
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Feature Requests
- AI model improvements
- Additional data sources
- Enhanced visualizations
- Custom integrations

## 📞 Support

### Documentation
- **This README**: Comprehensive setup and usage guide
- **Code Comments**: Detailed inline documentation
- **Example Files**: Sample configurations and data

### Common Questions
1. **Q**: How do I add more faculty members?
   **A**: Edit the `faculty_names` list in `csrr_faculty_tracker.py`

2. **Q**: Can I use without OpenAI API?
   **A**: Yes, basic functionality works without AI features

3. **Q**: How often should I run searches?
   **A**: Monthly automated searches are recommended

4. **Q**: Is this compatible with other law schools?
   **A**: Yes, easily adaptable by changing faculty lists and branding

## 📄 License

This project is developed for Rutgers Law School's Center for Security, Race and Rights (CSRR). 

---

## 🎯 Quick Start Commands

```bash
# Complete setup and launch
cd /Users/azrabano/csrr-dashboard
python install_ai_features.py
python advanced_app.py

# Access dashboard
open http://localhost:3000
```

**🎉 You're ready to go! The AI-enhanced CSRR Faculty Tracker is now running with all advanced features enabled.**
