import operator as op
from functools import reduce
from math import log2 as log


def nCr(n, r):
	r = min(r, n - r)
	numer = reduce(op.mul, range(n, n - r, -1), 1)
	denom = reduce(op.mul, range(1, r + 1), 1)
	return numer // denom

def prob(n, p, r):
	return nCr(n - 1, n - r) * p ** r * (1 - p) ** (n - r)

def infoMeasure(n, p, r):
	return -log(prob(n, p, r))

def sumProb(N, p, r):
	s = 0
	for i in range(r, N + 1):
		s += prob(i, p, r)
	return s
'''
Tong xac suat nay luon la 1 neu r bat dau tu 1
print (sumProb(50, 0.9, 1)) =1
print (sumProb(50, 0.3, 1)) =1

'''
def approxEntropy(N, p, r):
	Ent = 0
	for k in range(r, N + 1):
		Pr = prob(k, p, r)
		I = infoMeasure(k, p, r)
		Ent += Pr * I
	
	return Ent
'''
Gia tri entropy tien den 2 voi p=0.5 va r xuat phat tu 1
print(approxEntropy (30,0.5, 1))
print(approxEntropy (40,0.5, 1))
print(approxEntropy (60,0.5, 1))
'''
