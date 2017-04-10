# A cat has a(verbs)

#Tail - float/int
#color- string
#Fur length - float/int
# Smell - string
#name - string
# breed - string
#number of legs - int
#isMale(gender) - boolean(string)
#meow - string
# position - point (point is user defiend type)
# age - int

# can - dos(actions)

# jump -(height)
# sleep-(duration)
# run-(distance,angle)
# hunt(praey)
#play(toy)
#purr()
#meow()


class Cat:

    def __init__(self,color,name,isMale,meow)
        self.color = color
        self.name = name
        self.isMale = isMale
        self.meow = meow
        self.age = 0

    def sleep(self, durstion):
        print(self.name + "slept for" + str(duration))

    def getOlder(self):
        self.age += 1

    def makeMeow(self):
        print(self.name + "says : " + self.meow)

    def getAge(self):
        return self.name

    def setName(self,newName):
        self.name = newName


franklin = Cat("orange","Franklin",True,"Meoooooooow")
franklin.sleep(60)
franklin.makeMeow()


sally = Cat("Tortiesshell" )
