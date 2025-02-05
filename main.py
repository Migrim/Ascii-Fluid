from flask import Flask, render_template
import webview
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def run_flask():
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    webview.create_window("Block Game by Basti :3", "http://127.0.0.1:5000", width=800, height=600, resizable=False)
    webview.start()