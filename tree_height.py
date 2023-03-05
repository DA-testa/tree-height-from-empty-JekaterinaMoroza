import sys
import threading
#import numpy

def compute_height(n, parents):
    augstums= [0]*n
    root= parents.index(-1)

    def dfs(i) :
        if augstums[i] != 0:
            return augstums[i]
        if parents[i] == -1:
            augstums[i] = 1
        else:
            augstums[i] = 1 + dfs(parents[i])

        return augstums[i]
                
    for i in range(n):
        dfs(i)

    return max(augstums)


def main():
    text= input("I or F:")
    if "I" in text or "i" in text:
        n=int(input())
        parents = list(map(int, input().split()))
        max_augstums = compute_height(n, parents)
        print(max_augstums)
        
    if "F" in text:
        filename = input()
        file='./test/'+ filename
        if 'a' not in filename:
            with open (file) as file:
                n=int (file.readline())
                parents = list(map(int, file.readline().strip().split()))
                max_augstums = compute_height(n, parents)
                print(max_augstums)
        else: 
            print ("Error: invalid filename")

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#print(numpy.array([1,2,3]))