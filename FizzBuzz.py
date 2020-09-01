# FizzBuzz Game #
# The Following code will run the FizzBuzz Game
# However, unlike the original I have included Bang when the number 4 appears

for i in range(1, 101):

    output = ""
    if i % 3 == 0:
        output += 'Fizz'
    if i % 5 == 0:
        output += 'Buzz'
        if i % 4 == 0:
            output += 'Bang'
    elif output == '':
        output = str(i)

    print(output)
