import sqlite3
class UpdateTable:
    def updateEmployee(self):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        eid=input("Enter EID:")
        while True:

            choice=int(input("Enter choice: 1) Update ENO 2) Update SALARY 3) Update HOTELID 4) Update WORKSHOTELID 5) Exit"))
            if choice==1:
                eno=input("Enter new ENO:")
                c.execute("UPDATE employee SET ENO=(?) WHERE EID=(?)",(eno,eid))
            elif choice==2:
                salary=input("Enter new SALARY:")
                c.execute("UPDATE employee SET SALARY=(?) WHERE EID=(?)",(salary,eid))
            elif choice==3:
                hotelid=input("Enter new HotelID : ")
                c.execute("UPDATE employee SET HOTELID=(?) WHERE EID=(?)",(hotelid,eid))
            elif choice==4:
                workshotelid=input("Enter new WORKSHOTELID:")
                c.execute("UPDATE employee SET WORKSHOTELID=(?) WHERE EID=(?)",(workshotelid,eid))
            elif choice==5:
                break
            else:
                print("Valid choice not entered.")
        conn.commit()
        conn.close()

    def updateOwner(self):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        oid=input("Enter OID:")
        while True:
            choice=int(input("Enter choice: 1) Update MOBILENO 2) EMAILID 3) Exit"))
            if choice==1:
                ono=input("Enter new Mobile No.:")
                c.execute("UPDATE owner SET MOBILENO=(?) WHERE OID=(?)",(ono,oid))
            elif choice==2:
                email=input("Enter new EMAIL-ID:")
                c.execute("UPDATE owner SET EMAILID=(?) WHERE OID=(?)",(email,oid))
            elif choice==3:
                break
            else:
                print("Valid choice not entered.")
        conn.commit()
        conn.close()

    def updateRooms(self):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        hotelid=input("Enter HOTELID:")
        rid=input("Enter RID:")
        while True:
            choice=int(input("Enter choice: 1) Update RTYPE 2) RSTATUS 3) Exit"))
            if choice==1:
                rtype=""
                while True:
                    rtype=input("ENTER Room Type:")
                    if rtype.lower() in ['ac','non-ac']:
                        break
                    print("Room type must be ac or non-ac")
                c.execute("UPDATE rooms SET RTYPE=(?) WHERE HOTELID=(?) AND RID=(?)",(rtype,hotelid,rid))
            elif choice==2:
                rstatus=""
                while True:
                    rstatus=input("ENTER Room Status:")
                    if rstatus.lower() in ['available','not available']:
                        break
                    print("Room status must be available or not available")
                c.execute("UPDATE rooms SET RSTATUS=(?) WHERE HOTELID=(?) AND RID=(?)",(rstatus,hotelid,rid))
            elif choice==3:
                break
            else:
                print("Valid choice not entered.")
        conn.commit()
        conn.close()
    
    def updateServices(self):
        conn = sqlite3.connect('Hotel_Management.db')
        conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        sno=input("Enter SNO:")
        while True:
            choice=int(input("Enter choice: 1) Update STYPE 2) SSTATUS 3) PRICE 4) Exit"))
            if choice==1:
                while True:
                    stype=input("ENTER SType:")
                    if stype.lower() in ['gym','restaurant']:
                        break
                    print("Service type must be gym or restaurant")
                c.execute("UPDATE services SET STYPE=(?) WHERE SNO=(?)",(stype,sno))
            elif choice==2:
                while True:
                    sstatus=input("Enter Sstatus:")
                    if sstatus.lower() in ['available','not available']:
                        break
                    print("Service status must be available or not available")
                c.execute("UPDATE services SET SSTATUS=(?) WHERE SNO=(?)",(sstatus,sno))
            elif choice==3:
                price=input("Enter new price:")
                c.execute("UPDATE services SET PRICE=(?) WHERE SNO=(?)",(price,sno))
            elif choice==4:
                break
            else:
                print("Valid choice not entered.")
        conn.commit()
        conn.close()