"""booooo"""
def main():
    """oi oi oi baka"""
    word = input()
    total_u = 0
    max_u = 0
    for i in word.upper():
        if i == "B":
            total_u = 0
        elif i == "U":
            total_u += 1
        if total_u > max_u:
            max_u = total_u
    if max_u >= 2:
        print("Yes", max_u)
    elif "B" in word.upper():
        idx = word.upper().rfind("B")
        new_txt = word[:idx + 1] + "U" * (len(word) - (idx + 1))
        print(new_txt)
    else:
        txt = ("BUU" * len(word))[: len(word)]
        print(txt)

main()
