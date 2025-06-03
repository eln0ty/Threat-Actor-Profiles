from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
import json

def init_driver(socks_port):
    options = Options()
    options.headless = True

    options.set_preference("network.proxy.type", 1)
    options.set_preference("network.proxy.socks", "127.0.0.1")
    options.set_preference("network.proxy.socks_port", socks_port)
    options.set_preference("network.proxy.socks_remote_dns", True)

    return webdriver.Firefox(options=options)

def scrape_rhysida_victims(url, socks_port):
    driver = init_driver(socks_port)
    try:
        print(f"[+] Trying with SOCKS port {socks_port}...")
        driver.get(url)
        time.sleep(10)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        print(soup)
        victims = []

        entries = soup.select(".carousel-item")
        for entry in entries:
            try:
                name_tag = entry.select_one("div.h4 a")
                victim = name_tag.get_text(strip=True) if name_tag else "Unknown"

                desc_tag = name_tag.find_parent().find_next_sibling("div")
                description = desc_tag.get_text(strip=True) if desc_tag else ""

                time_tag = entry.select_one(".timer")
                date_listed = time_tag.get_text(strip=True) if time_tag else ""

                leaked_files = len(entry.select("img"))

                victims.append({
                    "victim": victim,
                    "description": description,
                    "date_listed": date_listed,
                    "leaked_files": leaked_files,
                    "status": "data posted"
                })
            except Exception:
                continue

        return victims
    finally:
        driver.quit()

def main():
    url = "http://rhysidafohrhyy2aszi7bm32tnjat5xri65fopcxkdfxhi4tidsg7cad.onion/"

    try:
        victims = scrape_rhysida_victims(url, 9050)
    except WebDriverException as e:
        print("[!] Failed on port 9050, trying 9150...")
        try:
            victims = scrape_rhysida_victims(url, 9150)
        except WebDriverException as e2:
            print("[X] Failed to connect using both 9050 and 9150.")
            return

    print(json.dumps(victims, indent=2))

if __name__ == "__main__":
    main()



"""
                                                            *****************  
                                                            * OUTPUT Example*
                                                            *****************
[
  {
    "victim": "Cator Ruma & Associates",
    "description": "Since our founding in 1959, Cator, Ruma & Associates has worked with many architects and clients to build thriving communities across the western and central United States.",
    "date_listed": "5 days 03:28:22",
    "leaked_files": 3,
    "status": "data posted"
  },
  {
    "victim": "Carrera Chevrolet",
    "description": "",
    "date_listed": "2 days 20:23:22",
    "leaked_files": 4,
    "status": "data posted"
  }
]
"""
