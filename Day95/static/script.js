const form = document.getElementById("searchForm");
const cityInput = document.getElementById("cityInput");
const unitsSelect = document.getElementById("units");
const result = document.getElementById("result");
const errorDiv = document.getElementById("error");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const city = cityInput.value.trim();
    const units = unitsSelect.value;
    if (!city) return;

    errorDiv.classList.add("hidden");
    result.classList.add("hidden");

    try {
        const res = await fetch(`/api/weather?city=${encodeURIComponent(city)}&units=${units}`);

        if (!res.ok) {
            const err = await res.json();
            throw new Error(err.error || "Error en la API");
        }

        const data = await res.json();
        renderWeather(data, units);

    } catch (err) {
        errorDiv.textContent = err.message;
        errorDiv.classList.remove("hidden");
    }
});

function renderWeather(data, units) {

    document.getElementById("cityName").textContent = `${data.city.name}, ${
        data.city.country || ""
    }`;

    const cur = data.current;
    const unitSymbol = units === "metric" ? "°C" : "°F";

    document.getElementById("currentTemp").textContent = `${Math.round(cur.temp)}${unitSymbol}`;
    document.getElementById("currentDesc").textContent = cur.description || "";
    document.getElementById("feels").textContent = `Sensación: ${Math.round(cur.feels_like) || "—"}${unitSymbol}`;
    document.getElementById("hum").textContent = `Humedad: ${cur.humidity || "—"}%`;
    document.getElementById("wind").textContent = `Viento: ${cur.wind_speed || "—"} m/s`;

    const iconEl = document.getElementById("currentIcon");
    iconEl.src = `https://openweathermap.org/img/wn/${cur.icon}@2x.png`;
    const forecastDiv = document.getElementById("forecast");
    forecastDiv.innerHTML = "";

    if (Array.isArray(data.forecast)) {
        data.forecast.slice(1, 6).forEach((day) => {
        const card = document.createElement("div");
        card.className = "day-card";
        card.innerHTML = `
            <div class="day">${day.date}</div>
            <img src="https://openweathermap.org/img/wn/${day.icon}@2x.png">
            <div class="d-desc">${day.description}</div>
            <div class="d-temps">${day.temp_min} / ${day.temp_max} ${unitSymbol}</div>
        `;
        forecastDiv.appendChild(card);
        });
    }

    result.classList.remove("hidden");
}