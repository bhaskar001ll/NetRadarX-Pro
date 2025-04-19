def format_scan_results(results):
    """
    Format the scan results for better readability.

    Parameters:
    results (str): The raw scan results.

    Returns:
    str: Formatted scan results.
    """
    devices = results.strip().split('\n')
    formatted_output = "Devices found:\n" + "\n".join(devices)
    return formatted_output