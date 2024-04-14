import luoguapi
import threading
import time
import random


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def front(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def find(self, item):
        return item in self.queue


ty = ['P', 'B', 'CF', 'SP', 'AT', 'UVA']

thread = 5

wait = []

ck = []


def searchProblem():
    unknown = luoguapi.session()
    r = 0
    for t in ty:
        pg = 0
        while True:
            pg += 1
            res = unknown.problem.list(f'type={t}&page={pg}')
            if res[0]:
                if res[1]['code'] == 418:
                    print(f'End of list {t}')
                    break
                data = res[1]['currentData']['problems']['result']
                if len(data) == 0:
                    break
                for problem in data:
                    print(f'Add {problem["pid"]}')
                    wait[r % thread].push(problem)
                    r += 1
            else:
                pass
            time.sleep(30)


def add(pid, name, diff):
    global user
    with open(f'./data.txt', 'a', encoding='utf-8') as f:
        f.write(
            f'{pid} {diff} {name}\n')


def checker(id):
    cnt = 0
    user = luoguapi.session()
    user.user.loginCookie(ck[id % len(ck)][0], ck[id % len(ck)][1])
    while True:
        if cnt == 30:
            print(f'Thread {id} Timeout')
            break
        elif wait[id].empty():
            print(f'Thread {id} wait {cnt}')
            cnt += 1
            time.sleep(random.uniform(1, 2))
        else:
            cnt = 0
            problem = wait[id].front()
            pid = problem['pid']
            name = problem['title']
            diff = problem['difficulty']
            print(f'Visit {pid}')
            try:
                re = user.problem.solution(pid)
            except:
                wait[id].push(problem)
                print(f'Error: {pid}, push again')
                continue
            if not re[0]:
                wait[id].push(problem)
                print(f'Error: {pid}, push again')
                continue
            so = re[1]
            if so['currentData']['acceptSolution']:
                print(f'Already submit solution {pid}')
                add(pid, name, diff)
            time.sleep(random.uniform(1, 2))


if __name__ == '__main__':
    with open('cookie.txt', 'r') as f:
        s = f.readlines()
        for c in s:
            c = c.split(' ')
            c[1] = c[1][:40]
            ck.append([c[0], c[1]])
    for i in range(thread):
        wait.append(Queue())
    threading.Thread(target=searchProblem).start()
    with open('./data.txt', 'w', encoding='utf-8') as f:
        pass
    for i in range(thread):
        threading.Thread(target=checker, args=(i,)).start()
