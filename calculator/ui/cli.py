from calculator import Calculator


def main(args):
    calculator = Calculator()
    calculator.expression = " ".join(args)
    try:
        result = calculator.compute_result()
        print(result)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
