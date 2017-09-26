def odwroc_str(zdanie):
    return zdanie[::-1]

def odwroc_input():
    zdanie = input("Podaj zdanie: ")
    return odwroc_str(zdanie)

def main():
    print(odwroc_input())

if __name__ == '__main__':
    main()