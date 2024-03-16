ans = 0
def getSome(here):
    global ans
    if here > howmany:return
    if here == howmany:
        ans += 1
        return
    getSome(here+1)
    getSome(here+2)

howmany = 3
getSome(0)
print(ans)