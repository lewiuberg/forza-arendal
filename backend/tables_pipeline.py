import os

from convert import convert_table_to_html
from scrape import scrape_tables

urls = [
    [
        "https://www.fotball.no/fotballdata/lag/tabell/?fiksId=133618",
        "PostNord-ligaen avd. 1",
        "Treningskamper seniorlag NFF Agder 2025",
    ],
    [
        "https://www.fotball.no/fotballdata/lag/tabell/?fiksId=210300",
        "3.div Kvinner avd Sør",
    ],
]
tables = scrape_tables(urls)

# Flatten the tables dictionary to use table names as keys
flattened_tables = {}
for url_tables in tables.values():
    flattened_tables.update(url_tables)

# Convert tables to HTML
html_tables = convert_table_to_html(flattened_tables)

# Specify the location to store the HTML files
output_directory = "docs/assets/tables"
os.makedirs(output_directory, exist_ok=True)

# Save each table as an HTML file
for table_name, html_table in zip(
    flattened_tables.keys(), html_tables, strict=False
):
    sanitized_name = table_name.replace(" ", "_").replace("/", "_")
    file_path = os.path.join(output_directory, f"{sanitized_name}.html")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_table)
