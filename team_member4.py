from tabulate import tabulate


class student:
    def __init__(self, fname="", lname="", id="", module_no=0, cw=[], weights=[]):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.cw = cw
        self.weights = weights
        self.module_no = module_no
        self.marks = []
        self.performance = []
        self.degree = []

    def set_performance(self, performance, degree):
        self.performance = performance
        self.degree = degree

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

    def set_mark(self, mark):
        self.mark = mark

    def get_marks(self):
        return self.marks

    def get_performance(self):
        return self.performance, self.degree

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

    def get_mark(self):
        return self.mark


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


module_obj = {}


def same_module_data():
    global cw_num
    print("\nYou can enter up to 6 modules.")
    module_num = INTvalidation("Enter number of modules: ")

    while module_num not in range(0, 7):
        print("\nYou can enter up to 6 modules ONLY.")
        module_num = INTvalidation("Enter number of modules: ")

    for j in range(module_num):
        module_name = input("\nEnter module {} name: ".format(j + 1)).upper()

        module_code = input("Enter module {} code (should be in numbers): ".format(j + 1)).upper()

        for sem in range(2):
            print("\n-------------------------------SEMESTER {} in MODULE {}---------------------------------\n".format(sem + 1, j + 1))

            cw_num = INTvalidation("Enter number of CWs of module {} in semester {}: ".format(j + 1, sem + 1))
            while cw_num not in range(0, 11):
                print("You can enter up to 10 courseworks only.")
                cw_num = INTvalidation("Enter number of CWs of module {} in semester {}: ".format(j + 1, sem + 1))

            sum = 0
            while sum != 100:
                sum = 0
                weight_list = []
                for k in range(cw_num):
                    weight_list.append(FLOATvalidation("Enter the weight of CW {}: ".format(k + 1)))
                    sum += weight_list[k]
                if sum != 100:
                    print("Invalid, sum of weights should be equal to 100.")

            print("\nYou can enter up to 1,000 students.")
            student_num = INTvalidation("Enter number of students you want to enter: ")
            while student_num not in range(0, 1001):
                print("You can enter up to 1,000 students ONLY.")
                student_num = INTvalidation("Enter number of students you want to enter: ")

            # call student fn to enter student info
            students_lst = student_data(student_num, cw_num, weight_list, module_num, sem)

            module_obj[j] = module(module_name, module_code, student_num, cw_num, students_lst)

            if sem == 0:
                semester1.append(module_obj[j])

            elif sem == 1:
                semester2.append(module_obj[j])

    modules.append(semester1)
    modules.append(semester2)


def diff_module_data():
    for sem in range(2):
        print("\n-------------------------------SEMESTER {}---------------------------------\n".format(sem + 1))
        print("You can enter up to 6 modules.")
        module_num = INTvalidation("\nEnter number of modules: ")

        while module_num not in range(0, 7):
            print("You can enter up to 6 modules ONLY.")
            module_num = INTvalidation("\nEnter number of modules: ")

        for j in range(module_num):

            module_name = input("\nEnter module {} name: ".format(j + 1)).upper()
            module_code = input("Enter module {} code (should be in numbers): ".format(j + 1)).upper()

            cw_num = INTvalidation("Enter number of CWs of module {} in semester {}: ".format(j + 1, sem + 1))
            while cw_num not in range(0, 11):
                print("You can enter up to 10 courseworks only.")
                cw_num = INTvalidation("Enter number of CWs of module {} in semester {}: ".format(j + 1, sem + 1))

            print(" ")

            sum = 0
            while sum != 100:
                sum = 0
                weight_list = []
                for k in range(cw_num):
                    weight_list.append(FLOATvalidation("Enter the weight of cw: " + str(k + 1) + " "))
                    sum += weight_list[k]
                if sum != 100:
                    print("Invalid, sum of weights should be equal to 100.")

            print("\nYou can enter up to 1,000 students.")
            student_num = INTvalidation("Enter number of students you want to enter: ")
            while student_num not in range(0, 1001):
                print("You can enter up to 1,000 students ONLY.")
                student_num = INTvalidation("Enter number of students you want to enter: ")

            # call student fn to enter student info
            students_lst = student_data(student_num, cw_num, weight_list, module_num, sem)

            module_obj[j] = module(module_name, module_code, student_num, cw_num, students_lst)

            if sem == 0:
                semester1.append(module_obj[j])

            elif sem == 1:
                semester2.append(module_obj[j])

    modules.append(semester1)
    modules.append(semester2)
    print(modules)


