
bike_parts = ["spark_plug", "air_filter", "engine_oil", "brake_pads", "headlight"]

print("--- checking parts with the help of 'for' loop---")

for part in bike_parts:
    print(f"Checking {part}... Done.")

print("checked every part\n")


print("--- 'range()' ---")

for number in range(10):
    print(f"Hello, loop number {number}")

print("...range loop end!\n")




engine_temp = 20

print(f"Engine's current temperature: {engine_temp}°C")
print("starting the warm up...")


while engine_temp < 90:
    print(f"Current temp: {engine_temp}°C. Warming up...")

    engine_temp = engine_temp + 10 

print(f"Warm up complete! Engine's final temperature: {engine_temp}°C. Ready to go!")