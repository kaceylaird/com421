import csv


def menu():
    while True:
        print("What would you lke to do?")
        print("1. Add a new destination.")
        print("2. Search for a place to stay.")
        print("3. Display all places to stay.")
        print("4. Exit.")

        choice = input("Enter your choice (1-4): ")

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

    new_row = [name, type_place, address, location]
    with open('dest.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(new_row)
        print(f"New entry added: {new_row}")


def main():
    menu()


if __name__ == "__main__":
    main()
