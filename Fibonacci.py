def matrix(A, B) :
    C = [A[0] * B[0] + A[2] * B[1], A[1] * B[0] + A[3] * B[1], A[0] * B[2] + A[2] * B[3], A[1] * B[2] + A[3] * B[3]]
    return C

ANS = [1, 0, 0, 1]
TMP = [1, 1, 1, 0]

print("This program is used to calculate Fibonacci number.")
print("Input n, and I will calculate F(n) for you.")

N = int(input())

while N > 0 :
    if N % 2 == 1 :
        ANS = matrix(ANS, TMP)
    TMP = matrix(TMP, TMP)
    N = N // 2

print("Done. F(n) is:")
print(ANS[1])