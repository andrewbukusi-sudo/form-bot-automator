from flask import Flask
from scheduler import submit_form
import random

app = Flask(__name__)

@app.route('/')
def home():
    try:
        submit_form()
        return "✅ Submitted 1 form successfully!"
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
