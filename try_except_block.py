
def try_block(num):
    try:  
        assert num % 2 == 0
    except Exception as e:
        print(e)
        print("Not an even number!")
    else:
        reciprocal = 1/num
        print(reciprocal)
    finally:
        print("This is finally block.")

num = int(input("Enter a number: "))
try_block(num)