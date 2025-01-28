def main():

    init_pupils_data()
    teachers = Teachers()

    while True:
        print("\n===============")
        print("     MENU ")
        print("1 - Create A Pupil")
        print("2 - Print A Pupil/All Pupils")
        print("3 - Update A Pupil")
        print("4 - Delete A Pupil")
        print("5 - Create A Teacher")
        print("6 - Read A Teacher")
        print("7 - Update A Teacher")
        print("8 - Delete A Teacher")
        print("9 - Exit")
        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            print("NEW PUPIL")
            print("===========")
            pupil = create_pupil()
            if pupil is None:
                continue
            else:
                print("NEW PUPIL")
                print_pupil(pupil)

        elif choice == 2:
            print("\n===============")
            print("     SUB-MENU (PRINT) ")
            print("1 - Print A Pupil")
            print("2 - Print All Pupils (Details)")
            print("3 - Print All Pupils (Just the Names)")
            print_choice = input("Enter the number of your choice: ")
            if print_choice.strip().isdigit():
                print_choice = int(print_choice)
            else:
                print("Wrong input!")
                continue

            if print_choice == 1:
                pupil_id = int(input("Enter the ID: "))
                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Pupil does not exist (with this ID)")
                else:
                    print("   PUPIL   ")
                    print_pupil(pupil)

            elif print_choice == 2:
                print_pupils_details()
            elif print_choice == 3:
                print_pupils_names()
            else:
                print("Wrong input! ")
                continue

        elif choice == 3:
            print("\n===============")
            print("     SUB-MENU (UPDATE) ")
            print("1 - Update A Pupil (search by ID)")
            print("2 - Update A Pupil (search by surname)")
            update_choice = input("Enter the number of your choice: ")
            if update_choice.strip().isdigit():
                update_choice = int(update_choice)
            else:
                print("Wrong input!")
                continue

            if update_choice == 1:
                pupil_id = int(input("Enter the ID: "))
                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Error! There is no pupil with this ID!")
                    continue
            elif update_choice == 2:
                surname = input("Enter the surname: ")
                matching_pupils = search_pupil_by_surname(surname)
                if not matching_pupils:
                    print("No matching pupils with this surname!")
                    continue
                elif len(matching_pupils) == 1:
                    pupil = matching_pupils[0]
                else:
                    for p in matching_pupils:
                        print_pupil(p)
                        print(f"ID = {p['id']}")
                        print("-" * 15)
                    pupil_id = int(input("Enter the ID: "))
                    pupil = search_pupil_by_id(pupil_id)

            # pupil: update
            pupil_update(pupil)

        elif choice == 4:
            print("\n===============")
            print("     SUB-MENU (DELETE) ")
            print("1 - Delete A Pupil (search by ID)")
            print("2 - Delete A Pupil (search by surname)")
            delete_choice = input("Enter the number of your choice: ")
            if delete_choice.strip().isdigit():
                delete_choice = int(delete_choice)
            else:
                print("Wrong input!")
                continue

            if delete_choice == 1:
                pupil_id = int(input("Enter the ID: "))
                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("Error! There is no pupil with this ID!")
                    continue
            elif delete_choice == 2:
                surname = input("Enter the surname: ")
                matching_pupils = search_pupil_by_surname(surname)
                if not matching_pupils:
                    print("No matching pupils with this surname!")
                    continue
                elif len(matching_pupils) == 1:
                    pupil = matching_pupils[0]
                else:
                    for p in matching_pupils:
                        print_pupil(p)
                        print(f"ID = {p['id']}")
                        print("-" * 15)
                    pupil_id = int(input("Enter the ID: "))
                    pupil = search_pupil_by_id(pupil_id)

            # pupil: delete
            delete_pupil_by_id(pupil["id"])
        elif choice==5:
            first_name = input("Enter the name: ")
            surname = input("Enter the surname: ")
            teachers.create_teacher(first_name, surname)
        elif choice==6:
            teacher_id = int(input("Enter the ID: "))
            teacher = teachers.read_teacher(teacher_id)
            if teacher is None:
                print("No such teacher exists!")
            else:
                teacher.print_teacher()
        elif choice==7:
            teacher_id = int(input("Enter the ID: "))
            teachers.update_teacher(teacher_id)
        elif choice==8:
            teacher_id = int(input("Enter the ID: "))
            teachers.delete_teacher(teacher_id)
        elif choice==9:
            print("Exit of the Program!")
            teachers.save_teachers_data()
            save_pupils_data()
            break


main()
