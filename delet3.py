
class S(str):
    def __add__(self, other):
        pass
    def sum(self,x,y) -> object:

        return x+y
    def __repr__(self):
        print("nh")
        return "你好"
s1=S()
repr(s1)

s1=S("nhao")
print(s1)
print(s1.__dict__)
sum1=s1.sum(2,3)
print(sum1)

if 0.1+0.2!=0.3:
    print("nh ")
