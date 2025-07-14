#!/usr/bin/env python3
"""
AI-Enhanced CSRR Faculty Tracker - Installation Script
Installs all required dependencies for AI features and advanced functionality
"""

import subprocess
import sys
import os
from pathlib import Path

def install_package(package):
    """Install a Python package using pip"""
    try:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {package}")
        return False

def check_and_install_dependencies():
    """Check and install all required dependencies"""
    
    print("🚀 Setting up AI-Enhanced CSRR Faculty Tracker")
    print("=" * 60)
    
    # Core dependencies
    core_packages = [
        "Flask>=2.0.0",
        "Flask-SQLAlchemy>=3.0.0", 
        "Flask-Login>=0.6.0",
        "Werkzeug>=2.0.0",
        "pandas>=1.5.0",
        "requests>=2.25.0",
        "beautifulsoup4>=4.9.0",
        "openpyxl>=3.0.0",
        "schedule>=1.1.0"
    ]
    
    # AI and visualization dependencies
    ai_packages = [
        "openai>=0.27.8",
        "scholarly>=1.7.11", 
        "plotly>=5.15.0",
        "python-docx>=0.8.11",
        "lxml>=4.9.3"
    ]
    
    print("\n📦 Installing core dependencies...")
    for package in core_packages:
        install_package(package)
    
    print("\n🤖 Installing AI and visualization dependencies...")
    for package in ai_packages:
        install_package(package)
    
    print("\n✅ Installation complete!")
    
def create_directories():
    """Create necessary directories"""
    directories = [
        "/Users/azrabano/CSRR_Reports",
        "/Users/azrabano/csrr-dashboard/static",
        "/Users/azrabano/csrr-dashboard/templates"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"📁 Created directory: {directory}")

def setup_environment():
    """Set up environment variables and configuration"""
    
    env_example = """
# CSRR Faculty Tracker - Environment Variables
# Copy this to .env and fill in your actual values

# OpenAI API Key (for advanced AI features)
OPENAI_API_KEY=your-openai-api-key-here

# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your-email@example.com
EMAIL_PASSWORD=your-app-password

# Flask Configuration
FLASK_SECRET_KEY=your-secret-key-here
FLASK_DEBUG=True

# Database (SQLite by default)
DATABASE_URL=sqlite:///csrr_tracker.db

# Rutgers Configuration
RUTGERS_LAW_URL=https://csrr.rutgers.edu
CSRR_NEWS_URL=https://csrr.rutgers.edu/newsroom/csrr-in-the-news/
"""
    
    env_path = Path("/Users/azrabano/csrr-dashboard/.env.example")
    with open(env_path, 'w') as f:
        f.write(env_example)
    
    print(f"📝 Created environment template: {env_path}")
    print("   Edit this file and rename to .env for production use")

def main():
    """Main installation function"""
    
    print("🎯 CSRR AI-Enhanced Faculty Tracker Installation")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists('/Users/azrabano/csrr_faculty_tracker.py'):
        print("❌ Error: csrr_faculty_tracker.py not found!")
        print("   Please run this script from the correct directory")
        return
    
    # Install dependencies
    check_and_install_dependencies()
    
    # Create directories
    print("\n📁 Creating necessary directories...")
    create_directories()
    
    # Set up environment
    print("\n⚙️ Setting up environment configuration...")
    setup_environment()
    
    print("\n" + "=" * 60)
    print("🎉 AI-Enhanced CSRR Faculty Tracker Setup Complete!")
    print("\nNext Steps:")
    print("1. Edit .env.example and rename to .env")
    print("2. Add your OpenAI API key for full AI features")
    print("3. Run: python advanced_app.py")
    print("4. Visit: http://localhost:3000")
    print("\n🤖 Features Available:")
    print("   • AI Chatbot Assistant (ChatGPT-style)")
    print("   • Content Summarization")
    print("   • Smart Recommendations")
    print("   • Timeline Visualizations")
    print("   • Enhanced Web Scraping")
    print("   • Google Scholar Integration")
    print("   • Monthly Automated Reports")
    print("   • Rutgers Law Themed UI")

if __name__ == "__main__":
    main()
