from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

custom_variable = "Initial value"

@app.route("/")
def home():
    global custom_variable
    return render_template("index.html", custom_variable=custom_variable)

@app.route("/change_variable", methods=["GET"])
def change_variable():
    global custom_variable
    new_value = request.args.get("new_value")
    if new_value:
        custom_variable = new_value
        return jsonify(status="success", custom_variable=custom_variable)
    else:
        return jsonify(status="error", message="No value provided")

if __name__ == "__main__":
    app.run(debug=True)
