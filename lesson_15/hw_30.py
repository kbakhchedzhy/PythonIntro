
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__grades = []

    def __str__(self):
        return '{name} - {age}: {grades}'.format(
            name=self.__name,
            age=self.__age,
            grades=' '.join('' + str(grade) + '' for grade in self.__grades)
        )

    def __set_name(self, name):
        if self.__name != name:
            self.__name = name

    def set_age(self, age):
        if 16 <= age < 100:
            self.__age = age

    def add_grades(self, *grades):
        for grade in grades:
            if 1 <= grade <= 12:
                self.__grades.append(grade)

    def __get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_grades(self):
        return self.__grades


class Group:
    def __init__(self, name):
        self.__name = name
        self.__students = []

    def add_students(self, *students):
        for student in students:
            self.__students.append(student)

    def show_group(self):
        for student in self.__students:
            print(student)

    def get_group(self):
        return self.__students


group = Group('PythonIntro07')
group.add_students(Student('Петрова Саша', 20), Student('Барашкин Иван', 30), Student('Мухина Олеся', 40))

students = group.get_group()
students[0].add_grades(5, 4, 0, 18, 1, 5, 5)
students[1].add_grades(0, 0, 2, 5, 0)
students[2].add_grades(10, 5, 0)
group.show_group()
