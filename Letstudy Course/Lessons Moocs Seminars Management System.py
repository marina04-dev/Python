from random import randrange, seed
from datetime import datetime

# Initialize seed for random numbers
seed(datetime.now().timestamp())


class Letstudy:
    lesson_id = 0

    def __init__(self, title="Unknown", name="Unknown", cost=0):
        self.title = title
        self.name = name
        self.cost = cost
        self.lesson_id = 'CRS-' + str(randrange(0, 9999))

    def less_id(self):
        return self.lesson_id


class Moocs(Letstudy):
    Num_Of_Mooc = 0

    def __init__(self, title="Unknown", name="Unknown", cost=0, mooc_type="Self-Paced", certification=False):
        super().__init__(title, name, cost)
        self.mooc_type = mooc_type
        self.certification = certification
        Moocs.Num_Of_Mooc += 1

    @classmethod
    def total_Moocs(cls):
        return cls.Num_Of_Mooc

    def __del__(self):
        Moocs.Num_Of_Mooc -= 1

    def __str__(self):
        return f"({self.lesson_id}) {self.title}"


class Seminars(Letstudy):
    Num_Of_Seminars = 0

    def __init__(self, title="Unknown", name="Unknown", cost=0, organizer="Unknown"):
        super().__init__(title, name, cost)
        self.organizer = organizer
        Seminars.Num_Of_Seminars += 1

    @classmethod
    def total_Seminars(cls):
        return cls.Num_Of_Seminars

    def __del__(self):
        Seminars.Num_Of_Seminars -= 1

    def __str__(self):
        return f"({self.lesson_id}) {self.title}"


mooc_list = []
seminar_list = []

while True:
    print("\n1- Create Lesson")
    print("2- Print Lessons")
    print("3- Exit")
    make = input("Enter your choice: ")

    if make == "1":
        make_type = input("1- Create MOOC\n2- Create Seminar\nEnter your choice: ")
        title_Of_Lesson = input("Enter the title: ")
        Name_Of_Teacher = input("Enter instructor's name: ")
        cost_Of_Lesson = int(input("Enter the cost: "))

        if make_type == "1":
            status = input("1- Self-Paced\n2- Instructor-Paced\nEnter your choice: ")
            certification = input("1- With Certification\n2- Without Certification\nEnter your choice: ")

            mooc_Type = "Self-Paced" if status == "1" else "Instructor-Paced"
            has_certification = True if certification == "1" else False

            newmooc = Moocs(title_Of_Lesson, Name_Of_Teacher, cost_Of_Lesson, mooc_Type, has_certification)
            mooc_list.append(newmooc)

        elif make_type == "2":
            organizer = input("Enter seminar's organizer: ")
            newseminar = Seminars(title_Of_Lesson, Name_Of_Teacher, cost_Of_Lesson, organizer)
            seminar_list.append(newseminar)

        else:
            print("Invalid choice! Please try again.")

    elif make == "2":
        view_lesson = input("1- Print MOOCs\n2- Print Seminars\nEnter your choice: ")

        if view_lesson == "1":
            print(f"Total MOOCs: {Moocs.total_Moocs()}")
            for i in mooc_list:
                print(i)

        elif view_lesson == "2":
            print(f"Total Seminars: {Seminars.total_Seminars()}")
            for i in seminar_list:
                print(i)

        else:
            print("Invalid choice! Please try again.")

    elif make == "3":
        print("Exiting the program.")
        break

    else:
        print("Invalid input! Please try again.")
