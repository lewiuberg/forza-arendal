import requests
from bs4 import BeautifulSoup

# Define the URL
urls = [
    "https://www.fotball.no/fotballdata/lag/tabell/?fiksId=133618",
    "https://www.fotball.no/fotballdata/lag/tabell/?fiksId=210300",
]

tables: list = []

# Define headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def fetch_table_data(url):
    # Fetch the page content
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad status codes

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all tables on the page
    tables_on_page = soup.find_all("table")  # Adjust the selector if necessary

    # Extract data from each table
    all_tables_data = []
    for table in tables_on_page:
        table_data = []
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all(["th", "td"])
            cell_data = [cell.get_text(strip=True) for cell in cells]
            table_data.append(cell_data)  # Collect row data
        all_tables_data.append(table_data)

    if not all_tables_data:
        print(f"No tables found on the page: {url}")
    return all_tables_data


# fetch the table data for each URL and store it in the tables list
for url in urls:
    print(f"Fetching data from {url}")
    tables_from_url = fetch_table_data(url)
    tables.extend(tables_from_url)  # Add each table as a separate entry
    print(f"Table data from {url} fetched successfully.")
    print("-" * 40)

for table in tables:
    print(table)
    print("-" * 40)
