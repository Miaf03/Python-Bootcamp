import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from collections import defaultdict
from flask import Flask, jsonify, render_template, request

load_dotenv()
OWM_KEY = os.getenv("OPENWEATHER_API_KEY")
if not OWM_KEY:
    raise RuntimeError("Setea OPENWEATHER_API_KEY en el archivo .env")

app = Flask(__name__, static_folder="static", template_folder="templates")

def fetch_current_weather(city: str, units: str = "metric"):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": OWM_KEY, "units": units, "lang": "es"}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

def fetch_5day_forecast(city: str, units: str = "metric"):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "appid": OWM_KEY, "units": units, "lang": "es"}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

def summarize_forecast(forecast_json):
    daily = defaultdict(list)
    for item in forecast_json.get("list", []):
        dt = datetime.fromtimestamp(item["dt"])
        day = dt.date().isoformat()
        main = item.get("main", {})
        weather = item.get("weather", [{}])[0]
        daily[day].append({
            "temp": main.get("temp"),
            "temp_min": main.get("temp_min"),
            "temp_max": main.get("temp_max"),
            "weather_main": weather.get("main"),
            "weather_desc": weather.get("description"),
            "icon": weather.get("icon"),
            "dt_txt": item.get("dt_txt")
        })

    summary = []
    for day, entries in list(daily.items())[:6]:
        temps = [e["temp"] for e in entries if e["temp"] is not None]
        mins = [e["temp_min"] for e in entries if e["temp_min"] is not None]
        maxs = [e["temp_max"] for e in entries if e["temp_max"] is not None]
        icon = max(entries, key=lambda e: entries.count(e))["icon"]
        descs = [e["weather_desc"] for e in entries if e.get("weather_desc")]
        most_common_desc = max(set(descs), key=descs.count) if descs else ""
        summary.append({
            "date": day,
            "temp": round(sum(temps)/len(temps), 1) if temps else None,
            "temp_min": round(min(mins), 1) if mins else None,
            "temp_max": round(max(maxs), 1) if maxs else None,
            "description": most_common_desc,
            "icon": icon
        })

    return summary

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/weather")
def api_weather():
    city = request.args.get("city")
    units = request.args.get("units", "metric")
    if not city:
        return jsonify({"error": "city is required"}), 400

    try:
        current = fetch_current_weather(city, units=units)
        forecast = fetch_5day_forecast(city, units=units)
    except requests.HTTPError as e:
        return jsonify({"error": "City not found or API error", "detail": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Unexpected error", "detail": str(e)}), 500

    data = {
        "city": {
            "name": current.get("name"),
            "country": current.get("sys", {}).get("country")
        },
        "current": {
            "temp": current.get("main", {}).get("temp"),
            "feels_like": current.get("main", {}).get("feels_like"),
            "temp_min": current.get("main", {}).get("temp_min"),
            "temp_max": current.get("main", {}).get("temp_max"),
            "humidity": current.get("main", {}).get("humidity"),
            "pressure": current.get("main", {}).get("pressure"),
            "wind_speed": current.get("wind", {}).get("speed"),
            "description": current.get("weather", [{}])[0].get("description"),
            "icon": current.get("weather", [{}])[0].get("icon")
        },
        "forecast": summarize_forecast(forecast)
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)