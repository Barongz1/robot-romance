"""Robot Romance: One-Line Pickup Lines for AI — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The pickup line: a robot that is also my Wi-Fi signal.
TEXT = "Are you a Wi-Fi signal? Because every time I lose you, nothing in my life works."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
