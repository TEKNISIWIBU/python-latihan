#latihan konfersi suhu
print("\nPROGRAM CONVERT SUHU\n")

celcius = float(input('masukkan data suhu celcius'))
print("suhu adalah",celcius,"C")
#REAMUR
reamur = (4/5)*celcius
print("suhu adalah",reamur,"R")
#FARENHAIT
farenhait = ((9/5)*celcius)+32
print("suhu adalah",farenhait,"F")
#KELVIN
kelvin = celcius+273
print("suhu adalah",kelvin,"K")
print("=========farent & kelvin to celcius==========")
#farenhait to celcius
faren = (5/9*(farenhait - 32))
print("farenhait ke celcius",faren,"C")
#kelvin to celcius
kel = kelvin - 273
print("kelvin ke celcius",kel,"C")
print("=========farent & kelvin to reamur==========")
#farenhait to celcius
faren = 4/9*(farenhait - 32)
print("farenhait ke celcius",faren,"C")
#kelvin to celcius
kel = 4/5*(kelvin - 273)
print("kelvin ke celcius",kel,"C")
