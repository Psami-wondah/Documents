class Person:


    def cage(self, age):
        #creates an instance variable age
        self.age=age

    def __init__(self, initialAge):
        #creates a constructor with variable initial age as parameter
        if initialAge>0:
            self.age=initialAge

        else:
            self.age=0
            print('Age is not valid, setting age to 0')



    def amI0ld(self):
        #creates an instance method amI0ld
        if self.age< 13:
            print('You are young')

        elif self.age >= 13 and self.age<18:
            print('You are a teenager')

        else:
            print('You are old')



    def yearPasses(self):
        #creates an instance method yearPasses
        self.age = self.age + 1


t = int(input())
for i in range(0, t):
    #makes code below run t times
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
#a function created within a class is called a method

