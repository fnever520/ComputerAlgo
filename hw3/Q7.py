def interwoven():
    T = "caabcbbabccdw"
    x = "abac"
    y = "awbcc"
    z = "ccd"
    xi = yi = zi = result = 0

    for i in range(len(T)):
        if xi < len(x):
            if x[xi] == T[i]:
                xi+=1

        if yi < len(y):
            if y[yi] == T[i]:
                yi+=1

        if zi < len(z):
            if z[zi] == T[i]:
                zi+=1

    if ((xi == len(x)) and (yi == len(y)) and (zi == len(z))):
        result = "interwoven."
    else:
        result = "not interwoven."

    return result

print("It is", interwoven())