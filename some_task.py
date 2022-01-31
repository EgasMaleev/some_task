class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __lt__(stud1, stud2):
        print(stud1.name)
        return stud1.grade < stud2.grade


st1 = Student('Egor', 10)
st2 = Student('Tolya', 9)
print(st1 > st2)
