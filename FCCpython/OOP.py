#from OOP import rohan
class rohan:

    _testPrivate = None #declaring a private variable without initializing it
    numHoes = 0 #this is an instance variable
    def __init__(self, age, name):
        if age != 20:
            self.age = 20
        else:
            self.age = 69
        self.name = name
        _testPrivate = 2#this is a local variable, not a private variable

#inheritance example
class jugu(rohan): #jugu inherits from rohan
    def __init__(self, nickname, age, name):
        super().__init__(age, name)
        self.nickname = nickname

#Encapsulation: typically use single underscore for protected/non-public, and
#double underscore for private, and python internally changes the name referred to loosely as name mangling

#polymorphism is when 2 different kinds of type animal, like dog and cat have the same method
#animalSound, with the same name, but different implementations, polymorphism allows you to call
#the proper method of the class rather than the parent's method

def main():
    rohan1 = rohan(20, "Rohan")
    rohan2 = rohan(20, "Rohan")

    rohan.numHoes = 69420 #you can modify the actual class variable for all instances of rohan
    rohan1.numHoes = 2103 #this modifys the class variable for only rohan1
    print("Rohan1's numHoes should be 2103: " + str(rohan1.numHoes))
    print("Rohan2's numHoes should be 69420: " + str(rohan2.numHoes))
    print("testPrivate, does it print a warning?", str(rohan1._testPrivate))





if __name__ == "__main__":
    main()
