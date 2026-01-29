# Time and timestamp utilities

import time


def timestamp_ms():
    # Get current timestamp in milliseconds (for logging)
    return int(time.time() * 1000)


def format_duration(seconds):
    # Format duration to human-readable string like "2m 15.3s"
    if seconds < 60:
        return f"{seconds:.1f}s"
    minutes = int(seconds // 60)
    secs = seconds % 60
    return f"{minutes}m {secs:.1f}s"
