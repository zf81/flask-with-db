import sqlite3

connect = sqlite3.connect('/Users/fizzahzaidi/Documents/development/python_projects/flask-with-db/Part4_DB_Sqlite/patients.db')  
db = connect.cursor()

db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()

table =  """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL, 
            ssn CHAR(25) NOT NULL, 
            streetaddress CHAR(25) NOT NULL, 
            zipcode CHAR(25) NOT NULL, 
            city CHAR(25) NOT NULL
        ); """
        
db.execute(table)
connect.commit()

db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('12345', 'John', 'Smith', '01/01/2000', '123456789', '123 Water St', '12345', 'New York')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('23456', 'Jane', 'Doe', '02/02/2001', '789345627', '100 Circle Rd', '34567','New York')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('34567', 'Mary', 'Smith', '03/03/2002','109563813','1 Rainbow Rd', '38470', 'Stony Brook')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('45678', 'Bob', 'Smith', '04/04/2003','285095643','2 Benjamin Dr', '01903', 'Brooklyn')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('56789', 'Harry', 'Potter', '06/15/1998', '302585467', '37 Marlboro St', '10567', 'Queens')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('03746', 'Draco', 'Malfoy', '02/11/1998', '204544767', '439 Cyprus Rd', '17306', 'Brooklyn')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('20947', 'Ronald', 'Weasley', '04/12/1997', '004824327', '48 Elmwood Ave', '11386', 'New York')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, ssn, streetaddress, zipcode, city) values('39579', 'Hermoine', 'Granger', '10/29/1997', '274784860', '21 Hogwarts Ave', '96250', 'Queens')")



connect.commit()


# close the connection
connect.close()