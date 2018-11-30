import re

ID_card = input("请输入身份证号")
if len(ID_card) == 18:
    pattern = r"(?P<province>\d{4})(?P<city>\d{2})(?P<date>\d{8})(?P<code>\d{4}|\d{3}X)"
    province = re.search(pattern, ID_card).group('province')
    city = re.search(pattern, ID_card).group('city')
    date = re.search(pattern, ID_card).group('date')
    code = re.search(pattern, ID_card).group('code')
    print(province, city, date, code)
else:
    print("您输入的身份证号有误请重新输入")


