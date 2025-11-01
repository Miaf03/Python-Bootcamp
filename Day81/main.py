# Day 81 Project: Text to Morse Code Converter (Supports letters, digits and symbols)

MORSE_CODE = {
    
    # Letters
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    
    # Digits
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    
    # Symbols
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    "\"": ".-..-.",
    "$": "...-..-",
    "@": ".--.-."
}

def text_to_morse(text: str) -> str:
    """
    Converts a string of text into Morse code
    - Unknown characters are replaced with '?'
    - Words are separated by 3 spaces
    - Letters by 1 space
    """
    morse_result = []

    for char in text.upper():
        if char == " ":
            morse_result.append("   ") # Space between words
        else:
            morse_char = MORSE_CODE.get(char, "?")
            morse_result.append(morse_char + " ") # Space between letters

    return "".join(morse_result).strip()


# User Interface

def main():
    print("\n" + "=" * 40)
    print("      MORSE CODE ENCODER")
    print("=" * 40 + "\n")
    print("Please provide a String to convert?")
    print("Type 'exit' to quit.\n")

    while True:
        user_text = input("Enter text: ").strip()
        if user_text.lower() == "exit":
            print("Goodbye!")
            break

        if not user_text:
            print("Please enter some text\n")
            continue

        morse = text_to_morse(user_text)
        print("\nMorse Code Output:")
        print(morse)
        print("\n" + "=" * 40 + "\n")


# Run Program

if __name__ == "__main__":
    main()