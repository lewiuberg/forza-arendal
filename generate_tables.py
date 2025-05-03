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

        # Remove 'Hjemme' and 'Borte' columns if present
        if (
            len(table_data) > 1
            and "Hjemme" in table_data[0]
            and "Borte" in table_data[0]
        ):
            # Identify indices for 'Hjemme' and 'Borte' columns
            hjemme_start = table_data[0].index("Hjemme")
            borte_start = table_data[0].index("Borte")
            total_start = table_data[0].index("Total")

            # Remove 'Hjemme' and 'Borte' columns from all rows
            for i, row in enumerate(table_data):
                del row[
                    hjemme_start : borte_start + 4
                ]  # Remove 'Hjemme' columns
                del row[
                    borte_start : total_start + 4 - len(row)
                ]  # Remove 'Borte' columns

        all_tables_data.append(table_data)

    if not all_tables_data:
        print(f"No tables found on the page: {url}")
    return all_tables_data


def export_table_to_html(table, output_file, highlight_rows=None):
    """
    Export a table (list of lists) to an HTML file with optional row highlighting.

    Parameters
    ----------
    table : list
        The table data as a list of lists.
    output_file : str
        The path to the output HTML file.
    highlight_rows : list, optional
        A list of row indices to highlight.
    """
    if highlight_rows is None:
        highlight_rows = []

    html_table = "<table>\n"
    for i, row in enumerate(table):
        row_class = ' class="row-highlight"' if i in highlight_rows else ""
        html_table += f"    <tr{row_class}>\n"
        html_table += "".join([f"        <td>{cell}</td>\n" for cell in row])
        html_table += "    </tr>\n"
    html_table += "</table>"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_table)

    print(f"Table exported to {output_file}")


# fetch the table data for each URL and store it in the tables list
for idx, url in enumerate(urls):
    print(f"Fetching data from {url}")
    tables_from_url = fetch_table_data(url)
    for table_idx, table in enumerate(tables_from_url):
        # Determine rows to highlight
        highlight_rows = [0]  # Always highlight the header row
        for i, row in enumerate(table):
            if any(
                keyword in " ".join(row)
                for keyword in ["Arendal", "Hisøy /Arendal 2"]
            ):
                highlight_rows.append(i)

        # Export each table to a separate HTML file
        output_file = f"./table_{idx + 1}_{table_idx + 1}.html"
        export_table_to_html(table, output_file, highlight_rows)

    tables.extend(tables_from_url)  # Add each table as a separate entry
    print(f"Table data from {url} fetched and exported successfully.")
    print("-" * 40)


for table in tables:
    print(table)
    print("-" * 40)
