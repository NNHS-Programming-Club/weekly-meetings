def func(input):
    print(input)
    if input == 1:
        quit()
    elif input % 2 == 1:
        func(input * 3 + 1)
    else:
        func(int(input / 2))
func(7)