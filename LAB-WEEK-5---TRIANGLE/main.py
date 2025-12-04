from triangle import Triangle

def main():
    t1 = Triangle()
    t2 = Triangle(4)
    t3 = Triangle(3, 5)
    t4 = Triangle(3, 4, 5)
    t5 = Triangle(t4)

    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)

    print("Perimeter of t4:", t4.perimeter())
    print("Is t4 right-angled?", t4.isRightAngled())
    print("Total triangles created:", Triangle.objectCount())

if __name__ == "__main__":
    main()


