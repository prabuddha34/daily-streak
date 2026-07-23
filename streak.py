from datetime import datetime

with open("README.md", "w") as f:
    f.write("# Daily Streak\n\n")
    f.write(f"Updated: {datetime.utcnow()} UTC\n")
