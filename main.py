import luoguapi
import time
import os

ty = ['P', 'B', 'CF', 'SP', 'AT', 'UVA']
color = ['unknown', 'red', 'orange', 'yellow',
         'green', 'blue', 'purple', 'black']

user = luoguapi.session()


def add(pid, name, diff):
    global user
    if res[0]:
        with open(f'./web/{color[diff]}.html', 'a', encoding='utf-8') as f:
            f.write(
                f'<a href="https://www.luogu.com.cn/problem/{pid}" target="_blank">{pid} {name}</a><br>')


if __name__ == '__main__':
    with open('cookie.txt', 'r') as f:
        s = f.readline()
        s = s.split(' ')
        res = user.user.login(s[0], s[1])
        if not res[0]:
            print('User login failed')
            exit(0)
    print('Success to login')
    old = f'./old{time.time()}'
    os.system(f'mkdir {old}')
    os.system('cp ./Web/*.html {old}')
    os.system('rm ./Web/*.html')
    for t in ty:
        pg = 0
        while True:
            pg += 1
            res = user.problem.list(f'type={t}&page={pg}')
            if res[0]:
                if res[1]['code'] == 418:
                    print(f'End of list {t}')
                    break
                data = res[1]['currentData']['problems']['result']
                for problem in data:
                    pid = problem['pid']
                    name = problem['title']
                    diff = problem['difficulty']
                    so = user.problem.solution(pid)[1]
                    print(f'Visit {pid}')
                    if not so['currentData']['acceptSolution']:
                        print(f'Already submit solution {pid}')
                        add(pid, name, diff)
                    pass
            else:
                print('Unknown Error')
                exit(0)
