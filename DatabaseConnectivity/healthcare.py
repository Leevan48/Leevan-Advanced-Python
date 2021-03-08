from hospital import HospitalRepository


def select_menu():
    print("\nHAA MENU")
    print("1. View Availability")
    print("2. Add Hospital")
    print("3. Update Beds and / or Availability")
    print("0. EXIT")
    try:
        action = int(input("> "))
        return action
    except (ValueError):
        return -1


def display_hospitals(hospitals):
    for id in hospitals:
        print(hospitals[id])


def add_new_hospital():
    name = input("Name: ")
    try:
        beds = int(input("Beds: "))
        available = int(input("Available: "))
    except (ValueError):
        print("Wrong value")
        return
    HospitalRepository.add_new(name, beds, available)


def update_hospital():
    try:
        id = int(input("ID: "))
        hospital = HospitalRepository.get_hospital(id)
        if hospital == None:
            print("Hospital not found")
            return
        else:
            beds = int(input("Beds (" + str(hospital.beds) + "): "))
            available = int(input("Available(" + str(hospital.available) + "): "))
            hospital.update(beds, available)
    except (ValueError):
        print("Wrong value")
        return


if __name__ == '__main__':
    while True:
        action = select_menu()
        if action == 1:
            hospitals = HospitalRepository.all_hospitals()
            display_hospitals(hospitals)
        elif action == 2:
            add_new_hospital()
        elif action == 3:
            update_hospital()
        elif action == 0:
            print("Bye!")
            break
        else:
            print("Invalid action")
        input("any key to continue ...")