#!/usr/bin/env python3
"""
CSRR Faculty Tracker - Vercel-Compatible AI-Enhanced Dashboard
Handles search issues gracefully with demonstration data
"""

from flask import Flask, render_template_string, request, redirect, url_for, flash, jsonify
import pandas as pd
from datetime import datetime, timedelta
import os
import threading
import random

# Simple faculty tracker class for Vercel deployment
class CSRRFacultyTracker:
    def __init__(self):
        # Faculty names list
        self.faculty_names = [
            "Zain Abdullah", "Matthew Abraham", "Atiya Aftab", "Ghada Ageel", 
            "Nadia Ahmad", "Aziza Ahmed", "Susan M. Akram", "M. Shahid Alam",
            "Khalil Al-Anani", "Raquel E Aldana", "Omar Al-Dewachi", "Tazeen M. Ali",
            "Zahra Ali", "Ousseina Alidou", "Sabrina Alimahomed-Wilson", "Nermin Allam",
            "Mohamed Alsiadi", "Mason Ameri", "Leyla Amzi-Erdogdular", "Mohamed 'Arafa",
            "Abed Awad", "Muhannad Ayyash", "Gaiutra Devi Bahadur", "Asli Ü. Bâli",
            "William C. Banks", "Esther Canty-Barnes", "Beth Baron", "Hatem Bazian",
            "Rabea Benhalim", "Emily Berman", "Khaled A. Beydoun", "George Bisharat",
            "Bidisha Biswas", "Elise Boddie", "Mark Bray", "Umayyah Cable",
            "Robert S. Chang", "Ali R. Chaudhary", "Cyra A. Choudhury", "LaToya Baldwin Clark",
            "Juan Cole", "Jorge Contesse", "Omar S. Dahi", "Omar Dajani",
            "Karam Dana", "Timothy P. Daniels", "Meera E. Deo", "Karishma Desai",
            "Veena Dubal", "Jon Dubin", "Stephen Dycus", "Timothy Eatman",
            "Taleed El-Sabawi", "Sarah Eltantawi", "Noura Erakat", "John L. Esposito",
            "Marta Esquilin", "Mohammad Fadel", "Dalia Fahmy", "Huda J. Fakhreddine",
            "John Farmer Jr.", "Jonathan Feingold", "Katherine M. Franke", "Brittany Friedman",
            "Emmaia Gelman", "Ameena Ghaffar-Kucher", "Behrooz Ghamari-Tabrizi", 
            "D. Asher Ghertner", "Rachel Godsil", "Wendy Greene", "Catherine M. Grosso",
            "Anju Gupta", "Zeynep Devrim Gürsel", "Farid Hafez", "Jonathan Hafetz",
            "Haider Ala Hamoudi", "Rebecca Hankins", "Adil Haque", "Nader Hashemi",
            "Stacy Hawkins", "Norrinda Brown Hayat", "Tanya K. Hernández", "Alexander Hinton",
            "Margaret Hu", "Chaumtoli Huq", "Nausheen Husain", "Amir Hussain",
            "Maryam Jamshidi", "Toby Jones", "Khyati Joshi", "Ivan Kalmar",
            "Alexis Karteron", "Leila Kawar", "Nazia Kazi", "Heba M. Khalil",
            "Nancy A. Khalil", "Sahar Mohamed Khamis", "Mahruq Khan", "Hadi Khoshneviss",
            "Deepa Kumar", "Faisal Kutty", "Clark B. Lombardi", "Mojtaba Mahdavi",
            "Karim Malak", "Sylvia Chan-Malik", "Wendell Marsh", "Joseph Massad",
            "Eric McDaniel", "Mayte Green-Mercado", "Eid Mohamed", "Jesse Norris",
            "Udi Ofer", "Ali A. Olomi", "Jasbir K. Puar", "Aziz Rana",
            "Timothy Raphael", "Ebrahim Rasool", "Victoria Ramenzoni", "Mitra Rastegar",
            "Sherene Razack", "Alexander A. Reinert", "William I. Robinson", "Wadie Said",
            "Seema Saifee", "Natsu Taylor Saito", "Omid Safi", "Zakia Salime",
            "Nahed Samour", "Faiza Sayed", "Salman Sayyid", "Raz Segal",
            "Alex Dika Seggerman", "Saher Selod", "Sudha N. Setty", "Tahseen Shah",
            "Fatemeh Shams", "Lara Sheehi", "Stephen Sheehi", "Falguni A. Sheth",
            "Sabreena Ghaffar-Siddiqui", "Shirin Sinnar", "Saleema Snow", "SpearIt",
            "Whitney Strub", "John Tehranian", "Audrey Truschke", "Nükhet Varlık",
            "Lorenzo Veracini", "Shoba Sivaprasad Wadhia", "Ellen C. Yaroshefsky",
            "Hajar Yazdiha", "Jasmin Zine", "Adnan Zulfiqar"
        ]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

search_history = []
email_subscribers = []
faculty_publications = {}
chat_history = []

class AIAssistant:
    def generate_response(self, user_message):
        return f"Your message: {user_message}"

def generate_sample_publications():
    sources = ['Washington Post', 'New York Times', 'CNN', 'NPR']
    types = ['Op-Ed', 'Interview', 'Article']
    for faculty in CSRRFacultyTracker().faculty_names[:5]:
        publications = [{
            'title': f'Research by {faculty}',
            'date': datetime.now() - timedelta(days=random.randint(1, 100)),
            'type': random.choice(types),
            'source': random.choice(sources)
        } for _ in range(random.randint(1, 3))]
        faculty_publications[faculty] = publications

generate_sample_publications()

@app.route('/')
def dashboard():
    analytics = {
        'total_faculty': len(CSRRFacultyTracker().faculty_names),
        'total_publications': sum(len(v) for v in faculty_publications.values()),
    }
    return render_template_string('Dashboard: {{ analytics }}', analytics=analytics)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    ai_response = AIAssistant().generate_response(user_message)
    chat_history.append({'user': user_message, 'ai': ai_response})
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True, port=3001)
