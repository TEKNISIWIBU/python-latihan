#operasi aritmatika

a = 10
b = 5
#penjumlahan
hasil = a+b
print(a,'+',b,'=',hasil)
#pengurangan
hasil = a-b
print(a,'-',b,'=',hasil)
#perkalian
hasil = a*b
print(a,'x',b,'=',hasil)
#pembagian
hasil = a/b
print(a,'/',b,'=',hasil)
#ekponen(pangkat)
hasil = a**b
print(a,'**',b,'=',hasil)
#modulus
hasil = a%b
print(a,'%',b,'=',hasil)
#flow division
hasil = a//b
print(a,'//',b,'=',hasil)

#proritas operasi
x = 3
y = 2
z = 4
hasil = x**y*z+y/x//z%z+y+y-z
print("hasil = ",hasil)