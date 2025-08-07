from flask import Flask
from scheduler import run_scheduler

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Form submission bot is running!'

@app.route('/run')
def run():
    run_scheduler()
    return '✅ Scheduler executed successfully.'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
