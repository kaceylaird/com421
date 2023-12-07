import csv


def menu():
    while True:
        print("What would you lke to do?")
        print("1. Add a new destination.")
        print("2. Search for a place to stay.")
        print("3. Display all places to stay.")
        print("4. Enquiries")
        print("5. Make a Booking.")
        print("6. Find a Route.")
        print("7. Exit the Program.")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            print("Loading Adding Queries")
            add()
            print("Would you like to continue? (yes/no)")
            cont = input()
            if cont == 'no':
                break
            else:
                print("----------------")

        elif choice == '2':
            print("Entering Search Query...")
            search()
            print("Would you like to continue? (yes/no)")
            cont = input()
            if cont == 'no':
                break
            else:
                print("----------------")

        elif choice == '3':
            print("Showing All Destinations:")
            show_all()
            print("Would you like to continue? (yes/no)")
            cont = input()
            if cont == 'no':
                break
            else:
                print("----------------")

        elif choice == '4':
            menu2()
            break

        elif choice == '5':
            print("Loading Booking Query:")
            print("Here is our list of locations:")
            print("------------------")
            show_all()
            print("------------------")
            booking()
            break

        elif choice == '6':
            routing()

        elif choice == '7':
            print("Exiting the program!")
            break

        else:
            print("Invalid Choice!")


def show_all():
    with open('dest.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        names = [row[0] for row in reader if row]
        names.sort()
        for name in names:
            print(name)


def search():
    choice = input("What accommodation are you looking for? (Hotel, BnB or Hostel)\n").lower()
    valid_choices = ["hotel", "hostel", "bnb"]
    if choice not in valid_choices:
        print("Invalid Choice, Please choose again!")
        return

    with open('dest.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        filtered_places = [row for row in reader if row and choice in row[1].lower()]
        filtered_places.sort(key=lambda x: x[0])

        for place in filtered_places:
            print(place[0])


def add():
    name = input("Please enter the name: ")
    type_place = input("Please enter the type: ")
    address = input("Please enter the address: ")
    location = input("Please enter the location: ")
    pet_friendly = input("Is it pet friendly? ")
    serves_food = input("Does it serve food? ")
    accessible = input("Is is accessible? ")

    new_row = [name, type_place, address, location, pet_friendly, serves_food, accessible]
    with open('dest.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(new_row)
        print(f"New entry added: {new_row}")


def query_location():
    print("Here is our list of locations:")
    print("------------------")
    show_all()
    print("------------------")
    location_name = input("Which location would you like to look at? ")
    found = False

    with open('dest.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row and row[0].lower() == location_name.lower():
                found = True
                print(f"{row[0]} - \nAvailability: {row[4]} \nPet Friendly: {row[5]}"
                      f"\nServes Food: {row[6]} \nAccessible: {row[7]}")
                break

    if not found:
        print("The location you entered was not found.")
        print("Try Again.")
        query_location()

    answer = input("Would you like to make a booking? (Yes/No) ").lower()
    if answer == 'yes':
        booking()
    else:
        print("Exiting")


def booking():
    location_name = input("Which location would you like to book? ").strip().lower()
    updated_rows = []
    booking_success = False

    with open('dest.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row and row[0].strip().lower() == location_name:
                if int(row[4]) > 0:
                    row[4] = str(int(row[4])-1)
                    booking_success = True
                else:
                    print("Sorry, No Rooms Available.")
            updated_rows.append(row)

    if booking_success:
        with open('dest.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(updated_rows)
        print(f"Booking confirmed for {location_name}.")

    else:
        answer2 = input("Would you like to try another location? (Yes/No) ").lower()
        if answer2 == 'yes':
            booking()
        else:
            print("Exiting")


def make_enquiry():
    enquiry = input("Please enter your enquiry: ")
    with open('enquiries.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([enquiry, ""])  # Write the enquiry with an empty answer
    print("Your enquiry has been recorded.")


def answer_enquiries():
    # Load all enquiries and answers
    with open('enquiries.csv', 'r', newline='') as file:
        rows = list(csv.reader(file))

    # Display the first unanswered enquiry
    for i, row in enumerate(rows):
        if not row[1]:  # Check if the answer is empty
            print(f"Enquiry: {row[0]}")
            answer = input("Enter your answer: ")
            rows[i][1] = answer  # Update the answer
            break
    else:
        print("There are no unanswered enquiries.")
        return

    # Save the updated enquiries and answers back to the file
    with open('enquiries.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("The enquiry has been answered.")


def menu2():
    while True:
        print("\n1. Make an Enquiry\n2. Answer Enquiries\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            make_enquiry()
        elif choice == '2':
            answer_enquiries()
        elif choice == '3':
            break
        else:
            print("Invalid option, please try again.")


distances_from_railway_station = {
        "Travelodge": 0.4,
        "Premier Inn": 1.1,
        "Winchester Royal": 12.4,
        "Holiday Inn": 4.9,
        "Oxford Street Stays": 1.7,
        "Moodys": 7.8,
        "Hermes Apartment": 1.8,
        "Casadele Bnb": 11,
        "Claremont Guest House": 0.6,
        "Stonehenge Hostel": 39.8,
        "Starboard Stays": 1.5,
        "Moxy": 1.5,
        "Leonardo": 1.7,
        "Best Western": 4.3,
        "The Star": 1.8,
        "Doubletree": 3.1,
        "No.4 Carlton": 0.3,
        "Ibis": 1.4,
        "Botley Park Hotel": 8.4,
        "Botleigh Grange": 7.3
    }


distances_from_bus_station = {
        "Travelodge": 0.2,
        "Premier Inn": 1.0,
        "Winchester Royal": 12.0,
        "Holiday Inn": 4.6,
        "Oxford Street Stays": 1.4,
        "Moodys": 7.3,
        "Hermes Apartment": 1.4,
        "Casadele Bnb": 10.4,
        "Claremont Guest House": 0.3,
        "Stonehenge Hostel": 39.3,
        "Starboard Stays": 1.2,
        "Moxy": 1.1,
        "Leonardo": 1.4,
        "Best Western": 4.1,
        "The Star": 1.3,
        "Doubletree": 2.9,
        "No.4 Carlton": 0.6,
        "Ibis": 0.4,
        "Botley Park Hotel": 8.1,
        "Botleigh Grange": 7.2

    }


def find_route(start_point, destination):
    if start_point == "railway station":
        distances = distances_from_railway_station
    elif start_point == "bus station":
        distances = distances_from_bus_station
    else:
        print("Invalid start point. Choose 'railway station' or 'bus station'.")
        return

    distance = distances.get(destination)
    if distance is not None:
        print(f"The distance from the {start_point} to {destination} is {distance} miles.")
    else:
        print("Destination not found.")


def routing():
    start_point = input("Enter the start point (railway station or bus station): ").lower()
    destination = (input("Enter the name of the destination: ").lower())
    find_route(start_point, destination)


def main():
    menu()


if __name__ == "__main__":
    main()
