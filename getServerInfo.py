import requests
from bs4 import BeautifulSoup

url = 'https://www.battlemetrics.com/servers/rust/30290660'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the container div
container = soup.find('div', class_='col-md-6 server-info')

if container:
    # Find the definition list inside the container
    dl = container.find('dl')
    
    # Extract all <dt> and <dd> tags inside the <dl>
    dts = dl.find_all('dt')
    dds = dl.find_all('dd')
    
    # Assuming <dt> and <dd> are paired in order
    for dt, dd in zip(dts, dds):
        key = dt.get_text(strip=True)
        
        # Sometimes <dd> contains nested tags, extract meaningful text carefully:
        # Use .stripped_strings to get all text fragments inside dd, join by space
        value = ' '.join(dd.stripped_strings)
        
        print(f"{key}: {value}")

else:
    print("Server info container not found")
