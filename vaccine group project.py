#nnt guna split() as delimiter untuk file
#range is < (var), not <= (var)
class Patient:
    def __init__(self, name, age, number, chronic_ill, urgency):  # normal constructor
        self.name = name
        self.age = age
        self.number = number
        self.illness = chronic_ill
        self.urgency = urgency

    def getName(self):  # getter
        return self.name

    def getAge(self):
        return self.age

    def getNumber(self):
        return self.number

    def getIllness(self):
        return self.illness


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password


def urgencylevel(chronic_ill, age, name):  # static method
    if chronic_ill.lower() == "yes":
        if age <= 20:
            lvl = "Moderately Urgent"
        elif age > 20 and age <= 40:
            lvl = "Urgent"
        else:
            lvl = "Highly Urgent"
    else:
        if age <= 60:
            lvl = "Not Urgent"
        elif age > 60:
            lvl = "Urgent"
    if name.lower() == "ammar":
        lvl = "Urgent nak mampus"
    return lvl


def append_new_line(filename, args):
    #Open the file in append & read mode ('a+')
    with open(filename, "a+") as baca:
        #Move read cursor to the start of file.
        baca.seek(0)
        #If file is not empty then append '\n'
        data = baca.read(100)
        if len(data) > 0:
            baca.write("\n")
        #Append text at the end of file
        baca.write(args)


def admin():
    value = True
    nilai = True
    adminlist = []
    username = input("\nEnter your username: ")
    pasw = input("Enter your password: ")
    readadmin = open("admindata.txt", "r")  # opens the file
    for i in readadmin:
        datamin = i.split(";")  # splits the line into list using delimiter ;
        un = datamin[0]
        pw = datamin[1]
        obj = Admin(un, pw)  # instantiating object
        adminlist.append(obj)  # append object into list
    for i in adminlist:
        if username == i.username and pasw == i.password:
            nilai = True
            adminauth()
            break
        elif username != i.username and pasw != i.password:
            continue
        else:
            nilai = False
    if nilai == False:
        print("Wrong credentials, try again.")
        admin()
    if nilai == True:
        pass
    readadmin.close()  # closes the file
    print("\n1 - Go to admin options")
    print("2 - Return to homepage (Yes/No)")
    print("3 - Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pw = input("Enter your password: ")
        for i in adminlist:
            if i.password == pw:
                adminauth()
                value = True
                break
            elif i.password != pw:
                value = False
        if value == False:
            print("\n\nWrong password but nice try tho :D")
    elif choice == 2:
        display()
    else:
        pass


def adminauth():
    value = True
    print("\n1 - Show patient data's list")
    print("2 - Search patient's data")
    print("3 - Register a new admin")
    print("4 - Exit")
    patdata = []
    choice = int(input("\nChoose your option: "))
    baca = open("patientdata.txt", "r")
    for x in baca:
        data = x.split(";")
        name = data[0]
        age = data[1]
        number = data[2]
        illness = data[3]
        urgency = data[4]
        obj = Patient(name, age, number, illness, urgency)
        patdata.append(obj)
    baca.close()
    if choice == 1:
        print("Name\t\t\tAge\tNumber\t\tChronic Illness\t\tUrgency")
        print("-------------------------------------------------------------------------------------------")
        for x in patdata:
            print(x.name + "\t\t\t" + x.age + "\t" + x.number + "\t" + x.illness + "\t\t\t" + x.urgency)
    elif choice == 2:
        searchname = input("Enter the name to be searched: ")
        for x in patdata:
            if searchname == x.name:
                print("Name\t\t\tAge\tNumber\t\tChronic Illness\tUrgency")
                print(
                    "-------------------------------------------------------------------------------------------")
                print(x.name + "\t\t\t" + x.age + "\t" + x.number + "\t" + x.illness + "\t\t\t" + x.urgency)
                value = True
                break
            else:
                value = False
        if value == False:
            print("Patient does not exist")
    elif choice == 3:
        nilai = True
        admindata = []
        readadmin = open("admindata.txt", "r")
        for i in readadmin:
            data = i.split(";")
            username = data[0]
            password = data[1]
            obj = Admin(username, password)
            admindata.append(obj)
        readadmin.close()
        paw = input("Enter your password again: ")
        for i in admindata:
            if paw == i.password:
                newusername = input("Enter new admin username: ")
                newpassword = input("Enter new admin password: ")
                data = newusername + ";" + newpassword
                append_new_line("admindata.txt", data)
                nilai = True
            elif paw != i.password:
                nilai = False
        if nilai == False:
            print("1 - Try again")
            print("2 - Exit")
            val = int(input("Enter your choice: "))
            if val == 1:
                adminauth()
            else:
                pass


patient = []


def display():  # static method
    opt = input("Do you want to use the system (Yes/No): ")
    while opt.lower() == "yes":
        signboard()
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            print("\nBe sure to write your data correctly")
            print("-------------------------------------")
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            number = input("Enter your phone number: ")
            illness = input("Do you have any chronic illness: ")
            obj = Patient(name, age, number, illness, urgencylevel(illness, age, name))
            data = name + ";" + str(age) + ";" + number + ";" + \
                illness + ";" + urgencylevel(illness, age, name)
            patient.append(obj)  # append object to list
            append_new_line("patientdata.txt", data)
            print(
                "\nYour data has been added to our database, your appointment will soon be given via phone.")
            opt = input("\nDo you want to use the system again? (Yes/No): ")
        elif choice == 2:
            admin()
            break
        elif choice == 3:
            break
        else:
            print("Invalid input")
            display()
    print("\nThank you for cooperating and contributing towards a better Malaysia")


def end():
    print("\nThank you for using this system.")
    print("If there is any feedback, do not hesitate to email us at vaccinemy@cyber.com\n")


def signboard():
    print("\n----------------------------------------")
    print("Welcome to Malaysia Immunisation Program")
    print("----------------------------------------")
    print("\n1 - Register Vaccine")
    print("2 - Admin")
    print("3 - Exit")


display()
end()
