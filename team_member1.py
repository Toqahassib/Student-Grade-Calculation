# from tabulate import tabulate


class student:
    def __init__(self, fname="", lname="", id="", module_no=0, cw=[], weights=[]):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.cw = cw  # list of how many of this item in each brand
        self.weights = weights
        self.module_no = module_no
        self.marks = []
        self.performance = []

    def init_marks(self, ass_num):
        for i in range(ass_num):
            self.marks.append(0)

    def init_performance(self, students):
        for i in range(students):
            self.performance.append(" ")

    def set_marks(self, mid, marks):
        self.marks[mid] = marks

    def set_performance(self, mid, performance):
        self.performance[mid] = performance

    def set_fname(self, fname):
        self.fname = fname

    def set_lname(self, lname):
        self.lname = lname

    def set_id(self, id):
        self.id = id

    def set_module_no(self, module_no):
        self.module_no = module_no

    def set_cw(self, cw):
        self.cw = cw

    def set_weights(self, weights):
        self.weights = weights

    def get_marks(self):
        return self.marks

    def get_performance(self):
        return self.performance

    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname

    def get_id(self):
        return self.id

    def get_module_no(self):
        return self.module_no

    def get_cw(self):
        return self.cw

    def get_weights(self):
        return self.weights


class module:

    def __init__(self, name="", code="", no_students=0, no_cw=0, students=[]):
        self.name = name
        self.code = code
        self.no_students = no_students

        self.students = students
        self.no_cw = no_cw

    def set_students(self, students):
        self.students = students

    def set_names(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_no_students(self, no_students):
        self.no_students = no_students

    def set_no_cw(self, no_cw):
        self.no_cw = no_cw

    def get_students(self):
        return self.students

    def get_names(self):
        return self.name

    def get_code(self):
        return self.code

    def get_no_students(self):
        return self.no_students

    def get_no_cw(self):
        return self.no_cw

        # calculate the avg score of the entire class for a specific assignment per module


module_obj = {}


def same_module_data():
    global module_num, student_num, cw_num, weight_list

    module_num = int(input("\nEnter number of modules: "))

    for j in range(module_num):

        module_name = input("Enter module {} name: ".format(j + 1)).lower()
        module_code = input("Enter module {} code: ".format(j + 1)).lower()

        for sem in range(2):
            single_m = []
            print("\n-------------------------------SEMESTER {}---------------------------------\n".format(sem + 1))

            cw_num = int(input("Enter number of CWs of module {} in semester {}: ".format(j + 1, sem + 1)))

            sum = 0
            while sum != 100:
                weight_list = []
                for k in range(cw_num):
                    weight_list.append(float(input("Enter the weight of CW {}: ".format(k + 1))))
                    sum += weight_list[k]
                if sum != 100:
                    print("Invalid, sum of weights should be equal to 100.")

                student_num = int(input("Enter number of students you want to enter: "))

                # call student fn to enter student info
                students_lst = student_data(module_obj, student_num, cw_num, weight_list, module_num, sem)

                # module_obj[j] = module(module_name, module_code, student_num, cw_num,students)
                module_obj[j] = module()
                module_obj[j].set_names(module_name)
                module_obj[j].set_code(module_code)
                module_obj[j].set_no_students(student_num)
                module_obj[j].set_no_cw(cw_num)
                module_obj[j].set_students(students_lst)

                # single_m.append(module_obj[j].name)
                # single_m.append(module_obj[j].code)
                # single_m.append(module_obj[j].no_students)
                # single_m.append(module_obj[j].no_cw)
                # single_m.append(module_obj[j].students)

                if sem == 0:
                    semester1.append(module_obj[j])
                    # main_studentslst_sem1.append(students_lst)

                elif sem == 1:
                    semester2.append(module_obj[j])
                    # main_studentslst_sem2.append(students_lst)

        modules.append(semester1)
        modules.append(semester2)
        print(modules)


def diff_module_data():
    for sem in range(2):

        print("\n-------------------------------SEMESTER {}---------------------------------\n".format(sem + 1))

        module_num = int(input("Enter number of modules in semester {}: ".format(sem + 1)))

        for j in range(module_num):

            module_name = input("\nEnter module {} name: ".format(j + 1))
            module_code = input("Enter module {} code: ".format(j + 1))

            cw_num = int(input("Enter number of CWs of module {} in semester {}: ".format(j + 1, sem + 1)))
            print(" ")

            sum = 0
            while sum != 100:
                weight_list = []
                for k in range(cw_num):
                    weight_list.append(float(input("Enter the weight of cw: " + str(k + 1) + " ")))
                    sum += weight_list[k]
                if sum != 100:
                    print("Invalid, sum of weights should be equal to 100.")

            student_num = int(input("\nEnter number of students you want to enter: "))

            # call student fn to enter student info
            students_lst = student_data(module_obj, student_num, cw_num, weight_list, module_num, sem)

            module_obj[j] = module(module_name, module_code, student_num, cw_num, students_lst)

            if sem == 0:
                semester1.append(module_obj[j])
                # modules.append(semester1)
                # main_studentslst_sem2.append(students_lst)

            elif sem == 1:
                semester2.append(module_obj[j])
                # modules.append(semester2)
                # main_studentslst_sem2.append(students_lst)

            # modules[j].set_no_students(len(students_lst))

    modules.append(semester1)
    modules.append(semester2)
    print(modules)


obj = {}


def student_data(module_obj, student_number, cw_num, weight_list, module_num, semester):
    students = []
    for i in range(student_number):
        students_fname = input("Enter student {} first name: ".format(i + 1))
        students_lname = input("Enter student {} last name: ".format(i + 1))
        ID = input("Enter id of student {}: ".format(i + 1))

        CWs_list = []

        # while True:
        #     for k in range(0, cw_num):
        #         grades = (float(input("Enter CW {} mark ".format(k + 1))))
        #         if grades <= 100:
        #             CWs_list.append((grades * weight_list[k]) / 100)
        #         else:
        #             print("Invalid, grade should be less than or equal 100.")
        #     break

        for k in range(0, cw_num):
            grades = (float(input("Enter CW {} mark: ".format(k + 1))))
            while grades > 100 or grades < 0:
                print("Invalid, grade should be less than or equal 100.")
                grades = (float(input("Enter CW {} mark: ".format(k + 1))))

            CWs_list.append((grades * weight_list[k]) / 100)

        # obj[i] = student(students_fname, students_lname, ID, module_num, CWs_list, weight_list)
        obj[i] = student()
        obj[i].set_fname(students_fname)
        obj[i].set_lname(students_lname)
        obj[i].set_id(ID)
        obj[i].set_module_no(module_num)
        obj[i].set_cw(CWs_list)
        obj[i].set_weights(weight_list)

        # obj.init_marks(module_num)
        students.append(obj[i])
        if semester == 0:
            main_studentslst_sem1.append(obj[i])
        elif semester == 1:
            main_studentslst_sem2.append(obj[i])

        # students.append(obj[i].fname)
        # students.append(obj[i].lname)
        # students.append(obj[i].id)
        # students.append(obj[i].module_no)
        # students.append(obj[i].cw)

        # module.set_students(students)
        # module_obj[i].set_students(students)
    return students


def validate_numberOfStudentsPerModule(main_studentslst_sem1, main_studentslst_sem2):
    # for semester 1

    id_target = -1
    count = 0
    for student in (main_studentslst_sem1):
        id_target = student.get_id()
        for my_student in (main_studentslst_sem1):
            if id_target == my_student.get_id():
                count = count + 1

        if count < 3:
            print(
                "Student {} {} with ID: {} has registered in less than 3 modules in semester 1, please add more modules.".format(
                    student.get_fname(), student.get_lname(), id_target))

        count = 0

        # for semester 2

    id_target = -1
    count = 0
    for student in (main_studentslst_sem2):
        id_target = student.get_id()
        for my_student in (main_studentslst_sem2):
            if id_target == my_student.get_id():
                count = count + 1

        if count < 3:
            print(
                "Student {} {} with ID: {} has registered in less than 3 modules in semester 2, please add more modules.".format(
                    student.get_fname(), student.get_lname(), id_target))

        count = 0


performance = ""
degree = ""

modules = []

semester1 = []
semester2 = []

students = []

main_studentslst_sem1 = []
main_studentslst_sem2 = []


def module_menu():
    print("-----------------------FIRST WE'LL START BY ENTERING THE MODULE DATA--------------------------")

    print("\n1- Enter the same modules in both semesters")
    print("2- Enter different modules in both semesters")
    same_module = int(input("\nPlease choose the option that suits you (1 or 2): "))

    if same_module == 1:
        same_module_data()
        # validate on number of students per modules in every semester
        validate_numberOfStudentsPerModule(main_studentslst_sem1, main_studentslst_sem2)

    elif same_module == 2:
        diff_module_data()
        # validate on number of students per modules in every semester
        validate_numberOfStudentsPerModule(main_studentslst_sem1, main_studentslst_sem2)

    # print("---------------------------------------STUDENT DATA----------------------------------------")

    # student_data(module_obj)


def menu():
    selection = 0

    while selection != 7:
        print("\n1- Enter student Data \n")
        print("2- calculate and display the avg score of a specific assignment in a module\n")
        print("3- calculate and display the avg score of a module\n")
        print("4- Calculate and display total marks for students in a module \n")
        print("5- Calculate and display total academic performance for students in a module \n")

        print("10-Find the student with the highest mark in a certain module \n")
        print("11-Find the student with the lowest mark in a certain module \n")
        print("12- End the program \n")

        selection = int(input("\nEnter your selection: "))
        if selection != 1 and len(modules) < 1:
            print("you don't have any data yet, please choose 1 to enter some data first \n")

        # input data

        elif selection == 1:
            print("\n1- Enter the same modules in both semesters")
            print("2- Enter different modules in both semesters")
            same_module = int(input("\nPlease choose the option that suits you (1 or 2): "))

            if same_module == 1:
                same_module_data()

            elif same_module == 2:
                diff_module_data()

        # calculate and display the avg score of a specifc assignment in a module

        elif selection == 2:
            mid = int(input("Enter the module number you want: "))
            mid = mid - 1

            cid = int(input("Enter the cw number you want: "))
            cid = cid - 1

            modules[mid].avg_specific_cw(cid)

        # calculate and display the avg score of a module

        elif selection == 3:
            mid = int(input("Enter the module number you want: "))
            mid = mid - 1

            modules[mid].total_marks(mid)

            modules[mid].avg_module(mid)

        # Calculate and display total marks for students in a module

        elif selection == 4:
            mid = int(input("Enter the module number you want: "))
            mid = mid - 1
            modules[mid].total_marks(mid)

            modules[mid].display3(mid)

        # calculate the academic performance for each student over all modules attended

        elif selection == 5:
            mid = int(input("Enter the module number you want: "))
            mid = mid - 1

            modules[mid].total_marks(mid)
            modules[mid].academic_performance(mid, performance, degree)

        # sort alphabetically

        elif selection == 6:
            pass

        # sort by grade

        elif selection == 7:
            pass


        # calculate max mark for a specific cw/module

        elif selection == 8:

            mid = int(input("Enter the module number you want: "))
            mid = mid - 1
            modules[mid].total_marks(mid)

            value, index = modules[mid].max_cw(mid)
            print(" the item with the hihgest mark is \n")
            modules[mid].display2(index, mid)

        # calculate min mark for a specific cw/module

        elif selection == 9:
            pass

        # Find the student with the highest mark in a certain module

        elif selection == 10:

            mid = int(input("Enter the module number you want: "))
            mid = mid - 1

            modules[mid].total_marks(mid)

            value, index = modules[mid].max_student(mid)
            print("the student with the hihgest mark is \n")
            modules[mid].display2(index, mid)

        # Find the student with the lowest mark in a certain module

        elif selection == 11:

            mid = int(input("Enter the module number you want: "))
            mid = mid - 1
            value, index = modules[mid].min_student(mid)

            modules[mid].total_marks(mid)

            print("the student with the lowest mark is \n")
            modules[mid].display2(index, mid)

        # quit

        elif selection == 12:
            print("Thanks for using the program ")


print("-------------------------------------PROGRAM HAS STARTED----------------------------------\n")

module_menu()
# menu()
