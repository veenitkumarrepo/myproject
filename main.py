import product
import re
import worker
import database
import datetime
def workergiver(workerid):
    if(len(database.workerlist) == 0):
        return -2
    for i in range(len(database.workerlist)):
        if(((database.workerlist)[i]).getid() == workerid):
            return i
    return -1

def productgiver(productid):
    if(len(database.productlist) == 0):
        return -2
    for i in range(len(database.productlist)):
        if(((database.productlist)[i]).getid() == productid):
            return i
    return -1

def inputgetterfloat():
    while(True):
        try:
            i = float(input())
            return i
        except:
            print("*imp: enter a numerical value eg: 12.465 , 1.45 , 9.6777")

def inputgetterint():
    while(True):
        i = input()
        if('.' in i):
            print("*imp: enter a integer value eg: 12 , 1 , 9")
        else:
            try:
                ii = int(i)
                return ii
            except:
                print("*imp: enter a integer value eg: 12 , 1 , 9")

def main():
    regex = re.compile('[0123456789@_!#$%^&*()<>?/\|}{~:]')
    f = open("workerdata.txt", "w")
    f.write("")
    f.close()
    f = open("productdata.txt", "w")
    f.write("")
    f.close()
    while(True):
        print("1) enter as worker")
        print("2) add worker")
        print("3) remove worker")
        print("4) add product")
        print("5) remove product")
        print("6) give salaries")
        print("7) product modification")
        print("8) worker modification")
        print("9) exit")
        print("enter number of option to select : ")
        i = inputgetterint()
        while(True):
            if(1 <= i <= 9):
                break
            else:
                print("please enter a number between 1 to 9 both included")
                i = inputgetterint()
        if(i == 1):
            currentworker = None
            while(True):
                print("enter worker id : ")
                workerid = input()
                presentornot = workergiver(workerid)
                if(presentornot == -2):
                    print("no worker is currently present , add some workers")
                    break
                if(presentornot != -1):
                    print("hello " + str(((database.workerlist)[presentornot]).getname()) + "!")
                    currentworker = ((database.workerlist)[presentornot])
                    break
                else:
                    print("this worker id entered is wrong")
            if(currentworker != None):
                bill = []
                if(len(database.productlist) == 0):
                    print("there are no products present , add some products")
                else:
                    for j in range(len(database.productlist)):
                        cp = database.productlist[j]
                        print("product id : " + str(cp.getid()) + "    product name : " + str(cp.getname()) + "    product quantity : " + str(cp.getquantity()) + "    product rate : " + str(cp.getrate()) + "    product tax : " + str(cp.gettax()))
                    while(True):
                        print("1) select product for sale")
                        print("2) exit")
                        j = inputgetterint()
                        while (True):
                            if (1 <= j <= 2):
                                break
                            else:
                                print("please enter a number between 1 to 2 both included")
                                j = inputgetterint()
                        if(j == 1):
                            while(True):
                                print("enter product id : ")
                                productid = input()
                                presentornot = productgiver(productid)
                                if(presentornot != -1):
                                    print("enter quantity : ")
                                    quantity = inputgetterint()
                                    while (True):
                                        if (1 <= quantity <= (database.productlist[presentornot]).getquantity()):
                                            costing = (database.productlist[presentornot]).productselling(quantity)
                                            costing.append(productid)
                                            bill.append(costing)
                                            currentworker.bonusadder(costing[0])
                                            break
                                        else:
                                            print("please enter an available quantity")
                                            quantity = inputgetterint()
                                    break
                                else:
                                    print("this product id entered is wrong")

                        elif(j == 2):
                            dt = str(datetime.datetime.now())
                            fname = dt.replace(" ","")
                            fname = fname.replace(".","_")
                            fname = fname.replace(":","_")
                            fname = fname.replace("-","_")
                            totalbill = 0
                            billtext = "<---------------------------------->\nBILL\n"+dt
                            # print()
                            for i in range(len(bill)):
                                payble = (((bill[i])[0]) - ((bill[i])[1]) + ((bill[i])[2]))
                                totalbill += payble
                                billtext += "\nproduct id : " + ((bill[i])[3]) + "\ntotal : " + str(((bill[i])[0])) + "\ndiscount : " + str(
                                ((bill[i])[1])) + "\ntax : " + str(((bill[i])[2])) + "\n"
                            f = open((fname + ".txt"), "w+")
                            billtext += "\npayble amount : "+str(totalbill)+"\n<---------------------------------->"
                            f.write(billtext)
                            print(billtext)
                            f.close()
                            break
        elif(i == 2):
            print("enter worker name : ")
            name = input()
            while(True):
                if(regex.search(name) != None):
                    print("name should not contain special characters or numbers\nenter worker name : ")
                    name = input()
                else:
                    break
            print("enter worker salary : ")
            salary = inputgetterfloat()
            print("enter worker bonus per 1000 rupees : ")
            bonus = inputgetterfloat()
            newworker = worker.worker(name , salary , bonus)
            database.workerlist.append(newworker)
            dt = datetime.datetime.now()
            info = "<---------------------------------->\nnew worker added\n"+ str(dt) +"\nworker id : " + str(newworker.getid()) + "\nname : " + str(newworker.getname()) + "\nsalary : " + str(newworker.getsalary()) + "\nbonus : " + str(newworker.getbonus()) + "\n<---------------------------------->\n"
            f = open("workerdata.txt", "a")
            f.write(info)
            f.close()
            print(info)
        elif(i == 3):
            currentworker = None
            while(True):
                print("enter worker id : ")
                workerid = input()
                presentornot = workergiver(workerid)
                if(presentornot == -2):
                    print("no worker is currently present , add some workers")
                    break
                if(presentornot != -1):
                    currentworker = ((database.workerlist)[presentornot])
                    dt = datetime.datetime.now()
                    info = "<---------------------------------->\nworker removed\n"+ str(dt) +"\nworker id : " + str(
                        currentworker.getid()) + "\nname : " + str(currentworker.getname()) + "\nsalary : " + str(
                        currentworker.getsalary()) + "\nbonus : " + str(
                        currentworker.getbonus()) + "\n<---------------------------------->\n"
                    database.workerlist.pop(presentornot)
                    f = open("workerdata.txt", "a")
                    f.write(info)
                    f.close()
                    print(info)
                    break
                else:
                    print("this worker id entered is wrong")
        elif(i == 4):
            print("enter product name : ")
            name = input()
            print("enter product quantity : ")
            quantity = inputgetterint()
            print("enter product rate : ")
            rate = inputgetterfloat()
            print("enter product discount percent (without %) : ")
            discount = inputgetterfloat()
            print("enter product tax percent (without %) : ")
            tax = inputgetterfloat()
            newproduct = product.product(name,quantity,rate,discount,tax)
            database.productlist.append(newproduct)
            dt = datetime.datetime.now()
            info = "<---------------------------------->\nnew product addded\n"+ str(dt) +"\nproduct id : " + str(
                newproduct.getid()) + "\nname : " + str(newproduct.getname()) + "\nquantity : " + str(
                newproduct.getquantity()) + "\nrate : " + str(
                newproduct.getrate()) + "\ndiscount : " + str(
                newproduct.getdiscount()) + "\ntax : " + str(
                newproduct.gettax())+ "\n<---------------------------------->\n"
            print(info)
            f = open("productdata.txt", "a")
            f.write(info)
            f.close()
        elif(i == 5):
            currentproduct = None
            while(True):
                print("enter product id : ")
                productid = input()
                presentornot = productgiver(productid)
                if(presentornot == -2):
                    print("no product is currently present , add some products")
                    break
                if(presentornot != -1):
                    currentproduct = ((database.productlist)[presentornot])
                    dt = datetime.datetime.now()
                    info = "<---------------------------------->\nproduct removed\n"+ str(dt) +"\nproduct id : " + str(
                        currentproduct.getid()) + "\nname : " + str(currentproduct.getname()) + "\nquantity : " + str(
                        currentproduct.getquantity()) + "\nrate : " + str(
                        currentproduct.getrate()) + "\ndiscount : " + str(
                        currentproduct.getdiscount()) + "\ntax : " + str(
                        currentproduct.gettax()) + "\n<---------------------------------->\n"
                    database.productlist.pop(presentornot)
                    f = open("productdata.txt", "a")
                    f.write(info)
                    f.close()
                    print(info)
                    break
                else:
                    print("this product id entered is wrong")
        elif(i == 6):
            if(len(database.workerlist) == 0):
                print("there are no workers present , add some workers")
            else:
                for j in range(len(database.workerlist)):
                    print("worker id : " + str((database.workerlist[j]).getid()) + "    worker name : " + str((database.workerlist[j]).getname()) + "     total : " + str((database.workerlist[j]).gettotal()))
        elif(i == 7):
            check = True
            while(check):
                print("enter product id : ")
                productid = input()
                presentornot = productgiver(productid)
                if(presentornot == -2):
                    print("no product is currently present , add some products")
                    break
                if(presentornot != -1):
                    while(True):
                        print("1) add quantity")
                        print("2) change rate")
                        print("3) change discount")
                        print("4) change tax")
                        print("5) exit")
                        choice = inputgetterint()
                        while (True):
                            if (1 <= choice <= 5):
                                break
                            else:
                                print("please enter a number between 1 to 5 both included")
                                choice = inputgetterint()
                        if(choice == 1):
                            print("enter quantity to add : ")
                            quantity = inputgetterint()
                            ((database.productlist)[presentornot]).addquantity(quantity)
                            print("done!")
                        elif(choice == 2):
                            print("enter new rate : ")
                            newrate = inputgetterfloat()
                            ((database.productlist)[presentornot]).setrate(newrate)
                            print("done!")
                        elif(choice == 3):
                            print("enter new discount : ")
                            newdiscount = inputgetterfloat()
                            ((database.productlist)[presentornot]).setdiscount(newdiscount)
                            print("done!")
                        elif(choice == 4):
                            print("enter new tax : ")
                            newtax = inputgetterfloat()
                            ((database.productlist)[presentornot]).settax(newtax)
                            print("done!")
                        elif(choice == 5):
                            currentproduct = ((database.productlist)[presentornot])
                            dt = datetime.datetime.now()
                            info = "<---------------------------------->\nproduct after changes\n"+ str(dt) +"\nproduct id : " + str(
                                currentproduct.getid()) + "\nname : " + str(currentproduct.getname()) + "\nquantity : " + str(
                                currentproduct.getquantity()) + "\nrate : " + str(
                                currentproduct.getrate()) + "\ndiscount : " + str(
                                currentproduct.getdiscount()) + "\ntax : " + str(
                                currentproduct.gettax()) + "\n<---------------------------------->\n"
                            f = open("productdata.txt", "a")
                            f.write(info)
                            f.close()
                            print(info)
                            check = False
                            break
                else:
                    print("this product id entered is wrong")
        elif(i == 8):
            check = True
            while(check):
                print("enter worker id : ")
                workerid = input()
                presentornot = workergiver(workerid)
                if(presentornot == -2):
                    print("no worker is currently present , add some workers")
                    break
                if(presentornot != -1):
                    while(True):
                        print("1) change salary")
                        print("2) change bonus")
                        print("3) exit")
                        choice = inputgetterint()
                        while (True):
                            if (1 <= choice <= 3):
                                break
                            else:
                                print("please enter a number between 1 to 3 both included")
                                choice = inputgetterint()
                        if(choice == 1):
                            print("enter new salary : ")
                            newsalary = inputgetterfloat()
                            ((database.workerlist)[presentornot]).setsalary(newsalary)
                            print("done!")
                        elif(choice == 2):
                            print("enter new bonus : ")
                            newbonus = inputgetterfloat()
                            ((database.workerlist)[presentornot]).setbonus(newbonus)
                            print("done!")
                        elif(choice == 3):
                            currentworker = ((database.workerlist)[presentornot])
                            dt = datetime.datetime.now()
                            info = "<---------------------------------->\nworker after changes\n"+ str(dt) +"\nworker id : " + str(
                                currentworker.getid()) + "\nname : " + str(
                                currentworker.getname()) + "\nsalary : " + str(
                                currentworker.getsalary()) + "\nbonus : " + str(
                                currentworker.getbonus()) + "\n<---------------------------------->\n"
                            f = open("workerdata.txt", "a")
                            f.write(info)
                            f.close()
                            print(info)
                            check = False
                            break
                else:
                    print("this worker id entered is wrong")
        elif(i == 9):
            print("thank you for using")
            break

database.workerlist.append(worker.worker("raju",1500,2))
database.productlist.append(product.product("jalebi" , 50 , 500 , 2 , 3.2))
database.productlist.append(product.product("fafda" , 60 , 600 , 3 , 3.1))
database.productlist.append(product.product("thepla" , 70 , 700 , 4 , 3.3))
database.productlist.append(product.product("khandvi" , 80 , 800 , 5 , 3.4))
database.productlist.append(product.product("khakra" , 90 , 900 , 6 , 3.6))
database.productlist.append(product.product("ladu" , 55 , 1000.93 , 7 , 3.9))
database.productlist.append(product.product("rasgulla" , 65 , 500.56 , 8 , 3))
database.productlist.append(product.product("dosa" , 75 , 50.5 , 9 , 3.8))
database.productlist.append(product.product("idli" , 85 , 880.63 , 10 , 3.7))
database.productlist.append(product.product("egg" , 95 , 950.48 , 1 , 3.4))
main()