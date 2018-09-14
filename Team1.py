for x in range(0, 100):
    if(x%5==0 and x%3==0):
        print('FizzBuzz')

    if(x%5==0 and x%3==0 and x%2 ==0):

        print('github')

    if x % 11 == 0:
        print('PULL')

    else:
        if (x % 10 == 0):
            print("github")
        else:
            if (x % 9 == 0):
                print("Version")
            else:
                if (x % 3 == 0):
                    print("fizz")
                else:

                    print(x)

