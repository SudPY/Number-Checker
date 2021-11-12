def valid(phone_num):
    if len(phone_num) != 10:
        return False
    
    if phone_num[0] != '9':
        return False
    
    return True

while True:
    mobilenum = input("Enter the number : ")
    if valid(mobilenum):
        print("Valid number!")
        break
    
    else:
        print("Not a valid number. Please re-enter")
