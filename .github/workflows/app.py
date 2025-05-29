from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Check"

if __name__ == "__main__":
    # check out
    app.run(host="0.0.0.0", port=8000)
