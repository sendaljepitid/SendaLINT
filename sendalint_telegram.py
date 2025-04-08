import argparse
import requests
from urllib.parse import urljoin, urlparse
from colorama import Fore, Style
from tqdm import tqdm
from bs4 import BeautifulSoup
import re, json, sys, os

# === Telegram Settings ===
TELEGRAM_TOKEN = "msukin token telegram kamu punya"
TELEGRAM_CHAT_ID = "masukin id chat kamu punya"

# Output data
report = {
    "vulnerabilities": [],
    "headers": {},
    "crawled_links": []
}

visited_links = set()

payloads = {
    "xss": ["<script>alert(1)</script>", "'\"><svg/onload=alert(1)>"],
    "sqli": ["' OR '1'='1", "'; DROP TABLE users; --"],
    "open_redirect": ["//evil.com", "http://malicious.com"],
    "lfi": ["../../../../etc/passwd", "..\\..\\..\\..\\windows\\win.ini"],
    "html_injection": ["<h1>Hacked</h1>", "<b>Bold</b>"]
}

default_wordlist = [
    "admin", "backup", "config", "uploads", "images", "assets", "js", "css",
    "includes", "private", "server-status", ".git", ".svn", ".htaccess", ".env"
]

admin_paths = ["/admin", "/admin.php", "/administrator", "/login", "/admin/login"]

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; SendaLINT/1.0)"}

def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"}
        requests.post(url, data=payload)
    except:
        print(Fore.YELLOW + "[WARNING] Gagal mengirim ke Telegram." + Style.RESET_ALL)

def print_info(text): print(Fore.CYAN + "[INFO] " + Style.RESET_ALL + text)
def print_vuln(text):
    print(Fore.RED + "[VULNERABLE] " + Style.RESET_ALL + text)
    report["vulnerabilities"].append(text)
    send_telegram(f"🚨 <b>Vulnerability Found</b>\n{text}")

def show_banner():
    print(f"""{Fore.GREEN}
     _______
    //  ||\\ \\
   ||   || \\ \\
   ||___||  ||   SendaLINT+ - CLI Scanner OSINT & Vuln
   |_____|  ||   by Sendaljepitid 🐍
   |     |  ||
   |_____|  ||
  (_______)||
   \\_____/ //
{Style.RESET_ALL}
    """)

def scan_env_file(url):
    target = urljoin(url, "/.env")
    try:
        r = requests.get(target, headers=HEADERS, timeout=5)
        if "APP_KEY" in r.text or "DB_PASSWORD" in r.text:
            print_vuln(f".env file leak at {target} (Sensitive information exposure)")
    except: pass

def scan_admin_panel(url):
    for path in admin_paths:
        full_url = urljoin(url, path)
        try:
            r = requests.get(full_url, headers=HEADERS, timeout=5)
            if r.status_code == 200 and ("admin" in r.text.lower() or "login" in r.text.lower()):
                print_vuln(f"Admin Panel found at: {full_url} (Potential unauthorized access)")
        except: pass

def scan_with_payloads(url, scan_type):
    for payload in tqdm(payloads.get(scan_type, []), desc=f"Scanning {scan_type.upper()}", leave=False):
        try:
            target = f"{url}?q={payload}"
            r = requests.get(target, headers=HEADERS, timeout=5)
            c = r.text.lower()
            if scan_type == "xss" and payload in r.text:
                print_vuln(f"XSS at: {target} (Cross-site scripting vulnerability)")
            elif scan_type == "sqli" and any(e in c for e in ["sql syntax", "mysql", "pg_query", "unclosed"]):
                print_vuln(f"SQL Injection at: {target} (Possible database manipulation)")
            elif scan_type == "open_redirect" and r.status_code in [301, 302] and any(p in r.headers.get("Location", "") for p in payloads["open_redirect"]):
                print_vuln(f"Open Redirect at: {target} (Redirection to malicious site)")
            elif scan_type == "lfi" and ("root:x:0:" in c or "[extensions]" in c):
                print_vuln(f"LFI at: {target} (Local file inclusion)")
            elif scan_type == "html_injection" and any(tag in c for tag in ["<h1>hacked</h1>", "<b>bold</b>"]):
                print_vuln(f"HTML Injection at: {target} (Content manipulation)")
        except: pass

