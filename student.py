class Student:
    def __init__(self, name, rollno):

        self.name = name
        self.rollno = rollno

    def display(self):

        print("name:", self.name)
        print("rollno:", self.rollno)


# The code will give the information as the output
name = str(input("Please enter your name: "))
rollno = str(input("Please enter your roll number: "))

main = Student(name, rollno)
main.display()
