from collections import deque

graph = {
    'bob': ['anu', 'peggy'],
    'you': ['alice', 'bob', 'claire'],
    'alice': ['peggy'],
    'claire': ['tom', 'jon'],
    'anuj': [],
    'peggy': [],
    'anu': [],
    'tom': [],
    'jon': []
}

def person_is_saller(name):
    return name[-1] == 'm'

def search(name):
    queue = deque()
    queue += graph[name]

    verified = []

    while queue:
        person = queue.popleft()
        if not person in verified:
            if person_is_saller(person):
                print(f'{person} is a mongo saller')
                return True
            else:
                queue += graph[person]
                verified.append(person)
    return False

search('you')
        