obj = {}


def student_data(student_number, cw_num, weight_list, module_num, semester):

    students = []
    for i in range(student_number):
        students_fname = str(input("\nEnter student {} first name: ".format(i + 1))).capitalize()
        students_lname = str(input("Enter student {} last name: ".format(i + 1))).capitalize()
        ID = input("Enter id of student {}: ".format(i + 1)).upper()

        CWs_list = []
        for k in range(0, cw_num):
            grades = (FLOATvalidation("\nEnter CW {} mark: ".format(k + 1)))
            while grades > 100 or grades < 0:
                print("Invalid, grade should be less than or equal 100.")
                grades = (FLOATvalidation("Enter CW {} mark: ".format(k + 1)))

            CWs_list.append((grades * weight_list[k]) / 100)

        mark = sum(CWs_list)

        obj[i] = student()
        obj[i].set_fname(students_fname)
        obj[i].set_lname(students_lname)
        obj[i].set_id(ID)
        obj[i].set_module_no(module_num)
        obj[i].set_cw(CWs_list)
        obj[i].set_weights(weight_list)
        obj[i].set_mark(mark)

        # academicPerformance(semester)
        obj[i].set_performance(performance, degree)
        students.append(obj[i])

        if semester == 0:
            main_studentslst_sem1.append(obj[i])
        elif semester == 1:
            main_studentslst_sem2.append(obj[i])

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
                "\nStudent {} {} with ID: {} has registered in less than 3 modules in semester 1, please add more modules.".format(
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

# view student data in a specific module
def displaydata():

    semester = 0
    while semester not in range(1, 3):
        print("Please choose 1 or 2.")
        semester = INTvalidation('Enter the required semester: ')

    module_code = input('Enter the module code: ')
    stu_table = []
    if semester == 1:
        for module in semester1:
            if module_code == module.get_code():
                for student in module.get_students():
                    academicPerformance(semester)

                    stu = [student.get_fname(), student.get_lname(), student.get_id(), student.get_cw(),
                           student.get_mark(), student.get_performance()]

                    stu_table.append(stu)

                print(tabulate(stu_table, headers=["FIRST NAME", "LAST NAME", "ID", "GRADES", "TOTAL GRADE",
                                                   "(PERFORMANCE , DEGREE)"], showindex=student,
                               tablefmt='fancy_grid'))

    if semester == 2:
        for module in semester2:
            if module_code == module.get_code():
                for student in module.get_students():
                    academicPerformance(semester=2)

                    stu = [student.get_fname(), student.get_lname(), student.get_id(), student.get_cw(),
                           student.get_mark(), student.get_performance()]

                    stu_table.append(stu)
                print(tabulate(stu_table, headers=["FIRST NAME", "LAST NAME", "ID", "GRADES", "TOTAL GRADE",
                                                   "(PERFORMANCE , DEGREE)"], showindex=student,
                               tablefmt='fancy_grid'))


# (a)
def avgScorePerAssessment():
    avg = 0

    semester = 0
    while semester not in range(1, 3):
        print("Please choose 1 or 2.")
        semester = INTvalidation('Enter the required semester: ')

    module_code = input('Enter the module code: ')


    assessment = INTvalidation('Enter the assessment number: ')
    while assessment not in range(1, cw_num + 1):
        print("\nPlease choose a valid number.")
        assessment = INTvalidation('Enter the assessment number: ')

    if semester == 1:
        for module in semester1:
            if module_code == module.get_code():
                for student in module.get_students():
                    assessments = student.get_cw()
                    avg = avg + (assessments[assessment - 1] / module.get_no_students())

        return "\nThe average score of CW {} in module {} is: {}".format(assessment, module_code, avg)

    if semester == 2:
        for module in semester2:
            if module_code == module.get_code():
                for student in module.get_students():
                    assessments = student.get_cw()
                    avg = avg + (assessments[assessment - 1] / module.get_no_students())

        return "\nThe average score of CW {} in module {} is: {}".format(assessment, module_code, avg)


# (b)
def avgScorePerModule():
    avg = 0

    semester = 0
    while semester not in range(1, 3):
        print("Please choose 1 or 2.")
        semester = INTvalidation('Enter the required semester: ')

    module_code = input('Enter the module code: ')

    if semester == 1:
        for module in semester1:
            if module_code == module.get_code():
                for student in module.get_students():
                    marks = student.get_mark()
                    avg = avg + (marks / module.get_no_students())
        return "The average score for module {} is: {}".format(module_code, avg)

    if semester == 2:
        for module in semester2:
            if module_code == module.get_code():
                for student in module.get_students():
                    marks = student.get_mark()
                    avg = avg + (marks / module.get_no_students())

        return "The average score for module {} is: {}".format(module_code, avg)


# (c)
def totalScoreForStudentsPerModule():
    semester = 0
    while semester not in range(1, 3):
        print("Please choose 1 or 2.")
        semester = INTvalidation('Enter the required semester: ')

    module_code = input('Enter the module code: ')
    stu_table = []
    if semester == 1:
        for module in semester1:
            if module_code == module.get_code():
                for student in module.get_students():
                    stu = [student.get_fname(), student.get_lname(), student.get_id(), student.get_mark()]
                    stu_table.append(stu)

                return tabulate(stu_table, headers=["FIRST NAME", "LAST NAME", "ID", "TOTAL GRADE"], showindex=student,
                                tablefmt='fancy_grid')

    if semester == 2:
        for module in semester2:
            if module_code == module.get_code():
                for student in module.get_students():
                    stu = [student.get_fname(), student.get_lname(), student.get_id(), student.get_mark()]
                    stu_table.append(stu)

                return tabulate(stu_table, headers=["FIRST NAME", "LAST NAME", "ID", "TOTAL GRADE"], showindex=student,
                                tablefmt='fancy_grid')


# (d)
def academicPerformance(semester):
    stu_table = []

    if semester == 1:
        for module in semester1:
            for student in module.get_students():
                totalmarks = student.get_mark()

                if totalmarks > 70:
                    performance = "Excellent to outstanding"
                    degree = "First"
                elif totalmarks >= 60:
                    performance = "good to very good"
                    degree = "Upper second 2:1"
                elif totalmarks >= 50:
                    performance = "satisfying"
                    degree = "Lower second 2:2"
                elif totalmarks >= 40:
                    performance = "Sufficient"
                    degree = "Third 3"
                else:
                    performance = "Unsatisfactory"
                    degree = "Fail"

                student.set_performance(performance, degree)

                stu = [student.get_fname(), student.get_lname(), student.get_id(), student.get_mark(),
                       student.get_performance()]
                stu_table.append(stu)

            return tabulate(stu_table,
                            headers=["FIRST NAME", "LAST NAME", "ID", "TOTAL GRADE", "( PERFORMANCE , DEGREE )"],
                            showindex=student, tablefmt='fancy_grid')

    if semester == 2:
        for module in semester2:
            for student in module.get_students():
                totalmarks = student.get_mark()

                if totalmarks > 70:
                    performance = "Excellent to outstanding"
                    degree = "First"
                elif totalmarks >= 60:
                    performance = "good to very good"
                    degree = "Upper second 2:1"
                elif totalmarks >= 50:
                    performance = "satisfying"
                    degree = "Lower second 2:2"
                elif totalmarks >= 40:
                    performance = "Sufficient"
                    degree = "Third 3"
                else:
                    performance = "Unsatisfactory"
                    degree = "Fail"

                student.set_performance(performance, degree)

                stu = [student.get_fname(), student.get_lname(), student.get_id(), student.get_mark(),
                       student.get_performance()]
                stu_table.append(stu)

            return tabulate(stu_table,
                            headers=["FIRST NAME", "LAST NAME", "ID", "TOTAL GRADE", "( PERFORMANCE , DEGREE )"],
                            showindex=student, tablefmt='fancy_grid')


# (e)
def sort_alph(lst, index):
    if len(lst) == 0:
        return []
    else:
        pivot = lst[0]
        lesser = sort_alph([x for x in lst[1:] if x[index] < pivot[index]], index)
        greater = sort_alph([x for x in lst[1:] if x[index] >= pivot[index]], index)
        return lesser + [pivot] + greater


# (e)
def sort_grade(lst, index):
    if len(lst) == 0:
        return []
    else:
        pivot = lst[0]
        lesser = sort_grade([x for x in lst[1:] if x[index] < pivot[index]], index)
        greater = sort_grade([x for x in lst[1:] if x[index] >= pivot[index]], index)
        return greater + [pivot] + lesser


#(f) #(h)
def MaxMinScoreForAssessment():
    maxPerAssessment = -1
    minPerAssessment = 101
    semester = 0
    while semester not in range(1, 3):
        print("Please choose 1 or 2.")
        semester = INTvalidation('Enter the required semester: ')

    module_code = input('Enter the module code: ')
    assessment = INTvalidation('Enter the assessment number: ')
    while assessment not in range(1, cw_num + 1):
        print("\nPlease choose a valid number.")
        assessment = INTvalidation('Enter the assessment number: ')
    while True:
        minmax = input("Do you want to find the minimum or maximum (min for minimum & max for maximum)").lower()
        if minmax == "max":
            break
        elif minmax == "min":
            break
        else:
            print("Invalid, please enter min for minimum and max for maximum.")
    c = 0
    if semester == 1:
        for module in semester1:
            if module_code == module.get_code():
                for student in module.get_students():
                    assessments = student.get_cw()
                    if assessments[assessment - 1] > maxPerAssessment:
                        maxPerAssessment = assessments[assessment - 1]
                        idx = c
                        c = c + 1
                    else:
                        c = c + 1
                max_fstudent = main_studentslst_sem1[idx].get_fname()
                max_lstudent = main_studentslst_sem1[idx].get_lname()
                max_idstudent = main_studentslst_sem1[idx].get_id()
                c = 0
                for student in module.get_students():
                    assessments = student.get_cw()
                    if assessments[assessment - 1] < minPerAssessment:
                        minPerAssessment = assessments[assessment - 1]
                        idx = c
                        c = c + 1
                    else:
                        c = c + 1
                min_fstudent = main_studentslst_sem1[idx].get_fname()
                min_lstudent = main_studentslst_sem1[idx].get_lname()
                min_idstudent = main_studentslst_sem1[idx].get_id()

        if minmax == "min":

            print(tabulate([[module_code, str(semester), str(minPerAssessment)]],
                           headers=['MODULE CODE', 'SEMESTER', 'MINIMUM GRADE'],
                           tablefmt='fancy_grid'))

            while True:
                choice = input("Do you want to view student data of this grade (yes or no): ")

                if choice == "yes":
                    print(tabulate([[min_fstudent, min_lstudent, min_idstudent, str(minPerAssessment)]],
                                   headers=['FIRST NAME', 'LAST NAME', 'ID', 'MINIMUM GRADE'],
                                   tablefmt='fancy_grid'))
                    break
                elif choice == "no":
                    break
                else:
                    print("Please answer with yes or no.")

        if minmax == "max":

            print(tabulate([[module_code, str(semester), str(maxPerAssessment)]],
                           headers=['MODULE CODE', 'SEMESTER', 'MAXIMUM GRADE'],
                           tablefmt='fancy_grid'))
            choice = input("Do you want to view student data of this grade (yes or no): ")

            while True:
                if choice == "yes":
                    print(tabulate([[max_fstudent, max_lstudent, max_idstudent, str(maxPerAssessment)]],
                                   headers=['FIRST NAME', 'LAST NAME', 'ID', 'MAXIMUM GRADE'],
                                   tablefmt='fancy_grid'))
                    break
                elif choice == "no":
                    break
                else:
                    print("Please answer with yes or no.")

    if semester == 2:
        for module in semester2:
            if module_code == module.get_code():
                for student in module.get_students():
                    assessments = student.get_cw()
                    if assessments[assessment - 1] > maxPerAssessment:
                        maxPerAssessment = assessments[assessment - 1]

                        idx = c
                        c = c + 1
                    else:
                        c = c + 1

                max_fstudent = main_studentslst_sem2[idx].get_fname()
                max_lstudent = main_studentslst_sem2[idx].get_lname()
                max_idstudent = main_studentslst_sem2[idx].get_id()

                c = 0
                for student in module.get_students():
                    assessments = student.get_cw()
                    if assessments[assessment - 1] < minPerAssessment:
                        minPerAssessment = assessments[assessment - 1]

                        idx = c
                        c = c + 1
                    else:
                        c = c + 1

                min_fstudent = main_studentslst_sem2[idx].get_fname()
                min_lstudent = main_studentslst_sem2[idx].get_lname()
                min_idstudent = main_studentslst_sem2[idx].get_id()

        if minmax == "min":

            print(tabulate([[module_code, str(semester), str(minPerAssessment)]],
                           headers=['MODULE CODE', 'SEMESTER', 'MINIMUM GRADE'],
                           tablefmt='fancy_grid'))

            while True:
                choice = input("Do you want to view student data of this grade (yes or no): ")

                if choice == "yes":
                    print(tabulate([[min_fstudent, min_lstudent, min_idstudent, str(minPerAssessment)]],
                                   headers=['FIRST NAME', 'LAST NAME', 'ID', 'MINIMUM GRADE'],
                                   tablefmt='fancy_grid'))
                    break
                elif choice == "no":
                    break

                else:
                    print("Please answer with yes or no.")

        if minmax == "max":

            print(tabulate([[module_code, str(semester), str(maxPerAssessment)]],
                           headers=['MODULE CODE', 'SEMESTER', 'MAXIMUM GRADE'],
                           tablefmt='fancy_grid'))
            choice = input("Do you want to view student data of this grade (yes or no): ")

            while True:
                if choice == "yes":
                    print(tabulate([[max_fstudent, max_lstudent, max_idstudent, str(maxPerAssessment)]],
                                   headers=['FIRST NAME', 'LAST NAME', 'ID', 'MAXIMUM GRADE'],
                                   tablefmt='fancy_grid'))
                    break
                elif choice == "no":
                    break
                else:
                    print("Please answer with yes or no.")


# (g) #(h)
def MaxMinScoreForSpecificModule():
    maxPerModule = -1
    minPerModule = 101

    semester = 0
    while semester not in range(1, 3):
        print("Please choose 1 or 2.")
        semester = INTvalidation('Enter the required semester: ')

    module_code = input('Enter the module code: ')

    while True:
        minmax = input("Do you want to find the minimum or maximum (min for minimum & max for maximum)").lower()
        if minmax == "max":
            break
        elif minmax == "min":
            break
        else:
            print("Invalid, please enter min for minimum and max for maximum.")

    c = 0
    if semester == 1:
        for module in semester1:

            if module_code == module.get_code():
                for student in module.get_students():
                    if student.get_mark() > maxPerModule:
                        maxPerModule = student.get_mark()

                        idx = c
                        c = c + 1

                    else:
                        c = c + 1
                max_fstudent = main_studentslst_sem1[idx].get_fname()
                max_lstudent = main_studentslst_sem1[idx].get_lname()
                max_idstudent = main_studentslst_sem1[idx].get_id()

                c = 0
                for student in module.get_students():

                    if student.get_mark() < minPerModule:
                        minPerModule = student.get_mark()
                        idx = c
                        c = c + 1

                    else:
                        c = c + 1

                min_fstudent = main_studentslst_sem1[idx].get_fname()
                min_lstudent = main_studentslst_sem1[idx].get_lname()
                min_idstudent = main_studentslst_sem1[idx].get_id()

        if minmax == "min":

            print(tabulate([[module_code, str(semester), str(minPerModule)]],
                           headers=['MODULE CODE', 'SEMESTER', 'MINIMUM GRADE'],
                           tablefmt='fancy_grid'))

            choice = input("Do you want to view student data of this grade (yes or no): ")

            while True:
                if choice == "yes":
                    print(tabulate([[min_fstudent, min_lstudent, min_idstudent, str(minPerModule)]],
                                   headers=['FIRST NAME', 'LAST NAME', 'ID', 'MINIMUM GRADE'],
                                   tablefmt='fancy_grid'))
                    break
                elif choice == "no":
                    break
                else:
                    print("Invalid, please answer with yes or no.")

        if minmax == "max":

            print(tabulate([[module_code, str(semester), str(maxPerModule)]],
                           headers=['MODULE CODE', 'SEMESTER', 'MAXIMUM GRADE'],
                           tablefmt='fancy_grid'))
            choice = input("Do you want to view student data of this grade (yes or no): ")

            while True:
                if choice == "yes":
                    print(tabulate([[max_fstudent, max_lstudent, max_idstudent, str(maxPerModule)]],
                                   headers=['FIRST NAME', 'LAST NAME', 'ID', 'MAXIMUM GRADE'],
                                   tablefmt='fancy_grid'))
                elif choice == "no":
                    break
                else:
                    print("Invalid, please answer with yes or no.")

    if semester == 2:
        for module in semester2:
            if module_code == module.get_code():
                for student in module.get_students():
                    if student.get_mark() > maxPerModule:
                        maxPerModule = student.get_mark()

                        idx = c
                        c = c + 1

                    else:
                        c = c + 1
                max_fstudent = main_studentslst_sem2[idx].get_fname()
                max_lstudent = main_studentslst_sem2[idx].get_lname()
                max_idstudent = main_studentslst_sem2[idx].get_id()

                c = 0
                for student in module.get_students():

                    if student.get_mark() < minPerModule:
                        minPerModule = student.get_mark()
                        idx = c
                        c = c + 1

                    else:
                        c = c + 1

                min_fstudent = main_studentslst_sem2[idx].get_fname()
                min_lstudent = main_studentslst_sem2[idx].get_lname()
                min_idstudent = main_studentslst_sem2[idx].get_id()

        if minmax == "min":

            print(tabulate([[module_code, str(semester), str(minPerModule)]],
                           headers=['MODULE CODE', 'SEMESTER', 'MINIMUM GRADE'],
                           tablefmt='fancy_grid'))

            choice = input("Do you want to view student data of this grade (yes or no): ")

            while True:
                if choice == "yes":
                    print(tabulate([[min_fstudent, min_lstudent, min_idstudent, str(minPerModule)]],
                                   headers=['FIRST NAME', 'LAST NAME', 'ID', 'MINIMUM GRADE'],
                                   tablefmt='fancy_grid'))
                elif choice == "no":
                    break
                else:
                    print("Invalid, please answer with yes or no.")


        if minmax == "max":

            print(tabulate([[module_code, str(semester), str(maxPerModule)]],
                           headers=['MODULE CODE', 'SEMESTER', 'MAXIMUM GRADE'],
                           tablefmt='fancy_grid'))
            choice = input("Do you want to view student data of this grade (yes or no): ")

            while True:
                if choice == "yes":
                    print(tabulate([[max_fstudent, max_lstudent, max_idstudent, str(maxPerModule)]],
                                   headers=['FIRST NAME', 'LAST NAME', 'ID', 'MAXIMUM GRADE'],
                                   tablefmt='fancy_grid'))
                elif choice == "no":
                    break
                else:
                    print("Invalid, please answer with yes or no.")


def INTvalidation(message):
    while True:
        try:
            userInput_int = int(input(message))

        except ValueError:
            print("Invalid, answer should be in numbers.")
            continue
        else:
            return userInput_int
            break


def FLOATvalidation(message):
    while True:
        try:
            userInput_float = float(input(message))

        except ValueError:
            print("Invalid, answer should be in numbers.")
            continue
        else:
            return userInput_float
            break


def input_menu():
    print("-----------------------FIRST WE'LL START BY ENTERING THE MODULE DATA--------------------------")

    print("\n1- Enter the same modules in both semesters")
    print("2- Enter different modules in both semesters")

    same_module = INTvalidation("\nPlease choose the option that suits you (1 or 2): ")
    while same_module not in range(1, 3):
        print("Pleace chose 1 or 2.")
        same_module = INTvalidation("\nPlease choose the option that suits you (1 or 2): ")

    if same_module == 1:
        same_module_data()
        # validate on number of students per modules in every semester
        validate_numberOfStudentsPerModule(main_studentslst_sem1, main_studentslst_sem2)

    elif same_module == 2:
        diff_module_data()
        # validate on number of students per modules in every semester
        validate_numberOfStudentsPerModule(main_studentslst_sem1, main_studentslst_sem2)


def menu():
    selection = 0

    while selection != 11:
        print("\nPlease choose one of the following: ")

        print("\n1- Display data of students in a module\n")
        print("2- calculate and display the avg score of a specific assessment in a module\n")
        print("3- calculate and display the average score of a module\n")
        print("4- Calculate and display total marks for students in a module \n")
        print("5- Calculate and display academic performance for students in a module \n")
        print("6- Sort the output alphabetically based on the first name of the students\n")
        print("7- Sort the output alphabetically based on the last name of the students\n")
        print("8- Sort the output based on the total score of the students\n")
        print("9- Find the student with the lowest/highest mark in a certain assessment in a module \n")
        print("10- Find the student with the lowest/highest mark in a certain module \n")
        print("11- End the program \n")

        selection = INTvalidation("\nEnter your selection: ")

        # (a) calculate and display the avg score of a specifc assignment in a module
        if selection == 1:
            displaydata()

        if selection == 2:
            print(avgScorePerAssessment())

        # (b) calculate and display the avg score of a module
        elif selection == 3:
            print(avgScorePerModule())

        # (c) Calculate and display total marks for students in a module
        elif selection == 4:
            print(totalScoreForStudentsPerModule())

        # (d) calculate the academic performance for each student over all modules attended
        elif selection == 5:
            semester = 0
            while semester not in range(1, 3):
                print("Please choose 1 or 2.")
                semester = INTvalidation('Enter the required semester: ')

            print(academicPerformance(semester))

        # (e) Sort the output alphabetically based on the first name of the students
        elif selection == 6:
            semester = 0
            while semester not in range(1, 3):
                print("Please choose 1 or 2.")
                semester = INTvalidation('Enter the required semester: ')
            module_code = input('Enter the module code: ')
            stu_table = []
            if semester == 1:
                for module in semester1:
                    if module_code == module.get_code():
                        for student in module.get_students():
                            stu = [student.get_fname(), student.get_lname(), student.get_id(), student.get_cw(),
                                   student.get_mark()]
                            stu_table.append(stu)
                        print(tabulate(sort_alph(stu_table, 0),
                                       headers=["FIRST NAME", "LAST NAME", "ID", "GRADES", "TOTAL GRADE",
                                                "(PERFORMANCE , DEGREE)"], tablefmt='fancy_grid'))

            if semester == 2:
                for module in semester2:
                    if module_code == module.get_code():
                        for student in module.get_students():
                            stu = [student.get_fname(), student.get_lname(), student.get_id(), student.get_cw(),
                                   student.get_mark()]
                            stu_table.append(stu)
                        print(tabulate(sort_alph(stu_table, 0),
                                       headers=["FIRST NAME", "LAST NAME", "ID", "GRADES", "TOTAL GRADE",
                                                "(PERFORMANCE , DEGREE)"], tablefmt='fancy_grid'))

        # (e) Sort the output alphabetically based on the last name of the students
        elif selection == 7:
            semester = 0
            while semester not in range(1, 3):
                print("Please choose 1 or 2.")
                semester = INTvalidation('Enter the required semester: ')
            module_code = input('Enter the module code: ')
            stu_table = []
            if semester == 1:
                for module in semester1:
                    if module_code == module.get_code():
                        for student in module.get_students():
                            stu = [student.get_fname(), student.get_lname(), student.get_id(), student.get_cw(),
                                   student.get_mark()]
                            stu_table.append(stu)
                        print(tabulate(sort_alph(stu_table, 1),
                                       headers=["FIRST NAME", "LAST NAME", "ID", "GRADES", "TOTAL GRADE",
                                                "(PERFORMANCE , DEGREE)"], tablefmt='fancy_grid'))
            if semester == 2:
                for module in semester2:
                    if module_code == module.get_code():
                        for student in module.get_students():
                            stu = [student.get_fname(), student.get_lname(), student.get_id(), student.get_cw(),
                                   student.get_mark()]
                            stu_table.append(stu)
                        print(tabulate(sort_alph(stu_table, 1),
                                       headers=["FIRST NAME", "LAST NAME", "ID", "GRADES", "TOTAL GRADE",
                                                "(PERFORMANCE , DEGREE)"], tablefmt='fancy_grid'))

        # (e) Sort the output based on the total score of the students
        elif selection == 8:
            semester = 0
            while semester not in range(1, 3):
                print("Please choose 1 or 2.")
                semester = INTvalidation('Enter the required semester: ')

            module_code = input('Enter the module code: ')
            stu_table = []

            if semester == 1:
                for module in semester1:
                    if module_code == module.get_code():
                        for student in module.get_students():
                            stu = [student.get_fname(), student.get_lname(), student.get_id(), student.get_cw(),
                                   student.get_mark()]

                            stu_table.append(stu)

                        print(tabulate(sort_grade(stu_table, 4),
                                       headers=["FIRST NAME", "LAST NAME", "ID", "GRADES", "TOTAL GRADE",
                                                "(PERFORMANCE , DEGREE)"], tablefmt='fancy_grid'))

            if semester == 2:
                for module in semester2:
                    if module_code == module.get_code():
                        for student in module.get_students():
                            stu = [student.get_fname(), student.get_lname(), student.get_id(), student.get_cw(),
                                   student.get_mark()]

                            stu_table.append(stu)

                        print(tabulate(sort_grade(stu_table, 4),
                                       headers=["FIRST NAME", "LAST NAME", "ID", "GRADES", "TOTAL GRADE",
                                                "(PERFORMANCE , DEGREE)"], tablefmt='fancy_grid'))

        # (f) max/min for specific assessment
        elif selection == 9:
            MaxMinScoreForAssessment()

        # (g) max/min for specific module
        elif selection == 10:
            MaxMinScoreForSpecificModule()

        # quit
        elif selection == 11:
            print("Thanks for using the program ")


performance = ""
degree = ""

modules = []

semester1 = []
semester2 = []

main_studentslst_sem1 = []
main_studentslst_sem2 = []

stu_table = []

print("-------------------------------------PROGRAM HAS STARTED----------------------------------\n")

input_menu()

menu()
