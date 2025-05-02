"""Convert Markdown table to HTML table with row highlighting."""


def markdown_table_to_html(markdown_file, output_file, highlight_rows=None):
    """
    Convert a Markdown table to an HTML table and write it to a file.

    This function reads a Markdown file, extracts the table, and converts it to HTML.

    Parameters
    ----------
    markdown_file : str
        The path to the Markdown file containing the table.
    output_file : str
        The path where the HTML table will be saved.
    highlight_rows : _type_: list, optional
        A list of row indices to highlight. The first row is index 0.
    """
    if highlight_rows is None:
        highlight_rows = []

    with open(markdown_file, encoding="utf-8") as file:
        lines = file.readlines()

    table_lines = []
    in_table = False

    for line in lines:
        if "|" in line:  # Detect table rows
            in_table = True
            table_lines.append(line.strip())
        elif in_table:  # Stop if table ends
            break

    if not table_lines:
        print("No table found in the Markdown file.")
        return

    # Extract headers and rows
    headers = table_lines[0].split("|")[1:-1]
    rows = [row.split("|")[1:-1] for row in table_lines[2:]]

    # Generate HTML table
    html_table = "<table>\n"
    for i, row in enumerate([headers] + rows):  # Combine headers and rows
        row_class = ' class="row-highlight"' if i in highlight_rows else ""
        html_table += f"    <tr{row_class}>\n"
        html_table += "".join(
            [f"        <td>{cell.strip()}</td>\n" for cell in row]
        )
        html_table += "    </tr>\n"
    html_table += "</table>"

    # Write to output file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_table)

    print(f"HTML table written to {output_file}")


# Example usage
markdown_file = "./table.md"
output_file = "./table.html"
highlight_rows = [0, 6]  # Highlight the header and second data rows
markdown_table_to_html(markdown_file, output_file, highlight_rows)
