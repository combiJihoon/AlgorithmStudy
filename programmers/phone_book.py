def solution(phone_book):
    phone_book = sorted(phone_book)
    cur = phone_book[0]
    for phone in phone_book[1:]:
        if phone.startswith(cur):
            return False
        cur = phone

    return True


phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))
