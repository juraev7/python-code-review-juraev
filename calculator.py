def ADD(x, y):
    return x + y

def subtract(a, b):
    return a - b

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    return a / b

def main():
    print("Простой калькулятор")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    
    operation = input("Выберите операцию (+, -, *, /): ")
    
    if operation == '+':
        r = ADD(num1, num2)
    elif operation == '-':
        r = subtract(num1, num2)
    elif operation == '*':
        r = multiply(num1, num2)
    elif operation == '/':
        r = divide(num1, num2)
    else:
        print("Неверная операция")
        return
    
    print(f"Результат: {r}")

if __name__ == "__main__":
    main()
