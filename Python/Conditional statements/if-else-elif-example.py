"""username = 'sadikturan'
password = '1234'

if (username == 'sadikturan'):

    if (password == '12345'):
        print('Hoş geldiniz')
    else:
        print('parola yanlış')
        
else:
    print('username yanlış')



x = 10
y = 20

if x > y:
    print("x y den büyük")

elif  x==y :
    print("x y eşit")

else :
    print("y x den büyüktür")



isim = input("İsminizi Giriniz: ")
yas = int(input("Yaşınızı giriniz: "))
egitim = input("Eğitim bilgini gir: ")


if (yas>=18) :
    if (egitim == ("lise") or ("üni")):
        print(f"{isim}Ehliyet Alabilirsiniz")
    else:
        print(f"{isim}Eğitim durumunuz tutmuyor")
else: 
    print (f"{isim}Eğliyet alamazsınız yaşınız tutmuyor")



sayı = float(input("Sayı Giriniz: "))


if (sayı<100) and (sayı>0) : 
    print (f"Girdiğiniz sayı {sayı} 0 ile 100 arasında bir sayıdır.")

else :
    print("giridiğiniz sayı {sayı} 0 ile 100 arasında bir sayı değildir.")





email= ("baris@öz")
password = ("1234")


inemail= input("e mail giriniz: ")
inpassword = input("parola giriniz: ")

if (inemail) == (email):
    print("E MAİL DOĞRU")
    if inpassword == password:
        print("Parola doğru")
        print("Giriş Başarılı")
    else:
        print("Parola yanlış")        
else:
    print("Email Yanlış")
"""