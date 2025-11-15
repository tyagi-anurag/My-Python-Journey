# --- 1. The Problem: A Program Crash ---
# Our original bike_info dictionary
bike_info = {
    "model": "Splendor",
    "year": 2023
}

print("Program started...")

# If we try to access a key that does not exist, the program will crash.
# Try removing the # below to see what happens:
# print(bike_info["status"])  # This will raise a 'KeyError' and stop the program

print("...if the program had crashed, this line would never run.\n")


# --- 2. The Solution: try...except (The 'Safety Net') ---
print("--- Now let's try with 'try...except' ---")

status = "unknown"  # Setting a default value beforehand

try:
    # TRY: This is where we run risky code
    print("Risky code starting... trying to access the 'status' key...")
    status = bike_info["status"]  # THIS LINE WILL FAIL
    print(f"The bike status is: {status}")  # This line will not run

except KeyError:
    # EXCEPT: This block runs if a 'KeyError' occurs
    print("!! Error Caught !!")
    print("Error: The 'status' key does not exist in the dictionary.")
    print(f"We will keep the default value '{status}' as the status.")

except Exception as e:
    # A general catch-all for any unknown error
    print(f"An unknown error occurred: {e}")

# The 'finally' block always runs, whether there is an error or not
finally:
    print("...Safety check complete (the 'finally' block always runs).\n")


print("The program did NOT crash!")
print(f"Final bike status: {status}")
print("Program finished successfully.")
