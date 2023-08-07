#tipe data variabel pada angka
#tipe data interger
data_interger = 1
print("data: ", data_interger)
print("bertipe: ",type(data_interger))
#tipe data float
data_float=10.5
print("data : ",data_float)
print("bertipe: ",type(data_float))
#tipe data karakter(string)
data_string = "m zadid ilmi"
print("data : ",data_string)
print("bertipe: ",type(data_string))
#tipe data biner true / false
data_bool=True
print("data : ",data_bool)
print("bertipe: ",type(data_bool))
##tipe data khusus bilangan kompleks
#tipe data float
data_complex=complex(3,10)
print("data : ",data_complex)
print("bertipe: ",type(data_complex))
#tipe data data bahasa c
from ctypes import c_double

data_c_double=c_double(33.3)
print("data : ",data_c_double)
print("bertipe: ",type(data_c_double))