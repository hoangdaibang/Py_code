'''

Dictionary : là một tập học các cặp khóa(key) và giá trị(value) có thể thây đổi được và lặp chỉ mục Dictionary được khởi tạo bằng 
cặp khóa {} vag cung có các khóa key-value mỗi cặp được xem như là một item,trong dictionary key mà được truyền giá trị cho là duy nhất.
còn giá trị(value) có thể là bất kì giá trị nào. 

Key phải là một giá trị không thể thay đổi (immutable) như chuỗi, số hoặc tuple

'''

#Create a new dictionary
#khởi tạo một Dictionary mới 
#có 2 cách để khởi tạo một Dictionary 
#chúng ta có thể dùng cú pháp name_dict = {key1 : value1, key2 : value2, key3 : value3 }
# Family_Member_1 = {"brother" : "Bang", "sister_1" : "Ly", "sister_2" : "Vy"}
#print(Family_Member_1) #>>{'brother': 'Bang', 'sister_1': 'Ly', 'sister_2': 'Vy'}
#Hoặc chúng ta có thể dùng hàm dict() với cú pháp name_dict = dict(key1 = value1, key2 = value2, key3 = value3)
# Family_Member_2 = dict(brother = "Bang", sister_1 = "Ly", sister_2 = "Vy")
# print(Family_Member_2) #>>{'brother': 'Bang', 'sister_1': 'Ly', 'sister_2': 'Vy'}
#yeah they are the same
#Access item
#truy Vấn các item trong Dictionary 
#để truy vấn một cặp key : value trong Dictionary ta có cú pháp 
# name_dict[key]
#Ví dụ
#print(Family_Member_1["brother"]) #>> Bang 
#trong ví dụ này kết quả trả về sẽ là "Bang" giá trị của key mà ta truy vấn 
#và nếu ta truy vấn một key không có trong Dictionary sẽ nhận được một thông báo lỗi KeyError: 'sister_3'
#print(Family_Member_1["sister_3"]) #>> KeyError: 'sister_3'
#Để kiểm tra một key có trong dictionary không ta có thêr dùng một trong hai cú pháp
#dùng cấu trúc if...in...else...
# if "brother" in Family_Member_1: 
#     print(Family_Member_1["brother"]) # >> Bang
# else:
#     print("key not found")
#kết quả ví dụ này trả về là đã tìm key "brother" trong Dictionary Family_Member_1 và in ra kết quả là >> Bang
# if "sister_3" in Family_Member_1: 
#     print(Family_Member_1["sister_3"])
# else:
#     print("key not found") # key not found 
#ở ví dụ này kết quả trả về là key not found do không thể tìm thấy key "sister_3" trong Dictionary Family_Member_1
#ngoài ra ta có thể sử dụng cú pháp 
# try:
# ...........
# except:
#............
# try: 
#     print(Family_Member_1["brother"]) #>> Bang
# except:
#     print("key not found")

# try:
#     print(Family_Member_1["sister_3"])
# except:
#     print("key not found") #>> key not found

#và ta sẽ nhận đươc kết quả tương tự 

#Add or change item (key:value) pairs
#Add item 
#ta có thể sử dung cú pháp 
#name_dict["key"] = value
#để thêm một item vào dictionary
#Ví dụ 
# Family_Member_1["dog"] = 'lu'
# Family_Member_1["cat"] = 'mun'
# print(Family_Member_1) #>> {'brother': 'Bang', 'sister_1': 'Ly', 'sister_2': 'Vy', 'dog': 'lu', 'cat': 'mun'}
# #Như ta thấy trong kết quả 2 cặp giá trị "dog" : lu và "cat" : 'mun' đã xuất hiện trong Dictionary 
# #và để thay thế một cặp giá trị ta cũng sử dụng cấu trúc tương tự: name_dict[key] = value  
# Family_Member_1["dog"] = "vang"
# print(Family_Member_1) #{'brother': 'Bang', 'sister_1': 'Ly', 'sister_2': 'Vy', 'dog': 'vang', 'cat': 'mun'}
#và kết quả cạp giá trị 'dog': 'vang' đả được thêm vào thay thế cho cặp  'dog': 'lu'
#bên cạnh việt thêm một item vào dictionary thì ta cũng có thể xóa item khỏi dictionary bằng cú pháp del name_dict[key]
# del Family_Member_1["cat"]
# print(Family_Member_1) #>> {'brother': 'Bang', 'sister_1': 'Ly', 'sister_2': 'Vy', 'dog': 'lu'}
# #như ta đã thấy kết quả hiện ra với cặp key : value 'cat': 'mun' đã biến mất 
# #bây giờ ta thêm vô lại 
# Family_Member_1["cat"] = 'mun'
# print(Family_Member_1) #>> {'brother': 'Bang', 'sister_1': 'Ly', 'sister_2': 'Vy', 'dog': 'lu', 'cat': 'mun'}
# #rồi sử dụng hàm khác để xóa hàm pop() có cú pháp name_dict.pop(key) 
# #ví dụ 
# print(Family_Member_1.pop("cat")) #>>mun 
# print(Family_Member_1) #>> {'brother': 'Bang', 'sister_1': 'Ly', 'sister_2': 'Vy', 'dog': 'lu'}
# #điều khác biệt là hàm pop() sẽ trả về kết quả là giá trị mà nó đã xóa như >>mun ở ví dụ trên á thấy hông 
#ngoài ra ta còn có hàm popitem() với cú pháp name_list.popitem() hàm popitem() sẽ xóa item cuối cùng trong Dictionary 
#ví dụ 
# ta lại thêm 'cat': 'mun' vào lại 
# Family_Member_1["cat"] = 'mun'
# print(Family_Member_1) #>> {'brother': 'Bang', 'sister_1': 'Ly', 'sister_2': 'Vy', 'dog': 'lu', 'cat': 'mun'}
# #và khi ta thêm phân tử mới vào thì nó sẽ nằm cuối Dictionary 
# print(Family_Member_1.popitem()) #>>('cat', 'mun')
# print(Family_Member_1) #>> {'brother': 'Bang', 'sister_1': 'Ly', 'sister_2': 'Vy', 'dog': 'lu'}
# #và thế là ('cat', 'mun') lại biến mất again
#loop over key:
# for key in Family_Member_1.keys():
#     print(key, Family_Member_1[key]) #brother Bang
#                                      #sister_1 Ly
#                                      #sister_2 Vy
#                                      #dog lu
#                                      #cat mun
# #loop over value:
# for value in Family_Member_1.values():
#     print(value) #Bang
#                  #Ly
#                  #Vy
#                  #lu
#                  #mun
# #loap over item:
# for key, value in Family_Member_1.items():
#     print(key, value) #brother Bang
#                       #sister_1 Ly
#                       #sister_2 Vy
#                       #dog lu
#                      #cat mun






