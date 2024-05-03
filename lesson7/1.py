av_mark, sum, n = 0, 0, 0
mark = int

while mark != 0:
    n = n + 1
    mark = int(input('Enter mark: '))
    if mark != 0:
        sum = sum + mark
        av_mark = sum/(n)
        #print(n, mark, av_mark, sum)
    else:
        continue

else:
    print('Average mark: ', av_mark)