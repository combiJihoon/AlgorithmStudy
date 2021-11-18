def solution(n, words):
    words_dict = dict()
    prev = words[0]
    words_dict[words[0]] = 1

    turn, num = 1, 2
    for word in words[1:]:
        answer = [num, turn]
        if prev[-1] != word[0] or (word in words_dict):
            return answer

        words_dict[word] = 1
        prev = word

        if num == n:
            turn += 1
            num = 1
        else:
            num += 1

    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel",
      "land", "dream", "mother", "robot", "tank"]))
