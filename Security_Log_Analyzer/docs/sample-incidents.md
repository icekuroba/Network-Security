# Sample Incidents

## Incident 1: SSH Brute Force Attempt

Source IP:

192.168.56.20

Summary:

The source generated 5 failed SSH login attempts against different users.

Impact:

This may indicate an automated brute force attempt.

Recommended response:

- Restrict SSH to trusted IP addresses.
- Disable password login if possible.
- Use SSH keys.
- Monitor repeated authentication failures.

## Incident 2: Web Probing

Source IP:

192.168.56.44

Summary:

The source requested suspicious paths such as:

- /admin
- /wp-admin
- /.env
- /etc/passwd
- /phpmyadmin

Impact:

This may indicate automated reconnaissance or directory probing.

Recommended response:

- Review web server logs.
- Confirm sensitive files are not exposed.
- Block abusive sources if behavior continues.

## Incident 3: Firewall Blocked Traffic

Source IPs:

192.168.56.60
192.168.56.61

Summary:

The firewall blocked connection attempts to ports such as SSH, RDP, and MySQL.

Recommended response:

- Review firewall rules.
- Confirm these services are not publicly exposed.
- Continue monitoring blocked attempts.
