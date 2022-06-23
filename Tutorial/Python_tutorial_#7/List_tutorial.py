'''List một kiểu giá trị trong Python tương tụ như Array '''

'''Create a list ( Khởi tạo một list )'''




# list_1 = ["banana","apple","orange","cherry"] #Khởi tạo một string list
# list_2 = [5, "Bang", True] #List có thể chứa nhiều kiểu dữ liệu khác nhau 
# list_3 = list() #Khởi tạo một  một list trống(empty list) bằng cú pháp name_list = list() 
# list_4 = [] #Hoặc Khởi tạo một  một list trống(empty list) bằng cú pháp name_list = []


# print(list_1)
# print(list_2)
# print(list_3)
# print(list_4)




'''Access emlements ( Truy cập các giá trị trong List)'''

# my_list = [1, 2, '3', True] # khởi tạo một list( my_list)

#print(len(my_list)) #Cú Pháp len(name_list) cho ta giá là độ dài của một list hay sôs phần tử có trong list
#print(my_list[2]) # Cú pháp name_list[index in list](tên list[số thứ tự]) trả về cho ta kết quả là phần tử tại vị trí đó ([số thứ tự]) trong list 
                  # trong ví dụ này là kí tự '3' ở vị trí thứ 2 trong list 
#print(my_list.index(2)) #Cú pháp name_list.index(emlement) trả về giá trị là vị trí của emlement(phần tử) trong list 
                        #trong ví dụ này hàm trả về vị trí của phần tử 2 có vị tí 1 trong list 
#from itertools import count


#my_list = [1, 2, 3, 3, 3, '3',  '3', True] # khởi tạo một list( my_list)

#print(my_list.count(3)) #Cú Pháp name_list.count(element) trả về giá trị là số element(phần tử) có giá trị giống nhau lặp lại trong list 
                        #Trong ví dụ này là 3 là số lần lặp lại của số 3 trong list (phần tử có giá trị 3 kiểu interger có số lần lặp lại là 3)
#print(my_list.count('3')) #Trong ví dụ này là 2 là số lần lặp lại của kí tự '3' trong list (phần tử '3' kiểu char có số lần lặp lại là 2)     
#for item in my_list : #ta cũng có thể dùng hàm for để truy cập đếm từ giá trị trong list 
#    print(item)       # trong ví dụ này hàm sẽ in ra giá trị của tần phần tử trong list 
                    #   #Kết quả :    1
                    #                 2
                    #                 3
                    #                 3
                    #                 3
                    #                 3
                    #                 3
                    #                 True
'''

Hàm Enumerate
Hàm Enumerate trả về gái trị của phần tử và cả vị trí của phần tử trong list 
Allows us to loop over a list and retieve
Both the index and the value of each item in the list

'''
#presidents = ["Washington", "Adams", "Jefferson",
#             "Madison", "Monroe", "Adams", "Jackson"]


# print(presidents)
# for index, president in enumerate(presidents):
#     print(f"President number {index} : {president}")


#or 


# for index, president in enumerate(presidents, start = 1): # Ta có thể công thiết lập giá trị của enumerate bắt đầu từ 1 để có kết quả hiểm thị thân thiện với người dùng hơn 
#     print(f"President number {index} : {president}")
'''

Slicing(Cắt list)
dấu : được goi là slicing 
cú pháp cắt chuổi là [start : end : step]
Slicing have format [start : end : step]

'''

# my_list = [1, 2 , '3',
#  True]

#print(my_list[:1:]) #Hàm trả về giá [1] là giá trị của phần tử đầu tiên 
                     #Trong ví dụ này cú phát slicing my_list với start để trong có nghỉa là khi cắt List ta sẽ lấy từ vị trí đầu tiên đến vị trí 1 của List(bỏ qua giá trị ở vị trí đó)
