# ctrl+/
# f2 可以在代码问题之间跳转
# alt f7 可以查找函数位置比较方便跳转
# ctrl ,能够进行代码提示
# ctrl shift enter 能补齐基本的括号之类的
# ctrl alt I能够自动实现代码缩进

print("你好")
'''这是一段代码练习1'''
print("hellow world", "我很好", sep='     下一个参数\n')
z = input("你想要吃什么呀：")
if z == "鱼":
    print('你很厉害')
else:
    print('你是')


'''这是一段代码练习2'''
x =7
y = 5
y, x = x, y
print(x, y, sep='  下一个值为\n')
d = int("fabcde131313", 16)
print(d)
sum()


'''这是一段代码练习3'''
# 读取路径的时候不想换斜杠就加r
print(r"D:\software_project\pycharm\n")
print("D:\software_project\pycharm\n" * 3, sep='\n')


'''这是一段代码练习4'''
# 定义一个函数，打印信息
def 打印信息(姓名, 年龄):
    print(f"{姓名}的年龄是{年龄}")
# 定义一个变量，重量
重量 = 50
打印信息("张三",20)
print(重量)


'''这是一段代码练习5'''
def 示例(输入的信息,判断的信息1,flag1):
    if 输入的信息==判断的信息1:
        print("恭喜你贼厉害")
        flag=1
    else:
        print("你好像错了，再次重新试试")
        flag=flag1
    return flag

print("你只有三次机会\n")
x=input("")
flag=0
次数=3
判断的信息="我想要吃鱼"
while 次数>0:
    flag=示例(x,判断的信息,flag)
    if flag==1:
        break
    else:
        x=input("")
    次数=次数-1


'''这是一段代码练习6，类的测试'''
