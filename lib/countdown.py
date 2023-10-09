# your code goes here!
# import time

# def countdown():
#     def countdown_with_sleep(count):
#         while count > 0:
#             print(f'{count} SECOND(S)!')
#             time.sleep(1)
#             count -= 1
#         print('HAPPY NEW YEAR!')
    
#     return countdown_with_sleep

# countdown_func = countdown()
# countdown_func(10)

import time

def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        time.sleep(1)
        number -= 1
    print('HAPPY NEW YEAR!')

countdown_with_sleep(10)
