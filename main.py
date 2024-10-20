from read_doctor_list import *
from write_doctor_list import *
from compute_distance import *
import os

csv_file = 'data/doctors_alba_iulia.csv'
data = read_doctor_list(csv_file)
origin = os.getenv('START_ADDRESS')
if origin is None:
    raise Exception('start address not found')
api_key = os.getenv('GOOGLE_MAPS_API_KEY')
if api_key is None:
    raise Exception('API key not found')

# # Compute distance to each doctor.
for row in data:
    row.km, row.minutes = compute_distance(api_key, origin, row.address)

write_doctor_list(data, "data/doctors_alba_iulia_distances.csv")
