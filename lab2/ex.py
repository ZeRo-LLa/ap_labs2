import unittest

def min_time_to_paint(K, T, L):
    def is_valid(mid):
        painters = 1
        total = 0
        
        for length in L:
            if total + length > mid:
                painters += 1
                total = length
                if painters > K:
                    return False
            else:
                total += length
        return True
    
    left, right = max(L), sum(L)
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result * T


K, T, *L = map(int, input("Введіть K, T та довжини щитів через пробіл: ").split())
print(min_time_to_paint(K, T, L))