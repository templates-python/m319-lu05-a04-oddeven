def main():
    number = int(input('Give a number:\n'))
    if number % 2 == 0:
        print(f'Number {number} is even')
    else:
        print(f'Number {number} is odd')


if __name__ == '__main__':
    main()