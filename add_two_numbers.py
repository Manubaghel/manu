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
    # Print as int if both inputs were integers
    if total.is_integer() and all(p.isdigit() or (p.startswith("-") and p[1:].isdigit()) for p in parts):
        print(int(total))
    else:
        print(total)


if __name__ == "__main__":
    main()
