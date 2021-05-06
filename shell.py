import basic

# f = open("consoleLog.txt", "r")
# command=f.read()

while True:
    cmd = input('basic > ')
    #result, error = basic.run('<stdin>', text)
    result, text = basic.run('<stdin>', cmd)

    consoleLine = ""
    numberCount = 0
    for char in text:
        if char != "#" :
            consoleLine += char
        if (char == "#"):
            numberCount += 1
        if numberCount == 2 :
            consoleLine += str(result)
            numberCount = 0 


    # resultIndex = text.find("#")
    # text =  text[:resultIndex] + text[1+resultIndex:]
    # text = text[:resultIndex] + str(result) + text[resultIndex:]

    print(consoleLine)