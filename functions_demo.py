def magic_sum(a, b, c='abc', d='*', e='\n'):
    res = a + b + c + d + e
    return res


def modify(L):
    L.append('new_value')
    return L

'''
M = [1, 2, 3]
print('До: ', M)
L = modify(M)
print('После: ', M)
print(L)
print(id(L) == id(M))
'''