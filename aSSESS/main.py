import csv


def menu():
    while True:
        print("What would you lke to do?")
        print("1. Add a new destination.")
        print("2. Search for a specific area to stay")
        print("3. Search for a place to stay.")
        print("4. Display all places to stay.")
        print("5. Enquiries")
        print("6. Make a Booking.")
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
            area()

        elif choice == '3':
            print("Entering Search Query...")
            search()
            print("Would you like to continue? (yes/no)")
            cont = input()
            if cont == 'no':
                break
            else:
                print("----------------")

        elif choice == '4':
            print("Showing All Destinations:")
            show_all()
            print("Would you like to continue? (yes/no)")
            cont = input()
            if cont == 'no':
                break
            elif cont == 'yes':
                print("----------------")
            else:
                print("Invalid Response!")
                break

        elif choice == '5':
            menu2()
            break

        elif choice == '6':
            print("Loading Booking Query:")
            print("Here is our list of locations:")
            print("------------------")
            show_all()
            print("------------------")
            booking()
            break

        elif choice == '7':
            print("Exiting the program!")
            break

        else:
            print("Invalid Choice!")


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def show_all():
    with open('dest.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        names = [row[0] for row in reader if row]

    bubble_sort(names)

    for name in names:
        print(name)


def area():
    print("What area would you like to stay in?")
    print("1. Southampton City Centre")
    print("2. Winchester")
    print("3. Eastleigh")
    print("4. Salisbury")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        area_to_search = "Southampton"
    elif choice == '2':
        area_to_search = "Winchester"
    elif choice == '3':
        area_to_search = "Eastleigh"
    elif choice == '4':
        area_to_search = "Salisbury"
    else:
        print("Invalid choice!")
        return

    with open('dest.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if area_to_search.lower() in row[3].lower():
                print(row[0])


def search():
    choice = input("What accommodation are you looking for? (Hotel, BnB or Hostel)\n").lower()
    valid_choices = ["hotel", "hostel", "bnb"]
    if choice not in valid_choices:
        print("Invalid Choice, Please choose again!")
        return

    with open('dest.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        filtered_places = [row for row in reader if row and choice in row[1].lower()]

        bubble_sort(filtered_places)

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
        writer.writerow([enquiry, ""])
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
            rows[i][1] = answer
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


def main():
    menu()


if __name__ == "__main__":
    main()
