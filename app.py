from flask import Flask, render_template, request
from ast import literal_eval
import subprocess
import sys
from main import count_intersections
from main import get_chords

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        # Get the selected preset as a string from the form
        selected_chords_str = request.form['chords']

        # Convert the string to a Python list
        chords = literal_eval(selected_chords_str)

        # Run main.py logic with the selected chords
        result_message = get_chords(chords)
            
    except subprocess.CalledProcessError as e:
        result_message = f"Error executing Python code: {e}"

    return render_template('index.html', result=result_message)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
