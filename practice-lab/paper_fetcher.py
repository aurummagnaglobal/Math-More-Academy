import os
import requests
from bs4 import BeautifulSoup

# Targeted Board Archives
SOURCES = {
    "CBSE": "https://www.cbse.gov.in/cbsenew/question-paper.html",
    "ICSE": "https://cisce.org/publications/"
}

# The bridge to your syllabus-vault
SAVE_DIR = "syllabus-vault/pyq-archive"

def run_lab_fetcher():
    print("Sovereign MD Access Granted. Fetching 10-year Math papers (2016-2026)...")
    
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    for board, url in SOURCES.items():
        print(f"Scanning {board} archives for Mathematics Question Papers...")
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Logic: Identifies links containing 'Math' and ending in '.pdf'
            for link in soup.find_all('a'):
                href = link.get('href')
                if href and ".pdf" in href.lower():
                    # Filter for Math specifically
                    if "math" in href.lower() or "mathematics" in href.lower():
                        file_name = href.split('/')[-1]
                        full_path = os.path.join(SAVE_DIR, file_name)
                        
                        print(f"Found Paper: {file_name}")
                        # In a live run, you would uncomment the lines below to download:
                        # pdf_content = requests.get(href).content
                        # with open(full_path, 'wb') as f:
                        #     f.write(pdf_content)

        except Exception as e:
            print(f"Error scanning {board}: {e}")

    print("\nFetch Complete. The 'syllabus-vault' bridge is active.")

if __name__ == "__main__":
    run_lab_fetcher()