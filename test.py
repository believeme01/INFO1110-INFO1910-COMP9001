def choose(n,k):
    frac = 1
    for i in range(n):
        frac = frac*(i+1)
    den = 1
    for i in range(k):
        den *= (i+1)
    for i in range(n-k):
        den *= (i + 1)
    return int(frac/den)

print(choose(3,3))
print(choose(4,3))
print(choose(5,3))

def related_board_ij(ci,cj):

    return [(ci,cj),(ci,cj+1),(ci+1,cj),(ci+1,cj+1)]