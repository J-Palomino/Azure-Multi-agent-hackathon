from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# In-memory log for demo (reset on restart)
call_log = []

SUB_AGENTS = [
    "Public Works (catch-all)",
    "Animal Control",
    "Waste Management"
]

def simulate_transcription():
    # For demo, just return a canned message or random phrase
    phrases = [
        "Caller: There's a stray dog in my yard.",
        "Dispatcher: Routing to Animal Control.",
        "Caller: My trash wasn't picked up.",
        "Dispatcher: Routing to Waste Management.",
        "Caller: There's a pothole on Main St.",
        "Dispatcher: Routing to Public Works."
    ]
    return random.choice(phrases)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        caller_id = request.form.get("caller_id", f"Caller{random.randint(100,999)}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        routed_to = random.choice(SUB_AGENTS)
        transcription = simulate_transcription()
        entry = {
            "call_id": len(call_log) + 1,
            "timestamp": timestamp,
            "caller_id": caller_id,
            "routed_to": routed_to,
            "transcription": transcription
        }
        call_log.append(entry)
        return redirect(url_for('index'))
    return render_template("index.html", call_log=call_log)

@app.route("/api/log")
def api_log():
    return jsonify(call_log)

if __name__ == "__main__":
    app.run(debug=True)
