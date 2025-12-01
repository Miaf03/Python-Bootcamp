const chat = document.getElementById("chat");
const input = document.getElementById("input");
const sendBtn = document.getElementById("send");
const clearBtn = document.getElementById("clear");
const modeSelect = document.getElementById("mode");
const difficultySelect = document.getElementById("difficulty");
const themeToggle = document.getElementById("themeToggle");


modeSelect.addEventListener("change", () => {
    if (modeSelect.value === "challenge")
        difficultySelect.style.display = "inline-block";
    else difficultySelect.style.display = "none";
});


function autoResize() {
    input.style.height = "auto";
    input.style.height = input.scrollHeight + "px";
}
input.addEventListener("input", autoResize);

input.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        sendBtn.click();
    }
});

function appendMessage(text, who = "bot") {
    const div = document.createElement("div");
    div.className = "msg " + (who === "user" ? "user" : "bot");
    div.innerHTML = text.replace(/\n/g, "<br/>");
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

sendBtn.onclick = async () => {

    const text = input.value.trim();
    if (!text) return;

    appendMessage(`<b>Tú:</b> ${text}`, "user");
    appendMessage(`<i>Buggy está pensando...</i>`, "bot");

    const payload = {
        message: text,
        mode: modeSelect.value,
        difficulty: difficultySelect.value,
    };

    try {
        const res = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
        });

        const data = await res.json();

        chat.removeChild(chat.lastChild);

        if (data.error) {
        appendMessage(`<b>Error:</b> ${data.error}`, "bot");
        } else {
        appendMessage(`<b>Buggy:</b> ${data.reply}`, "bot");
        }

    } catch (err) {
        chat.removeChild(chat.lastChild);
        appendMessage(`<b>Error de conexión:</b> ${err}`, "bot");
    }

    input.value = "";
};

clearBtn.onclick = () => {
    chat.innerHTML = "";
    input.value = "";
};