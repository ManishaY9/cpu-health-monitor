import psutil
import time

def monitor_cpu_usage(threshold=80, check_interval=5):
    """
    Continuously monitor CPU usage and alert when threshold is exceeded.
    
    Args:
        threshold (int): CPU usage percentage threshold for alerting. Defaults to 80%.
        check_interval (int): Time interval between CPU usage checks in seconds. Defaults to 5 seconds.
    """
    print(f"Monitoring CPU usage... (Threshold: {threshold}%)")
    print("Press CTRL+C to stop monitoring.")
    
    try:
        while True:
            # Get current CPU usage percentage
            cpu_percent = psutil.cpu_percent(interval=1)
            
            # Check if CPU usage exceeds threshold
            if cpu_percent > threshold:
                print(f"\nAlert! CPU usage exceeds threshold: {cpu_percent}%")
            
            # Optional: Print current usage for context
            print(f"Current CPU Usage: {cpu_percent}%", end='\r')
            
            # Wait before next check
            time.sleep(check_interval)
    
    except KeyboardInterrupt:
        # Handle manual interruption (CTRL+C)
        print("\n\nCPU monitoring stopped by user.")
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"\nAn error occurred during monitoring: {e}")

if __name__ == "__main__":
    # Run the monitoring function with default threshold
    monitor_cpu_usage()