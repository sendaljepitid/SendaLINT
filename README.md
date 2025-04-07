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
