from katas import pig_it
from katas import validBraces
from katas import snail
if __name__ == '__main__':
    from undecorated import undecorated


    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")

        return wrapper


    @my_decorator
    def say_whee():
        print("Whee!")


    say_whee_org = undecorated(say_whee)
    say_whee_org()
    #print(pig_it('Pig latin is cool ?'))
    print(validBraces("[()]{{()}}"))

    print("\n\n\n")

    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    snail(array)


