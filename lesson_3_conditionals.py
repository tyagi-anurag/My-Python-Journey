
speed = 70  #km/h

print(f"your current speed is: {speed} km/h")


if speed > 60:
    print(">> Warning: High Speed! Slow down.")

print("...checking done...\n")




bike_status = "ok" 

print(f"Bike ka status hai: {bike_status}")

if bike_status == "needs_service":
    print(">> Decision: bike needs service")
else:
    print(">> Decision: bike is good enjoy the ride")

print("...status check done...\n")




petrol_percentage = 45 

print(f" petrol is : {petrol_percentage}%")

if petrol_percentage < 10:
    print(">> Result: Tank is empty fill it")
elif petrol_percentage < 50:
    print(">> Result: Tank is more than half empty")
elif petrol_percentage < 90:
    print(">> Result: enough Petrol")
else:
    print(">> Result: Tank full LETS GO!")

print("...petrol check done...\n")