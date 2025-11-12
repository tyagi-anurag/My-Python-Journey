

def check_bike_status(status):
    
    print(f"Function got the 'status': {status}")

    if status == "needs_service":
        print(">> Decision: Take bike for service")
    elif status == "ok":
        print(">> Decision: Bike is ok")
    else:
        print(f">> Decision: Unknown status '{status}'.")

    print("...status checked function did the job\n")




print("--- Calling function fisrst time ---")
check_bike_status("ok") 

print("--- Calling function second time ---")
check_bike_status("needs_service") 

print("--- Calling function third time ---")
check_bike_status("engine_hot") 




def calculate_birth_year(current_year, age):
    birth_year = current_year - age
    return birth_year 


my_birth_year = calculate_birth_year(2025, 25) 

print(f"The birth year that is calculated with the help of function is: {my_birth_year}")