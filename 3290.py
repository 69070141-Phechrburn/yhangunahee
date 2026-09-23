"""frick you arrow"""
def main():
    """**k**u**y**"""
    lenght = int(input())
    line = int(input())
    wings = line // 2
    for i in range(-wings, wings + 1):
        print(" " * abs(i) + "*" * lenght)

main()
