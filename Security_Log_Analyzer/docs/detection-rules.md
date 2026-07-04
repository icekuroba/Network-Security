# Detection Rules

## SSH Brute Force Attempt

Source: `sample_auth.log`

Condition:

- The same source IP generates 5 or more failed SSH login attempts.

Severity:

- HIGH

Recommendation:

- Restrict SSH access.
- Use key-based authentication.
- Use firewall allowlists.
- Consider fail2ban.

## Suspicious Web Probing

Source: `sample_nginx_access.log`

Condition:

- A source IP requests suspicious paths such as:
  - `/admin`
  - `/wp-admin`
  - `/.env`
  - `/etc/passwd`
  - `/phpmyadmin`

Severity:

- HIGH

Recommendation:

- Review web logs.
- Block abusive IPs.
- Ensure sensitive files are not exposed.

## Multiple HTTP 404 Errors

Source: `sample_nginx_access.log`

Condition:

- A source IP generates 5 or more HTTP 404 responses.

Severity:

- MEDIUM

Recommendation:

- Investigate possible directory brute forcing or automated scanning.

## Firewall Blocked Traffic

Source: `sample_ufw.log`

Condition:

- UFW blocks one or more connection attempts from a source IP.

Severity:

- MEDIUM

Recommendation:

- Review firewall logs.
- Block repeated suspicious sources.
- Validate exposed services.
