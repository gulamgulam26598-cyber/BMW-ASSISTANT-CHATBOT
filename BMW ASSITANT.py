# ==========================================
# BMW CAR ASSISTANT
# Class 12 Computer Science Project
# Concepts Used:
# Functions, Dictionaries, Loops,
# Conditional Statements, OOP,
# Error Handling, User Input Validation
# ==========================================

# -------- BMWCar Class --------
class BMWCar:
    """Class to store BMW car information"""

    def __init__(self, model, price, engine, horsepower, top_speed, category):
        self.model = model
        self.price = price
        self.engine = engine
        self.horsepower = horsepower
        self.top_speed = top_speed
        self.category = category

    def display_details(self):
        """Display complete car details"""
        print("\n" + "=" * 50)
        print(f"Model      : {self.model}")
        print(f"Price      : {self.price}")
        print(f"Engine     : {self.engine}")
        print(f"Horsepower : {self.horsepower} HP")
        print(f"Top Speed  : {self.top_speed} km/h")
        print(f"Category   : {self.category}")
        print("=" * 50)

    def compare_with(self, other_car):
        """Compare two BMW cars"""

        print("\n" + "=" * 60)
        print(f"{self.model} VS {other_car.model}")
        print("=" * 60)

        print(f"\nHorsepower:")
        print(f"{self.model}: {self.horsepower} HP")
        print(f"{other_car.model}: {other_car.horsepower} HP")

        if self.horsepower > other_car.horsepower:
            print(f"Winner: {self.model}")
        elif self.horsepower < other_car.horsepower:
            print(f"Winner: {other_car.model}")
        else:
            print("Both have equal horsepower.")

        print(f"\nTop Speed:")
        print(f"{self.model}: {self.top_speed} km/h")
        print(f"{other_car.model}: {other_car.top_speed} km/h")

        if self.top_speed > other_car.top_speed:
            print(f"Faster Car: {self.model}")
        elif self.top_speed < other_car.top_speed:
            print(f"Faster Car: {other_car.model}")
        else:
            print("Both have same top speed.")


# -------- BMW Database --------

bmw_cars = {
    "BMW M2": BMWCar("BMW M2", "₹1.03 Crore", "3.0L Twin Turbo I6", 453, 285, "Sports Car"),

    "BMW M3": BMWCar("BMW M3", "₹1.48 Crore", "3.0L Twin Turbo I6", 503, 290, "Sports Car"),

    "BMW M4": BMWCar("BMW M4", "₹1.53 Crore", "3.0L Twin Turbo I6", 503, 290, "Sports Car"),

    "BMW M5": BMWCar("BMW M5", "₹1.99 Crore", "4.4L Twin Turbo V8", 717, 305, "Sports Car"),

    "BMW 3 Series": BMWCar("BMW 3 Series", "₹74 Lakh", "2.0L Turbo Petrol", 255, 250, "Sedan"),

    "BMW 5 Series": BMWCar("BMW 5 Series", "₹73 Lakh", "2.0L Turbo Petrol", 255, 250, "Sedan"),

    "BMW 7 Series": BMWCar("BMW 7 Series", "₹1.84 Crore", "3.0L Turbo Petrol", 375, 250, "Luxury"),

    "BMW X1": BMWCar("BMW X1", "₹50 Lakh", "2.0L Turbo Petrol", 241, 235, "SUV"),

    "BMW X3": BMWCar("BMW X3", "₹75 Lakh", "2.0L Turbo Petrol", 248, 240, "SUV"),

    "BMW X5": BMWCar("BMW X5", "₹97 Lakh", "3.0L Turbo Petrol", 375, 250, "SUV"),

    "BMW X7": BMWCar("BMW X7", "₹1.30 Crore", "3.0L Turbo Petrol", 375, 250, "SUV"),

    "BMW Z4": BMWCar("BMW Z4", "₹92 Lakh", "3.0L Turbo I6", 382, 250, "Sports Car"),

    "BMW i4": BMWCar("BMW i4", "₹72 Lakh", "Electric Motor", 536, 225, "Electric"),

    "BMW i7": BMWCar("BMW i7", "₹2.05 Crore", "Dual Electric Motor", 650, 250, "Electric"),

    "BMW XM": BMWCar("BMW XM", "₹2.60 Crore", "4.4L Twin Turbo V8 Hybrid", 738, 290, "Luxury")
}


