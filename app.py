from flask import Flask, render_template
import subprocess
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        # Run main.py using subprocess
        result_message = subprocess.check_output([sys.executable, 'main.py'], universal_newlines=True)
    except subprocess.CalledProcessError as e:
        result_message = f"Error executing Python code: {e}"

    return render_template('index.html', result=result_message)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
