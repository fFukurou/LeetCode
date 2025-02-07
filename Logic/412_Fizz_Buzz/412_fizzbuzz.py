

def fizz_buzz(num_range) -> list[str]:
    array : str = []
    for i in range(1, num_range + 1):
        if i % 5 == 0 and i % 3 == 0:
            array.append("FizzBuzz")
        elif i % 3 == 0 :
            array.append("Fizz")
        elif i % 5 == 0:
            array.append("Buzz")
        else:
            array.append(str(i))

    return array


def main():
    print(fizz_buzz(15))


if __name__ == '__main__':
    main()