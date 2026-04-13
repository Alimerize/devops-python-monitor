# 🚀 Auto-Admin Monitoring Tool

A lightweight Python automation tool designed for system administrators to monitor service health and log status reports.

## 📌 Project Overview
This tool automates the routine task of checking critical system services (like Nginx). It uses system-level calls to verify if a process is running, handles security through environment variables, and generates structured reports.

## 🛠 Features
- **Proactive Monitoring**: Checks service status using `subprocess`.
- **Security First**: Sensitive data is managed via `.env` files (never hardcoded).
- **Structured Logging**: Saves health check history into a valid JSON format.
- **Developer Friendly**: Clean code with error handling and type hints.

## ⚙️ Installation & Setup

1. **Clone the repo:**
    ```
    git clone https://github.com
    cd auto-admin-tool
    ```

2. **Set up virtual environment (recommended):**
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

4. **Environment Variables:**
   Rename .env.example to .env
   Set your ADMIN_TOKEN and other credentials.
5. **🚀 Usage**
   Run the script manually or set it up as a Cron job:
    ```
    python3 src/admin_tool.py
    ```

## 📊 Technical Stack
**Language:** Python 3.10+
**Libraries:** python-dotenv, requests
**Formats:** JSON, .env
