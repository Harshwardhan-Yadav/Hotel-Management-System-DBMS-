import sys
import sqlite3
from CreateTable import CreateTable
from InsertTable import InsertTable
from ViewTable import ViewTable
from UpdateTable import UpdateTable
from DeleteTable import DeleteTable

def initialize():
    ob = CreateTable()
    ob.createEmployee()
    ob.createHotel()
    ob.createOwner()
    ob.createCustomer()
    ob.createServices()
    ob.createBill()
    ob.createRooms()
    ob.createProvides()
    ob.createBooking()
    ob.login()

def insert():
    ob = InsertTable()
    choice=int(input("Enter your choice: 1) Employee 2) Hotel 3) Owner 4) Customer 5) Services 6) Rooms"))
    if(choice==1):
        eid=input("Enter EID:")
        efirstname=input("Enter EFIRSTNAME:")
        elastname=input("Enter ELASTNAME:")
        eno=input("Enter ENO:")
        salary=input("Enter SALARY:")
        hotelid=input("Enter HOTELID:")
        workshotelid=input("Enter WORKSHOTELID:")
        ob.insertEmployee(eid,efirstname,elastname,eno,salary,hotelid,workshotelid)
        print("Data Entered Successfully")
    elif(choice==2):
        hotelid=(input("Enter HOTELID:"))
        location=(input("Enter LOCATION:"))
        hname=(input("Enter HNAME:"))
        oid=(input("Enter OID:"))
        ob.insertHotel(hotelid,location,hname,oid)
        print("Data Entered Successfully")
    elif(choice==3):
        oid=input("Enter Owner ID:")
        mobileno=input("Enter Mobile Number:")
        emailid=input("Enter EMAIL-ID:")
        fname=input("Enter First Name:")
        lname=input("Enter Last Name:")
        ob.insertOwner(oid,mobileno,emailid,fname,lname)
        print("Data Entered Successfully")
    elif(choice==4):
        cid=input("Enter customer ID: ")
        mobileno=input("Enter Mobile No.: ")
        emailid=input("Enter e-mail:")
        fname=input("Enter First Name: ")
        lname=input("Enter Last Name: ")
        hotelid=input("Enter Hotel-ID: ")
        billid=input("Enter Bill-ID: ")
        amount=input("Enter amount :")
        while True:
            mode=input("Enter Mode:")
            if mode.lower() in ['cash','credit']:
                break
            print("Mode of payment must be cash or card")
        ob.insertCustomer(cid,mobileno,emailid,fname,lname)
        ob.insertBill(billid,cid,amount,mode)
        ob.insertBooking(hotelid,cid)
        print("Data Entered Successfully")
    elif(choice==5):
        sno=input("Enter SNO:")
        price=input("Enter Price:")
        while True:
            stype=input("ENTER SType:")
            if stype.lower() in ['gym','restaurant']:
                break
            print("Service type must be gym or restaurant")
        while True:
            sstatus=input("Enter Sstatus:")
            if sstatus.lower() in ['available','not available']:
                break
            print("Service status must be available or not available")
        hotelid=input("Enter HotelID:")
        ob.insertServices(sno,stype,price,sstatus)
        ob.insertProvides(hotelid,sno)
        print("Data Entered Successfully")
    elif(choice==6):
        rid=input("ENTER Room-ID.:")
        hotelid=input("ENTER Hotel-ID:")
        while True:
            rtype=input("ENTER Room Type:")
            if rtype.lower() in ['ac','non-ac']:
                break
            print("Room type must be ac or non-ac")
        while True:
            rstatus=input("ENTER Room Status:")
            if rstatus.lower() in ['available','not available']:
                break
            print("Room status must be available or not available")
        ob.insertRooms(rid,hotelid,rtype,rstatus)
        print("Data Entered Successfully")
    else:
        print("VALID CHOICE NOT ENTERED!")

def view(mode):     # 1-admin 2-owner 3-employee 4-customer
    ob = ViewTable()
    if(mode==1):
        choice=int(input("Enter your choice: 1) Employee 2) Hotel 3) Owner 4) Customer 5) Services 6) Rooms 7) Provides 8) Booking 9) Bill"))
        if choice==1: 
            ob.viewEmployee(mode)
        elif choice==2:
            ob.viewHotel()
        elif choice==3:
            ob.viewOwner()
        elif choice==4:
            ob.viewCustomer(mode)
        elif choice==5:
            ob.viewServices()
        elif choice==6:
            ob.viewRooms()
        elif choice==7:
            ob.viewProvides()
        elif choice==8:
            ob.viewBooking(mode)
        elif choice==9:
            ob.viewBill(mode)
        else:
            print("Invalid choice.")
    elif(mode==2):
        choice=int(input("Enter your choice: 1) Employee 2) Hotel 3) Owner 4) Customer 5) Services 6) Rooms 7) Provides 8) Booking 9) Bill"))
        if choice==1: 
            ob.viewEmployee(mode)
        elif choice==2:
            ob.viewHotel()
        elif choice==3:
            ob.viewOwner()
        elif choice==4:
            ob.viewCustomer(mode)
        elif choice==5:
            ob.viewServices()
        elif choice==6:
            ob.viewRooms()
        elif choice==7:
            ob.viewProvides()
        elif choice==8:
            ob.viewBooking(mode)
        elif choice==9:
            ob.viewBill(mode)
        else:
            print("Invalid choice.")
    elif(mode==3):
        choice=int(input("Enter your choice: 1) Employee 2) Hotel 3) Owner 4) Services 5) Rooms 6) Provides"))
        if choice==1: 
            ob.viewEmployee(mode)
        elif choice==2:
            ob.viewHotel()
        elif choice==3:
            ob.viewOwner()
        elif choice==4:
            ob.viewServices()
        elif choice==5:
            ob.viewRooms()
        elif choice==6:
            ob.viewProvides()
        else:
            print("Invalid choice.")
    else:
        choice=int(input("Enter your choice: 1) Hotel 2) Customer 3) Services 4) Rooms 5) Provides 6) Booking 7) Bill"))
        if choice==1:
            ob.viewHotel()
        elif choice==2:
            ob.viewCustomer(mode)
        elif choice==3:
            ob.viewServices()
        elif choice==4:
            ob.viewRooms()
        elif choice==5:
            ob.viewProvides()
        elif choice==6:
            ob.viewBooking(mode)
        elif choice==7:
            ob.viewBill(mode)
        else:
            print("Invalid choice.")

