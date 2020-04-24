ucase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z']
lcase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']
specialchar = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '+', '-', '_', '/', '?']
digit = ['1','2','3','4','5','6','7','8','9','0']

def hasUppercase(password):
    for letter in password:
        if letter in ucase:
            return True            
    else:
        return False

def hasLowercase(password):
    for letter in password:
        if letter in lcase:
            return True            
    else:
        return False

def hasSpecialChar(password):
    for letter in password:
        if letter in specialchar:
            return True
            break
    else:
        return False

def hasNumber(password):
    for letter in password:
        if letter in digit:
            return True
            break
    else:
        return False
      
passwrd = str(input('Enter your password: '))
if len(passwrd) >= 8 and len(passwrd) <= 16:
    if hasLowercase(passwrd) == True:
        if hasUppercase(passwrd) == True:
            if hasSpecialChar(passwrd) == True:
                if hasNumber(passwrd) == True:
                    print('Your password qualifies all conditions')
                else:
                    print('You must have atleast one number in your password!')
            else:
                print('Your Password must contain atleast one special character,try again')
        else:
            print('Your Password must contain atleast one upper letter, try again')
    else:
        print('Your Password must contain atleast one lower letter, try again')
else:
    print("invalid password.\nYour password must have minimum 8 and maximum 16 characters")
