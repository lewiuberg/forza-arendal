import requests
from bs4 import BeautifulSoup


def scrape_tables(urls) -> dict[str, dict[str, list[dict]]]:
    """
    Scrape tables from a list of URLs and return the data as a dictionary.

    This version supports both 'enkel' (simple) and 'utvidet' (detailed) table formats.
    Tables are found by matching header text (h2/h3 tags) with the provided table names.

    Parameters
    ----------
    urls : list[list[str]]
        A list where each element is a list containing:
        - URL (str): The page URL
        - Table header (str): The header text to match (e.g., "2 divisjon menn avdeling 1")
        - Format type (str): Either "enkel" or "utvidet" (optional, will auto-detect if not provided)

    Returns
    -------
    dict[str, dict[str, list[dict]]]
        A dictionary where each key is a URL, and the value is another dictionary
        where each key is a table name and the value is a list of dictionaries representing rows.
    """
    all_data = {}

    for url_entry in urls:
        url = url_entry[0]
        expected_table_header = url_entry[1]
        format_type = url_entry[2] if len(url_entry) > 2 else None

        # Define headers to mimic a browser
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # Fetch the page content
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all tables and their preceding titles
        data = {}
        tables = soup.find_all("table")
        
        if not tables:
            print(f"No tables found on the page: {url}")
            all_data[url] = data
            continue

        # Find the table that matches the expected header and format
        target_table = None
        table_name = expected_table_header
        
        for table in tables:
            # Find the closest preceding <h2> or <h3> tag as the title
            title_tag = table.find_previous(["h2", "h3"])
            if title_tag:
                title_text = title_tag.get_text(strip=True)
                # Remove common suffixes like "Gå til turnering"
                title_text_cleaned = title_text.replace("Gå til turnering", "").strip()
                expected_cleaned = expected_table_header.strip()
                
                # Case-insensitive matching with normalized whitespace
                if title_text_cleaned.lower() == expected_cleaned.lower():
                    # Check if this table matches the requested format
                    rows = table.find_all("tr")
                    if len(rows) < 2:
                        continue
                    
                    first_row_ths = rows[0].find_all("th")
                    second_row_ths = rows[1].find_all("th") if len(rows) > 1 else []
                    
                    # Determine table format
                    is_two_row_header = len(second_row_ths) > 0
                    table_format = "utvidet" if is_two_row_header else "enkel"
                    
                    # If format is specified, match it; otherwise take the first match
                    if not format_type or format_type == table_format:
                        target_table = table
                        table_name = title_text_cleaned
                        if not format_type:
                            format_type = table_format  # Auto-detect
                        break

        if not target_table:
            print(f"Table with header '{expected_table_header}' not found on page: {url}")
            all_data[url] = data
            continue

        # Parse the table
        table_data = []
        rows = target_table.find_all("tr")
        
        if len(rows) < 2:
            print(f"Table '{table_name}' has insufficient rows")
            all_data[url] = data
            continue

        # Extract headers
        header_rows = []
        data_start_index = 1
        
        # Check if we have a two-row header (utvidet format)
        first_row = rows[0].find_all("th")
        if len(rows) > 1:
            second_row = rows[1].find_all("th")
            # If second row also has th elements, it's a two-row header
            if second_row:
                header_rows = [first_row, second_row]
                data_start_index = 2
            else:
                header_rows = [first_row]
        else:
            header_rows = [first_row]

        # Determine format based on column count or provided format_type
        first_data_row = rows[data_start_index].find_all("td") if len(rows) > data_start_index else []
        column_count = len(first_data_row)
        
        # Auto-detect format if not provided
        if not format_type:
            if column_count >= 15:  # Utvidet format has 17 columns
                format_type = "utvidet"
            else:  # Enkel format has 9 columns
                format_type = "enkel"

        # Parse data rows
        for row in rows[data_start_index:]:
            cells = row.find_all("td")
            cell_data = [cell.get_text(strip=True) for cell in cells]

            if len(cell_data) < 5:  # Skip rows with too few columns
                continue

            try:
                if format_type == "enkel":
                    # Enkel format: Plass, Lag, Kamper, Vunnet, Uavgjort, Tap, Mål, Diff, Poeng
                    if len(cell_data) >= 9:
                        entry = {
                            "Plass": int(cell_data[0]),
                            "Lag": cell_data[1],
                            "Kamper": int(cell_data[2]),
                            "Vunnet": int(cell_data[3]),
                            "Uavgjort": int(cell_data[4]),
                            "Tap": int(cell_data[5]),
                            "Mål": cell_data[6],
                            "Diff": int(cell_data[7]),
                            "Poeng": int(cell_data[8]),
                        }
                        table_data.append(entry)
                else:  # utvidet format
                    # Utvidet format: Same as v1 with Hjemme/Borte/Total structure
                    if len(cell_data) >= 17:
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
                        if len(cell_data) > 17:
                            entry["Extra"] = cell_data[17:]
                        table_data.append(entry)
            except (ValueError, IndexError) as e:
                print(f"Error parsing row in table '{table_name}': {e}")
                continue

        if table_data:
            data[table_name] = table_data
        else:
            print(f"No valid data rows found in table '{table_name}'")

        all_data[url] = data

    return all_data
