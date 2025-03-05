import unittest

def is_monotonic(arr):
    increasing = decreasing = True 

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:  
            decreasing = False
        elif arr[i] < arr[i - 1]:  
            increasing = False

        if not increasing and not decreasing:
            return False

    return True  

user_input = input("Введіть масив чисел через пробіл: ")
arr = list(map(int, user_input.split()))
    
print("Монотонний:", is_monotonic(arr))
