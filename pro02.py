# Yêu cầu người dùng nhập vào năm sinh
# Tính tuổi

# Xử lý trường hợp người dùng nhập vào
# năm sinh bằng năm hiện tại,
# thì chương trình sẽ thông báo
# "Bạn vừa sinh ra trong năm nay"

# Hiện thỉ tên chương trình
print("CHƯƠNG TRÌNH TÍNH TUỔI")
# Nhập năm sinh
birthyear = int(input("Vui lòng nhập năm sinh: "))
# Tính tuổi
age = 2022 - birthyear
# Kiểm tra tuổi
if (age == 0):
    print("Bạn vừa sinh ra trong năm nay")
elif (age < 0):
    print("Bạn chưa được sinh ra")
else:
    print("Tuổi của bạn là", age)
