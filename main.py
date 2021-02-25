from katas import pig_it
from katas import validBraces
from katas import snail
from katas import encode
from katas import decode
from katas import int32_to_ip
from katas import parts_sums
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

    print(encode("hey h"))
    print(decode("000111111000111000000000000111111000000111000111000111111111111000000111000000111000000000000000000111111000111000000000")+"*")
            #      0   1   0   0    0  0   0   0   0    1  1   0   0   1   0   1
            #       01000000
    print("CODIGOS IP4")
    print(int32_to_ip(10))

    print(parts_sums([0, 1, 3, 6, 10]))
