from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form['name']
    blood_type = request.form['blood_type']

    # Save to database (SQLite for simplicity)
    conn = sqlite3.connect('blood_bank.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO donors (name, blood_type) VALUES (?, ?)", (name, blood_type))
    conn.commit()
    conn.close()

    return f"Thank you, {name}, for your submission! We have recorded your blood type: {blood_type}."

if __name__ == '__main__':
    app.run(debug=True)
