class UserProfile:
    def __init__(self,userName,userAge,userGender):
        self.userName = userName
        self.userAge = userAge
        self.__userGender = userGender
    def printUserName(self):
        print(self.userName)
    def printUserAge(self):
        print(f"{self.userName} is {20-18}")
    def printUserAddress(self):
        print(f"{self.userName} lives in New York")

class childClass(UserProfile):
    def __init__(self,userName,userAge,userGender,userAddress,userCity):
        super().__init__(userName,userAge,userGender)
        self.userAddress = userAddress
        self.userCity = userCity
    def printUserAddress(self):
        print(f"{self.userName} lives in New York")