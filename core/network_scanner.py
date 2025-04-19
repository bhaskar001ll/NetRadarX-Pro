import subprocess
from db.db_handler import create_connection, create_table, insert_result
from utils.helpers import format_scan_results

def scan_network(interface='wlp0s20f3'):
    """
    Scans the local network for devices using arp-scan.

    Parameters:
    interface (str): The network interface to use for scanning (default is 'wlp0s20f3').

    Returns:
    str: A string containing the scan results or an error message.
    """
    try:
        result = subprocess.run(
            ['sudo', 'arp-scan', '--interface=' + interface, '--localnet'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        if result.returncode != 0:
            return f"Error during scan:\n{result.stderr.strip()}"
        
        # Format the output for better readability
        formatted_output = format_scan_results(result.stdout)
        
        # Database connection
        conn = create_connection("scan_results.db")
        if conn is not None:
            # Create table if it doesn't exist
            create_table(conn)
            # Insert results into the database
            for line in result.stdout.strip().split('\n'):
                parts = line.split()
                if len(parts) >= 2:
                    device = parts[0]  # Assuming the first part is the device name
                    ip = parts[1]      # Assuming the second part is the IP address
                    insert_result(conn, device, ip)
            conn.close()
        
        return formatted_output

    except Exception as e:
        return f"Exception occurred:\n{str(e)}"