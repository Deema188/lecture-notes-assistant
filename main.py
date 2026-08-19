from summarizer import summarize

def main():
    print("=== Smart Lecture Notes Assistant ===")
    print("Paste your lecture text below, then press Enter twice when done:\n")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    text = " ".join(lines)
    
    if not text.strip():
        print("No text entered. Please try again.")
        return
    
    summary = summarize(text, num_sentences=3)
    
    print("\n--- Summary ---")
    print(summary)

if __name__ == "__main__":
    main()