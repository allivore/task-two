def pi(n):
    n1 = 0
    c = 10002499687
    mc = 8
    m = mc
    f1 = 10**mc
    f2 = f1**2
    a = 10005*f2 - c**2
    while mc<n:
        a *= f2
        b = c*2 * f1
        d = a//b
        c = c*f1 + d
        a -= d * (b+d)
        mc += m
        if mc*2 > n:
            m = n-mc
        else:
            m = mc
        f1 = 10**m
        f2 = f1**2
        n1 += 1

    n += 2
    base = 10**n
    A = 13591409*base
    B = A
    c3 = 13591409
    i = 1
    while abs(A) > 5:
        c1 = ((108-72*i)*i-46)*i + 5
        c2 = 10939058860032000 * i**3
        c4 = c3
        c3 += 545140134
        i += 1
        A = A*c1*c3 // (c2*c4)
        B+=A
    p = 426880*base*c // B // 100
    return '3,' + str(p)[1:n-1]
