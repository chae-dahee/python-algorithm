def SolveTowers(n, ffrom, to, spare):
    if n == 1:
        print(ffrom+" 에서"+to+" 로 이동")
        return
    SolveTowers(n-1, ffrom, spare, to)      # 2개를 from에서 spare로 이동시켜야함
    SolveTowers(1, ffrom, to, spare)    #1개를 from에서 to로 이동
    SolveTowers(n-1, spare, to, ffrom)

SolveTowers(3,"from", "to", "spare")
