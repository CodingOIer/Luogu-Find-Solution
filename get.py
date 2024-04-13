import luoguapi

ty = ['P', 'B', 'CF', 'SP', 'AT', 'UVA']

user = luoguapi.session()


def add(pid, name, diff):
    global user
    if res[0]:
        with open(f'./data.txt', 'a', encoding='utf-8') as f:
            f.write(
                f'{pid} {diff} {name}\n')


if __name__ == '__main__':
    with open('cookie.txt', 'r') as f:
        s = f.readline()
        s = s.split(' ')
        user.user.loginCookie(s[0], s[1])
    with open('data.txt', 'w') as f:
        pass
    for t in ty:
        pg = 0
        while True:
            pg += 1
            res = user.problem.list(f'type={t}&page={pg}')
            print(f'Get url {f'type={t}&page={pg}'}')
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
                    if so['currentData']['acceptSolution']:
                        print(f'Already submit solution {pid}')
                        add(pid, name, diff)
                    pass
            else:
                print('Unknown Error')
                exit(1)
