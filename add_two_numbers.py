def main() -> None:
    raw = input("Enter two numbers separated by space: ").strip()
    parts = raw.split()
    if len(parts) != 2:
        raise SystemExit("Error: please provide exactly two numbers.")

    try:
        a = float(parts[0])
        b = float(parts[1])
    except ValueError as exc:
        raise SystemExit("Error: both inputs must be numbers.") from exc

    total = a + b
    product = a * b
    inputs_are_int = all(p.isdigit() or (p.startswith("-") and p[1:].isdigit()) for p in parts)

    # Print as int if both inputs were integers
    if inputs_are_int and total.is_integer():
        print(f"Sum: {int(total)}")
    else:
        print(f"Sum: {total}")

    if inputs_are_int and product.is_integer():
        print(f"Product: {int(product)}")
    else:
        print(f"Product: {product}")


if __name__ == "__main__":
    main()
