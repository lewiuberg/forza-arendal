def convert_table_to_html(tables_dict: dict) -> list[str]:
    """
    Convert a dictionary of tables into a list of HTML table strings.

    Parameters
    ----------
    tables_dict : dict
        A dictionary where keys are table names and values are lists of rows (dictionaries).

    Returns
    -------
    list[str]
        A list of HTML table strings.
    """
    html_tables = []

    for table_name, rows in tables_dict.items():
        # Start the table with headers
        html = '<table>\n  <thead>\n    <tr class="row-highlight">\n'
        headers = list(rows[0].keys())
        for header in headers:
            if isinstance(rows[0][header], dict):  # Handle nested headers
                colspan = len(rows[0][header])
                html += f'      <th colspan="{colspan}">{header}</th>\n'
            else:
                html += f'      <th rowspan="2">{header}</th>\n'
        html += '    </tr>\n    <tr class="row-highlight">\n'
        for header in headers:
            if isinstance(rows[0][header], dict):  # Add sub-headers
                for sub_header in rows[0][header].keys():
                    html += f"      <th>{sub_header}</th>\n"
        html += "    </tr>\n  </thead>\n  <tbody>\n"

        # Add rows
        for row in rows:
            row_class = (
                ' class="row-highlight"'
                if "Arendal" in row.get("Lag", "")
                else ""
            )
            html += f"    <tr{row_class}>\n"
            for header in headers:
                if isinstance(row[header], dict):  # Handle nested data
                    for sub_header in row[header].values():
                        html += f"      <td>{sub_header}</td>\n"
                else:
                    html += f"      <td>{row[header]}</td>\n"
            html += "    </tr>\n"

        html += "  </tbody>\n</table>"
        html_tables.append(html)

    return html_tables
