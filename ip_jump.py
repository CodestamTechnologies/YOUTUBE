import subprocess
import time
import random

def get_network_interfaces():
    result = subprocess.run("netsh interface show interface", shell=True, capture_output=True, text=True)
    interfaces = [line.split()[-1] for line in result.stdout.split('\n') if "Dedicated" in line or "Ethernet" in line]
    return interfaces

def change_ip_address(interface, ip_address, subnet_mask, gateway):
    subprocess.run(f"netsh interface ip set address name=\"{interface}\" static {ip_address} {subnet_mask} {gateway}", shell=True)

def generate_ip():
    return f"192.168.1.{random.randint(1, 254)}"

def main():
    interfaces = get_network_interfaces()
    if not interfaces:
        print("No network interfaces found.")
        return

    interface = interfaces[0]
    subnet_mask = "255.255.255.0"
    gateway = "192.168.1.1"
    
    while True:
        new_ip = generate_ip()
        print(f"Changing IP of {interface} to {new_ip}")
        change_ip_address(interface, new_ip, subnet_mask, gateway)
        time.sleep(3)

if __name__ == "__main__":
    main()
