import csv


def group_lines_as_csv_rows(
        input_file: str,
        num_lines_per_row: int,
        output_file: str):
    """Turn a text file in a csv file such that every row of the csv file is formed of multiple lines of the text file.

    Specifically, for num_lines_per_row = 3, row n of output_file will be "l1,l2,l3" where:
    l1 = line n*3   from input_file
    l2 = line n*3+1 from input_file
    l3 = line n*3+2 from input_file
    Useful for example if you want to copy-paste a table from a pdf and when you paste, it outputs a line for each cell, going from left to right, top to bottom. This helps recreate the table in a format other tools (e.g. Excel) can work with.

    Args:
        input_file (str): input text file
        num_lines_per_row (int): number of lines to group per csv row
        output_file (str): output file written in csv format
    """

    # Open the input text file in read mode.
    with open(input_file, encoding="utf8") as infile:
        # Read all lines from the text file and remove any trailing newlines.
        lines = [line.strip() for line in infile.readlines()]

    # Group lines into rows of num_lines_per_row.
    rows = [lines[i:i + num_lines_per_row]
            for i in range(0, len(lines), num_lines_per_row)]

    # Open the output CSV file in write mode.
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write each row to the CSV.
        for row in rows:
            # Check if row has exactly num_lines_per_row items, if not, fill with empty strings.
            writer.writerow(row + [''] * (num_lines_per_row - len(row)))


# Check that everything works as expected.
if __name__ == "__main__":
    group_lines_as_csv_rows('data/doctors_all.txt', 3, 'data/doctors_all.csv')
