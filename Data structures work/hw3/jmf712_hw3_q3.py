def print_triangle(n):
    if n > 0:
        print("*" * n)
        print_triangle(n-1)

def print_opposite_triangle(n, ans = ["",""]):
    if n<=0:
        print(ans[0][1:])
        print(ans[1][1:])
    else:
        ans[0] += "\n" + "*"*n
        ans[1] = "\n" + ("*"*n) + ans[1]
        print_opposite_triangle(n-1,ans)

print_triangle(10)
print_opposite_triangle(10)
