from pathlib import Path

from backend.convert import convert_table_to_html
from backend.scrape import scrape_tables

urls = [
    [
        "https://www.fotball.no/fotballdata/lag/hjem/?fiksId=133618&underside=tabeller",
        "2 divisjon menn avdeling 1",
        "enkel",
    ],
    [
        "https://www.fotball.no/fotballdata/lag/hjem/?fiksId=210300&underside=tabeller",
        "3 div kvinner region sør",
        "enkel",
    ],
]

tables = scrape_tables(urls)

# Flatten the tables dictionary to use table names as keys
flattened_tables = {}
for url_tables in tables.values():
    flattened_tables.update(url_tables)

# Convert tables to HTML
html_tables = convert_table_to_html(flattened_tables)

# Specify the location to store the HTML files (relative to project root)
project_root = Path(__file__).parent.parent
output_directory = project_root / "docs" / "assets" / "tables"
output_directory.mkdir(parents=True, exist_ok=True)

# Save each table as an HTML file
for table_name, html_table in zip(
    flattened_tables.keys(), html_tables, strict=False
):
    sanitized_name = table_name.replace(" ", "_").replace("/", "_")
    file_path = output_directory / f"{sanitized_name}.html"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_table)
    print(f"Saved table: {file_path}")
