"""classsroom"""
def main():
    """classermixser"""
    c, t = int(input()), int(input())
    total_t = c * t
    if not total_t:
        print("No teaching")
    else:
        hours = total_t // 60
        minuts = total_t % 60
        if not hours:
            print(f"{minuts} minute")
        elif not minuts:
            print(f"{hours} hours")
        else:
            print(f"{hours} hours {minuts} minute")

main()
