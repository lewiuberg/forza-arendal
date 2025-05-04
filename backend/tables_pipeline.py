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

# for url, tables_data in tables.items():
#     print(f"Data from URL: {url}")
#     for table_name, table in tables_data.items():
#         print(f"{table_name}:")
#         for row in table:
#             print(row)
#         print("\n")

# print()
# print(tables)

# a_table = {}
