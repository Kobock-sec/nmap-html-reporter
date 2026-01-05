#!/usr/bin/env python3
# ----------------------------------------
# Project : Nmap HTML Reporter
# Author  : Kobock
# GitHub  : https://github.com/Kobock-sec
# License : MIT
# ----------------------------------------

VERSION = "1.1"

BANNER = f"""
=====================================
   Nmap HTML Reporter v{VERSION}
   Author : Kobock
   GitHub : https://github.com/kobock-sec
=====================================
"""

print(BANNER)

import argparse
import xml.etree.ElementTree as ET
from datetime import datetime

# === CLI Arguments ===
parser = argparse.ArgumentParser(description="Convert Nmap XML scan to HTML report")
parser.add_argument("-i", "--input", required=True, help="Input Nmap XML file")
parser.add_argument("-o", "--output", required=True, help="Output HTML file")
parser.add_argument("--open-only", action="store_true", help="Show only open ports")
args = parser.parse_args()

INPUT_FILE = args.input
OUTPUT_FILE = args.output
OPEN_ONLY = args.open_only

# === متغيرات التاريخ ===
scan_date = datetime.now().strftime("%Y-%m-%d %H:%M")

# === Parse XML ===
tree = ET.parse(INPUT_FILE)
root = tree.getroot()

# === تجميع جداول جميع Hosts ===
host_tables = ""

for host in root.findall("host"):
    target = "Unknown"
    rows = ""
    open_ports_count = 0

    address = host.find("address")
    if address is not None:
        target = address.get("addr")

    # المرور على جميع المنافذ لهذا Host
    for port in host.findall(".//port"):
        port_id = port.get("portid")
        state = port.find("state").get("state")
        service = port.find("service").get("name")

        # عدّ المنافذ المفتوحة
        if state == "open":
            open_ports_count += 1

        # فلترة المنافذ المفتوحة فقط
        if OPEN_ONLY and state != "open":
            continue

        # تحديد لون كل حالة
        if state == "open":
            css = "open"
        elif state == "closed":
            css = "closed"
        else:
            css = "filtered"

        rows += f"""
        <tr>
            <td>{port_id}</td>
            <td class="{css}">{state}</td>
            <td>{service}</td>
        </tr>
        """

    # إنشاء جدول HTML كامل لكل Host
    host_table = f"""
    <h2>Target: {target}</h2>
    <div class="info">
        <p><strong>Scan Date:</strong> {scan_date}</p>
        <p><strong>Open Ports:</strong> {open_ports_count}</p>
    </div>
    <table>
        <tr>
            <th>Port</th>
            <th>Status</th>
            <th>Service</th>
        </tr>
        {rows}
    </table>
    <hr>
    """
    host_tables += host_table

# === قراءة قالب HTML ===
with open("template.html", "r") as f:
    html = f.read()

# === استبدال مكان Host Tables في القالب ===
html = html.replace("{{HOST_TABLES}}", host_tables)

# === كتابة التقرير النهائي ===
with open(OUTPUT_FILE, "w") as f:
    f.write(html)

print("[+] Report created:", OUTPUT_FILE)
if OPEN_ONLY:
    print("[+] Showing only open ports")


