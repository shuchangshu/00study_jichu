import  time
def feibola(abc,abc2):
    def febola1(function):
        def feibola2(arge):
            start=time.time_ns()
            function(arge)
            end=time.time_ns()
            print ("{0}\n{1}\n这个程序运行了{2}秒".format(abc,abc2,(end-start)/10e+9))
        return feibola2
    return febola1
@feibola(abc="你好第一次用",abc2="我会努力加油的")
def jisuan(arge):
    # arge=int(input("输入你想要的数据长度："))
    i=0
    sum1=0
    sum2 =1
    print(sum1,sum2,sep="\n")
    while i<arge-2:
        sum =sum1+sum2
        sum1,sum2=sum2,sum
        print(sum)
        i+=1
# 继续打印你好
print("你好")
print("它也好")
lenth1=int(input("你好"))
jisuan(lenth1)
print("ncnaocnaoc")

