import requests
from bs4 import BeautifulSoup
import sys

url = "https://www.doviz.com/"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content,"html.parser")

dövizler = soup.find_all("span",{"class","name"})
values =  soup.find_all("span",{"class","value"})

print("""**********DÖVİZ UYGULAMIZA HOŞGELDİNİZ*********
Lütfen İşlem Yapacağınız Döviz Cinsinizi Parantez İçinde Belirtilen Tuşa Basarak Giriniz
GRAM ALTIN (1)
DOLAR (2)
EURO (3)
STERLİN (4)
ÇIKIŞ (Q/q)
""")

while(True):
    işlem = input("İşlem>>")
    if (işlem == "q"):
        print("Çıkış yapılıyor....")
        break
    miktar = float(input("Lütfen mikarı giriniz:"))
    if(işlem=="1"):
        döviz_values = zip(dövizler, values)
        for k,v in döviz_values:
            k = k.text
            v = v.text
            v = v.replace(",", ".")
            if(k =="GRAM ALTIN"):
                print("{} GRAM ALTIN {}TL'dir.".format(miktar,float(v)*miktar))
                break
    elif(işlem=="2"):
        döviz_values = zip(dövizler, values)
        for k,v in döviz_values:
            k = k.text
            v = v.text
            v = v.replace(",", ".")
            if(k=="DOLAR"):
                print("{} DOLAR {}TL'dir.".format(miktar,float(v)*miktar))
                break

    elif (işlem == "3"):
        döviz_values = zip(dövizler, values)
        for k, v in döviz_values:
            k = k.text
            v = v.text
            v = v.replace(",", ".")
            if (k == "EURO"):
                print("{} EURO {}TL'dir.".format(miktar, float(v) * miktar))
                break
    elif (işlem == "4"):
        döviz_values = zip(dövizler, values)
        for k, v in döviz_values:
            k = k.text
            v = v.text
            v = v.replace(",",".")
            if (k == "STERLİN"):
                print("{} STERLİN {}TL'dir.".format(miktar, float(v) * miktar))
                break

    else:
        sys.stderr.write("Geçerli Bir İşlem Girilmeli")
        sys.stderr.flush()



