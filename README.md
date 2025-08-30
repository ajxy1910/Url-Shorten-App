# Flask URL Shortener

A simple **URL shortener web application** built using **Flask** and **SQLite**.  
This project allows users to convert long URLs into short, shareable links.

---

## Features
- Shorten long URLs with a unique 6-character code.
- Redirect short URLs to the original long URLs.
- Simple and responsive user interface using **Bootstrap**.
- Database stored locally in **SQLite**.

---

## Demo
- Visit the app at: `http://127.0.0.1:5000` after running locally.
- Enter a long URL and get a short link instantly.

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/ajxy1910/Url-Shorten-App.git
cd Url-Shorten-App

Create a virtual environment (recommended):
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

Install dependencies:
pip install flask

Run the app:
python app.py

Open in your browser:
http://127.0.0.1:5000

Usage

1.Enter a long URL in the form.
2.Click Shorten URL.
3.Copy or share the generated short URL.
4.Accessing the short URL will redirect to the original long URL.