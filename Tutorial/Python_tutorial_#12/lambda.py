'''

Hàm Ân Danh  - Lambda trong Python
lambda arguments: expression

'''
# A lambda funtion is a small (one line) anonymous funtion
#là một hàm nhỏ chỉ cần định nghĩa bằng một dòng 
#that is defined without a name 
#và không đinh nghĩa bằng một tên 

#ví dụ một hàm Lambda cộng 100 với một số nhặp vào từ bàn phím 



# sum=  lambda a : a + 100
# print(sum(10))
# #hàm lambda này  tương tự với hàm sau nhưng hàm lambda chỉ cần viết trên 1 dòng
# def test_lambda_funtion(a):
#     return(a + 100)
# print(test_lambda_funtion(10))
# #tương tự ta cung có thêr định nghĩa hàm lambda với nhiều giá trị hơn ví dụ 
# sum_1= lambda x, y, z : x + y - z
# print(sum_1(3, 4, 5))
#ta có thể viết lại cú pháp của hàm lambda như sau 
#funtion_name = lambda variables : definition function
#tên hàm = lambda các biến : hàm định nghĩa 
'''

thay đổi điều kiện sắp xếp hàm sorting sử dụng sử dung tham số key = lambda
custom sorrting using a lamda funtion as key parameter


'''
#ví dụ 
from ast import Lambda
from distutils.ccompiler import new_compiler
from functools import reduce


sample_dict = {(1, 12, 8),(3, 9, 7),(8, 8, 11)}
print(sorted(sample_dict,key= lambda el : el[0]))
#hoặc là sắp xếp theo giá trị tuyệt đối của tùng phần tử trong list
sample_list = [6, -5, 8, 6, -4, -7, 1, -6]
print(sorted(sample_list,key= lambda x : abs(x)))
'''

sử dụng lamda trong hàm map
hàm map giúp chuyển đổi từng phần tử của một List bằng một hàm nào đó
cú pháp :
map(func,seq)
map(Hàm, Chuỗi)
transforms each element with function.

'''
# list_keyword = ["Bang", "xin chao", "cac ban"]
# print(list(map(lambda x : x.title(), list_keyword)))
# #Hàm hàm map (lambda func, seq ) trong trường hợp này cũng có tác dung tương tự như List Comprehension có cấu trúc như sau
# new_list = [x.title() for x in list_keyword]
# print(new_list)
#đó kết quả cho ra không khác gì trơn 

'''

dùng lambda trong hàm filter
use lambda for filter funtion 
hàm filter trả về kết quả là tất cả phần tử có giá trị mà khi xét bàng hàm đã cho trả về kết quả là true 
hàm filter cũng có cú pháp filter(func, seq)
filter funtion return all elements for which funtion return True 

'''
#ví dụ
list_number = [1, 3 , 7 , 9,  11, 12, 4 , 7, 8, 2]
print(list(filter(lambda x : x % 2 == 0, list_number)))

#và trong trường hợp này hàm filter cũng được có tác dung như một list comprehension khác 

new_list_number = [x for x in list_number if x % 2 == 0]
print(new_list_number)
#và tức nhiên kết quả trả về cung chả khác gì nhau cả 
'''
dùng lambda trong hàm reduce
Hàm reduce áp dụng hàm cho từng phần tử trong chuỗi cho đến hết chuỗi và trả về kết quả là một giá trị duy nhất là kết quả của hàm(func)

'''
#ví dụ 
sequence = [1, 4, 7 , 3, 5, 13]
#tính tổng các phần tử trong chuỗi 
print(reduce(lambda a , b : a + b, sequence))
#tìm giá trị lớn nhất 
print(reduce(lambda a, b : a if a > b else b, sequence))

