def staircase(n):
    '''#(n-abs(n))/2 = {0 for n pos
                        n for n neg
        (n+abs(n))/2 = {n for n pos
                        0 for n neg
        ''.join([(((n+abs(n))/2-(abs(n)/n)*j-(n+abs(n))/2n)*'_' + ((n-abs(n))/2 + (abs(n)/n)*j + (n+abs(n))/2n)*'#' + '\n ') for j in range(abs(n))])'''
    return ''.join([((int(((n+abs(n))/2)*(1-1/n)-(abs(n)/n)*j))*'_' + (int(abs((n-abs(n))/2) + (abs(n)/n)*j + (n+abs(n))/(2*n)))*'#' + '\n') for j in range(abs(n))])


print(staircase(7))