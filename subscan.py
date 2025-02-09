import requests
import threading
import pyfiglet

ascii_banner = pyfiglet.figlet_format("SubScan")
print(ascii_banner)


def check_subdomain(subdomain, domain):
    urls = [f"http://{subdomain}.{domain}", f"https://{subdomain}.{domain}"]
    headers = {"User-Agent": "Mozilla/5.0"}

    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=2)
            print(f"[*] {url} aktif, ({response.status_code})")
            return 
        except requests.RequestException:
            pass  


domain = input("Domain girin:  ")
wordlist_path = input("Wordlist yolunu girin:  ")

try:
    with open(wordlist_path, "r") as f:
        subdomains = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print("Hata: Wordlist dosyası bulunamadı")
    exit()

threads = []
for sub in subdomains:
    thread = threading.Thread(target=check_subdomain, args=(sub, domain))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    