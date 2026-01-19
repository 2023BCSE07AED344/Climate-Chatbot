from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"].lower()

    if "energy" in user_msg:
        reply = "You can save energy by using LED lights and turning off unused devices."
    elif "waste" in user_msg:
        reply = "Waste segregation and recycling are key steps toward sustainability."
    elif "climate" in user_msg:
        reply = "Climate action includes reducing emissions and promoting renewable energy."
    else:
        reply = "I can help with energy, waste, climate, and campus sustainability topics."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
