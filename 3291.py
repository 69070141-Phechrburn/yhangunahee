"""frick you arrow"""
def main():
    """**k**u**y**"""
    lenght = int(input())
    line = int(input())
    pra_aek = line // 2
    for i in range(-pra_aek, pra_aek + 1):
        spaces = pra_aek - abs(i)
        print(" " * spaces + "*" * lenght)

main()
