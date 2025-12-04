from dimensional import Vector

if __name__ == "__main__":
    v = Vector(5)
    v[1] = 46
    v[-1] = 90
    print("v:", v)   # <0, 46, 0, 0, 90>

    u = Vector(5)
    u[1] = 1
    u[2] = 2
    print("u:", u)   # <0, 1, 2, 0, 0>

    # Vector + Vector
    w = u + v
    print("u + v =", w)  # <0, 47, 2, 0, 90>

    # Vector + list
    z = u + [5, 3, 10, -2, 1]
    print("u + [5,3,10,-2,1] =", z)  # <5, 4, 12, -2, 1>

    # Equality
    print("u == v ?", u == v)
    print("u != v ?", u != v)

    # Iteration & len
    print("Length of v:", len(v))
    print("Sum of v:", sum(v))
