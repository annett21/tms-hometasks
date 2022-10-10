# В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов


with open("Homework_7/marks.txt", "r") as f:
    for student in f:
        if int(student.replace("\n", "")[-1]) < 3:
            print(student, end="")
    print()
