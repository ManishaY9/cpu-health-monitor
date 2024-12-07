# CPU Usage Monitor

A simple Python script to continuously monitor CPU usage and alert when the usage exceeds a specified threshold. This script is particularly useful for tracking system performance and identifying potential bottlenecks in real-time.

## Features
- Monitors CPU usage at regular intervals.
- Alerts when CPU usage exceeds the specified threshold.
- Easy-to-use, with customizable parameters for threshold and check intervals.
- Handles interruptions gracefully (e.g., CTRL+C).

---

## Requirements

- Python 3.6 or higher
- [psutil](https://pypi.org/project/psutil/) library


Install `psutil` using pip:

```bash
pip install psutil
```

### Basic Usage
```bash
python cpu_monitor.py
```

### Advanced Usage with Custom Parameters
```python
# Customize threshold and check interval
monitor_cpu_usage(threshold=85, check_interval=3)
```

### Parameters
- `threshold` (optional): CPU usage percentage to trigger alerts (default: 80)
- `check_interval` (optional): Time between CPU usage checks in seconds (default: 5)

## Example Output
```
Monitoring CPU usage... (Threshold: 80%)
Press CTRL+C to stop monitoring.
Current CPU Usage: 75%
Alert! CPU usage exceeds threshold: 85%
Current CPU Usage: 90%
```

## Stopping the Monitor
- Press `CTRL+C` to gracefully stop the monitoring process

## Customization
You can easily modify the script to:
- Change alert threshold
- Adjust monitoring frequency
- Add logging or notification mechanisms

