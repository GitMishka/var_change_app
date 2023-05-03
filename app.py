from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize the counter variable
counter = 0

@app.route("/")
def home():
    global counter
    return render_template("index.html", counter=counter)

@app.route("/update_counter", methods=["POST"])
def update_counter():
    global counter
    action = request.form.get("action")

    if action == "increment":
        counter += 1
    elif action == "decrement":
        counter -= 1

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
