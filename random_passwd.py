import random

kucuk_harf = "abcdefghijklmnoprstuvyzxqw"
buyuk_harf = "ABCDEFGHIJKLMNOPRSTUVYZXQW"
rakam = "0123456789"
sembol = "[]{}()*/.-%&"
hepsı = kucuk_harf + buyuk_harf + rakam + sembol
sifre_uzunlugu = input("Şifrenizin Karakter Sayısını Giriniz : ")
sifre_uzunlugu = int(sifre_uzunlugu)
sifre = "".join(random.sample(hepsı, sifre_uzunlugu))
print("Şifreniz : ", sifre)

