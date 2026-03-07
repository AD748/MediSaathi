import json
import time


def log_latency(metrics):

    entry = {
        "timestamp": time.time(),
        "metrics": metrics
    }

    with open("latency_logs.json", "a") as f:
        f.write(json.dumps(entry) + "\n")