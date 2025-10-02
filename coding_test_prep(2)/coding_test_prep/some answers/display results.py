def print_finished(fn):
    dict_students = {}

    with open(fn) as f:
        for l in f:
            l = l.strip("\n")
            l_list = l.split(", ")

            l_name = l_list[0]
            l_exam = l_list[1]
            l_grade = int(l_list[2])

            dict_students.setdefault(l_name, {"A" : False, "B" : False, "C" : False, "D" : False, "E" : False})

            result = dict_students[l_name][l_exam]

            if l_grade >= 2 and result <= 0:
                dict_students[l_name][l_exam] = l_grade

    for k, v in dict_student.items():
        graduated = True
        for grade in v.values():
            if grade <= 0:
                graduated = False
                break
        if graduated:
            print(k)





def print_best_student(fn):

    dict_student = {"name" : (0, 0)}
    with open(fn) as f:
        for l in f:
            l = l.strip("\n")
            l_list = l.slip(", ")

            l_name = l_list[0]
            l_exam = l_list[1]
            l_grade = int(l_list[2])

            dict_student.setdefault(l_name, [0, 0])

            if l_grade >= 2:
                dict_student[l_name][0] += 1
                dict_student[l_name][1] += l_grade

    dict_averages ={}
    for k, v in dict_student.items():
        if v[0] == 5:
            dict_averages[k] = v[1] / 5

    averages = sorted(list(dict_averages.items()), key = lambda: x: x[1], reverse = True)
    result = averages[0]
    print(f"{result[0], result[1]}")

print_best_student("grades.txt")
