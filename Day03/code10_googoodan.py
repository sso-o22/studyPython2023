# 구구단 프로그램
for x in range(2, 10):
    print(f'{x}단 시작 =======')
    for y in range(1, 10):
        # print(x, 'X', y, '=', x*y)  # 이렇게 써도 되지만, 
        print(f'{x} X {y} = {x*y:>2}', end=' ')  # 포맷팅 쓰는게 더 좋다! 최신식!
    print()