import csv


def menu():
    while True:
        print("What would you lke to do?")
        print("1. Add a new destination.")
        print("2. Search for a place to stay.")
        print("3. Display all places to stay.")
        print("4. Query Destinations.")
        print("5. Make a Booking.")
        print("6. Exit the Program.")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("Loading Adding Queries")
            add()
            print("Would you like to continue? y/n")
            cont = input()
            if cont == 'n':
                break
            else:
                print("----------------")

        elif choice == '2':
            print("Entering Search Query...")
            search()
            print("Would you like to continue? y/n")
            cont = input()
            if cont == 'n':
                break
            else:
                print("----------------")

        elif choice == '3':
            print("Showing All Destinations:")
            show_all()
            print("Would you like to continue? y/n")
            cont = input()
            if cont == 'n':
                break
            else:
                print("----------------")

        elif choice == '4':
            query_location()
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


def main():
    menu()


if __name__ == "__main__":
    main()
