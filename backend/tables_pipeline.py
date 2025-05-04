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

# Print the HTML tables
for html_table in html_tables:
    print(html_table)
    print("\n" + "=" * 80 + "\n")
