
bike_parts = [
    "spark_plug", 
    "air_filter", 
    "engine_oil", 
    "brake_pads"
]

print(f"Lists of bike parts: {bike_parts}")



first_part = bike_parts[0] 
third_part = bike_parts[2] 

print(f"first item in the list: {first_part}")
print(f"third item in the list: {third_part}")



print("\n adding headlights in the list")
bike_parts.append("headlight")

print(f"new list of bike parts: {bike_parts}")



print("\n--- full list of bike parts (Loop) ---")
for part in bike_parts:
    print(f"the part: {part}")




total_parts = len(bike_parts)
print(f"\nTotal parts (count): {total_parts}")