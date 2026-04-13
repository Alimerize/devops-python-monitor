import os
import subprocess
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def check_nginx() -> str:
    status = subprocess.run(['pgrep', 'nginx'], capture_output=True)

    if status.returncode == 0:
        return "Active"
    else:
        return "Down"

def save_report(status):
    report = {
        "timestamp": str(datetime.now()),
        "service": "nginx",
        "status": status
    }
    with open("health_check.json", "w") as f:
        json.dump(report, f, indent=4)



if __name__ == "__main__":
    admin_token = os.getenv("ADMIN_TOKEN")
    if admin_token:
        current_status = check_nginx()
        print(f"Статус сервиса: {current_status}")
        save_report(current_status)
    else:
        print("Ошибка: Нет токена доступа!")
