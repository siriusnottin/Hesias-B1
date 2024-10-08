
import math

a = int(input('valeur a : '));
b = int(input('valeur b : '));
c = int(input('valeur c : '));

delta = b*b - 4*a*c

if delta < :
    print('Pas de solution')
elif delta == 0:
    print(-b/(2*a))
else:
    print((-b + math.sqrt(delta)) / (2*a))
    print((-b - math.sqrt(delta)) / (2*a))
