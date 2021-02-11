import math

def escapevelocity(r,m):
    g=(6.67430 * (10 ** (-11)))
    Ve=(((2.0 * g * float(m)) / r) ** (1 / 2))
    return Ve

def volume(r):
    V=(float((4/3)*math.pi*(r**3)))
    return V

r=input('Enter radius of planet in meters:\n')
r=int(r)
m=input('Enter mass of planet in kg:\n')
m=int(m)

print('The escape velocity of the planet is:',(escapevelocity(r, m)), 'm/s')
print('The volume of the planet is:', (volume(r)),('m^3'))


