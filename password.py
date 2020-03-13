class Email:

    def __init__(self, demo):
        self.passwd = demo

    def display(self):
        if len(self.passwd) <= 20:
            print ("Correct length")
        else:
            print ("Incorrect length")
            print("the length of your email is", len(self.passwd))


send1 = Email(str(input("Enter pass: ")))
send1.display()


class Email:

    def __init__(self):
        self.is_sent = False

    def send_email(self):
        self.is_sent = True


my_email = Email()
print(my_email.is_sent)

my_email.send_email()
print(my_email.is_sent)
