meyveler = {"orange", "apple", "banana"}

#print (meyveler[0]) bu şekilde indexlenemez sets dizileri

for x in meyveler:
    print(x)


meyveler.add("chery")   #tekli ekleme
meyveler.update(["mango","grep"])  #çoklu ekleme
meyveler.remove("mango")
meyveler.discard("apple")
meyveler.pop()  #pop hernagi bir elemanı siler setlerde 
meyveler.clear()#bütün elemanları temileme silme işlemi


print(meyveler)
