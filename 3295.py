"""Electric_Using"""
def main():
    """Electric_Using"""
    fire = int(input())
    if fire <= 10:
        cost = fire * 5
    elif fire <= 50:
        cost = 50 + (fire - 10) * 7
    elif fire <= 100:
        cost = 330 + (fire - 50) * 10
    elif fire <= 200:
        cost = 830 + (fire - 100) * 12
    else:
        cost = 2030 + (fire - 200) * 15
    vat = cost * 0.07
    ft = fire * 0.50
    total = cost + vat + ft
    print(f"{(total + 0.01):.1f}")

main()
