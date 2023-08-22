import math

def odd_series(x, k):
    result = 0
    for i in range(1, k+1, 2):
        result += math.sin(i * x)/i
    return result
k = 500
x = math.pi/2
ans = odd_series(x,k)
print('THE APP. ANSWER IS: ', 4*ans)
print('WHERE THE EXACT VALUE FOR PI: ', math.pi)
print('THE ERROR:', abs((4*ans - math.pi)/math.pi)*100,'%')




