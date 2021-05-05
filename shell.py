import basic

while True:
    text = input('basic > ')
    result, text = basic.run('<stdin>', text)

    print(text)
    print(result)