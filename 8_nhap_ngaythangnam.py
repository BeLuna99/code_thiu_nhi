#nhap ngay thang nam xuat ra ngay tiep theo

ngay = int(input("nhap ngay: "))
thang = int(input("nhap thang: "))
nam = int(input("nam: "))
thang_31_ngay = (1,3,5,7,8,10,12)
thang_30_ngay = (4,6,9,11)

if thang >= 1 and thang <= 12:
    if ngay >= 1 and ngay <= 29 and thang != 2:
        ngay += 1
        print(ngay,thang,nam,sep="-")
    elif ngay == 30 and thang in thang_30_ngay:
        thang += 1
        print(1,thang,nam,sep="-")
    elif ngay == 31 and thang in thang_31_ngay and thang != 12:
        thang += 1
        print(1,thang,nam,sep="-")
    elif ngay == 31 and thang == 12:
        nam += 1
        print(1,1,nam, sep="-")
    elif ngay == 28 and thang == 2 and nam % 400 == 0:
        ngay =+ 1
        print(ngay,thang,nam,sep="-")
    elif ngay == 29 and thang == 2 and nam % 400 == 0:
        thang += 1
        print(1,thang,nam,sep="-")
    elif ngay == 28 and thang == 2 and nam % 400 != 0:
        thang += 1
        print(1,thang,nam,sep="-")
