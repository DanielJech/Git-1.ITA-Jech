print("Kalkulacka: + - * / sin cosinus tangus")
operace = input()
if operace == "+":
    print("zadej první číslo")
    a = float(input())
    print("zadej druhý číslo")
    b = float(input())
    plus = a + b
else:
    if operace == "-":
        print("zadej první číslo")
        a = float(input())
        print("zadej druhý číslo")
        b = float(input())
        minus = a - b
    else:
        if operace == "*":
            print("zadej první číslo")
            a = float(input())
            print("zadej druhý číslo")
            b = float(input())
            krat = a * b
        else:
            if operace == "/":
                print("zadej první číslo")
                a = float(input())
                print("zadej druhý číslo")
                b = float(input())
                deleno = a / b
            else:
                if operace == "sin":
                    print("zadej první číslo")
                    a = float(input())
                    sinus = sin(a)
                else:
                    if operace == "cosinus":
                        print("zadej první číslo")
                        a = float(input())
                        cosinus = cos(a)
                    else:
                        if operace == "tangus":
                            print("zadej první číslo")
                            a = float(input())
                            tangus = tan(a)
                        else:
