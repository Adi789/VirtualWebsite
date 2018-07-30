from flask import Flask, render_template

# variable to store flask object instance
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

# decorator with a function
@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
