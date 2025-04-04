# Submission link: https://codeforces.com/contest/238/submission/287288224
def main():
    n, h = MII()
    nums = LII()

    inf = 10 ** 8
    mi1, mi2, mi3 = inf, inf, inf
    ma1, ma2 = 0, 0

    for v in nums:
        if v <= mi1:
            mi1, mi2, mi3 = v, mi1, mi2
        elif v <= mi2:
            mi2, mi3 = v, mi2
        elif v < mi3:
            mi3 = v
        
        if v >= ma1:
            ma1, ma2 = v, ma1
        elif v > ma2:
            ma2 = v

    f1 = (ma1 + ma2) - (mi1 + mi2)
    f2 = fmax(ma1 + ma2, ma1 + mi1 + h) - fmin(mi1 + mi2 + h, mi2 + mi3)

    if f1 <= f2:
        print(f1)
        print(*[1] * n)
    else:
        print(f2)
        ans = [1] * n
        for i in range(n):
            if nums[i] == mi1:
                ans[i] = 2
                break
        print(*ans)