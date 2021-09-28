def solution(clothes):
    clothes_dict = dict()
    for val, key in clothes:
        if key not in clothes_dict:
            clothes_dict[key] = [val]
        else:
            clothes_dict[key].append(val)

    ans = 1
    for key in clothes_dict.keys():
        # 선택하는 경우 len(clothes_dict[key])
        # 0개를 선택하는 경우도 있으므로 + 1
        ans *= (len(clothes_dict[key]) + 1)

    # 아무것도 선택하지 않는 경우의 수가 추가되었으므로 -1
    return ans - 1


clothes1 = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes2 = [["crowmask", "face"], [
    "bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes2))
