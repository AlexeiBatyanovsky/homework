av_mark, n = 0, 0
mark = int(input('Enter mark: '))

while mark != 0:
    n += 1
    av_mark += mark
    mark = int(input('Enter mark: '))
else:
    print('Average mark: ', av_mark/n)