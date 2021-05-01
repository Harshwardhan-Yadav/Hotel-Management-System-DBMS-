# Hotel-Management-System-DBMS-
Hotel Management system using Python sqlite3
Hotel Management System

DBMS Innovative Assignment
(Phase-1)

19BCE301 - Harshwardhan Yadav
19BCE255 - Param Shah
19BCE254 - Neel Shah

FUNCTIONAL REQUIREMENTS
1) The database should save all
information about every hotel,
employee, customer, and owner.
2) It should define a clear and
precise relationship between hotels
and their employees, owners, and
customers
3) There should be a clear
relationship present between each
entity under consideration.
4) It should provide an easy user
interface to customers as well as
employees.
5) It should automatically update
itself upon new billings.
6) It should go with cash as well as
cashless modes of payment.
7) Proper constraints should be
dealt with.
8) Normalization must be achieved.
9) Availability of rooms and services
of a hotel should be known
beforehand.

Relational Schemas:-
1) Hotel(Hotelid int, Location
varchar2(30) NOT NULL, Hname
varchar2(15) NOT NULL, Oid int
REFERENCES Owner(Oid))
2) Owner(Oid int, MobileNo int
Unique, EmailId varchar2(20),
Fname varchar2(15) Not NULL,
Lname varchar2(15) NOT NULL)
3) Bill(Billid int, Cid int
REFERENCES Customer(Cid),
Amount int NOT NULL, Mode
varchar2(4) IN (‘CASH’, ‘CARD’)
NOT NULL)
4) Customer(Cid int, MobileNo int
UNIQUE, EmailId varchar2(20),
Fname varchar2(15) Not NULL,
Lname varchar2(15) NOT NULL)
5) Booking(HotelId int
REFERENCES Hotel(HotelId) NOT
NULL, Cid int REFERENCES
Customer(Cid) NOT NULL)
6) Employee(Eid int, EFirstName
varchar2(15) NOT
NULL,ELastName varchar2(15)
NOT NULL, Eno int UNIQUE,
Salary int NOT NULL, HotelId int
REFERENCES Hotel(HotelId) NOT
NULL, WorksHotelId int
REFERENCES Hotel(HotelId))
7) Provides(HotelId int
REFERENCES Hotel(HotelID) NOT
NULL, Sno int REFERENCES
Services(Sno) NOT NULL)
8) Services(Sno int, Stype
varchar2(10) IN (‘GYM’ ,
‘RESTAURANT’), Price int NOT
NULL, Sstatus varchar2(15) IN
(‘AVAILABLE’ , ‘NOT AVAILABLE’)
NOT NULL)
9) Rooms(Rid int, HotelId int
REFERENCES Hotel(HotelId),
RType varchar2(15) IN (‘AC’, ‘NON
- AC’), Rstatus varchar2(15) IN
(‘Available’, ‘Not Available’))
