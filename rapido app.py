print("🚲 Welcome to Python rides 🚲")

rides = {
    "bike": 40,
    "auto": 80,
    "cab": 120
}

booking = {}

def show_rides():
    print("\n🚗 Available Ride Types:")
    print("-" * 30)
    for ride, price in rides.items():
        print(f"{ride:<10} ₹{price} per km")
    print("-" * 30)


def book_ride():
    ride = input("Enter ride type (bike/auto/cab): ").lower()

    if ride in rides:
        try:
            distance = float(input("Enter distance in km: "))
            if distance <= 0:
                print("❌ Distance must be positive!")
                return

            fare = rides[ride] * distance
            booking["ride"] = ride
            booking["distance"] = distance
            booking["fare"] = fare

            print(f"✅ {ride} booked for {distance} km.")

        except ValueError:
            print("❌ Invalid distance.")
    else:
        print("❌ Ride type not available!")


def view_booking():
    if not booking:
        print("\n🚫 No ride booked yet.")
        return

    print("\n📋 Current Ride Details")
    print("-" * 30)
    print(f"Ride Type : {booking['ride']}")
    print(f"Distance  : {booking['distance']} km")
    print(f"Fare      : ₹{booking['fare']}")
    print("-" * 30)


def cancel_ride():
    if booking:
        booking.clear()
        print("🗑 Ride cancelled successfully.")
    else:
        print("❌ No ride to cancel.")


def confirm_ride():
    if not booking:
        print("🚫 No ride booked!")
        return

    total = booking["fare"]

    discount = 0
    if total >= 200:
        discount = total * 0.10

    final = total - discount

    print("\n🧾 --- RIDE BILL ---")
    print(f"Ride Type : {booking['ride']}")
    print(f"Distance  : {booking['distance']} km")
    print(f"Fare      : ₹{total}")
    print(f"Discount  : ₹{discount:.2f}")
    print(f"Total Pay : ₹{final:.2f}")
    print("🚲 Driver arriving soon!")

    booking.clear()


while True:

    print("\n📱 RAPIDO MENU")
    print("1. Show Ride Types")
    print("2. Book Ride")
    print("3. View Booking")
    print("4. Cancel Ride")
    print("5. Confirm Ride")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_rides()

    elif choice == "2":
        book_ride()

    elif choice == "3":
        view_booking()

    elif choice == "4":
        cancel_ride()

    elif choice == "5":
        confirm_ride()

    elif choice == "6":
        print("👋 Thank you for using Python Rapido!")
        break

    else:
        print("❌ Invalid choice.")
