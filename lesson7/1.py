av_mark, sum1, n = 0, 0, 0
mark = int

while mark != 0:
    n = n + 1
    mark = int(input('Enter mark: '))
    if mark != 0:
        sum1 = sum1 + mark
        av_mark = sum1/n
        #print(n, mark, av_mark, sum)
else:
    print('Average mark: ', av_mark)