"""Schreiben Sie ein Programm, das die Zahlen von 1 bis 100 ausgibt. 
Bei jeder Zahl, die durch 5 teilbar ist, soll "fizz" ausgegeben werden und 
bei jeder Zahl, die durch 7 teilbar ist, soll "buzz" ausgegeben werden. 
Wenn die Zahl sowohl durch 7 als auch durch 5 teilbar ist, soll "fizzbuzz" ausgegeben werden. """

zahl = 1
while(zahl <=200):
    if zahl % 5 == 0 and zahl % 7 == 0:
        print("fizzbuzz")
        zahl = zahl + 1
    elif zahl % 5 == 0:
        print("fizz")
        zahl = zahl + 1
    elif zahl % 7 == 0:
        print("buzz")
        zahl = zahl + 1
    else:
        print(zahl)
        zahl = zahl + 1