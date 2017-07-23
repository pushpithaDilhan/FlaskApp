

class Data:
    users = [
        {
            "uid":1,
            "fname":"Pushpitha",
            "lname":"Dilhan",
            "bdate":"1994-11-29",
            "username":"pushpitha",
            "password":"pushpitha123"
        },
        {
            "uid":2,
            "fname":"Mahela",
            "lname":"Jayawardena",
            "bdate":"1984-10-19",
            "username":"mahela",
            "password":"mahela123"
        },
        {
            "uid":3,
            "fname":"Kumar",
            "lname":"Sangakkara",
            "bdate":"1980-01-02",
            "username":"kumara",
            "password":"kumara123"
        },
        {
            "uid":4,
            "fname":"Nuwan",
            "lname":"Kulasekara",
            "bdate":"1988-04-03",
            "username":"nuwan",
            "password":"nuwan123"
        },
        {
            "uid":5,
            "fname":"Anjelo",
            "lname":"Mathews",
            "bdate":"1990-04-05",
            "username":"anjelo",
            "password":"anjelo123"
        },
        {
            "uid":6,
            "fname":"Nimal",
            "lname":"Fernando",
            "bdate":"1990-04-05",
            "username":"a",
            "password":"a"
        }
    ]

    admins = [
        {
            "uid":1000,
            "fname":"Ravindu",
            "lname":"Perera",
            "bdate":"1994-11-29",
            "username":"a",
            "password":"a"
        }
    ]
    
    
    def addUser(self,fname,lname,bdate,username,password):
        uid = max([ user["uid"] for user in self.users])+1
        temp = {
            "uid":uid,
            "fname":fname,
            "lname":lname,
            "bdate":bdate,
            "username":username,
            "password":password        
        }
        self.users.append(temp)

    def updateUser(self,uid,fname,lname,bdate,username,password):
        self.removeUser(uid)
        temp = {
            "uid":uid,
            "fname":fname,
            "lname":lname,
            "bdate":bdate,
            "username":username,
            "password":password        
        }
        sorted(self.users, key=lambda k: k['uid']) 
        self.users.append(temp)

    def removeUser(self,uid):
        for user in self.users:
            if user["uid"]==uid:
                self.users.remove(user)
    
    def getUser(self,uid):
        for user in self.users:
            if user["uid"]==uid:
                return user
    
    def isUser(self,username,password):
        print "user",username,password
        for user in self.users:
            if user["username"]==username and user["password"]==password:
                return user
                print "got it"
            else:
                return False
    
    def isAdmin(self,username,password):
        print "admin",username,password
        for admin in self.admins:
            if admin["username"]==username and admin["password"]==password:
                return admin
            else:
                return False
   

    
