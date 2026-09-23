"""spacerrker"""
def main():
    """spacerbigger"""
    words = [input() for _ in range(5)]
    #ใส่ลูปรับตัวแปรเข้าไปในลิสเลยครับไอ้หน้าหี
    long = max(len(w) for w in words)
    #หาคำที่มีความยาวมากที่เลยในตัวแปรใหม่ด้วยลูปครับไอ้หน้าหี
    print("*" * (long + 4))
    #ใส่เพดาน
    for i in words:
        print(f"* {i:<{long}} *")
    #คลุมคำด้วยช่องว่างกับ*ด้วย (:<number, {ตัวแปร} มันคือf string method ไว้ใช้กำหนดว่าคำที่พิมมา
    # ต้องมีความยาวเท่าไหร่แล้วเติมด้วยช่องว่างถ้าขาด)
    print("*" * (long + 4))
    #ใส่พื้น

main()
