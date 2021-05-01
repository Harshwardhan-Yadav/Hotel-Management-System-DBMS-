import sqlite3
class ViewTable:
    def viewEmployee(self,mode):
        conn = sqlite3.connect('Hotel_Management.db')
        c = conn.cursor()
        if(mode==3):
            eid=input("Enter EID:")
            c.execute("SELECT * FROM employee WHERE EID=(?);",(eid,))
            print(c.fetchall())
            conn.close()
            return
        choice=int(input("Enter choice: 1)Specific employee 2)All employees"))
        if choice==1:
            eid=input("Enter EID:")
            c.execute("SELECT * FROM employee WHERE EID=(?);",(eid,))
            print(c.fetchall())
        elif choice==2:
            c.execute("SELECT * FROM employee;")
            print(c.fetchall())
        conn.close()
        

    def viewHotel(self):
        conn = sqlite3.connect('Hotel_Management.db')
        c = conn.cursor()
        choice=int(input("Enter choice: 1)Specific hotel 2)All hotels"))
        if choice==1:
            hotelid=input("Enter HOTELID:")
            c.execute("SELECT * FROM hotel WHERE HOTELID=(?);",(hotelid,))
            print(c.fetchall())
        elif choice==2:
            c.execute("SELECT * FROM hotel;")
            print(c.fetchall())
        conn.close()




    def viewCustomer(self,mode):
        conn = sqlite3.connect('Hotel_Management.db')
        c = conn.cursor()
        if(mode==4):
            cid=input("Enter CID:")
            c.execute("SELECT * FROM customer WHERE CID=(?);",(cid,))
            print(c.fetchall())
            conn.close()
            return
        choice=int(input("Enter choice: 1)Specific customer 2)All customers"))
        if choice==1:
            cid=input("Enter CID:")
            c.execute("SELECT * FROM customer WHERE CID=(?);",(cid,))
            print(c.fetchall())
        elif choice==2:
            c.execute("SELECT * FROM customer;")
            print(c.fetchall())
        conn.close()
        
    
    def viewServices(self):
        conn = sqlite3.connect('Hotel_Management.db')
        c = conn.cursor()
        choice=int(input("Enter choice: 1)Specific service 2)All services"))
        if choice==1:
            sno=input("Enter SNO:")
            c.execute("SELECT * FROM services WHERE SNO=(?);",(sno,))
            print(c.fetchall())
        elif choice==2:
            c.execute("SELECT * FROM services;")
            print(c.fetchall())
        conn.close()

    def viewOwner(self):
        conn = sqlite3.connect('Hotel_Management.db')
        c = conn.cursor()
        choice=int(input("Enter choice: 1)Specific owner 2)All owners"))
        if choice==1:
            oid=input("Enter OID:")
            c.execute("SELECT * FROM owner WHERE OID=(?);",(oid,))
            print(c.fetchall())
        elif choice==2:
            c.execute("SELECT * FROM owner;")
            print(c.fetchall())
        conn.close()


    def viewRooms(self):
        conn = sqlite3.connect('Hotel_Management.db')
        c = conn.cursor()
        choice=int(input("Enter choice: 1)Specific room 2)All rooms"))
        if choice==1:
            hotelid=input("Enter HOTELID:")
            rid=input("Enter RID:")
            c.execute("SELECT * FROM rooms WHERE RID=(?) AND HOTELID=(?);",(rid,hotelid,))
            print(c.fetchall())
        elif choice==2:
            c.execute("SELECT * FROM rooms;")
            print(c.fetchall())
        conn.close()
        
    def viewProvides(self):
        conn = sqlite3.connect('Hotel_Management.db')
        c = conn.cursor()
        choice=int(input("Enter choice: 1)Specific provision 2)All provisions"))
        if choice==1:
            hotelid=input("Enter HOTELID:")
            sno=input("Enter SNO:")
            c.execute("SELECT * FROM provides WHERE HOTELID=(?) AND SNO=(?);",(hotelid,sno,))
            print(c.fetchall())
        elif choice==2:
            c.execute("SELECT * FROM provides;")
            print(c.fetchall())
        conn.close()
    
    def viewBooking(self,mode):
        conn = sqlite3.connect('Hotel_Management.db')
        c = conn.cursor()
        if(mode==4):
            hotelid=input("Enter HOTELID:")
            cid=input("Enter CID:")
            c.execute("SELECT * FROM booking WHERE HOTELID=(?) AND CID=(?);",(hotelid,cid,))
            print(c.fetchall())
            conn.close()
            return
        choice=int(input("Enter choice: 1)Specific Booking 2)All Bookings"))
        if choice==1:
            hotelid=input("Enter HOTELID:")
            cid=input("Enter CID:")
            c.execute("SELECT * FROM booking WHERE HOTELID=(?) AND CID=(?);",(hotelid,cid,))
            print(c.fetchall())
        elif choice==2:
            c.execute("SELECT * FROM booking;")
            print(c.fetchall())
        conn.close()
        
    def viewBill(self,mode):
        conn = sqlite3.connect('Hotel_Management.db')
        c = conn.cursor()
        if(mode==4):
            billid=input("Enter BILLID:")
            cid=input("Enter CID:")
            c.execute("SELECT * FROM bill WHERE CID=(?) AND BILLID=(?);",(cid,billid,))
            print(c.fetchall())
            conn.close()
            return
        choice=int(input("Enter choice: 1)Specific Bill 2)All Bills"))
        if choice==1:
            billid=input("Enter BILLID:")
            cid=input("Enter CID:")
            c.execute("SELECT * FROM bill WHERE CID=(?) AND BILLID=(?);",(cid,billid,))
            print(c.fetchall())
        elif choice==2:
            c.execute("SELECT * FROM bill;")
            print(c.fetchall())
        conn.close()