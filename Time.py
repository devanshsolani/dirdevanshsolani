class Time:

    hours = 0
    minutes = 0

    def accept(self):
        self.hours = int(input(" Enter time in Hours: "))
        self.minutes = int(input(" Enter time in Minutes: "))

    def display(self):
        print(self.hours, " Hours and: ", self.minutes, " Minutes: ")


class final_time:

    hours = 0
    minutes = 0

    def accept(self, t):
        self.hours = t.hours
        self.minutes = t.minutes

    def sum(self, time1, time2):
        self.minutes = time1.minutes + time2.minutes
        self.hours = self.minutes / 60
        self.minutes = self.minutes % 60
        self.hours = self.hours + time1.hours + time2.hours

    def display(self):
        print(self.hours, "Hours and", self.minutes, "Minutes")

time1_obj = Time()
time1_obj.accept()

time2_obj = Time()
time2_obj.accept()

final = final_time()
final.accept(time1_obj)
final.accept(time2_obj)
final.sum(time1_obj, time2_obj)

print("Time 1 = ")
time1_obj.display()
print("Time 2 = ")
time2_obj.display()
print("Final time  = ")
final.display()
