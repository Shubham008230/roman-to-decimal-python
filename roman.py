VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def roman_to_decimal(text):
    """Return the number for a Roman numeral, or None if it is invalid."""
    text = text.strip().upper()
    if not text:
        return None

    total = 0
    for i in range(len(text)):
        if text[i] not in VALUES:
            return None                 # not a Roman letter
        value = VALUES[text[i]]

        # Is there a next letter, and is it bigger than this one?
        if i + 1 < len(text) and text[i +1] in VALUES and value < VALUES[text[i + 1]]:
            total -= value                      # smaller before bigger: subtract
        else:
            total += value                      # otherwise: add
    return total


def main():
    while True:
        text =input("Enter a Roman numeral (or 'quit' to exit): ").strip()
        if text.lower() == "q":
            break
        result = roman_to_decimal(text)
        if result is None:
            print("Error: use only the letters I, V, X, L, C, D, M.")
        else:
            print(f"Decimal: {result}")

if __name__ == "__main__":
    main()