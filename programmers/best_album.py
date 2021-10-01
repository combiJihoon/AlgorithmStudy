def solution(genres, plays):
    n = len(genres)
    d = dict()
    for i in range(n):
        if genres[i] not in d:
            d[f'{genres[i]}'] = [(plays[i], i)]
        else:
            d[f'{genres[i]}'].append((plays[i], i))

    sum_list = []
    for key, _list in d.items():
        tmp = 0
        for i in _list:
            tmp += i[0]
        sum_list.append((tmp, key))

    sum_list = sorted(sum_list, key=lambda x: -int(x[0]))
    ans = []
    for i in sum_list:
        tmp = sorted(d[i[1]], key=lambda x: (-int(x[0]), x[1]))
        cnt = 0
        for i in tmp:
            ans.append(i[1])
            cnt += 1
            if cnt == 2:
                break
    return ans


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))
