"""booooo"""
def main():
    """oi oi oi baka"""
    word = input()
    counting = False
    total_u = 0
    max_u = 0
    if "BUU" in word.upper():
        for i in word.upper():
            if i == "B":
                counting = True
                total_u = 0
            elif counting is True and i == "U":
                total_u += 1
                if total_u > max_u:
                    max_u = total_u
            else:
                counting = False
        print("Yes", max_u)
    elif "B" in word or "b" in word :
        idx = max(word.rfind("B"), word.rfind("b"))
        new_txt = word[:idx + 1] + "U" * (len(word) - (idx + 1))
        print(new_txt)
    else:
        txt = ("BUU" * len(word))[: len(word)]
        print(txt)

main()
