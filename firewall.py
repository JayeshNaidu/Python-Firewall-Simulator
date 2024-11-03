#Jayesh

import random

#Generating a random IP
def generate_ip_address():
    return f"192.168.1.{random.randint(0,15)}"

#checking Firewall Rules
def check_rule(Ip,rules):
    for rule_ip,action in rules.items():
        if Ip == rule_ip:
            return action
    return "allow" 


def main():
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.6": "block",
        "192.168.1.10": "block",
        "192.168.1.13": "block",
        "192.168.1.15": "block"
    }

    for _ in range(12):
        Ip = generate_ip_address()
        action = check_rule(Ip, firewall_rules)
        print(f"IP: {Ip} , Action: {action}")
        

main()