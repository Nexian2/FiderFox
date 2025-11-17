FiderFrox – Safe Recon Framework

Created by NTSTeam

FiderFrox adalah safe passive recon dan light active enumeration tool untuk bug bounty hunter.
Dirancang aman, legal, dan tidak melakukan tindakan destruktif atau eksploitasi otomatis.

Features

ASCII Art “FiderFrox” dan spinner animasi saat proses berjalan

DNS Resolve dan Reverse DNS

Passive subdomain enumeration dari crt.sh

Lightweight WHOIS info (tanpa API tambahan)

Light port probing (non-agresif)

HTTP header grabbing (port 80, 443, 8080, 8443)

Output rapi dalam folder hasil:

fiderfrox_results/<target>/
├── meta.txt
├── whois_stub.txt
├── crtsh_subdomains.txt
├── ports.txt
└── http_headers.txt

Installation
Linux & macOS
git clone https://github.com/<yourname>/FiderFrox.git
cd FiderFrox
chmod +x fiderfrox.py
sudo mv fiderfrox.py /usr/local/bin/fiderfrox

Windows (Python + PowerShell)

Install Python 3

Buat file bernama fiderfrox.bat:

@echo off
python "%~dp0\fiderfrox.py" %*


Tambahkan folder berisi file tersebut ke PATH

Usage

Basic command:

fiderfrox target.com


Contoh:

fiderfrox hackerone.com

Output Example
fiderfrox_results/hackerone.com/
├── meta.txt
│   ├ target: hackerone.com
│   ├ resolved_ip: 104.16.x.x
│   └ reverse_dns: <no-reverse>
├── whois_stub.txt
├── crtsh_subdomains.txt
├── ports.txt
└── http_headers.txt

ASCII Banner
  ______ _ _           ______            _
 |  ____(_) |         |  ____|          | |
 | |__   _| | ___ __ _| |__ ___  ___  __| | ___
 |  __| | | |/ / __` |  __/ _ \/ _ \/ _` |/ _ \
 | |    | |   < (_| | | |  __/  __/ (_| |  __/
 |_|    |_|_|\_\__,_|_|  \___|\___|\__,_|\___|

                 Created by NTSTeam

Legal Disclaimer

FiderFrox hanya boleh digunakan pada target yang secara eksplisit mengizinkan pengujian keamanan, seperti:

Program bug bounty resmi

Server milik pribadi

Lingkungan lab CTF

Penulis tidak bertanggung jawab atas penggunaan yang tidak sesuai atau ilegal.

Contributing

Pull request dipersilakan.
Silakan menambahkan fitur baru, perbaikan bug, atau peningkatan dokumentasi.

License

MIT Licensem
```
