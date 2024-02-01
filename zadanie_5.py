car = 'Lexus'
color = 'Belaya'
wanted_cars = ("Toyota", "Lexus")
year = 2004
probeg = 150000
wanted_color = ("Belaya", "Seraya")
wheel = "Leviy"
master = 2
cost = 10000

if car in wanted_cars and 2004 <= year <= 2024 and probeg <= 150000 and color in wanted_color and wheel == 'Leviy' and master <= 2 and cost <= 10000:
    print('Deal')
elif car in wanted_cars and 2004 <= year <= 2024 and probeg <= 200000 and color in wanted_color and wheel == 'Leviy' and master <= 2 and cost <= 8000:
    print("Deal")
else:
    print("Net")
