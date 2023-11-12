import sys
import socket
import json
import requests
from pyfiglet import Figlet


def get_ipinfo(ip_address):
    try:
        response = requests.get(f'http://ipinfo.io/{ip_address}/json')
        ipinfo_data = response.json()
        return ipinfo_data
    except Exception as e:
        print(f"Error getting IP information from ipinfo: {e}")
        return None

def get_system_info():
    try:
        system_info = {
            'platform': sys.platform,
            'version': sys.version,
            'hostname': socket.gethostname(),
        }
        return system_info
    except Exception as e:
        print(f"Error getting system information: {e}")
        return None

def main():
    f = Figlet(font='slant')
    print(f.renderText("IP-Sharingan"))
    print("\t \t \t \t \t \t @by Faizal Imam")

    user_input = input("Enter an IP address: ")
    system_info = get_system_info()

    if system_info:
        ip_info = get_ipinfo(user_input)

        if ip_info:
            data = {'system_info': system_info, 'ip_info': ip_info}
            print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
