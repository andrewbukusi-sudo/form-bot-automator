from flask import Flask
from scheduler import submit_form

app = Flask(__name__)

@app.route('/')
def home():
    submit_form()
    return "✅ Form submitted successfully (or attempted). Check logs for any errors."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
