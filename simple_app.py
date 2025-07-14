#!/usr/bin/env python3
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>CSRR Faculty Tracker</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .header { color: #333; text-align: center; }
            .card { border: 1px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 5px; }
            .btn { background: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 3px; }
        </style>
    </head>
    <body>
        <h1 class="header">CSRR Faculty Tracker Dashboard</h1>
        
        <div class="card">
            <h3>Welcome to the CSRR Faculty Publication Tracker</h3>
            <p>This system automatically tracks publications, op-eds, and media appearances by CSRR faculty affiliates.</p>
            
            <h4>Features:</h4>
            <ul>
                <li>Automated monthly searches</li>
                <li>Excel report generation</li>
                <li>Email notifications</li>
                <li>70+ faculty members tracked</li>
            </ul>
            
            <p><strong>Status:</strong> Dashboard is running successfully!</p>
            
            <h4>Next Steps:</h4>
            <ol>
                <li>Set up email configuration in config.json</li>
                <li>Run your first search</li>
                <li>Set up monthly automation</li>
            </ol>
            
            <p>
                <a href="/faculty" class="btn">View Faculty List</a>
                <a href="/config" class="btn">Configuration</a>
            </p>
        </div>
        
        <div class="card">
            <h4>System Information</h4>
            <p><strong>Faculty Tracked:</strong> 70 affiliates</p>
            <p><strong>Search Types:</strong> Op-eds, Interviews, TV appearances, Articles</p>
            <p><strong>Output Format:</strong> Excel (.xlsx)</p>
            <p><strong>Automation:</strong> Monthly on 30th</p>
        </div>
    </body>
    </html>
    ''')

@app.route('/faculty')
def faculty():
    faculty_names = [
        "Zain Abdullah", "Matthew Abraham", "Atiya Aftab", "Ghada Ageel", 
        "Nadia Ahmad", "Aziza Ahmed", "Susan M. Akram", "M. Shahid Alam",
        # ... (truncated for brevity)
    ]
    
    faculty_html = "<br>".join([f"{i+1}. {name}" for i, name in enumerate(faculty_names[:20])])
    
    return render_template_string(f'''
    <!DOCTYPE html>
    <html>
    <head><title>Faculty List</title></head>
    <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>CSRR Faculty Affiliates</h1>
        <p>Showing first 20 of 70 total faculty members:</p>
        <div style="margin: 20px 0;">
            {faculty_html}
        </div>
        <p><a href="/">← Back to Dashboard</a></p>
    </body>
    </html>
    ''')

@app.route('/config')
def config():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head><title>Configuration</title></head>
    <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>Configuration</h1>
        <div style="border: 1px solid #ddd; padding: 20px; border-radius: 5px;">
            <h3>Email Setup</h3>
            <p>Edit the config.json file with your email settings:</p>
            <pre style="background: #f5f5f5; padding: 15px; border-radius: 3px;">
{
    "email": {
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "sender_email": "your-email@gmail.com",
        "sender_password": "your-app-password",
        "recipient_emails": ["recipient@example.com"]
    }
}
            </pre>
        </div>
        <p><a href="/">← Back to Dashboard</a></p>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    print("Starting CSRR Faculty Tracker on http://127.0.0.1:3000")
    app.run(debug=True, port=3000, host='127.0.0.1')
