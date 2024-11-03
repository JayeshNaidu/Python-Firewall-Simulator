# Python Firewall Simulator

This is a Python script that simulates firewall functionality by generating random IP addresses and checking them against predefined firewall rules.

## Features

- **Random IP Generation**: The script generates random IP addresses in the range `192.168.1.0` to `192.168.1.15`.
- **Firewall Rule Checking**: The IP addresses are checked against predefined firewall rules, and either `block` or `allow` actions are determined.

## How It Works

1. The script generates a random IP address using the `generate_ip_address()` function.
2. The generated IP is checked against a list of predefined firewall rules (block rules) in the `check_rule()` function.
3. If the IP matches any of the blocked IP addresses, the action is `block`; otherwise, the action is `allow`.
4. The script runs this process 12 times to simulate checking 12 random IP addresses.

## Code Structure

### `generate_ip_address()`
Generates a random IP address in the format `192.168.1.X` where `X` is a random number between 0 and 15.

### `check_rule(Ip, rules)`
Takes an IP address and a dictionary of firewall rules. If the IP matches a blocked IP in the dictionary, it returns `"block"`. Otherwise, it returns `"allow"`.

### `main()`
- Defines the firewall rules in the form of a dictionary, where the key is the IP address and the value is the action (`"block"`).
- Generates 12 random IP addresses and checks them against the firewall rules, printing the results.

## Example Output

![Output](./img/Screenshot%20(107).png)
