"""ticketdickywicky"""
def main():
    """ticketdickywicky"""
    seat = int(input())
    total_cost = 0
    while seat > 0:
        age, ticket = map(int, input().split(" "))
        cost = 150
        if 15 <= age <= 22:
            cost = cost - (cost * 0.2)
        elif age >= 60:
            cost = cost / 2
        elif 22 < age < 60:
            pass
        else:
            print(-1)
            continue
        if seat < ticket:
            print(-2)
            continue
        total_cost = cost * ticket
        seat -= ticket
        print(round(total_cost), seat)

main()
