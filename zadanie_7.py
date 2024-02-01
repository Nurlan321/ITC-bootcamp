rayon = 'chon aryk'
moteryals = 'kirpich'
wonted_rayon = ("chon aryk", "baytyk", "ortosay")
uchastok = 4
wonted_materials = ("kirpich", "peskoblok")
sost = 'good'
pryse = 50000

if rayon in wonted_rayon and moteryals in wonted_materials and uchastok <= 4 and  pryse <= 50000:
    print("good")
elif rayon in wonted_rayon and moteryals in wonted_materials and uchastok <= 5 and  pryse <= 45000:
    print("good")
else:
    ("not")
