'''

List Comprehensions

List Comprehension giúp bạn viết code ngắn gọn (đặc biệt khi dang ở trong một vòng lặp đã có)
và dễ đọc , nhìn code hơn 

'''

#new_list[<action> for <item> in <iterator> if <some condition>]
#Ta có cấu trúc cơ bản để in ra các phần tử trong một chuỗi kí tự 
#vd ta có :
# word = "Hello Wolrd"
# for char in word:
#     print(char) #cấu trúc này giúp chung ta in ra một phần tử trong chuỗi kí tự 
#Đây là cấu trúc cơ bản dể in ra các phần tử trong một chuỗi kí tự 
#ngoài ra việc sử dụng List Comprehension giúp chung ta thu gọn cấu trúc này thành một câu lệnh duy nhất 
#print([char for char in word]) #Tương tự như ví dụ trên tuy nhiên cấu trúc này giả quyết vấn đề chỉ tron một dòng code 
#Ngoài ra ta có thể điều kiện cho chuỗi 
#Tương tự ví dụ ở trên ta có mô chuỗi số 
# enven_number = [item for item in range(0, 10)]
# print(enven_number) # >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
#Khi thêm điều kiện chia hết cho 2 ta có được 
# enven_number = [item for item in range(0, 10) if item % 2 == 0]
# print(enven_number) #>> [0, 2, 4, 6, 8]
# #Một chuỗi mới chỉ bao gồm các phần tử có giá trị chia hết cho 2
# Một ví dụ thực tế sử dung List comprehension
#Trong một cửa hàng bán bút cao cấp của The Meisterstück mỗi chiết bú có giá( đơn vị triệu đồng )như sau :
#List_pen = [148, 148, 130, 49]

#trên mỗi chiết bút bán ra % lợi nhuận thu được là:
#profit = 0.3

#và số tiền thuế phải chịu là:
#tax = 0.1 

#Tạo một hàm để tính lợi nhuận ròng của mỗi chiếu bút:
# def Cal_Real_Profit(pen): 
#     return( pen*(profit - tax))

#sử dụng hàm đó Và cấu trúc List Comprehension để tính ra lợi nhuận của toàn bộ bút trong cửa hàng: 
# real_profit = [Cal_Real_Profit(pen) for pen in List_pen]
# print(real_profit)
#Tada~
#Vậy là ta có được kết quả là lợi nhuận ròng của từng chiết bút 
#Chúc bạn mau giàu !!!!!!!!!!

'''

Các hàm nâng cao sử dụng List
Avanced Funtions  

'''
'''

Hàm list()
Hàm list() dùng để chuyển đổi một chuỗi String thành một List 

'''
# print(list(123456)) #print(list(123456))
#                     #TypeError: 'int' object is not iterable
#                     #đó int không được mô nghen 
#print(list("123456")) # >> ['1', '2', '3', '4', '5', '6'] 
                      #String cơ 

'''

Hàm sum() thì để cộng giá trị các phần tử trong list lại với nhau 
Cái ni hắn khác Str.join(List or name list) một chỗ là Sum() hắn cộng số(int, cộng giá trị của số)
Còn Str.join(List or name list) Hắn nối chuỗi được ngăn cách bằng Str


'''

# a = sum(['1', '2', '3', '4', '5']) 



# b = sum([1, 2, 3, 4, 5, 6]) 

# c = ' '.join(['1', '2', '3', '4', '5']) 

# print(a) #a = sum(['1', '2', '3', '4', '5'])
#          #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(b) #>> 21
# print(c) #>> 1 2 3 4 5

'''

Hàm zip()
looping through two list simoltanusly 
giúp ta có thể truy cập các phần tử(element) từ cả nhiều List  

'''

# family_members = ['Ba', 'Me', 'Bang', 'Ly', 'Vy']
# year_old = [47, 47, 24, 18, 9]
# candies = [6, 5, 3 , 10, 12]

# for member, y_o,  candy in zip(family_members, year_old, candies):
#     print(f"{member} {y_o} tuổi, có số kẹo là:{candy} ")

# #Khi sử dụng hàm zip() kết quả trả về sẽ là một list với mỗi phần tử sẽ là nhóm các phần tử trong mỗi list
# #ví dụ : hàm zip() ở trên sẽ tạo thành một list() mới như sau 
# # a=  [
# #         ['Ba', 47, 6],
# #         ['Me', 47, 5],
# #         ['Bang', 24, 3],
# #         ['Ly', 18, 10],
# #         ['Vy', 9, 12]

# #     ]
# #Nên ta có thể dùng hàm enumurate() để lấy index từng phần tử như sau 
# for index, (member, y_o, candy) in enumerate(zip(family_members, year_old, candies)):
#     print(f"{index + 1}. {member} {y_o} tuổi, có số kẹo là:{candy} ")

'''

Advanced funtion

'''
#Hàm sorted() như đã biết hàm sorted() dung để sắp xếp các phần tử theo thứ tự tăng dần nên sắp xếp kiểu mặc định sẽ sắp xếp theo kí tự dầu tiên 
# ví dụ :


# child_name = ['Vy', 'Bang', 'Ly']
# print(sorted(child_name)) #>> ['Bang', 'Ly', 'Vy']
# #nhưng nếu chúng ta muôn sắp xếp kiểu more advanced hơn thì sao sắp xêos theo kí tự thứ hai chẳng hạn
# #nào xem đây: 
# print(sorted(child_name,key=lambda el: el[1]))
# #đó thấy chưa kết qua bây giờ là : ['Bang', 'Vy', 'Ly'] sắp xếp theo kí tự thứ hai rồi đó 
# #rồi cái ni nữa nếu mà sắp xếp cái Dictionary thì răng coi nì :
# #Ví dụ 
# List_Dict_Friend = [{'name' : 'Bang', 'age' : 24, 'sex' : 'male'}, {'name' : 'Chau', 'age' : 18, 'sex' : 'female'}, {'name' : 'Hung', 'age' : 24, 'sex' : 'male'}, {'name' : 'Ngan', 'age' : 25, 'sex' : 'female'}]
# print(sorted(List_Dict_Friend,key=lambda el: el['age']))
#đó thấy chưa hắn sẽ sắp xếp theo từng thuộc tính 
#trong ví dụ này có kết qua sẽ là : [{'name': 'Chau', 'age': 18, 'sex': 'female'}, {'name': 'Bang', 'age': 24, 'sex': 'male'}, {'name': 'Hung', 'age': 24, 'sex': 'male'}, {'name': 'Ngan', 'age': 25, 'sex': 'female'}]
'''

2D array,List
matrix 
mảng hai chiều 

'''
#ta có ví dụ 
# matrix= [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9],
#          [10, 11, 12]]
#để truy suất một phần tử 2D List ta làm ta có cú pháp name_matrix[row][col]
#ví dụ 
# print(matrix[1][1])
#here we go ta có kết quả in ra màng hình là : >> 5 
#phần tử ở dòng 2, cột 2 trong ma trận(dòng 1 cột 1 trong Python)
# for row in range(4):
#     for col in range(3):
#         print(matrix[row][col])
#để duyệt qua từng phần tử của 2D List ta có thê dùng hai vong for lồng nhau 
#hoặc áp dung list comprehension ta có thể rút gọn như sau :
# Convert_matrix = [matrix[row][col] for row in range(4) for col in range(3)]
# print(Convert_matrix)
'''

Chuyển đổi hàng thành cột trong ma trận(2D List) sử dụng cú pháp zip(*name_matrix)

'''
# print([element for element in zip(*matrix)])
     




















