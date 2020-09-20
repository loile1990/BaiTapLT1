import math

def prob(n,p):
    f = p*(pow(1-p, n-1))*1.0
    return f

#print (prob(3,0.2))

def infoMeasure(n, p):
    return -math.log2(p*(pow(1-p, n-1))*1.0)

def sumProb(N, p):
    sum=0
    for i in range(1, N+1):
        sum+=p*(pow(1-p, i-1))*1.0
    return sum

     
      
'''
print(sumProb(5,0.1))
print(sumProb(30,0.1))
print(sumProb(100,0.1))

print(sumProb(5,0.5))
print(sumProb(30,0.5))
print(sumProb(100,0.5)) 
Ket qua:
0.40951000000000004
0.9576088417247841
0.9999734386011131
0.96875
0.9999999990686774
1.0

in ra 2 truong hop cho thay khi N cang lon thi sumProb cang tien dan ve 1 nhanh
Do do ta uoc doan la  tổng xác suất của phân bố geometric = 1

'''

def approxEntropy(N,p):
    entropy =0
    for i in range(1, N+1):
        entropy += (p*(pow(1-p, i-1))*1.0)*(-math.log2(p*(pow(1-p, i-1))*1.0))
    return entropy



'''
Khi N càng lon, thi xac suat vo cùng nho. Do do ham -log2 tra ve giá tri kha lon
Khi chia cho xac suat thì se tien ve 0. Boi vi ham log2 cham hon so voi ham tuyen tinh

print(approxEntropy(5,0.5))
print(approxEntropy(50,0.5))
print(approxEntropy(500,0.5))


Voi p=0.5 Emtroy cua phan phoi Geometrics se tien ve 2

1.78125
1.9999999999999538
1.9999999999999998
'''
