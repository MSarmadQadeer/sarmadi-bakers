import json
import random
import datetime

lucky_draw_limit = 4

print("")
print("\t|======|     /\     |====| |\        /|     /\     |===)   =====   ")
print("\t|           /  \    |    | | \      / |    /  \    |    )    |     ")
print("\t|======|   /====\   |====| |  \    /  |   /====\   |     )   |     ")
print("\t       |  /      \  |  \   |   \  /   |  /      \  |    )    |     ")
print("\t|======| /        \ |   \_ |    \/    | /        \ |===)   =====   ")
print()
print("\t\t|=====)     /\     |   /  |=====  |====| |======| ")
print("\t\t|     |    /  \    |  /   |       |    | |        ")
print("\t\t|=====)   /====\   |_/    |=====  |====| |======| ")
print("\t\t|     |  /      \  | \    |       |  \          | ")
print("\t\t|=====) /        \ |  \_  |=====  |   \_ |======| ")
print()
print("\t\t\t    ( WE TIP-TOP FOODIES )")


def dob_check(x):  # FUNCTION TO CHECKS VALIDITY OF DATE OF BIRTH
    while True:
        if len(x) == 10 and x[0:2].isdigit and (int(x[0:2]) in range(1, 32)) and x[2] == "/" and x[3:5].isdigit() and (
                int(x[3:5]) in range(1, 13)) and x[5] == "/" and x[6:10].isdigit() and (
                int(x[6:10]) in range(1900, 2020)):
            return x
        elif len(x) == 10 and (int(x[0:2]) not in range(1, 32)) and x[0:2].isdigit and x[2] == "/" and x[
            3:5].isdigit() and (
                int(x[3:5]) in range(1, 13)) and x[5] == "/" and x[6:10].isdigit() and (
                int(x[6:10]) in range(1900, 2020)) and len(x) == 10:
            x = input("Invalid Day. Enter A Valid Date: ")
        elif len(x) == 10 and (int(x[3:5]) not in range(1, 13)) and x[0:2].isdigit and (int(x[0:2]) in range(1, 32)) and \
                x[2] == "/" and x[3:5].isdigit() and x[5] == "/" and x[6:10].isdigit() and (
                int(x[6:10]) in range(1900, 2020)) and len(x) == 10:
            x = input("Invalid Month. Enter A Valid Date: ")
        elif len(x) == 10 and (int(x[6:10]) not in range(1900, 2020)) and x[0:2].isdigit and (
                int(x[0:2]) in range(1, 32)) and x[2] == "/" and x[3:5].isdigit() and (int(x[3:5]) in range(1, 13)) and \
                x[5] == "/" and x[6:10].isdigit() and len(x) == 10:
            x = input("This Year Is Not Available. Enter A Valid Date: ")
        else:
            x = input("Invalid Entry. Enter A Valid Date: ")


def mobile_no_check(x):  # FUNCTION TO CHECK VALIDITY OF MOBILE NUMBER
    while True:
        if x[0:4].isdigit() and x[5:13].isdigit() and x[0:2] == "03" and len(x) == 12 and x[4] == "-":
            return x
        else:
            x = input(
                "Invalid Entry. Enter Mobile No# in formate '03XX-XXXXXXX' : ")


def cnic_check(x):  # FUNCTION TO CHECK VALIDITY OF CNIC
    while True:
        if len(x) == 15 and x[5] == "-" and (x[0:5].isdigit()) and x[6:13].isdigit() and x[13] == "-" and x[14].isdigit():
            return x
        else:
            x = input(
                "Invalid Entry. Enter CNIC in this Format 'XXXXX-XXXXXXX-X': ")


def main_end_check(x):  # TO CHECK MAIN AND END VALID COMMAND
    main_end_check_list = ["#", "*", "b", "B"]
    while True:
        if x in main_end_check_list:
            return x
        else:
            x = input("Invalid Entry. Kindly Reply in '#' OR '*' : ")


def yes_no_check(x):  # CHECK FOR YES NO COMMAND
    while True:
        yes_no_check_list = ["y", "yes", "no", "n"]
        if x in yes_no_check_list:
            return x
        else:
            x = input("Invalid Entry. Kindly Reply in 'yes' or 'no': ")


