class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber


    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        k = sum(self.scores) /len(self.scores)
        if k<= 100 and k>=90 :
            return 'O'
        elif k <90 and k>= 80:
            return 'E'
        elif k <80 and k>= 70:
            return 'A'
        elif k <70 and k>= 55:
            return 'P'
        elif k <55 and k>= 40:
            return 'D'
        elif k <40:
            return 'T'





line = input().split()
firstName = line[0]
lastName =line [1]
idNum = line [2]
numScores = int(input())
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())