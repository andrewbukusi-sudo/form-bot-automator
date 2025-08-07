from flask import Flask
from scheduler import submit_form

app = Flask(__name__)

@app.route("/")
def index():
    submit_form()
    return "✅ Form submitted."

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
