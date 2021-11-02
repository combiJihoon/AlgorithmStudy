import sys

input = sys.stdin.readline

p1, p2 = [0], [0]

t = int(input())
for _ in range(t):
    n = int(input())
    nodes = [0] * (n+1)
    for _ in range(n-1):
        p, c = map(int, input().split())
        nodes[c] = p  # 자식 노드에 대한 부모 노드 정보 저장
    child1, child2 = map(int, input().split())
    p1 = [0, child1]
    p2 = [0, child2]

    while nodes[child1]:
        p1.append(nodes[child1])
        child1 = nodes[child1]
    while nodes[child2]:
        p2.append(nodes[child2])
        child2 = nodes[child2]
    i = 1
    while p1[-i] == p2[-i]:
        i += 1
    print(p1[-i+1])


'''
-1 인덱스부터 왼쪽으로 인덱스를 이동하게 되는데
가장 오른쪽에 있는 원소는 가장 먼 조상이다.
왼쪽으로 이동하다가 같지 않은 원소가 나오면 그 전 원소가 
가장 가까운 공통 조상이 되는 것이다.
'''