# print(my_list[-1]) #Cú Pháp này trả về giá trị của phần tử cuối cung trong List 
# print(my_list[::]) #Cú pháp Slicing tuy nhiên không chọn start,end hay step sẽ trả về kết quá là chính List đó  
# print(my_list[::2]) #Step là bước nhảy của cac phần tử 
# print(my_list[::-1]) # cú pháp cắt chứa step = - 1 trả về giá trị là một list có vị trí các phần tử được đảo ngược 
                       # dấu trừ (-) của step biểu thị list sẽ được duyệt từ cuối list lên đầu list
'''

List Operations And Useful Methods
Các cú pháp thường dùng với list


'''
# my_list = [1, 2, '3',
#            True]
#print(my_list*2) #ta có thể dùng cú pháp name_list*a để lặp lại(nhân) một List với a là số lần lặp lại 
                 #Trong ví dụ này phét nhân List cho 2 trả về kết quả là một List mới có các phần tử trong List được lặp lại hai lần 
#print(my_list + ['Bang', 100]) #Cấu Trúc name_list + [element,element ] được dùng để tạo một List mới bao gồm các phần tử trong List đã cho và các phần tử thêm và 
#print(my_list) #Hành động cộng ở trên không hề thay đổi my_list 
#Hàm append cộng một phần vào list
#print(my_list.append(100)) #Hàm name_list.append(element) tuy nhiên không thể in ra giá trị tức thời như cú pháp cộng 
                           #trong ví dụ này giá trị của my_list đã thay đổi tuy nhiên câu lệnh ở ví dụ này sẽ in ra mành hình là None 
#print(my_list) #Để thấy được kết quả list đã thay đổi ta phải thực hiện lệnh print một lần nữa lần này kết quả trả về là [1, 2, '3', True, 100]
#Tương tư như hàm append hàm extend cũng thêm trực tiếp phần tử vào trong list tuy nhiên khác với hàm append chỉ thêm một phần tử vào cuối list hàm extend lại có thêm một lần nhiều phần tử hay một list khác 
#print(my_list.extend([100, 'Bang']))
#print(my_list)
#Ngoài ra để chèn một phần tử(element) vào một vị trí(index) xác định trong List ta có cú pháp name_list.insert(index, element)
#print(my_list.insert(3, 4)) #trong ví dụ này ta  thêm một phần tử có giá trị là 4 vào vị trí số 3 của List 
#print(my_list) #kết quả : [1, 2, '3', 4, True]
'''
Remore from list 
Xóa phần tử ra khỏi List

'''
# my_list = [1, 2, '3',
#           True]
#print(my_list.pop()) #Cấu trúc name_list.pop(index = 0) thực hiện xóa giá trị cuối cùng của list đồng thời trả về kết quả là giá trị của phần tử bị xóa 
                     #Trong ví dụ này kết quả in ra màng hình sẽ là True 
