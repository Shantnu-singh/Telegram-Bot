import mysql.connector

class database():
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host = "localhost" , user = "root" , password = "" , database = "whatsapp" )
            self.mycursor = self.conn.cursor()
        except Exception as e:
            print("Can't connect to my database " , e)
        else:
            print("Connected to my databse")
            
    def register(self , id , name , age , emerge_contanct):
        try:
            self.mycursor.execute("""
                                  INSERT INTO `users` (id , name , age , emergency_contact) VALUES ({} , '{}' , {} , {})
                                  """.format(id, name , age ,emerge_contanct ))
            self.conn.commit()
        except Exception as e:
            print("Can't insert values in table " , e)
        else:
            print("values inserted sucessfully!!! ")
    
    def get_detail(self, name , id):
        try:
            self.mycursor.execute("""
                                  SELECT * FROM `users` WHERE id = {}  OR name LIKE  '{}'
                                  """.format(id , name))
            date = self.mycursor.fetchall()
            print(date)
            
        except Exception as e:
            print("can't retrive values because of :" , e)
        else:
            print("details fatched sucessfully")
            
        
    
if __name__ == "__main__":
    obj = database()
    
    print("You have these choices:")
    print("1. Register ")
    print("2. Get Detail ")
    choice = int(input())
    
    if choice ==  1:
        id = input("Enter ID: ")
        name = input("Enter your name: ")
        age = int(input("Enter the age: ") )
        emerge_contanct = int(input("Enter emergency contact: "))
        obj.register(id,name, age , emerge_contanct)
        
    elif choice ==  2:
        name = input("Enter name to get data: ")
        id = int(input("Enter id: "))
        obj.get_detail(name , id)  
        
    else:
        print("Entered the wrong choice....")
            
    