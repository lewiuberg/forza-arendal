import requests
from bs4 import BeautifulSoup


def scrape_tables(urls) -> dict[str, dict[str, list[dict]]]:
    """
    Scrape tables from a list of URLs and return the data as a dictionary.

    The function dynamically handles varying column counts and formats the data
    into a structured dictionary format. Table names are assigned based on the
    provided input or matched with titles found near the tables.

    Parameters
    ----------
    urls : list[list[str]]
        A list where each element is a list containing a URL followed by the expected table names.

    Returns
    -------
    dict[str, dict[str, list[dict]]]
        A dictionary where each key is a URL, and the value is another dictionary
        where each key is a table name (e.g., "PostNord-ligaen avd. 1") and the value
        is a list of dictionaries representing rows.
    """
    all_data = {}

    for url_entry in urls:
        url = url_entry[0]
        expected_table_names = url_entry[1:]

        # Define headers to mimic a browser
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # Fetch the page content
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract all tables and their preceding titles
        data = {}
        tables = soup.find_all("table")  # Find all tables
        if tables:
            table_titles = []
            for table in tables:
                # Find the closest preceding <h2> or <h3> tag as the title
                title_tag = table.find_previous(["h2", "h3"])
                table_titles.append(
                    title_tag.get_text(strip=True) if title_tag else None
                )

            for index, table in enumerate(tables):
                # Match the provided table names with the actual titles dynamically
                if index < len(expected_table_names):
                    expected_name = expected_table_names[index]
                    actual_name = table_titles[index]
                    if actual_name and actual_name in expected_table_names:
                        table_name = actual_name
                    else:
                        table_name = expected_name
                else:
                    table_name = (
                        table_titles[index]
                        if table_titles[index]
                        else f"Table_{index + 1}"
                    )

                table_data = []
                rows = table.find_all("tr")
                headers = [
                    header.get_text(strip=True)
                    for header in rows[0].find_all("th")
                ]  # Extract headers
                for row in rows[1:]:  # Skip the header row
                    cells = row.find_all("td")
                    cell_data = [cell.get_text(strip=True) for cell in cells]

                    # Dynamically handle varying column counts
                    if len(cell_data) >= len(
                        headers
                    ):  # Ensure row matches header count
                        entry = {
                            "Plass": int(cell_data[0]),
                            "Lag": cell_data[1],
                            "Kamper": int(cell_data[2]),
                            "Hjemme": {
                                "V": int(cell_data[3]),
                                "U": int(cell_data[4]),
                                "T": int(cell_data[5]),
                                "Mål": cell_data[6],
                            },
                            "Borte": {
                                "V": int(cell_data[7]),
                                "U": int(cell_data[8]),
                                "T": int(cell_data[9]),
                                "Mål": cell_data[10],
                            },
                            "Total": {
                                "V": int(cell_data[11]),
                                "U": int(cell_data[12]),
                                "T": int(cell_data[13]),
                                "Mål": cell_data[14],
                                "Diff": int(cell_data[15]),
                            },
                            "Poeng": int(cell_data[16]),
                        }
                        # Adjust mapping logic if additional columns exist
                        if len(cell_data) > 17:
                            entry["Extra"] = cell_data[
                                17:
                            ]  # Store extra columns if present
                        table_data.append(entry)
                data[table_name] = table_data  # Use the table name as key
        else:
            print(f"No tables found on the page: {url}")
        all_data[url] = data  # Group tables under the URL key

    return all_data
