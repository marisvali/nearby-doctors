import csv
from doctor import *
from typing import List


def read_doctor_list(csv_file: str) -> List[Doctor]:
    """Read a csv that contains a list of doctors in the form:
    (company_name_1, doctor_name_1, address_1)
    (company_name_2, doctor_name_2, address_2)
    ..
    """
    list: List[Doctor] = []

    # Open the CSV file and read it.
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)

        # Iterate over each row in the CSV.
        for row in reader:
            # Ensure the row has exactly 3 items.
            if len(row) == 3:
                # Create a Doctor structure and append it to the list.
                row_data = Doctor(
                    company_name=row[0], doctor_name=row[1], address=row[2], km="", minutes="")
                list.append(row_data)
            else:
                print(f"Skipping row due to unexpected number of items: {row}")

    return list


# Check that everything works as expected.
if __name__ == "__main__":
    data = read_doctor_list('data/doctors_alba_iulia.csv')
    for row in data:
        print(row)
