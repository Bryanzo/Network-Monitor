import subprocess

devices = [
    "8.8.8.8",
    "1.1.1.1",
    "192.168.1.1"
]

for ip in devices:
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:
        print(f"{ip} is UP")
    else:
        print(f"{ip} is DOWN")