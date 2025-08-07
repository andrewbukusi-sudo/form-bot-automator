from flask import Flask
import threading
import random
import time
from form_bot import submit_form

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Bot is ready and running!'

@app.route('/submit')
def submit():
    try:
        submit_form()
        return "✅ Submitted 1 form"
    except Exception as e:
        return f"❌ Error: {e}"

def schedule_submissions():
    num_forms = 80
    total_seconds = 24 * 60 * 60
    for i in range(num_forms):
        delay = random.uniform(0, total_seconds / num_forms)
        time.sleep(delay)
        try:
            submit_form()
            print(f"✅ Submitted form {i + 1}")
        except Exception as e:
            print(f"❌ Error submitting form {i + 1}: {e}")

if __name__ == '__main__':
    threading.Thread(target=schedule_submissions).start()
    app.run(host='0.0.0.0', port=5000)
