def get_number(prompt: str) -> float:
    raw = input(prompt).strip()
    try:
        return float(raw)
    except ValueError as exc:
        raise SystemExit("Error: please enter a valid number.") from exc


def get_operation() -> str:
    raw = input("Choose operation (+, -, *, /): ").strip()
    if raw not in {"+", "-", "*", "/"}:
        raise SystemExit("Error: operation must be one of +, -, *, /.")
    return raw


def main() -> None:
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")
    op = get_operation()

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    else:
        if b == 0:
            raise SystemExit("Error: division by zero.")
        result = a / b

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