def scan_headers(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=5)
        headers = r.headers
        issues = []
        check = {
            "X-Frame-Options": "Prevent clickjacking",
            "Content-Security-Policy": "Control script sources",
            "Strict-Transport-Security": "Force HTTPS",
            "X-Content-Type-Options": "Prevent MIME sniffing",
            "Referrer-Policy": "Referrer privacy",
            "Permissions-Policy": "Feature restrictions"
        }
        for h, desc in check.items():
            if h not in headers:
                issues.append(f"Missing {h} ({desc})")
        if issues:
            for i in issues:
                print_vuln(f"Header Issue: {i}")
        report["headers"] = dict(headers)
    except: pass

def crawl_links(base_url, limit=15):
    queue = [base_url]
    domain = urlparse(base_url).netloc

    while queue and len(visited_links) < limit:
        current_url = queue.pop(0)
        if current_url in visited_links: continue
        try:
            r = requests.get(current_url, headers=HEADERS, timeout=5)
            soup = BeautifulSoup(r.text, "html.parser")
            visited_links.add(current_url)
            report["crawled_links"].append(current_url)
            for link in soup.find_all("a", href=True):
                href = link.get("href")
                full_url = urljoin(current_url, href)
                if urlparse(full_url).netloc == domain and full_url not in visited_links:
                    queue.append(full_url)
        except: continue

def directory_listing_scan(base_url, wordlist):
    print_info("📁 Scanning for directories...")
    for path in tqdm(wordlist, desc="Directory Listing", leave=False):
        full_url = urljoin(base_url, path + "/")
        try:
            r = requests.get(full_url, headers=HEADERS, timeout=5, allow_redirects=True)
            if r.status_code in [200, 401, 403]:
                if "Index of /" in r.text or "<title>Index of" in r.text:
                    print_vuln(f"Directory listing enabled at: {full_url} (May expose sensitive files)")
                else:
                    print_info(f"Found: {full_url} (Status: {r.status_code})")
        except: continue

def save_report():
    with open("vuln_result.txt", "w") as f:
        for v in report["vulnerabilities"]:
            f.write(v + "\n")
    with open("vuln_result.json", "w") as f:
        json.dump(report, f, indent=2)
    print_info("✅ Hasil disimpan di: vuln_result.txt & vuln_result.json")

def load_wordlist(file_path):
    if not file_path: return default_wordlist
    if not os.path.exists(file_path):
        print(Fore.RED + f"[ERROR] Wordlist not found: {file_path}" + Style.RESET_ALL)
        return default_wordlist
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def main():
    parser = argparse.ArgumentParser(description="SendaLINT+ CLI - OSINT & Vulnerability Scanner")
    parser.add_argument('--url', required=True, help='Target URL (e.g. https://example.com)')
    parser.add_argument('--wordlist', help='Custom wordlist file for directory scan')
    parser.add_argument('--limit', type=int, default=15, help='Crawl limit (default: 15)')
    args = parser.parse_args()

    show_banner()

    url = args.url
    wordlist = load_wordlist(args.wordlist)
    limit = args.limit

    print_info("🧭 Crawling links...")
    crawl_links(url, limit=limit)

    for link in visited_links:
        print_info(f"🔍 Scanning: {link}")
        for typ in payloads.keys():
            scan_with_payloads(link, typ)

    print_info("🔐 Header Analysis...")
    scan_headers(url)

    print_info("🔓 .env File Check...")
    scan_env_file(url)

    print_info("🔐 Admin Panel Check...")
    scan_admin_panel(url)

    print_info("📂 Directory Listing Check...")
    directory_listing_scan(url, wordlist)

    save_report()
    send_telegram("✅ <b>SendaLINT+ Scan Completed</b>\nHasil disimpan di vuln_result.txt & vuln_result.json")
    print(Fore.GREEN + "\n🎯 Selesai! Semua scan selesai dilakukan." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