#print(my_list)       #Kết quả in ra màn hình True đã bị xóa [1, 2, '3']
#print(my_list.pop(2)) #Ngoài ra ta có thên chỉ đinh vị trí(index) để xóa phần tử(element) tại vị trí đó trong ví dụ nay ta xóa phần tử ở vị trí 2 trong list là phần tử '3'
#print(my_list) #kết quả là : [1, 2, True]
#Tương tự hàm pop Hàm remove cũng dùng để xóa một phần tử ra khỏi list tuy nhiên khác với name_list.pop(index) hàm name_list.remome(value) sẽ xóa phần tử đầu tiên trong list có giá trị được chỉ định nhưng không trả về giá trị phần tử bị xóa(of couse) 
# my_list = [1, 2, 2, 2, '3', 
#             True]
# print(my_list.remove(2)) #kết quả in ra màn hình là None 
# print(my_list) # kết quả in ra màn hình là [1, 2, 2, '3', True] với phần tử có giá trị 2 đầu tiên dã bị xóa 
# my_list.remove(4)
# print(my_list) # kết quả :     my_list.remove(4)
#                                #ValueError: list.remove(x): x not in list #
#                                #Hàm remote sẽ báo lỗi nếu như ta chọn xóa một phần tử có gí trị không tồn tại trong list 
############Bên cạnh name_list.pop(index) và name_list.remove(value) ta còn có del name_list[index] là dùng để xóa phần tử có vị trí được chỉ định trong list
# my_list = [1, 2, 2, 2, '3', 
#            True]
# del my_list[4]
# print (my_list) # câu lên lên này trả về kết quả là [1, 2, 2, 2, True] với phần tử thứ 4 có giá Trị '3' đã bị xóa 
#print(del my_list[4]) #không thể thực hiện cú pháp này 
'''
sorting list 
sắp xếp các phần tử trong List 

'''
###########Hàm name_list.sort() được dùn để sắp xếp cá phần tử(element) trong list theo chiều gias trị tăng dần 
# my_list = [ 4, 2, 7, 1, 5, 8 ,6 , 3 ]
#my_list.sort()
#print(my_list.sort()) không thể dùng cú pháp này vì hàm my_list.sort() không trả về giá trị tức thời 
#print(my_list) #kết quả câu lên này in ra [1, 2, 3, 4, 5, 6, 7, 8]  các phần tử trong List đã được sắp sếp theo giá trị tăng dần 
#Ngoài ra cú pháp name_list.sort(reverse= True) với key reverse= True trả về cho ta giá trị là một list được sắp xếp theo giá trị giảm dần 
#my_list.sort(reverse= True)
#print(my_list) #kết quả câu lên này in ra [8, 7, 6, 5, 4, 3, 2, 1] các phần tử trong List đã được sắp sếp theo giá trị giảm dần
###########Ngoài ra ta còn có hàm name_list.reverse() trả về giá trị là một list có các phần tử được sắp xếp đảo ngược vị trí với list ban đầu
# my_list.reverse()
# print(my_list) #kết quả câu lên này in ra [3, 6, 8, 5, 1, 7, 2, 4]  các phần tử trong List đã được sắp xếp đảo ngược vị trí với list ban đầu
##########Tương tự như Hàm name_list.sort() và name_list.sort(reverse= True), Cú pháp sorted(name_list) và reversed(name_list) cũng dùng để sắp sếp các phần tử(element) trong list theo thứ tự tăng dần và giảm dần 
#tuy nhiên khác với Hàm name_list.sort() và name_list.sort(reverse= True), Cú pháp sorted(name_list) tạo ra một list mới có các phần tử được sắp xếp theo thứ tự tăng dần mà không thay đổi thứ tự trong list đã cho 
#Hàm reversed(name_list) sẽ tao ra một list_reverseiterator object và convert ta sẽ có được một list với các phần tử trong mảng được đảo ngược mà không thay đổi thứ tự trong list đã cho 
# print(sorted(my_list)) # cú pháp này trả về kết quả là một list mới [1, 2, 3, 4, 5, 6, 7, 8] có thứ tự được sắp xếp theo giá trị tăng dần 
# print(my_list) #và không làm thay đổi thứ tự sắp xếp trong my_list cũ 
# print(reversed(my_list)) # cú pháp reversed(name_list) tạo ra một <list_reverseiterator object at 0x00000188050B4C10>
# print(list(reversed(my_list))) # và để in ra list sau khi đảo ngược ta phải convert object này bằng hàm list(name_list)
# print(my_list) # sau đó in ra kết quả ta được một list mới [4, 2, 7, 1, 5, 8, 6, 3] với các phần tử trong mảng được đảo ngược
'''

Những thao tác hữu ích với list 
Useful operations

'''
# my_list = [ 4, 2, 7, 1, 5, 8 ,6 , 3 ]
# my_list_1 = [ 'a', 'b' , 'c']
#Hàm Max có cú pháp max(name_list) trả về kết quả là phần tử có giá trí lớn nhất trong list
#print(max(my_list)) # câu lệnh in ra kết quả là giá trị lớn nhất trong list >> 8
#ngược lại với max(name_list) hàm min(name_list) kết quả là phần tử có giá trí nhỏ nhất trong list
#print(min(my_list))  # câu lệnh in ra kết quả là giá trị nhỏ nhất trong list >> 1 
#Hàm sum(name_list) trả về kết quả là tổng cua các phần tử trong list
#print(sum(my_list)) # câu lệnh in ra kết quả là giá trị tổng của my_list >> 36



