I wanted to search for a new family doctor in my city, closer to where I live now. It turns out there's an official list of all registered family doctors in Alba county: https://dspalba.ro/wp-content/uploads/2024/03/CONTRACT_MF_LA_01_03_2024_MF_FINAL.pdf

It turns out I could compute the distances from my home to the doctors in my city using Python and the Google Maps API.

I then cleaned up the code and committed this repo so that it can serve as inspiration if I want to do something similar in the future. I outlined all the steps, but step 5 is the interesting one (using Google Maps API to compute distances).

1. Manually select all from the pdf and copy-paste it to a text file.
`CONTRACT_MF_LA_01_03_2024_MF_FINAL.pdf  -> doctors_all.txt`

2. Automatically convert from txt to csv, because the copy-paste directly to Excel doesn't work the way I'd like (doesn't generate a table, but a list of strings). Use group_lines_as_csv_rows.
`doctors_all.txt                         -> doctors_all.csv`

3. Manually load the csv in an Excel file, filter which ones I care about (the ones in the city of Alba Iulia) and tweak the address field where necessary.
`doctors_all.csv                         -> doctors_all.xlsx`
csv file (all doctors)                  -> Excel (doctors in Alba Iulia)

4. Manually save the sheet with the processed data to a csv.
`doctors_all.xlsx                        -> doctors_alba_iulia.csv`

5. Automatically compute the distances from the start address to each of the addresses in the csv.
`doctors_alba_iulia.csv                  -> doctors_alba_iulia_distances.csv`

6. Manually load the csv in an Excel file, sort by distance and further filter and check details about each doctor.
`doctors_alba_iulia_distances.csv        -> doctors_alba_iulia_distances.xls`

PS: Did this automation actually save any time, for this particular task? I doubt it, there's 42 rows in the output, I could have used Google Maps manually, search for the 42 addresses one by one and write down the distances, in the time it took to get write the first draft of the code (<1 hour). And I spent another 2 hours cleaning up and uploading. But it was fun and it might help someday for another project.