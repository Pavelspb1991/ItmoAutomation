from random import randint, sample, randrange

class People:
    possible_sex = {'мужской', 'женский'}

    def __init__(self, name: str, age: int, sex: str):

        self.name = name
        self.age = age
        self.sex = sex
        if sex in self.possible_sex:
            self.sex = sex
        else:
            raise NameError("неверный пол")

class Student(People):

    def __init__(self, name: str, age: int, sex: str):
        super().__init__(name, age, sex)
        self.students_taught: int = 0
        self.knowlendge = []

    def __len__(self):
        return len(self.knowlendge)

    def take(self, topic: str):
       return  self.knowlendge.append(topic)

    def forget(self):
        if self.knowlendge:
            self.knowlendge.pop(randrange(len(self.knowlendge)))


class Teacher(People):
    def __init__(self, name: str , age: int, sex: str):
        super().__init__(name, age, sex)
        self.students_taught: int = 0

    def teach(self, topic: str, *args):
        for student in args:
                student.take(topic)
                self.students_taught += 1



class Materials:
    def __init__(self, *args):
        self.topics = list(args)

    def __len__(self):
        len(self.topics)


themes = Materials("Python", "Version Control Systems", "Relational Databases", "NoSQL databases",
                   "Message Brokers")
teacher = Teacher()
students_data = (("Павел", 23 ,"мужской"),
                 ("Павел", 27 ,"мужской"),
                 ("Лена", 25 ,"женский"),
                 ("Павел", 21 ,"мужской"))

students = [Student(*data) for data in students_data]



for theme in themes.topics:
    students_set = sample(students, k=randint(1, len(students)))
    teacher.teach(theme, *students_set)

for student in students:
    print(student.knowlendge)

for student in students:
    student.forget()

 print('-' * 30)

for student in students:
     print(student.knowlendge)
     print(len(student))

