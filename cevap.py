markalar=["Toyoto","BMW","Renault","Mercedes"]

elemanSayısı=len(markalar)
print(elemanSayısı)

print(markalar[0]+" "+markalar[3])


markalar[2]="Togg"
print(markalar)

sonuc= "togg" in markalar
print(sonuc)

markalar.append("Ford")
markalar.append("Citroen")
print(markalar)


markalar.pop()
print(markalar)




