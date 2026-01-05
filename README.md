# Nmap HTML Reporter

A simple Python tool to convert **Nmap XML scans** into clean and readable
**HTML reports**.

---

## 🖼️ Screenshots

### Dark Mode
![HTML Report Dark Mode](darkmode.png)

### Light Mode
![HTML Report Light Mode](lightmode.png)

---

## ✨ Features

- Supports **multiple hosts**
- Shows **only open ports** with `--open-only` option
- Displays **scan date** and **number of open ports**
- Color-coded tables for port states
- **Dark mode** toggle
- Easy to use with CLI arguments

---

## 📦 Requirements

- Python 3
- Nmap

---

## 🛠️ Installation

```bash
git clone https://github.com/kobock-sec/nmap-html-report.git
cd nmap-html-report

🚀 Usage
1️⃣ Run Nmap scan

nmap scanme.nmap.org -oX scan.xml

2️⃣ Generate HTML report

python3 parser.py -i scan.xml -o report.html --open-only

3️⃣ Open the report


explorer.exe report.html


👤 Author

Name: Kobock

Country: Algeria 🇩🇿

GitHub: https://github.com/kobock-sec

This tool was created for educational and ethical security testing purposes.

⚠️ Legal Disclaimer

This tool is intended for educational purposes only.

Do NOT scan any system, network, or website without explicit permission.
The author is not responsible for any misuse of this tool.
