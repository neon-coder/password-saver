#obsrerve the code and set your passwords you want
print("Hello sir")
    type_password = input("Enter the password: ").strip().capitalize()
    if type_password == "Enty password goes here":
        passwords = print("Here are the passwords")
        print("""
        keep your any email id and others....

        """)

    name = input("Enter your name: ")

    while True:
        if name == "here goes your name":
            enter = input("Please enter the password you want: ")
#what you type which is there after the two equals to you will get the print
        if enter == "your gmail...":
            print("password")
#you can set your passwords and gmail. continue the elif statment or add loop and database to add other passwords
        elif enter == "any other":
            print("password")
#this will keep your passwords safe that nobody can see your passwords without the entry password. if you don't keep else and quit it can print 'Please Enter the passwords you want' in the enter variable
        else:
            quit()  
    
