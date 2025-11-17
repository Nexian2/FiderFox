#!/usr/bin/env python3
import argparse
import time
import sys
import threading
import os

# ============================
# ASCII Banner
# ============================
BANNER = r"""
███████╗██╗██████╗ ███████╗██████╗ ███████╗██████╗ ██████╗  ██████╗ ██╗  ██╗
██╔════╝██║██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██║  ██║
█████╗  ██║██████╔╝█████╗  ██████╔╝█████╗  ██████╔╝██████╔╝██║   ██║███████║
██╔══╝  ██║██╔══██╗██╔══╝  ██╔══██╗██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██║
██║     ██║██║  ██║███████╗██║  ██║███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
                       Created by NTSTeam
"""

# ============================
# Loading Animation
# ============================
loading = False

def animate(text="Processing"):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if not loading:
            break
        sys.stdout.write(f'\r{text} ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r')


# ============================
# Placeholder Handlers
# (You can replace with actual recon funcs)
# ============================
def passive_recon(target):
    print(f"\n[+] Passive recon on: {target}")
    time.sleep(2)
    print("[+] (placeholder) Subdomain enumeration done.")
    print("[+] (placeholder) HTTP tech fingerprint done.")


def port_scan(target):
    print(f"\n[+] Port scan on: {target}")
    time.sleep(2)
    print("[+] (placeholder) Port scan done.")


def dirsearch(target, wordlist=None):
    print(f"\n[+] Directory search on: {target}")
    if wordlist:
        print(f"[+] Using wordlist: {wordlist}")
    time.sleep(2)
    print("[+] (placeholder) Directory brute-force done.")


def full_recon(target):
    print(f"\n[+] Running full recon workflow on: {target}")
    time.sleep(2)
    passive_recon(target)
    port_scan(target)
    dirsearch(target)


# ============================
# Main CLI
# ============================
def main():
    parser = argparse.ArgumentParser(
        description="FiderFrox - Safe Bug Bounty Recon Tool"
    )

    parser.add_argument("target", help="Target domain/IP")
    
    parser.add_argument("--passive", action="store_true", help="Run passive recon only")
    parser.add_argument("--scan", action="store_true", help="Run port scan")
    parser.add_argument("--dir", action="store_true", help="Directory brute-force")
    parser.add_argument("--wordlist", help="Custom wordlist for dir scan")
    parser.add_argument("--full", action="store_true", help="Run full recon workflow")
    
    args = parser.parse_args()
    target = args.target

    print(BANNER)

    # valid command check
    if not (args.passive or args.scan or args.dir or args.full):
        print("[!] No mode selected. Use -h to see available commands.")
        sys.exit(1)

    # start loading animation
    global loading
    loading = True
    t = threading.Thread(target=animate, args=("Running",))
    t.start()

    try:
        time.sleep(1)
        loading = False
        t.join()
        print("\n")

        if args.full:
            full_recon(target)

        if args.passive:
            passive_recon(target)

        if args.scan:
            port_scan(target)

        if args.dir:
            dirsearch(target, args.wordlist)

    except KeyboardInterrupt:
        loading = False
        print("\n[!] Process interrupted.")

if __name__ == "__main__":
    import itertools
    main()
