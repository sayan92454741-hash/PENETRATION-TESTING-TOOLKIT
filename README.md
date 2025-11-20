# PENETRATION-TESTING-TOOLKIT

"COMPANY" : CODTECH IT SOLUTIONS

"NAME" : SAYAN PANIGRAHI

"INTERN ID" : CT04DR1763

"DOMAIN" : CYBER SECURITY AND ETHICAL HACKING

"DURATION" : 4 WEEKS

"MENTOR" : NEELA SANTOSH

# DESCRIBED ABOUT THE TASK

Penetration testing is an essential part of cybersecurity, used to identify security weaknesses before real attackers can exploit them. This project focuses on building two important modules commonly found in penetration testing toolkits: a Port Scanner and a Brute-Force Authentication Tester. Together, these modules help security professionals analyze system exposure, check for weak login mechanisms, and understand network vulnerabilities in a controlled, legal environment.

1. Port Scanner Module

A port scanner is a tool used to identify which network ports on a target machine are open, closed, or filtered. Every device connected to a network uses ports to send and receive data. Some ports correspond to specific services (e.g., Port 80 for HTTP, Port 443 for HTTPS, Port 22 for SSH, Port 445 for SMB, etc.). If these ports are left open unnecessarily, attackers may use them to exploit vulnerabilities or gain unauthorized access.

The port scanner created in this project performs a simple yet effective scan by sending connection requests to a range of ports defined by the user. If a connection is successfully established, the port is labeled as OPEN; if the connection is refused, it is considered CLOSED. This helps the user identify which services are accessible from the network, and whether these services pose any security risks.

For example, ports like 135, 139, and 445 are often associated with Windows networking protocols (RPC, NetBIOS, SMB). If these ports are open on a machine that does not require them, it may indicate poor configuration and a potential attack surface. By detecting open ports, administrators can take corrective action such as closing unnecessary ports, enabling firewalls, or updating vulnerable services.

2. Brute-Forcer Module

The brute-forcer module is designed to simulate password-guessing attacks in a safe and controlled environment. Brute-force attacks occur when an attacker repeatedly tries different username and password combinations until the correct one is found. Although simple, this method remains one of the most common attack techniques due to weak or reused passwords.

In this project, the brute-forcer tests credentials against a local login server, ensuring all activities remain legal and ethical. The tool iterates through a list of passwords and sends login attempts to the server. If a password matches the stored credentials, the tool identifies it as the correct password and stops the process. This feature helps users understand how weak passwords can be easily guessed, emphasizing the importance of strong authentication practices.
