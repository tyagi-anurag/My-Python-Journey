
bike_location = (27.1751, 78.0421) # (latitude, longitude)

print(f"Bike's location (Tuple): {bike_location}")


print(f"Latitude: {bike_location[0]}")


#bike_location[0] = 28.0 

print("Tuples can't be changed\n")



parts_list = [
    "oil_filter", 
    "spark_plug", 
    "air_filter", 
    "spark_plug", # Duplicate
    "oil_filter", # Duplicate
    "brake_pads"
]

print(f"List of Original Parts (with duplicates): {parts_list}")


unique_parts = set(parts_list)

print(f"Unique parts (Set): {unique_parts}")



check_part = "spark_plug"

if check_part in unique_parts:
    print(f"\nYes, '{check_part}' is in unique parts")
else:
    print(f"\nNo, '{check_part}' isn't in unique parts")