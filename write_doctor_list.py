import csv
from dataclasses import asdict
from typing import List
from read_doctor_list import *


def write_doctor_list(data: List[Doctor], output_file: str):
    # Open the CSV file in write mode.
    with open(output_file, 'w', newline='') as file:
        # Create a CSV writer.
        writer = csv.DictWriter(
            file, fieldnames=["company_name", "doctor_name", "address", "km", "minutes"])

        # Write the header row (the field names from the dataclass).
        writer.writeheader()

        # Iterate over each dataclass instance in the list.
        for person in data:
            # Convert the dataclass instance to a dictionary and write it as a row.
            writer.writerow(asdict(person))
