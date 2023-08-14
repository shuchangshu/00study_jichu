
i = 1   # 定义全局变量记录次数
def move(n, a, c):
    global i
    print("第{}步：将编号为{}的盘子从{}--->{}".format(i, n, a, c))
    i += 1
def hanoi(n,a,b,c):
    #a,b,c分别是三根柱子，n为套在a柱上的圆圈个数
    if n == 1:
        move(n, a, c)
    else:
        hanoi(n-1, a, c, b)
        move(n, a, c)
        hanoi(n-1, b, a, c)

n = int(input("请输入盘子数量："))
hanoi(n,"a","b","c")
print(i)