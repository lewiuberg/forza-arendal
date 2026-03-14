import os
from datetime import UTC, datetime, timedelta

# Paths to the input HTML files
herrer_table_path = "docs/assets/tables/2_divisjon_menn_avdeling_1.html"
kvinner_table_path = "docs/assets/tables/3_div_kvinner_region_sør.html"

# Path to the output Markdown file
output_md_path = "docs/tabell.md"

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_md_path), exist_ok=True)

if not os.path.exists(herrer_table_path):
    print(f"File not found: {herrer_table_path}")
if not os.path.exists(kvinner_table_path):
    print(f"File not found: {kvinner_table_path}")
if not os.path.exists(output_md_path):
    print(f"File not found: {output_md_path}")

# Read the HTML tables
with open(herrer_table_path, encoding="utf-8") as herrer_file:
    herrer_table = herrer_file.read()

with open(kvinner_table_path, encoding="utf-8") as kvinner_file:
    kvinner_table = kvinner_file.read()

# Generate the Markdown content
timestamp = (datetime.now(UTC) + timedelta(hours=2)).strftime(
    "%Y-%m-%d %H:%M:%S"
)  # Adjust for UTC+2

markdown_content = f"""---
author: "Lewi Lie Uberg"
---

# Tabell

Her vil du finne informasjon om tabellene i 2 divisjon menn avdeling 1 og 3 div kvinner region sør, og hvordan Arendal Fotball ligger an i forhold til de andre lagene i ligaen.

??? forza "Informasjon"

    Disse tabellene er hentet fra [2 divisjon menn avdeling 1](https://www.fotball.no/fotballdata/lag/hjem/?fiksId=133618&underside=tabeller) og [3 div kvinner region sør](https://www.fotball.no/fotballdata/lag/hjem/?fiksId=210300&underside=tabeller), og oppdateres jevnlig. Tabellen viser lagene i ligaen, antall kamper spilt, seire, uavgjorte, tap, mål for, mål mot og poeng.

Tabellene er sist oppdatert: {timestamp}

## A-lag Herrer

{herrer_table}

## A-lag Kvinner

{kvinner_table}
"""

# Write the Markdown content to the output file
with open(output_md_path, "w", encoding="utf-8") as output_file:
    output_file.write(markdown_content)

print(f"Markdown file generated at {output_md_path}")
