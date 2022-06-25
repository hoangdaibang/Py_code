

def reversed_func(lar, n):
    for i in range(n // 2):
       temp = lar[i]
       lar[i] = lar[-(i + 1)]
       lar[-(i + 1)]= temp
    return(lar)


def main():
    while True:
        l = []
        n = input("nhập vào số phần tử của list :")
        if n: 
            n = int(n)
            for i in range(n):
                e = input(f"Nhập vào phần tử thứ {i + 1} của list: ")
                l.append(e)
            lar = reversed_func(l, n)
            print(l)
            print(lar)
            break
        else:
            continue


if __name__ == "__main__" :
    main()