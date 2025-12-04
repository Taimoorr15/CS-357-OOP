What is a Multidimensional Vector?

A vector is an ordered collection of numbers that can represent points, directions, or magnitudes in space.

A 1D vector is just a number line value, e.g. ⟨3⟩.

A 2D vector has two components, e.g. ⟨3, 4⟩ (like coordinates on a plane).

A 3D vector has three components, e.g. ⟨3, 4, 5⟩ (like coordinates in 3D space).

An N-dimensional vector generalizes this idea to any number of dimensions:
⟨x₁, x₂, …, xₙ⟩.

⚡ Why are N-dimensional vectors useful?

Mathematics: Represent solutions to equations, transformations, and geometric objects.

Computer Science: Store data, machine learning feature vectors, graphics (position, velocity, color channels, etc.).

Physics: Describe forces, velocities, and higher-dimensional state spaces.

🐍 In Python (this project)

This project implements a Vector class that can create, manipulate, and operate on vectors in any dimension (n).

Features:

Create an N-dimensional vector of zeros: v = Vector(5) → ⟨0,0,0,0,0⟩

Indexing & updating: v[2] = 10

Vector addition: u + v

Equality/inequality: u == v, u != v

String output: print(v) → <0, 10, 0, 0, 5>

Works with lists and tuples as well (polymorphic addition).
