import codecs

f = ['r3st', '4s_a', 'b3_c', 'm4tt', 'l3t_']
l = ['4ll0', '30_1', '7t3_', 'jkin', 'p1ck']
a = ['5_th', '3_4n', '1t_1', '00p5', '1n_1']
g = ['p1_7', '3_w0', 't0g3', '00_k', 'n0th']
s = ['ear5', 'k!1!', '1n6!', '33p5', 'rd_!']

def print_flag(indexes):
    flag = ''
    flag += f[indexes[0]]
    flag += l[indexes[1]]
    flag += a[indexes[2]]
    flag += g[indexes[3]]
    flag += s[indexes[4]]
    flag = 'upgs{' + flag + '}'
    flag = codecs.encode(flag, 'rot13')
    print(flag)

print_flag([3, 1, 0, 1, 4])