class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        k=1
        divisor=[]
        for i in range(n):
            if (n%k)==0:
                divisor.append(n//k)
            else:
                pass
            k=k+1
        return sum(divisor)




n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)