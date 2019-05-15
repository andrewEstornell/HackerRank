# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    a = sorted(arr)
    print(str(sum(a[:4])) + " " + str(sum(a[1:5])))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
