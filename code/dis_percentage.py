k = open('F:/dataset/new1.txt')
arr_a = []
arr_b = []
arr_c = []
arr_d = []
arr_e = []
arr_f = []
for line in k.readlines():
    a = line.split(' ')[1]
    b = line.split(' ')[2]
    c = line.split(' ')[3]
    d = line.split(' ')[4]
    e = line.split(' ')[5]
    f = line.split(' ')[6]
    a = float(a.strip('%'))/100
    b = float(b.strip('%'))/100
    c = float(c.strip('%'))/100
    d = float(d.strip('%'))/100
    e = float(e.strip('%'))/100
    f = float(f.strip('%'))/100
    arr_a.append(a)
    arr_b.append(b)
    arr_c.append(c)
    arr_d.append(d)
    arr_e.append(e)
    arr_f.append(f)
k.close()
print(sum(arr_a)/len(arr_a))
print(sum(arr_b)/len(arr_b))
print(sum(arr_c)/len(arr_c))
print(sum(arr_d)/len(arr_d))
print(sum(arr_e)/len(arr_e))
print(sum(arr_f)/len(arr_f))