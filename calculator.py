def add(a, b):
    """Сложение двух чисел."""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел."""
    return a - b

def multiply(a, b):
    """Умножение двух чисел."""
    return a * b

def divide(a, b):
    """Деление двух чисел с проверкой деления на ноль."""
    if b == 0:
        raise ValueError("Ошибка: деление на ноль!")
    return a / b

def power(a, b):
    """Возведение в степень."""
    return a ** b

def main():
    """Основная функция калькулятора."""
    print("=== ПРОСТОЙ КАЛЬКУЛЯТОР ===")
    
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите корректные числа!")
        return
    
    print("\nДоступные операции:")
    print("+ - сложение")
    print("- - вычитание") 
    print("* - умножение")
    print("/ - деление")
    print("^ - возведение в степень")
    
    operation = input("\nВыберите операцию: ")
    
    try:
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        elif operation == '^':
            result = power(num1, num2)
        else:
            print("Неверная операция!")
            return
        
        print(f"\nРезультат: {num1} {operation} {num2} = {result}")
        
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()