def updation():
    ob = UpdateTable()
    choice=int(input("Enter Choice: 1) Employee 2) Owner 3) Rooms 4) Services"))
    if choice==1:
        ob.updateEmployee()
    elif choice==2:
        ob.updateOwner()
    elif choice==3:
        ob.updateRooms()
    elif choice==4:
        ob.updateServices()
    else:
        print("Invalid choice.")

def deletion(mode):
    ob = DeleteTable()
    if mode==1:
        choice=int(input("Enter your choice: 1)Employee 2) Customer 3) Owner 4) Rooms 5) Services 6) Hotel 7) Provides 8) Booking 9) Bill"))
        if choice==1:
            ob.deleteEmployee(1)
        elif choice==2:
            ob.deleteCustomer()
        elif choice==3:
            ob.deleteOwner()
        elif choice==4:
            ob.deleteRooms(1)
        elif choice==5:
            ob.deleteServices(1)
        elif choice==6:
            ob.deleteHotel()
        elif choice==7:
            ob.deleteProvides()
        elif choice==8:
            ob.deleteBooking()
        elif choice==9:
            ob.deleteBill()
        else:
            print("Invalid Choice")
    else:
        choice=int(input("Enter your choice: 1)Employee 2) Rooms 3) Services"))
        if choice==1:
            ob.deleteEmployee(2)
        elif choice==2:
            ob.deleteRooms(2)
        elif choice==3:
            ob.deleteServices(2)
        else:
            print("Invalid Choice")

initialize()
MODE=0
while True:
    choice=int(input("Enter choice: 1) SignUp 2) Login"))
    if choice==1:
        try:
            usr=input("Enter USERNAME:")
            pwd=input("Enter PASSWORD:")
            mode=int(input("Enter MODE: 1)ADMIN 2)OWNER 3)EMPLOYEE 4)CUSTOMER: "))
            conn = sqlite3.connect('Hotel_Management.db')
            conn.execute("PRAGMA foreign_keys = 1")
            c = conn.cursor()
            c.execute("INSERT INTO login VALUES(?,?,?);",(usr,pwd,mode))
            conn.commit()
            conn.close()
        except:
            print("Username not available or mode entered is wrong.")
    elif choice==2:
        loginstatus = False
        usr=input("Enter USERNAME:")
        pwd=input("Enter PASSWORD:")
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute("SELECT * FROM login WHERE USERNAME=(?) AND PASSWORD=(?);",(usr,pwd))
        row = c.fetchall()
        if(len(row)!=0):
            loginstatus=True
            MODE= int(row[0][2])
        else:
            print('login unsuccessful.')
        conn.commit()
        conn.close()
        if(loginstatus):
            break
    else:
        print("Valid choice not entered.")
while True:
    if(MODE==1):
        c1=int(input("Enter choice: 1) Insert 2) Delete 3) Update 4) View 5) Exit"))
        if(c1==1):
            insert()
        elif(c1==2):
            deletion(MODE)
        elif(c1==3):
            updation()
        elif(c1==4):
            view(MODE)
        elif(c1==5):
            break
        else:
            print("Enter valid choice.")
    elif(MODE==2):
        c1=int(input("Enter choice: 1) Insert 2) Delete 3) Update 4) View 5) Exit"))
        if(c1==1):
            insert()
        elif(c1==2):
            deletion(MODE)
        elif(c1==3):
            updation()
        elif(c1==4):
            view(MODE)
        elif(c1==5):
            break
        else:
            print("Enter valid choice.")
    elif(MODE==3):
        c1=int(input("Enter choice: 1) View 2) Exit"))
        if(c1==1):
            view(MODE)
        elif(c1==2):
            break
        else:
            print("Enter valid choice.")
    else:
        c1=int(input("Enter choice: 1) View 2) Exit"))
        if(c1==1):
            view(MODE)
        elif(c1==2):
            break
        else:
            print("Enter valid choice.")