email = input("Enter your Email: ")
k,j,d=0,0,0
if len(email) >=6 or len(email) <=15:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1) and (email[-10] == "@"):
            if (email[-4] ==".") ^ (email[-3] ==".") and (email[-9:-4] == "gmail" ):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i== "_" or i=="." or i=="@":
                        continue
                    else:
                        d=0
                if k==1 or j==1 or d==1:
                    print("Do not use space or any uppercase letter or any special character.")
                else:
                    print("Correct email address.")
            else:
                print("Sorry, this is not a valid email address.")
        else:
            print("@ should be used properly.")
    else:
        print("First letter of a email should be an alphabet.")
else:
    print("Email should be greater than 6 characters and less than 15 characters.")