def digit(x):  # FUNCTION CHECK FOR DIGIT ENTRY
    while True:
        if x.replace(".", " ").lstrip("+,-").isdigit():
            return x
        else:
            x = input("Invalid Entry. Kindly Enter in Numbers: ")


def space(x):  # FUNCTION TO GIVE SPACE AND ARRANGE LIST IN ORDER
    for z in range(x, 30):
        print(" ", end="")


def space2(x):  # FUNCTION TO GIVE SPACE AND ARRANGE LIST IN ORDER
    for z in range(x, 16):
        print(" ", end="")


def space3(x):  # FUNCTION TO GIVE SPACE AND ARRANGE LIST IN ORDER
    for z in range(x, 22):
        print(" ", end="")


def product_space(x):  # FUNCTION TO GIVE SPACE AND ARRANGE LIST IN ORDER
    for z in range(x, 16):
        print(" ", end="")


def price_space(x):  # FUNCTION TO GIVE SPACE AND ARRANGE LIST IN ORDER
    for z in range(x, 6):
        print(" ", end="")


repeat = "y"
while repeat == "y" or repeat == "yes":  # THIS LOOP IS TO REPEAT THE CODE
    name = input("\nDear User Kindly Enter your name: ")
    address = input("Kindly Enter Your Address: ")

    while True:  # THIS LOOP IS FOR THE MAIN MENU

        with open("data.json") as jsonFile:
            project_data = json.load(jsonFile)
            jsonFile.close()

        print(
            "\n\nPress '1' To Buy Something From Stock \nPress '2' To Apply For Job in SARMADI BAKERS \nPress '3' To "
            "Apply For Lucky Draw of Umrah Ticket")

        def choice(x):  # FUNCTION FOR CHECK PURPOSE
            while True:
                if x == "1" or x == "2" or x == "3":
                    return x
                else:
                    x = input("Kindly Enter a Valid Choice: ")

        initial_choice = int(choice(input("Enter Your Choice: ")))

        if initial_choice == 1:
            # RANDOMLY CHOOSE OUR EMPLOY
            employ = random.choice(["Mr. Ali", "Mr. Talha"])
            # LIST FOR CHECK PURPOSE OF ITEM SELECTION
            item_selection_check_list = ["e"]
            # LIST FOR CHECK PURPOSE TO REMOVE ITEMS
            remove_check_list = ["e", "b"]
            products = project_data["products"]
            print("\n")
            sold_items = []  # LIST FOR STORING SOLD ITEMS
            remove_items = []  # LIST FOR STORING ITEM NUMBERS THAT WE WANNA REMOVE

            remove = "b"
            while remove == "b":  # LOOP FOR MOVING BACK
                sold_items_prices = []  # LIST FOR STORING PRICES OF SOLD ITEMS
                total_price = 0  # VARIABLE FOR STORING TOTAL BILL
                print("\nLIST OF AVAILABLE PRODUCTS :")
                print("----------------------------")
                # THESE BELOW LINES OF CODE IS DISPLAYING PRODUCTS IN LIST
                for k in range(len(products)):
                    print(k, ": ", end="")
                    item_selection_check_list.append(str(k))
                    key_tuple = tuple(products.keys())
                    value_tuple = tuple(products.values())
                    for i in range(k, len(key_tuple)):
                        print(key_tuple[i], end="")
                        item = key_tuple[i]
                        Length = len(item)
                        for j in range(Length, 16):
                            print(" ", end="")
                        print("=\t", value_tuple[k])
                        break

                while True:  # THIS LOOP IS FOR CHECK PURPOSE AND FOR STORING USER CHOICES REGARDING PRODUCT SELLING
                    item_selection = input(
                        "\nChoose Item or Enter 'e' to Exit: ").lower()
                    if item_selection in item_selection_check_list:
                        if item_selection == "e":
                            break
                        else:
                            bought = key_tuple[int(item_selection)]
                            sold_items.append(bought)
                    else:
                        print("Invalid Entry. This Choice is Not Available")

                # THIS LOOP IS FOR STORING SOLD ITEM PRICES
                for items_nos in range(len(sold_items)):
                    price = str(products[sold_items[items_nos]])
                    sold_items_prices.append(price)

                # THESE BELOW LINES ARE DISPLAYING SELECTED ITEMS IN LIST
                print("\nLIST OF CHOOSEN ITEMS:")
                print("----------------------")
                for l in range(len(sold_items)):
                    print(l, ") ", sold_items[l], end="")
                    remove_check_list.append(str(l))
                    total_price = total_price + products[sold_items[l]]

                    for m in range(len(sold_items[l]), 16):
                        print(" ", end="")
                    print("=\t", sold_items_prices[l])
                print("------------------------------")
                print("Total           =\t", total_price)

                while True:  # THIS LOOP IS STORING THE ENTRIES THAT WE WANNA REMOVE
                    remove = input(
                        "\nChoose Item To Remove or Type 'e' To End or type 'b' To Go Back: ").lower()
                    if remove in remove_check_list:
                        if remove == "e" or remove == "b":
                            break
                        else:
                            remove_items.append(int(remove))
                    else:
                        print("Invalid Entry. This Choice is Not Available")
                if remove == "b":
                    continue

            # THESE BELOW LINES OF CODE IS DISPLAY THE FINAL RECEIPT
            print("\nFINAL RECEIPT :")
            print("-----------------")
            for y in range(len(sold_items)):
                if y in remove_items:
                    print(y, ") ", sold_items[y], end="")
                    product_space(len(sold_items[y]))
                    print("=\t", sold_items_prices[y], end="")
                    price_space(len(sold_items_prices[y]))
                    print("REMOVED")
                    total_price = total_price - products[sold_items[y]]
                else:
                    print(y, ") ", sold_items[y], end="")
                    product_space(len(sold_items[y]))
                    print("=\t", sold_items_prices[y])
            print("------------------------------")
            print("Total           =\t", total_price)

            time = (datetime.datetime.today() + datetime.timedelta(hours=0.5)).strftime(
                "%I:%M %p")  # TO DISPLAY 30 MINS AFTER TIME

            if total_price == 0:
                final = main_end_check(
                    input("\nType '#' To Move To Main Menu OR Type '*' To End:  "))
                if final == "#":
                    continue
                elif final == "*":
                    break
            else:
                print("\nDear ", name, ", you will have to pay the bill of Rs:", total_price, " to ", employ,
                      " he will be at: ", address, " with your products uptill ", time)
                final = main_end_check(
                    input("\nType '#' To Move To Main Menu OR Type '*' To End:  "))
                if final == "#":
                    continue
                elif final == "*":
                    break

        if initial_choice == 2:
            jobs = ["Chef", "Retailer", "Promoter", "Security Guard", "Sanitary Inspector", "Food Inspector",
                    "Emergency Dealer", "Cash Manager"]
            print("\nLIST OF AVAILABLE JOBS:")
            print("-----------------------")
            job_selection_check_list = []  # LIST FOR CHECK PURPOSE OF JOB SELECTION

            for i in range(len(jobs)):  # LOOP FOR DISPLAYING JOBS IN PROPER LIST
                print(i, ": ", jobs[i])
                job_selection_check_list.append(str(i))

            apply = input("\nChoose The Job You Want To Apply For: ")
            while True:  # LOOP FOR CHECK PURPOSE
                if apply in job_selection_check_list:
                    break
                else:
                    apply = input(
                        "This Choice Is Not Available. Kindly Enter A Valid Choice: ")

            # BELOW LINES OF CODE ARE JOB CONDITIONS
            if jobs[int(apply)] == "Chef":
                degree = yes_no_check(
                    input("Have you got the degree of Culinary Arts: ").lower())
                if degree == "yes":
                    print("\nDear ", name,
                          ", kindly come to our office on Monday at 10:00 AM, CEO Muhammad Sarmad and Manager Waqas will conduct a short interview")
                if degree == "no":
                    print(
                        "\nDear ", name, ", You should have the degree of Culinary Arts if you want this Job")

            elif jobs[int(apply)] == "Retailer":
                degree = yes_no_check(
                    input("Would you have a Good English Speaking and Communication Skills: ").lower())
                if degree == "yes":
                    print("\nDear ", name,
                          ", kindly come to our office on Monday at 10:00 AM, CEO Muhammad Sarmad and Manager Waqas "
                          "will conduct a short interview")
                if degree == "no":
                    print("\nDear ", name,
                          ", You should have a Good English Speaking and Communication Skills if you want this Job")

            elif jobs[int(apply)] == "Promotor":
                degree = yes_no_check(
                    input("Would you have a Degree in Marketing: ").lower())
                if degree == "yes":
                    print("\nDear ", name,
                          ", kindly come to our office on Monday at 10:00 AM, CEO Muhammad Sarmad and Manager Waqas "
                          "will conduct a short interview")
                if degree == "no":
                    print(
                        "\nDear ", name, ", You should have a Degree in Marketing if you want this Job")

            elif jobs[int(apply)] == "Security Guard":
                height = int(
                    digit(input("Kindly Enter your height in Centimeters: ")))
                age = int(digit(input("Kindly Enter your age in Years: ")))
                if height < 178 and (age in range(25, 46)):
                    print("\nDear ", name, ", You are short-heighted for this job")
                elif height > 187 and (age in range(25, 46)):
                    print("\nDear ", name, ", You are over-heighted for this job")
                elif age < 25 and (height in range(178, 188)):
                    print("\nDear ", name, ", You are below age for this job")
                elif age > 45 and (height in range(178, 188)):
                    print("\nDear ", name, ", You are over age for this job")
                elif height < 178 and age < 25:
                    print("\nDear ", name,
                          ", You are short-heighted and Below age for this job")
                elif height < 178 and age > 45:
                    print("\nDear ", name,
                          ", You are short-heighted and over age for this job")
                elif height > 187 and age < 25:
                    print("\nDear ", name,
                          ", You are over-heighted and Below age for this job")
                elif height > 187 and age > 45:
                    print("\nDear ", name,
                          ", You are over-heighted and over age for this job")
                else:
                    print(
                        "\nCome to our office on Monday at 10:00 AM to take your Uniform")

            elif jobs[int(apply)] == "Sanitary Inspector":
                degree = yes_no_check(
                    input("Would you have a Diploma in Sanitary Inspector's course: ").lower())
                if degree == "yes":
                    print("\nDear ", name,
                          ", kindly come to our office on Monday at 10:00 AM, CEO Muhammad Sarmad and Manager Waqas will conduct a short interview")
                if degree == "no":
                    print("\nDear ", name,
                          ", You should have a Diploma in Sanitary Inspector's course if you want this Job")

            elif jobs[int(apply)] == "Food Inspector":
                degree = yes_no_check(
                    input("Would you have a Food Processing Degree: ").lower())
                if degree == "yes":
                    print("\nDear ", name,
                          ", kindly come to our office on Monday at 10:00 AM, CEO Muhammad Sarmad and Manager Waqas will conduct a short interview")
                if degree == "no":
                    print(
                        "\nDear ", name, ", You should have a Food Processing Degree if you want this Job")

            elif jobs[int(apply)] == "Emergency Dealer":
                degree = yes_no_check(
                    input("Would you have a complete Knowledge of First Aid: ").lower())
                if degree == "yes":
                    print("\nDear ", name,
                          ", kindly come to our office on Monday at 10:00 AM, CEO Muhammad Sarmad and Manager Waqas will conduct a short interview")
                if degree == "no":
                    print(
                        "\nDear ", name, ", You should have a complete Knowledge of First Aid if you want this Job")

            elif jobs[int(apply)] == "Cash Manager":
                degree = yes_no_check(
                    input("Would you have a Degree in Accounting and Finance: ").lower())
                if degree == "yes":
                    print("\nDear ", name,
                          ", kindly come to our office on Monday at 10:00 AM, CEO Muhammad Sarmad and Manager Waqas will conduct a short interview")
                if degree == "no":
                    print(
                        "\nDear ", name, ", You should have a Degree in Accounting and Finance if you want this Job")

            final = main_end_check(
                input("\nType '#' To Move To Main Menu OR Type '*' To End:  "))
            if final == "#":
                continue
            elif final == "*":
                break

        # UMRAH TICKET CODING
        if initial_choice == 3:

            try:  # TO WRITE ONCE AND READ EVERYTIME PURPOSE

                if len(project_data["lucky_draw_records"]) == lucky_draw_limit:
                    print("\n------ The Registration Is Over ------")
                    lucky_number = random.randint(0, lucky_draw_limit)

                    try:
                        lucky_number = project_data["lucky_number"]

                    except:
                        project_data["lucky_number"] = str(lucky_number)
                        # save data
                        with open("data.json", "w+") as jsonFile:
                            json.dump(project_data, jsonFile, indent=4)
                            jsonFile.close()

                    # THESE BELOW LINES ARE TO ANNOUNCE THE TICKET WINNER
                    print("\nTHE WINNER OF UMRAH TICKET IS :\n")
                    print(project_data["lucky_draw_records"]
                          [int(lucky_number)]["name"], end="")
                    space3(
                        len(project_data["lucky_draw_records"][int(lucky_number)]["name"]))
                    print("|", project_data["lucky_draw_records"][int(
                        lucky_number)]["cnic"], end="")
                    space2(
                        len(project_data["lucky_draw_records"][int(lucky_number)]["cnic"]))
                    print("|", project_data["lucky_draw_records"][int(
                        lucky_number)]["mobile"], end="")
                    space2(
                        len(project_data["lucky_draw_records"][int(lucky_number)]["mobile"]))
                    print("|", project_data["lucky_draw_records"][int(
                        lucky_number)]["email"], end="")
                    space(
                        len(project_data["lucky_draw_records"][int(lucky_number)]["email"]))
                    print(
                        "|", project_data["lucky_draw_records"][int(lucky_number)]["dob"])
            except:
                print()

            if len(project_data["lucky_draw_records"]) < lucky_draw_limit:
                print(
                    "\n\nPress 1 To Apply For Umrah Ticket\nPress 2 To View The List of Appliers For Umrah Ticket")
                umrah_ticket_check_list = ["1", "2"]  # LIST FOR CHECK PURPOSE

                choice = input("Kindly Choose One of These: ")
                while True:  # LOOP FOR CHECK PURPOSE
                    if choice in umrah_ticket_check_list:
                        break
                    else:
                        choice = input(
                            "Invalid Entry. Kindly Choose '1' or '2' : ")

                # CODE FOR APPLYING FOR TICKET
                if choice == "1":
                    cnic = cnic_check(
                        input("Enter Your CNIC XXXXX-XXXXXXX-X: "))
                    mobile = mobile_no_check(input("Enter Your Mobile N0#: "))
                    email = input("Enter Your Email Address: ")
                    dob = dob_check(
                        input("Enter Your Date of Birth dd/mm/yyyy: "))

                    # add data new
                    project_data["lucky_draw_records"].append({
                        "name": name,
                        "cnic": cnic,
                        "mobile": mobile,
                        "email": email,
                        "dob": dob
                    })

                    # save data new
                    with open("data.json", "w+") as jsonFile:
                        json.dump(project_data, jsonFile, indent=4)
                        jsonFile.close()

                # CODE FOR DISPLAYING APPLIERS IN PROPER LIST
                if choice == "2":
                    if len(project_data["lucky_draw_records"]) > 0:
                        print(
                            "\n     NAME                  |CNIC             |MOBILE NO#       |EMAIL ADDRESS                  |DATE OF BIRTH")
                        print(
                            "-----------------------------------------------------------------------------------------------------------------")
                        for index, record in enumerate(project_data["lucky_draw_records"]):
                            print(index, ") ", record["name"], end="")
                            space3(len(record["name"]))
                            print("|", record["cnic"], end="")
                            space2(len(record["cnic"]))
                            print("|", record["mobile"], end="")
                            space2(len(record["mobile"]))
                            print("|", record["email"], end="")
                            space(len(record["email"]))
                            print("|", record["dob"])
                    else:
                        print("\nRECORD NOT AVAILABLE")

                # CONDITION TO GO TO MAIN OR TO END
                final = main_end_check(
                    input("\nType '#' To Move To Main Menu OR Type '*' To End:  "))
                if final == "#":
                    continue
                elif final == "*":
                    break

    repeat = yes_no_check(
        input("\nDo You Want To Run The Code Again: ").lower())
