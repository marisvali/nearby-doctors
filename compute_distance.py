import googlemaps
import os


def compute_distance(api_key, origin, destination):
    # Initialize the Google Maps client with your API key.
    gmaps = googlemaps.Client(key=api_key)

    # Request distance matrix.
    result = gmaps.distance_matrix(origins=origin,
                                   destinations=destination,
                                   # You can use 'driving', 'walking', 'bicycling', 'transit'.
                                   mode="walking")

    # Extract the distance information.
    try:
        distance_info = result['rows'][0]['elements'][0]

        if distance_info['status'] == 'OK':
            # Get distance in meters.
            distance = distance_info['distance']['value']
            # Get duration in seconds.
            duration = distance_info['duration']['value']
            return str(distance/1000.0), str(duration/60.0)
        else:
            return 'Error: Unable to find the distance', None
    except (KeyError, IndexError) as e:
        return f'Error: {str(e)}', None


if __name__ == "__main__":
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    if api_key is None:
        raise Exception('API key not found')

    origin = 'Alba Iulia, Romania'
    destination = 'Turda, Romania'
    km, min = compute_distance(api_key, origin, destination)

    print(f'The distance between "{origin}" and "{destination}" is {km}.')
    print(f"Estimated travel time: {min}.")
