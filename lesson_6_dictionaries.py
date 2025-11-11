
bike_info = {
    "make": "Hero",
    "model": "Splendor",
    "year": 2023,
    "status": "needs_check",
    "engine_running": False 
}

print(f"info of orignal bike: {bike_info}")



bike_model = bike_info["model"] 
bike_year = bike_info["year"]

print(f"\n this bike is {bike_model} which was made in year {bike_year}")




print("\nadding bike's owner...")
bike_info["owner"] = "Anurag"

print(f"new info: {bike_info}")




print("\nupdating bike's status")
bike_info["status"] = "service_done"
bike_info["engine_running"] = True

print(f"after update: {bike_info}")



print("\n--- Final Summary ---")

for key, value in bike_info.items():
    print(f"Key: {key}  |  Value: {value}")