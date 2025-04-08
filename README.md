# SendaLINT
Gabungan dari Sendal + Lint (scanner) Cocok untuk tools yang “ngecek” kerentanan website sambil “nyepak” bug kayak sendal jepit.

# 🩴 SendaLINT - Web Vulnerability Scanner Sederhana Tapi Nyepak!

**SendaLINT** adalah tools pemindai kerentanan berbasis Python yang dirancang untuk memudahkan para pemula atau pentester santai dalam melakukan uji keamanan web. Namanya terinspirasi dari **sendal jepit** – sederhana, praktis, tapi kalau nyepak bisa kena bug langsung!

---

## 🧠 Filosofi

> "Karena nggak semua pahlawan pakai sepatu."

SendaLINT berasal dari gabungan kata **Sendal** dan **Lint (scanner)**.
- **Sendal**: Simbol kesederhanaan dan kecepatan gerak tanpa ribet.
- **Lint**: Seperti *code linter*, tools ini membantu menemukan potensi masalah — tapi dalam hal ini adalah **bug dan celah keamanan** di website!

---

## 🛠️ Fitur

- 🔍 Scan **XSS (Cross-site Scripting)**
- 💥 Scan **SQL Injection**
- 🔁 Scan **Open Redirect**
- 📂 Scan **Local File Inclusion (LFI)**
- 🧬 Scan **HTML Injection**
- 🧾 Cek kebocoran **`.env` file**
- 🔓 Deteksi **admin panel exposure**
- 🧨 **ALL-IN-ONE Mode** (scan semua sekaligus!)

---

## ⚠️ Disclaimer
Tools ini hanya untuk tujuan edukasi dan riset.
DILARANG digunakan pada sistem tanpa izin.
Gunakan dengan tanggung jawab, karena sendal bisa nyepak balik kalau salah langkah.

---
- XSS
- SQL Injection
- LFI (Local File Inclusion)
- Open Redirect
- HTML Injection
- .env Leak
- Directory Listing
- Admin Panel Exposure
- Security Header Check

> 🔍 Cocok untuk edukasi, lab praktikum keamanan siber, atau pentesting awal secara ringan dan cepat.

---

## ✨ Fitur Unggulan

- ✅ CLI interface untuk penggunaan cepat
- 🌐 Crawling link dalam domain
- 🔍 Scanner payload XSS, SQLi, Open Redirect, LFI, HTML Injection
- 📁 Scanner direktori dari wordlist
- 🔐 Pendeteksi admin panel login
- 🔓 Deteksi file `.env` bocor
- 🧠 Pemeriksaan keamanan header HTTP
- 📦 Simpan hasil dalam format `.txt` dan `.json`

---

## 🚀 Instalasi

### 1. Clone Repositori

```bash
git clone https://github.com/sendaljepitid/sendalint.git
cd sendalint

```

### 2. Install Dependency

Pastikan kamu menggunakan Python 3.7 ke atas. Lalu install dependencies:

```bash
pip install -r requirements.txt
```

Isi `requirements.txt`:
```
requests
beautifulsoup4
colorama
tqdm
```

---

## 🧪 Cara Penggunaan

### Basic Scan

```bash
python sendalint.py --url https://target.com
```

### Gunakan Wordlist Kustom

```bash
python sendalint.py --url https://target.com --wordlist mywordlist.txt
```

### Atur Jumlah Maksimum Link yang Di-crawl

```bash
python sendalint.py --url https://target.com --limit 30
```

---

## 📁 Contoh Output

- `vuln_result.txt`: hasil kerentanan dalam bentuk list.
- `vuln_result.json`: hasil lengkap termasuk headers & link yang di-scan.

---

## ⚠️ Catatan

- Gunakan tools ini hanya untuk **tujuan edukasi dan pentest legal**.
- Jangan gunakan terhadap sistem tanpa izin. Ini bisa melanggar hukum!

---

## 🙌 Kontribusi

Pull request sangat diterima! Jika kamu punya saran fitur baru atau ingin menambahkan payload, langsung saja fork dan kirim PR.

---

## 🧑‍💻 Author

Budi Wibowo - [LinkedIn]([https://www.linkedin.com/in/budiwibowo-/])

---
## jika error muncul
~/sendalint# python3 sendalint.py  --url http://testphp.vulnweb.com/index.php
Traceback (most recent call last):
  File "/root/sendalint/sendalint.py", line 5, in <module>
    from tqdm import tqdm
ModuleNotFoundError: No module named 'tqdm'

✅ Opsi 1: Install via APT (cara direkomendasikan)
Karena kamu hanya butuh tqdm, install langsung lewat APT:

```bash
sudo apt update
sudo apt install python3-tqdm

```

---


## 📜 License

MIT License – bebas digunakan, mohon sertakan atribusi jika dibagikan ulang.
```

---



