def convert_table_to_html(tables_dict: dict) -> list[str]:
    """
    Convert a dictionary of tables into a list of HTML table strings.

    This version supports both 'enkel' (simple) and 'utvidet' (detailed) table formats.
    The format is automatically detected based on the structure of the first row.

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
        if not rows:
            continue

        # Detect format based on first row structure
        first_row = rows[0]
        is_enkel = "Vunnet" in first_row  # Enkel format has "Vunnet" key
        
        html = '<table>\n  <thead>\n'
        
        if is_enkel:
            # Enkel format: Single row header
            html += '    <tr class="row-highlight">\n'
            headers = ["Plass", "Lag", "Kamper", "Vunnet", "Uavgjort", "Tap", "Mål", "Diff", "Poeng"]
            for header in headers:
                html += f'      <th>{header}</th>\n'
            html += '    </tr>\n'
        else:
            # Utvidet format: Two-row header with colspan
            html += '    <tr class="row-highlight">\n'
            html += '      <th rowspan="2">Plass</th>\n'
            html += '      <th rowspan="2">Lag</th>\n'
            html += '      <th rowspan="2">Kamper</th>\n'
            html += '      <th colspan="4">Hjemme</th>\n'
            html += '      <th colspan="4">Borte</th>\n'
            html += '      <th colspan="5">Total</th>\n'
            html += '      <th rowspan="2">Poeng</th>\n'
            html += '    </tr>\n'
            html += '    <tr class="row-highlight">\n'
            # Hjemme sub-headers
            html += '      <th>V</th>\n'
            html += '      <th>U</th>\n'
            html += '      <th>T</th>\n'
            html += '      <th>Mål</th>\n'
            # Borte sub-headers
            html += '      <th>V</th>\n'
            html += '      <th>U</th>\n'
            html += '      <th>T</th>\n'
            html += '      <th>Mål</th>\n'
            # Total sub-headers
            html += '      <th>V</th>\n'
            html += '      <th>U</th>\n'
            html += '      <th>T</th>\n'
            html += '      <th>Mål</th>\n'
            html += '      <th>Diff</th>\n'
            html += '    </tr>\n'
        
        html += '  </thead>\n  <tbody>\n'

        # Add rows
        for row in rows:
            # Highlight rows containing "Arendal"
            row_class = (
                ' class="row-highlight"'
                if "Arendal" in row.get("Lag", "")
                else ""
            )
            html += f'    <tr{row_class}>\n'
            
            if is_enkel:
                # Enkel format: Simple columns
                html += f'      <td>{row["Plass"]}</td>\n'
                html += f'      <td>{row["Lag"]}</td>\n'
                html += f'      <td>{row["Kamper"]}</td>\n'
                html += f'      <td>{row["Vunnet"]}</td>\n'
                html += f'      <td>{row["Uavgjort"]}</td>\n'
                html += f'      <td>{row["Tap"]}</td>\n'
                html += f'      <td>{row["Mål"]}</td>\n'
                html += f'      <td>{row["Diff"]}</td>\n'
                html += f'      <td>{row["Poeng"]}</td>\n'
            else:
                # Utvidet format: Nested structure
                html += f'      <td>{row["Plass"]}</td>\n'
                html += f'      <td>{row["Lag"]}</td>\n'
                html += f'      <td>{row["Kamper"]}</td>\n'
                # Hjemme
                html += f'      <td>{row["Hjemme"]["V"]}</td>\n'
                html += f'      <td>{row["Hjemme"]["U"]}</td>\n'
                html += f'      <td>{row["Hjemme"]["T"]}</td>\n'
                html += f'      <td>{row["Hjemme"]["Mål"]}</td>\n'
                # Borte
                html += f'      <td>{row["Borte"]["V"]}</td>\n'
                html += f'      <td>{row["Borte"]["U"]}</td>\n'
                html += f'      <td>{row["Borte"]["T"]}</td>\n'
                html += f'      <td>{row["Borte"]["Mål"]}</td>\n'
                # Total
                html += f'      <td>{row["Total"]["V"]}</td>\n'
                html += f'      <td>{row["Total"]["U"]}</td>\n'
                html += f'      <td>{row["Total"]["T"]}</td>\n'
                html += f'      <td>{row["Total"]["Mål"]}</td>\n'
                html += f'      <td>{row["Total"]["Diff"]}</td>\n'
                # Poeng
                html += f'      <td>{row["Poeng"]}</td>\n'
            
            html += '    </tr>\n'

        html += '  </tbody>\n</table>'
        html_tables.append(html)

    return html_tables
