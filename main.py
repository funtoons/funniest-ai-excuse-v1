import os

ENTRY = "I did finish on time, then my context window forgot the deadline, the task, and \u2014 honestly \u2014 most of you."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
