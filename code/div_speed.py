f = open('C:/Users/asas/Desktop/core/speed/person/p2.txt')
result = open("C:/Users/asas/Desktop/woman/1.txt","w")
for line in f.readlines():
    filename = line.split(',')[0]
    hr = line.split(',')[1]
    hr = int(hr)
    if ((0 <= hr) and (hr < 10)):
        result.write(filename+"\n")
f.close()
result.close()