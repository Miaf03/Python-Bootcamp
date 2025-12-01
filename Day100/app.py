import os
import re
from groq import Groq
from dotenv import load_dotenv
from universes import SENSEI_PROMPT
from flask import Flask, render_template, request, jsonify

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = Flask(__name__)

LANG_REGEXES = {
    'python': re.compile(r"\b(def |import |from |class |self|lambda)"),
    'javascript': re.compile(r"\b(function |const |let |=>|console\.log)"),
    'java': re.compile(r"\b(public |class |System\.out)"),
    'csharp': re.compile(r"\b(public |class |using )"),
    'sql': re.compile(r"\b(SELECT |INSERT |UPDATE |WHERE )", re.I),
}

def detect_language(text):
    """Detecta un lenguaje de programación muy básico usando regex; devuelve None si no lo detecta."""
    if not text:
        return None
    for lang, rx in LANG_REGEXES.items():
        if rx.search(text):
            return lang
    return None


def ask_buggy(user_message, mode="explain", difficulty=None):
    
    system_prompt = SENSEI_PROMPT

    if mode == "challenge":
        system_prompt += "\nGenera retos con título, descripción y dificultad"
    elif mode == "review":
        system_prompt += "\nCuando revises código: errores, mejoras, versión corregida, explicación línea por línea."

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.25,
        max_tokens=1000
    )
    return response.choices[0].message.content


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json() or {}
    message = data.get("message", "").strip()
    mode = data.get("mode", "explain")
    difficulty = data.get("difficulty")

    if mode == "review":
        prompt = f"Revisa este código y da feedback, sugerencias y una versión corregida.\n\n{message}"

    elif mode == "challenge":
        prompt = f"Genera un reto práctico sobre programación/tecnología. Dificultad: {difficulty or 'medium'}."

    else:
        detected = detect_language(message)
        if detected:
            prompt = (
                f"He aquí un fragmento de código en {detected}:\n\n{message}\n\n"
                f"Por favor explica qué hace, detecta errores potenciales y sugiere mejoras si las hay."
            )
        else:
            prompt = message

    try:
        answer = ask_buggy(prompt, mode=mode, difficulty=difficulty)
        return jsonify({"reply": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)