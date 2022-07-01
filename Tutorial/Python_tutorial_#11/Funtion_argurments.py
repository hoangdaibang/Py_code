

'''

Required Parameter & Default Parameter
Tham số bắt buột và tham số mặt định

'''
# def print_name(name, greeting = "Wellcome"):
#      print(f'{name} , {greeting}') #>> Bang , Wellcome
#trong chương trình ở trên name gọi là tham số bắt buột để sử dụng hàm bắt buột ta phải truyền vào nó các tham số tham số bắt buột 
#chương trình sẽ báo lỗi nếu trong cú pháp gọi hàm của ta không bao gồm những tham số này 
#để có thể chạy gọi hàm ở trên hàm main sẽ được viết lại như sau 
# def main():
#     print_name("Bang")
#trong trường hợp này "Bang" chính là tham số mà ta truyền vào hàm print_name "Bang" là giá trị của tham số bắt buột được truyền vào hàm 
#bên cạnh đó như ta thấy ở trên tham số greeting cũng được khởi tạo tuy nhiên ta không cần truyền một giá trị tham số nào mà hàm vẫn không báo lỗi 
# vì trong trường hợp này tham ssos greeting dã nhận giá trị default(giá trị mặc định) là Wellcome 
#và nếu truyền và nó một tham số khác thì kết quả trả về sẽ hiển thị tham số ta truyền vào tham số mặc đinh đã bị ghi đè 
# def print_name(name, greeting = "Wellcome"):
#     print(f'{name} , {greeting}') #>> Bang , Xin chào 

# def main():
#     print_name("Bang", "Xin chào")


# def Test_Aguments(a, b, c):
#     print(a, b, c) #>> 1 2 3

# def main():
#     #Positional Aguments
#     Test_Aguments(1, 2, 3)
#Tham số theo vị trí là cách truyền tham số mà các tham số được truyền theo thứ tự vị trí tương ứng như vị trí tham số nhận trong hàm def Test_Aguments(a, b, c): cũng như tham số khi truyền vào Test_Aguments(1, 2, 3)


# def Test_Aguments(a, b, c):
#     print(a, b, c) #>>14 43 22

# #     #Keyword arguments
# def main():
#     Test_Aguments(a= 14, c= 22, b= 43)
#Tham số được Truyền theo keyword sẽ được truyền bằng cách gán các giá trị Truyền vào tương ứng với các giá trị mà hàm nhận

#Variable-length parameters (*args and **kwargs)
#Tham số có chiều dài thây đổi 
#If you mark a parameter with one asterrisk (*),
#you can pass any number of positional arguments to your function (Typically called *argrs)
#tham số *args thuôc kiểu tuple nên tham số truyên vào *args cũng có dạng là những phần tử trong tuple
#ta không cần phải thêm dấu sao(*) vào trước tham số khi truy cập trong hàm 
# def varibleLengthArgExample(a,b, *args):
#     print(a, b)
#     for arg in args:
#         print(arg)
 
# def main():
#     varibleLengthArgExample(3, 5, "Hoang", "Dai", "Bang")
#If you mark a parameter with two asterrisks (**),
#you can pass any number of keyword arguments to this function (Typically called *argrs)
# tương tự tham số **kwagrs thuộc kiểu Dict nên các tham số truyền vào cũng có dạ là các phần tử trong Dict 
#và ta cũng không cần thêm hai dấu sao vào trước tham số name_kwargs khi truy cạp nó trong hàm 
# def varibleLengthArgExample(a,b, *args, **kwargs):
#     print(a, b) # >> 3 5
#     for arg in args:
#         print(arg) # >> Hoang
#                    # >> Dai
#                    # >> Bang
#     for key, value in kwargs.items():
#         print(f"{key} : {value}") # >>foot_size : 42
#                                   # >>age : 24

# def main():
#     varibleLengthArgExample(3, 5, "Hoang", "Dai", "Bang", foot_size = 42, age = 24)

#không cố định là *args và **kwargs hai tham số này có thể được dặt vói tên bất kì vói cú pháp *name_parameter và **name_parameter
def varibleLengthArgExample_1(a, b, *c, **d):
    print(a, b) 
    for arg in c:
        print(arg) 
    for key, value in d.items():
        print(f"{key} : {value}")


 
def main():
    varibleLengthArgExample_1(3, 5, "Hoang", "Dai", "Bang", foot_size = 42, age = 24)






if __name__ == "__main__":
    main()
