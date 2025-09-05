print("==============================      THIRD HOMEWORK       ==========================" )
print("==============================      Exercise 1        ==========================" )
# برنامه شبیه‌سازی‌ دستگاه ATM را بنویسید که قابلیت‌های زیر را داشته باشد.
# 1. mojoudi
# 2. variz
# 3. bardasht
# 4. khorouj
# ابتدا باید یک مقدار موجودی اولیه تعریف بشود. کاربر با انتخاب گزینه اول بتواند موجودی حساب خود را
# ببیند. با انتخاب گزینه دوم مقدار دلخواه را به موجودی قبلی اضافه کند. با گزینه سوم بتواند از حساب خود
# مقدار دلخواهی را برداشت کند. در نهایت با انتخاب گزینه آخر از برنامه خارج شود. تا زمانی که گزینه خروج
# را نزده است باید منو همچنان روی صفحه آماده دریافت دستور باشد.
Mojoudi = 100
variz = 0
bardasht = 0
mandeh = Mojoudi + variz - bardasht
while True:
    User_Request = int(input('Please Enter Your Request: \n1.Moujodi\n2.Variz\n3.Bardasht\n4.Khorouj\n---> '))
    if User_Request == 1:
        print(f'Mablaq MOjoudi : {Mojoudi}')
    elif User_Request == 2:
        variz = int(input('Mablaq Varizi Ra Vared Konid \n ---> ')) 
        mandeh = Mojoudi + variz
        Mojoudi = mandeh
        print(f'Mablaq MOjoudi : {Mojoudi}')
    elif User_Request == 3:
        bardasht = int(input('Mablaq Bardashti Ra Vared Konid \n ---> '))
        mandeh = Mojoudi -bardasht
        Mojoudi = mandeh
        print(f'Mablaq MOjoudi : {Mojoudi}')
    elif User_Request == 4:
        break
print("==============================      Exercise 2        ==========================" )
print("==============================      Exercise 2.1        ==========================" )
#شمارش تعداد کلمات متن 
my_text = """python is a high-level, general-purpose programming language.
Its design philosophy emphasizes code readability with the use of significant indentation.
Python is dynamically type-checked and garbage-collected.
It supports multiple programming paradigms, including structured (particularly
procedural), object-oriented and functional programming.
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC
programming language, and he first released it in 1991 as Python 0.9.0.
Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not
completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last
release of Python 2.
Python consistently ranks as one of the most popular programming languages, and it has
gained widespread use in the machine learning community."""
print(len(my_text.split()))
print("==============================       SEC 2.2       ==========================" )
my_list = my_text.split()
my_dict ={}
for values in my_list:
    if values not in my_dict:
        my_dict[values]=1
    else:
        my_dict[values]=  my_dict[values]+1
print(my_dict)
print("==============================       SEC 2.3       ==========================" )
#تکرار کلمه پایتون
my_lst= my_text.split()
new_lst =[]
for ch in my_lst:
    if ch == 'Python'or ch=="python":
        new_lst.append(ch)
    else:
        continue
print(len(new_lst))