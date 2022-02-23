# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    T = dict()

    for i in range(W+1):
        T[i,0] = 0
    for u in range(n+1):
        T[0,u] = 0
    
    for i in range(1,n+1):
        for j in range(1,W+1):
            T[j,i] = T[j,i-1]
            if j >= w[i-1]:
                T[j,i] = max(T[j,i],
                    T[j-w[i-1],i-1]+w[i-1])
    return T[W,n]


if __name__ == '__main__':
    W, n, *w = list(map(int, input().split()))
    print(optimal_weight(W, w))
