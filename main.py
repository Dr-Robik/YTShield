import pickle
import re
import time
import sys
import random
from core.youtube_api import fetch_comments
from colorama import Fore, Style, init

init(autoreset=True)

model = pickle.load(open("ai/spam_model.pkl", "rb"))
vectorizer = pickle.load(open("ai/vectorizer.pkl", "rb"))


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def spinner(text, duration=2):
    """Print a spinning animation for 'duration' seconds."""
    spinner_chars = "|/-\\"
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in spinner_chars:
            sys.stdout.write(f"\r{text} {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * (len(text) + 2) + "\r")

def progress_bar(total, prefix=""):
    """Print a progress bar."""
    for i in range(total):
        bar = "[" + "#" * (i+1) + " " * (total-i-1) + "]"
        sys.stdout.write(f"\r{prefix} {bar} {i+1}/{total}")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\n")

def print_banner():
    banner = r"""
 __     _________ _____ _     _      _     _ 
 \ \   / /__   __/ ____| |   (_)    | |   | |
  \ \_/ /   | | | (___ | |__  _  ___| | __| |
   \   /    | |  \___ \| '_ \| |/ _ \ |/ _` |
    | |     | |  ____) | | | | |  __/ | (_| |
    |_|     |_| |_____/|_| |_|_|\___|_|\__,_|
                                             
    """
    print(Fore.CYAN + banner)
    print(Fore.MAGENTA + "=" * 70 + "\n")

def main():
    print_banner()

    video_url = input(Fore.YELLOW + "Enter YouTube video URL: ").strip()
    count = int(input(Fore.YELLOW + "How many comments to analyze (e.g., 50): "))

    print()
    spinner(Fore.CYAN + "[+] Connecting to YouTube API...")
    spinner(Fore.CYAN + "[+] Fetching comments...")
    try:
        comments = fetch_comments(video_url, count)
    except ValueError as ve:
        print(Fore.RED + f"[ERROR] {ve}")
        return
    except Exception as e:
        print(Fore.RED + f"[ERROR] Failed to fetch comments: {e}")
        return

    print(Fore.GREEN + f"[+] {len(comments)} comments fetched!\n")
    time.sleep(0.5)

    spam_count = 0

    print(Fore.MAGENTA + "[+] Analyzing comments:\n")
    for idx, comment in enumerate(comments):
        sys.stdout.write(Fore.BLUE + f"[{idx+1}/{len(comments)}] ")
        sys.stdout.flush()
        time.sleep(random.uniform(0.05, 0.15))  

        comment_clean = clean_text(comment)
        X_vec = vectorizer.transform([comment_clean])
        prob = model.predict_proba(X_vec)[0][1]

        if prob >= 0.5:
            spam_count += 1
            print(Fore.RED + "[SPAM]   " + comment)
        else:
            print(Fore.GREEN + "[OK]     " + comment)

    print("\n")
    progress_bar(30, prefix="Calculating spam percentage")
    percent = spam_count / len(comments) * 100
    print(Fore.CYAN + f"\n[+] Total spam comments: {spam_count}/{len(comments)} ({percent:.2f}%)\n")

    print(Fore.MAGENTA + "=" * 70)
    print(Fore.YELLOW + "Analysis Complete! ")
    print(Fore.MAGENTA + "=" * 70 + "\n")

if __name__ == "__main__":
    main()
