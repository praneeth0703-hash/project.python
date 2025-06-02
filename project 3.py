# Simple Firewall Rule Checker (No packet sniffing)

# Sample blocked IPs and ports
BLOCKED_IPS = ["192.168.0.5", "10.0.0.10"]
BLOCKED_PORTS = [80, 21, 23]  # HTTP, FTP, Telnet

# Function to simulate checking a request
def firewall_check(ip, port):
    if ip in BLOCKED_IPS:
        print(f"[BLOCKED] Connection from {ip} is blocked.")
    elif port in BLOCKED_PORTS:
        print(f"[BLOCKED] Port {port} is restricted.")
    else:
        print(f"[ALLOWED] Connection from {ip} on port {port} is allowed.")

# Main loop
print("=== Simple Firewall Rule Checker ===")
while True:
    ip_input = input("Enter source IP (or 'exit' to quit): ")
    if ip_input.lower() == 'exit':
        break

    try:
        port_input = int(input("Enter destination port: "))
    except ValueError:
        print("Invalid port. Please enter a number.")
        continue

    firewall_check(ip_input, port_input)

