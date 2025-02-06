# openvpn-auth-hook
OpenVPN Access Server post-authentication script to block outdated clients (below v3.5.0) from connecting. Ensures security compliance by enforcing minimum client version requirements.

# OpenVPN Access Server Post-Auth Script

## Overview
This script is designed for OpenVPN Access Server to prevent clients using versions lower than `v3.5.0` from connecting. It applies to all three connection profile types:
- Server-locked
- User-locked
- Auto-login

The script executes as a **post-authentication hook** and checks the client's version upon authentication. If the client's version is below `v3.5.0`, the connection attempt will be denied with an appropriate message.

## Features
- Ensures security compliance by blocking outdated OpenVPN client versions.
- Works automatically upon user authentication.
- Provides a user-friendly error message for denied clients.
- Compatible with OpenVPN Access Server authentication workflow.

## Installation
### 1. Deploy the script
Ensure you have SSH access to your OpenVPN Access Server and place the script in the appropriate directory:
```bash
cd /usr/local/openvpn_as/scripts
nano openvpn_deny_client_below_v3.5.0.py
```
Paste the script content and save the file.

### 2. Activate the script
Run the following command to set the post-auth script:
```bash
cd /usr/local/openvpn_as/scripts
./sacli --key "auth.module.post_auth_script" --value_file=/usr/local/openvpn_as/scripts/openvpn_deny_client_below_v3.5.0.py ConfigPut
./sacli start
```

## Uninstallation
To remove the script and restore default authentication behavior, execute:
```bash
cd /usr/local/openvpn_as/scripts
./sacli --key "auth.module.post_auth_script" ConfigDel
./sacli start
```

## How It Works
1. The script extracts the **client version** from the authentication attributes.
2. It compares the client's version against the defined threshold (`v3.5.0`).
3. If the client version is lower, access is denied with a clear error message.
4. If the client meets the required version, authentication proceeds normally.

## Example Logs
Upon execution, the script logs details of the authentication attempt:
```
****************************************************************************************
POST_AUTH {username} {attributes} {authret} {info}
****************************************************************************************
Access Denied: Client version is too old. Please upgrade to version 3.5.0 or higher.
```

## Script Details
- **File:** `openvpn_deny_client_below_v3.5.0.py`
- **Last Updated:** February 2025
- **Author:** Kevin Lim Chu Chen
- **Version:** 1.0

## License
This script is provided as-is with no warranties. Use at your own discretion.

## Contributing
Contributions and improvements are welcome! Feel free to submit a pull request or report issues.

---
This script ensures that only clients with the appropriate security updates can connect, improving overall VPN security and compliance.

