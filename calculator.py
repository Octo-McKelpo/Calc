import math

ALLOWED_VALUES = {
    k: v for k, v in math.__dict__.items() if not k.startswith("__")
}

msg = "Type 'exit' or 'quit' to close the program. \nEnter your expression here: "


def evaluate(expression):
    """Evaluate a math expression."""
    # Компиляция выражения
    code = compile(expression, "<string>", "eval")

    # Проверка на разрешенные символы
    for name in code.co_names:
        if name not in ALLOWED_VALUES:
            raise NameError(f"The use of '{name}' is not allowed")

    return eval(code, {"__builtins__": {}}, ALLOWED_VALUES)

def main():
    while True:
        # Чтение ввода юзера
        try:
            expression = input(f"{msg} ")
        except (KeyboardInterrupt, EOFError):
            raise SystemExit()

        # Возможность выхода из программы
        if expression.lower() in {"quit", "exit"}:
            raise SystemExit()

        # Обработка выражения
        try:
            result = evaluate(expression)
        except SyntaxError:
            # Если введено неверное выражение
            print("Invalid input expression syntax")
            continue
        except (NameError, ValueError) as err:
            # Если юзер вводит неверное значение или название команды
            print(err)
            continue

        # Печать результата, если нет ошибок
        print(f"The result is: {result}")

if __name__ == "__main__":
    main()