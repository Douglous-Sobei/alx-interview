#!/usr/bin/python3

"""
contains the Pascal's Triangle function
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row [1]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1

        for j in range(1, i):
            # Each element (except the first and last) in a row is the sum of the two elements above it
            element = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(element)

        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
