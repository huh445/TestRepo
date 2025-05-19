from flask import Flask, render_template_string, request
import psutil
import socket
import os
import platform
import requests
from datetime import timedelta

app = Flask(__name__)

DOWNLOAD_DIR = "/home/huh445/Downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

TEMPLATE = """
<html>
<head>
    <title>Charlie’s Pi Dashboard</title>
    <style>
        body { font-family: sans-serif; background: #111; color: #eee; padding: 20px; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 2em; }
        td, th { border: 1px solid #555; padding: 8px; }
        th { background: #222; }
        form input[type=text] { padding: 8px; width: 80%; border: none; border-radius: 4px; }
        form button { padding: 8px 16px; border: none; border-radius: 4px; background-color: #4CAF50; color: white; }
    </style>
</head>
<body>
    <h1>📊 Raspberry Pi Dashboard</h1>
    <table>
        {% for key, value in info.items() %}
        <tr><th>{{ key }}</th><td>{{ value }}</td></tr>
        {% endfor %}
    </table>
    <h2>⬇️ Download a File</h2>
    <form method="POST" action="/download">
        <input type="text" name="url" placeholder="Paste file URL..." required>
        <button type="submit">Download</button>
    </form>
</body>
</html>
"""

def get_system_info():
    uname = platform.uname()
    uptime = timedelta(seconds=int(psutil.boot_time()))
    ip_address = socket.gethostbyname(socket.gethostname())
    try:
        temp = psutil.sensors_temperatures().get("cpu-thermal", [{}])[0].get("current", "N/A")
    except:
        temp = "N/A"

    return {
        "Hostname": uname.node,
        "OS": f"{uname.system} {uname.release}",
        "Uptime (boot time)": uptime,
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "RAM Usage (%)": psutil.virtual_memory().percent,
        "Disk Usage (%)": psutil.disk_usage('/').percent,
        "Load Avg": os.getloadavg(),
        "IP Address": ip_address,
        "Temperature (°C)": temp
    }

def get_location_and_weather():
    try:
        geo = requests.get("https://ipinfo.io/json").json()
        loc = geo["city"] + ", " + geo["region"]
        coords = geo["loc"]
        lat, lon = coords.split(",")

        weather = requests.get(
            f"https://wttr.in/{lat},{lon}?format=3"
        ).text.strip()
        first, rest = weather.split(" ", 1)
        return {
            "Location": loc,
            "Weather": rest
        }
    except:
        return {
            "Location": "Unavailable",
            "Weather": "Unavailable"
        }

@app.route("/")
def index():
    info = get_system_info()
    info.update(get_location_and_weather())
    return render_template_string(TEMPLATE, info=info)

@app.route("/download", methods=["POST"])
def download():
    url = request.form["url"]
    filename = url.split("/")[-1]
    path = os.path.join(DOWNLOAD_DIR, filename)

    try:
        r = requests.get(url, stream=True)
        with open(path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        return f"<p>✅ Downloaded <b>{filename}</b> to Pi!</p><a href='/'>Back</a>"
    except Exception as e:
        return f"<p>❌ Error: {e}</p><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
