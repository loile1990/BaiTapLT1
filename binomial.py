import operator as op
import math
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def prob(n, p, N):
    p= ncr(N, n)* (p**n)*(1-p)**(N-n)
    return p
#print (prob(4,0.3,6))

    
def infoMeasure(n, p, N):
    return (-(math.log2( prob(n, p, N))))
#print (infoMeasure(4,0.3,6))

def sumProb(N,p):
    sum=0
    for i in range(1, N+1):
        sum+=prob(i, p, N)
    return sum
'''
print (sumProb(5,0.3))
print (sumProb(30,0.3))
print (sumProb(60,0.3))
0.8319299999999998
0.9999774606597077
0.9999999994919746
Ta thay tong tien gan ve 1. Do do ta co the nói tong la 1
'''
def approxEntropy(p,N):
    entropy =0
    for i in range(1, N+1):
        entropy += prob(i, p, N) *infoMeasure(i, p, N)
    return entropy
'''
Khi n càng lon, thi xac suat vo cùng nho. Do do ham -log2 tra ve giá tri kha lon
Khi chia cho xac suat thì se tien ve 0. Boi vi ham log2 cham hon so voi ham tuyen tinh

Voi p=0.5 Emtroy cua phan phoi Binomial là 

print (approxEntropy(2,0.5))
print (approxEntropy(3,0.5))
print (approxEntropy(4,0.5))
print (approxEntropy(200,0.5))
print (approxEntropy(250,0.5))
print (approxEntropy(300,0.5))

1.0
1.436278124459133
1.7806390622295665
4.869020643912809
5.029985788332068
5.161503585599376

'''

