# OpenVPN Access Server post_auth script for preventing v3.5.0 clients from connecting.
# Version: 1.0
# Contributions by:
# - Kevin Lim Chu Chen
#
# It adds an additional check when authentication is done through the VPN connection.
# It applies to all 3 connection profiles types (server-locked, user-locked, auto-login).
# 
# How to use:
# 1. To install, Run the command below to activate the script. --value_file should be the path of the script.
# cd /usr/local/openvpn_as/scripts
# ./sacli --key "auth.module.post_auth_script" --value_file=/usr/local/openvpn_as/scripts/openvpn_deny_client_below_v3.5.0.py ConfigPut
# ./sacli start
#
# 2. To Remove, Run the command below to deactivate the script.
# cd /usr/local/openvpn_as/scripts
# ./sacli --key "auth.module.post_auth_script" ConfigDel
# ./sacli start
#
# Script last updated in Feb 2025

from pyovpn.plugin import *

def post_auth(authcred, attributes, authret, info):
        
    def is_version_lower(version_str, threshold="3.5.0"):
        # Convert versions into tuples of integers (e.g., "3.6.0" → (3, 6, 0))
        version_tuple = tuple(map(int, version_str.split('-')[0].split('.')))
        threshold_tuple = tuple(map(int, threshold.split('.')))
        
        return version_tuple < threshold_tuple  # Compare tuples directly
    
    client_version = attributes.get("client_info", {}).get("UV_ASCLI_VER")

    print("\n\n\n****************************************************************************************\n\n\n")
    print("POST_AUTH %s %s %s %s" % (authcred, attributes, authret, info))
    print("\n\n\n****************************************************************************************\n\n\n")

    # Check and deny user if version is lower than 3.5.0
    threshold_version = "3.5.0"
    if client_version and is_version_lower(client_version, threshold_version):
        authret["status"] = 1 #deny access
        authret["client_reason"] = "Access Denied: Client version is too old. Please upgrade to version" + threshold_version + "or higher."
        print("Access Denied: Client version is too old. Please upgrade to version" + threshold_version + "or higher.")

    return authret
