import math
from twod_vectors import Vector2D

def run_vector_tests():
    print("=== 2D VECTOR TESTS ===\n")

    # Create some vectors
    v1 = Vector2D(3, 4)   # classic 3-4-5 triangle
    v2 = Vector2D(1, 2)
    v3 = Vector2D(-5, 6)

    print("Initial Vectors:")
    print("v1 =", v1)
    print("v2 =", v2)
    print("v3 =", v3, "\n")

    # Addition
    print("Addition:")
    print(f"{v1} + {v2} = {v1.add(v2)}")
    print(f"{v2} + {v3} = {v2.add(v3)}\n")

    # Subtraction
    print("Subtraction:")
    print(f"{v1} - {v2} = {v1.subtract(v2)}")
    print(f"{v2} - {v3} = {v2.subtract(v3)}\n")

    # Scalar Multiplication
    print("Scalar Multiplication:")
    print(f"{v1} * 3 = {v1.multiply(3)}")
    print(f"{v2} * -2 = {v2.multiply(-2)}\n")

    # Dot Product
    print("Dot Product:")
    print(f"{v1} · {v2} = {v1.dot(v2)}")
    print(f"{v2} · {v3} = {v2.dot(v3)}\n")

    # Magnitude
    print("Magnitude:")
    print(f"|{v1}| = {v1.magnitude()}")
    print(f"|{v3}| = {v3.magnitude()}\n")

    # String representations
    print("String Representations:")
    print("str(v1) =", str(v1))
    print("repr(v1) =", repr(v1))


if __name__ == "__main__":
    run_vector_tests()