# -------- Welcome Function --------

def welcome():
    print("=" * 60)
    print("               BMW CAR ASSISTANT")
    print("=" * 60)
    print("Welcome to BMW Car Assistant.")
    print("We currently have information about 15 BMW car models.\n")


# -------- Show Models --------

def show_models():
    print("\nAvailable BMW Models:\n")

    for car in bmw_cars:
        print("•", car)


# -------- Get Car Details --------

def get_car_details(model):

    if model in bmw_cars:

        car = bmw_cars[model]

        print("\nThe", car.model,
              "is one of BMW's most popular models.")

        car.display_details()

    else:
        print("\nSorry, that BMW model is not available.")


# -------- Compare Cars --------

def compare_cars(car1, car2):

    if car1 in bmw_cars and car2 in bmw_cars:

        bmw_cars[car1].compare_with(
            bmw_cars[car2]
        )

    else:
        print("\nInvalid BMW model name.")


# -------- Search By Budget --------

def search_by_budget(budget):

    print("\nBMW Cars Within Your Budget:\n")

    found = False

    for car in bmw_cars.values():

        price_text = car.price

        if "Lakh" in price_text:
            value = float(price_text.replace("₹", "").replace("Lakh", ""))

        else:
            value = float(price_text.replace("₹", "").replace("Crore", "")) * 100

        if value <= budget:
            print(f"{car.model} - {car.price}")
            found = True

    if not found:
        print("No BMW found within this budget.")


# -------- Search By Category --------

def search_by_category(category):

    found = False

    print(f"\nBMW Cars in '{category}' Category:\n")

    for car in bmw_cars.values():

        if car.category.lower() == category.lower():
            print(car.model)
            found = True

    if not found:
        print("No BMW found in this category.")


# -------- Fastest BMW --------

def show_fastest_car():

    fastest = max(
        bmw_cars.values(),
        key=lambda car: car.top_speed
    )

    print("\nFastest BMW Car")

    fastest.display_details()


# -------- Most Powerful BMW --------

def show_most_powerful_car():

    powerful = max(
        bmw_cars.values(),
        key=lambda car: car.horsepower
    )

    print("\nMost Powerful BMW")

    powerful.display_details()


# -------- Menu --------

def display_menu():

    print("\n")
    print("=" * 60)
    print("BMW CAR ASSISTANT MENU")
    print("=" * 60)

    print("1. View All BMW Models")
    print("2. View Car Details")
    print("3. Compare Two Cars")
    print("4. Search Cars by Budget")
    print("5. Search Cars by Category")
    print("6. Show Fastest BMW")
    print("7. Show Most Powerful BMW")
    print("8. Exit")


# -------- Main Chatbot --------

def chatbot():

    welcome()

    show_models()

    while True:

        display_menu()

        choice = input("\nEnter your choice (1-8): ")

        # Option 1
        if choice == "1":

            show_models()

        # Option 2
        elif choice == "2":

            model = input(
                "\nEnter BMW Model Name: "
            ).strip()

            get_car_details(model)

        # Option 3
        elif choice == "3":

            car1 = input(
                "\nEnter First BMW Model: "
            ).strip()

            car2 = input(
                "Enter Second BMW Model: "
            ).strip()

            compare_cars(car1, car2)

        # Option 4
        elif choice == "4":

            try:

                print("\nEnter budget in Lakhs.")
                print("Example:")
                print("50 = ₹50 Lakh")
                print("100 = ₹1 Crore")

                budget = float(
                    input("\nEnter Budget: ")
                )

                search_by_budget(budget)

            except ValueError:

                print(
                    "\nPlease enter a valid number."
                )

        # Option 5
        elif choice == "5":

            print("\nAvailable Categories:")
            print("Sedan")
            print("SUV")
            print("Sports Car")
            print("Electric")
            print("Luxury")

            category = input(
                "\nEnter Category: "
            )

            search_by_category(category)

        # Option 6
        elif choice == "6":

            show_fastest_car()

        # Option 7
        elif choice == "7":

            show_most_powerful_car()

        # Option 8
        elif choice == "8":

            print("\nThank you for using BMW Car Assistant.")
            print("We hope we helped you explore BMW cars.")
            print("Have a great day!")

            break

        else:

            print(
                "\nInvalid Choice. Please select between 1 and 8."
            )


# -------- Program Start --------

chatbot()