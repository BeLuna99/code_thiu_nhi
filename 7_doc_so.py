#nhap so n toi da 2 chu so, Doc ra dang chu
#SO = {0:"Khong", 1:"Mot", 2:"Hai",3:"Ba",4:"Bon",5:"Nam",6:"Sau",7:"Bay",8:"Tam",9:"Chin"}



so = ["không", "một", "hai","ba","bốn","năm","sáu","bảy","tám","chín"]
n = int(input("nhap so: "))
hangdonvi = n % 10
hang_chuc = n // 10
print("số có hàng chục là: ", hang_chuc)
print("số có hàng đơn vị là: ", hangdonvi)
if n >=0 and n<10:
    doc_so_n = so[n]
    print(doc_so_n)
elif n == 10:
    print("mười")
elif n > 10 and n < 20:
    if hang_chuc == 1 and hangdonvi == 5:
        print("mười lăm")
    elif  hang_chuc == 1 and hangdonvi !=0:
        print("mười", so[hangdonvi])
elif n == 20:
    print("hai mươi")
elif n > 20 and n < 30:
    if hang_chuc == 2 and hangdonvi == 5:
        print("hai muơi lăm")
    elif hang_chuc == 2 and hangdonvi !=0:
        print(so[hang_chuc],"muơi",so[hangdonvi])
