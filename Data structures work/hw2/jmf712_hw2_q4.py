def e_approx(n):
    denom = 1
    ans = 1
    for i in range(1,n+1):
        denom *= i
        ans += (1/denom)
    return ans

def main():
    print("time to bring out my main!")
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)
main()
