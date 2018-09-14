for x in range(0, 100):
    if(x%5==0 and x%3==0):
        print('FizzBuzz')
    elif(x%5==0 and x%3==0 and x%2 ==0):
        print('github')
    elif x % 11 == 0:
        print('PULL')
    elif (x % 10 == 0):
        print("github")
    elif (x % 9 == 0):
        print("Version")
    elif(x % 3 == 0):
        print("fizz")
    elif (x%2 == 0):
        print("GIT")
    else:
        print(x)

