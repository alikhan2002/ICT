temp = float(input())
speed = float(input())
if(temp > 10 or speed < 4.8):
    print("WCI not valid with this parametres")
else:
    WCI = 13.12 + 0.6215 * temp - 11.37 * speed **0.16 + 0.3965 * temp * speed** 0.16
    WCI = round(WCI)
    print("WCI is", WCI)
