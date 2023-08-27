import datetime

def gettime():
    return datetime.datetime.now()


def write(b):
    count=0
    if (b==1):
        c=int(input("Press 1 for Exerecise and Press 2 for Diet:- "))
        if c==1:
            while(True):
                count=count+1
                value=input("Type your Exercise:- ")
                with open("Harry_exr.txt","a") as op:

                    op.write(str(count) + ":- " + str([str(gettime())])+ ":- "+ value + "\n")

                more=input("Do you want to add more data:- ")
                if (more=="yes"):
                    print("********Please enter new data*********")
                else:
                    print("********************Thanks your data is added to Harry_exr File*******************")
                    print("*********Data written in file Successfully******************")
                    break
            d=input("you want to display your data? :- ")
            if d=="yes":
                display(b)
            else:
                print("thanks")

        else:
            while (True):
                count = count + 1
                value = input("Type your Diet:- ")
                with open("Harry_diet.txt", "a") as op:

                    op.write(str(count) + ":-" + str([str(gettime())])+ ":- "+ value + "\n")

                more = input("Do you want to add more data:- ")
                if (more == "yes"):
                    print("********Please enter new data*********")
                else:
                    print("********************Thanks your data is added to Harry_diet File*******************")
                    print("*********Data written in file Successfully******************")
                    break
            d = input("you want to display your data? :- ")
            if d == "yes":
                display(b)
            else:
                print("thanks")
    elif (b==2):
        c = int(input("Press 1 for Exerecise and Press 2 for Diet:- "))
        if c == 1:
            while (True):
                count = count + 1
                value = input("Type your Exercise:- ")
                with open("Shubham_exr.txt", "a") as op:
                    op.write(str(count) + ":-" + str([str(gettime())]) + ":- " + value + "\n")

                more = input("Do you want to add more data:- ")
                if (more == "yes"):
                    print("********Please enter new data*********")
                else:
                    print("********************Thanks your data is added to Shubham_exr File*******************")
                    print("*********Data written in file Successfully******************")
                    break
            d = input("you want to display your data? :- ")
            if d == "yes":
                display(b)
            else:
                print("thanks")
        else:
            while (True):
                count = count + 1
                value = input("Type your Diet:- ")
                with open("Shubham_diet.txt", "a") as op:

                    op.write(str(count) + ":-" + str([str(gettime())]) + ":- " + value + "\n")

                more = input("Do you want to add more data:- ")
                if (more == "yes"):
                    print("********Please enter new data*********")
                else:
                    print("********************Thanks your data is added to Shubham_diet File*******************")
                    print("*********Data written in file Successfully******************")
                    break
            d = input("you want to display your data? :- ")
            if d == "yes":
                display(b)
            else:
                print("thanks")
    else:
        c = int(input("Press 1 for Exerecise and Press 2 for Diet:- "))
        if c == 1:
            while (True):
                count = count + 1
                value = input("Type your Exercise:- ")
                with open("Priyanshu_exr.txt", "a") as op:

                    op.write(str(count) + ":-" + str([str(gettime())]) + ":- " + value + "\n")

                more = input("Do you want to add more data:- ")
                if (more == "yes"):
                    print("********Please enter new data*********")
                else:
                    print("********************Thanks your data is added to Priyanshu_exr File*******************")
                    print("*********Data written in file Successfully******************")
                    break
            d = input("you want to display your data? :- ")
            if d == "yes":
                display(b)
            else:
                print("thanks")

        else:
            while (True):
                count = count + 1
                value = input("Type your Diet:- ")
                with open("Priyanshu_diet.txt", "a") as op:

                    op.write(str(count) + ":-" + str([str(gettime())]) + ":- " + value + "\n")

                more = input("Do you want to add more data:- ")
                if (more == "yes"):
                    print("********Please enter new data*********")
                else:
                    print("********************Thanks your data is added to Priyanshu_diet File*******************")
                    print("*********Data written in file Successfully******************")
                    break
            d = input("you want to display your data? :- ")
            if d == "yes":
                display(b)
            else:
                print("thanks")



def display(b):
    if b==1:
        c=int(input("Press 1 for Exerecise and Press 2 for Diet:- "))
        if c==1:
            try:
                with open("Harry_exr.txt") as op:
                    for i in op:
                        print(i, end=" ")
            except Exception as e:
                print("************** Data not found in database Add the data first then try again ****************")

        else:
            try:
                with open("Harry_diet.txt") as op:
                    for i in op:
                        print(i, end=" ")
            except Exception as e:
                print("************** Data not found in database Add the data first then try again ****************")
    elif b==2:
        c = int(input("Press 1 for Exerecise and Press 2 for Diet:- "))
        if c == 1:
            try:
                with open("Shubham_exr.txt") as op:
                    for i in op:
                        print(i, end=" ")
            except Exception as e:
                print("************** Data not found in database Add the data first then try again ****************")
        else:
            try:
                with open("Shubham_diet.txt") as op:
                    for i in op:
                        print(i, end=" ")
            except Exception as e:
                print("************** Data not found in database Add the data first then try again ****************")
    else:
        c = int(input("Press 1 for Exerecise and Press 2 for Diet:- "))
        if c == 1:
            try:
                with open("Priyanshu_exr.txt") as op:
                    for i in op:
                        print(i, end=" ")
            except Exception as e:
                print("************** Data not found in database Add the data first then try again ****************")
        else:
            try:
                with open("Priyanshu_diet.txt") as op:
                    for i in op:
                        print(i, end=" ")
            except Exception as e:
                print("************** Data not found in database Add the data first then try again ****************")


def delete(b):
    if (b==1):
        c=int(input("Press 1 for Exerecise and Press 2 for Diet:- "))
        if c==1:
            value=""

            try:
                with open("Harry_exr.txt") as op:
                    op.write(value)
                    print("********* Exerecise Data Deleted Successfully******************")
            except Exception as e:
                print("************** Data not found in database Add the data first then try again ****************")
            f = input("you want to Add your Exerecise data? :- ")
            if f == "yes":
                write(b)
            else:
                print("thanks")
        else:
            value=""
            try:
                with open("Harry_diet.txt") as op:

                    op.write(value)
                    print("********* Diet Data Deleted Successfully******************")
            except Exception as e:
                print("************** Data not found in database Add the data first then try again ****************")
            f = input("you want to Add your Diet data? :- ")
            if f == "yes":
                write(b)
            else:
                print("thanks")
    elif (b==2):
        c = int(input("Press 1 for Exerecise and Press 2 for Diet:- "))
        if (c ==1):
            value = ""
            try:
                with open("Shubham_exr.txt") as op:
                    op.write(value)
                    print("********* Exerecise Data Deleted Successfully******************")
            except Exception as e:
                print("************** Data not found in database Add the data first then try again ****************")

            f = input("you want to  Exerecise Add your data? :- ")
            if f == "yes":
                write(b)
            else:
                print("thanks")
        else:
            value = ""
            try:
                  with open("Shubham_diet.txt") as op:
                    op.write(value)
                    print("********* Diet Data Deleted Successfully******************")
            except Exception as e:
                print("************** Data not found in database Add the data first then try again ****************")

            f = input("you want to Add your Diet data? :- ")
            if f == "yes":
                write(b)
            else:
                print("thanks")
    else:
        c = int(input("Press 1 for Exerecise and Press 2 for Diet:- "))
        if (c ==1):
            value = ""
            try:
                  with open("Priyanshu_exr.txt") as op:

                    op.write(value)
                    print("********* Exerecise Data Deleted Successfully******************")
            except Exception as e:
                print("************** Data not found in database Add the data first then try again ****************")

            f = input("you want to Add your Exerecise data? :- ")
            if f == "yes":
                write(b)
            else:
                print("thanks")
        else:
            value = ""
            try:
                  with open("Priyanshu_diet.txt") as op:

                    op.write(value)

                    print("*********Diet Data Deleted Successfully******************")
            except Exception as e:
                print("************** Data not found in database Add the data first then try again ****************")

            f = input("you want to Add your Diet data? :- ")
            if f == "yes":
                write(b)
            else:
                print("thanks")



print("Health Menagement System")

a=int(input("Press 1 for Write the value and 2 for Displayed the value and 3 for Delete the value from the file:- "))

if a==1:
    b=int(input("Press 1 for Harry 2 for Shubham 3 for Priyanshu:- "))
    write(b)

elif a==2:
    b=int(input("Press 1 for Harry 2 for Shubham 3 for Priyanshu:- "))
    display(b)
else:
    b = int(input("Press 1 for Harry 2 for Shubham 3 for Priyanshu:- "))
    delete(b)