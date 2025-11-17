# FiderFrox

Lightweight and safe reconnaissance tool for bug bounty research.

## Features

-   Single-command recon workflow
-   Subdomain enumeration
-   Port scanning
-   HTTP service probing
-   Directory discovery (optional)
-   Built-in animated CLI renderer
-   Runs from any directory
-   Designed for legal and permission-based bug bounty programs

## Preview

    ███████╗██╗██████╗ ███████╗██████╗ ███████╗██████╗ ██████╗  ██████╗ ██╗  ██╗
    ██╔════╝██║██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗██║  ██║
    █████╗  ██║██████╔╝█████╗  ██████╔╝█████╗  ██████╔╝██████╔╝██║   ██║███████║
    ██╔══╝  ██║██╔══██╗██╔══╝  ██╔══██╗██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██║
    ██║     ██║██║  ██║███████╗██║  ██║███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
                        Created by NTSTeam

## Installation

Clone repository:

``` bash
git clone https://github.com/USERNAME/fiderfrox.git
cd fiderfrox
```

Make executable:

``` bash
chmod +x fiderfrox.py
```

Install globally:

``` bash
sudo mv fiderfrox.py /usr/local/bin/fiderfrox
```

## Usage

Basic recon:

``` bash
fiderfrox example.com
```

Save output:

``` bash
fiderfrox example.com -o results.txt
```

Directory brute force:

``` bash
fiderfrox example.com --dir
```

Custom wordlist:

``` bash
fiderfrox example.com --dir --wordlist /path/to/wordlist.txt
```

Verbose mode:

``` bash
fiderfrox example.com -v
```

## Output

-   subdomains.txt
-   ports.txt
-   http_services.txt
-   directories.txt (optional)

## Legal Notice

Use only on targets where you have explicit permission.

## Credits

Created by NTSTeam
