head = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodingOIer 的洛谷题解站</title>
</head>
'''
color = ['unknown', 'red', 'orange', 'yellow',
         'green', 'blue', 'purple', 'black']
for c in color:
    with open(f'./Web/{c}.html', 'w', encoding='utf-8') as f:
        f.write(head)
data = []
with open('./data.txt', encoding='utf-8') as f:
    data = f.readlines()
for x in data:
    temp = x .split(' ')
    pid = temp[0]
    diff = temp[1]
    name = ''
    for i in range(2, len(temp)):
        name += temp[i]
    name = name[:-1]
    with open(f'./Web/{color[int(diff)]}.html', 'a', encoding='utf-8') as f:
        f.write(
            f'<a href="https://www.luogu.com.cn/problem/{pid}">{name}</a><br>\n')
