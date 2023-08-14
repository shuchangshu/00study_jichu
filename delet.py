a = [0] * 3
for i in range(3):
    a[i] = [1+i,2,3]
print(len(a))
bb = [j for j in a ]
bb = [a[j][len(a) - j - 1] for j in range(len(a))]
print(bb)

x="FF"
d=[ord(x) for x in x]
print(d)
x ="ff"
d = int(x[0], 16) * 256 + int(x[1], 16)

print("你好")
print("它也好")