# --- 1. Creating a 'Class' (Blueprint) ---
# A blueprint is created using the 'class' keyword. Class names should always start with a capital letter.
class Bike:

    # --- 2. The "Constructor" (__init__) ---
    # This is a special function that runs when a NEW object is created from this class.
    # It sets the initial values (properties) of the object.
    # 'self' means "the object itself".
    def __init__(self, bike_model, bike_year, bike_status):
        print(f"--- Creating a new bike: Model {bike_model} ---")
        
        # Using 'self' to store data inside the object
        self.model = bike_model
        self.year = bike_year
        self.status = bike_status

    # --- 3. A 'Method' (Function inside an Object) ---
    # This is a "tool" that the object has.
    # Notice, the first parameter is always 'self'.
    def display_info(self):
        # Using 'self' to read the object's own data
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Status: {self.status}\n")

    # The function from Lesson 8 is now turned into a "Method"
    def check_status(self):
        print(f"Checking status for {self.model}...")
        if self.status == "needs_service":
            print(">> Decision: Take the bike for servicing.")
        elif self.status == "ok":
            print(">> Decision: The bike is perfectly fine. Enjoy your ride!")
        else:
            print(f">> Decision: Unknown status '{self.status}'.")
        print("...check complete.\n")


# --- 4. Creating Actual "Objects" from the Blueprint ---
# We are calling the 'Bike' class to create two different bike objects.

print("### Creating Object 1 ###")
my_splendor = Bike("Splendor", 2023, "ok")

print("### Creating Object 2 ###")
friends_bike = Bike("Apache RTR", 2021, "needs_service")


# --- 5. Calling the "Methods" (Functions) of the Objects ---

# Display Splendor's data and check status
my_splendor.display_info()
my_splendor.check_status()

# Display Apache's data and check status
friends_bike.display_info()
friends_bike.check_status()
