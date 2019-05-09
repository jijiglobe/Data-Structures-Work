def interpret(variables, exp):
    nums= []
    symbols = ["+","-","*","/"]
    for character in exp:
        if character in symbols:
            second = float(nums.pop())
            first = float(nums.pop())
            
            if character == "+":
                nums.append(first + second)
            if character == "-":
                nums.append(first - second)
            if character == "*":
                nums.append(first * second)
            if character == "/":
                nums.append(first / second)
        elif character in variables:
            nums.append(variables[character])
        else:
            nums.append(character)
    ans = nums.pop()
    print(ans)
    if float(ans) % 2 == 0:
        return int(ans)
    else:
        return ans

def main():
    variables = {}
    expression = input("--> ")
    while expression != "done()":
        expression = expression.split()
        #print(expression)
        if len(expression) >1 and expression[1] == "=":
            variables[expression[0]] = interpret(variables, expression[2:])
            print(expression[0])
        else:
            print(interpret(variables,expression))
        expression = input("--> ")
if __name__ == "__main__":
    main()
