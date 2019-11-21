"""
Six Tests for Hypothetical Function line_intersect(l1, l2)

l1 and l2 are lists containing 2 floats, representing a line with 2 points on a grid. Function will check whether
the two lines are parallel, intersecting (and the point of intersection) or coincident.

1. two intersecting lines


2. two parallel lines
line_intersect([[-1.0, 2.0], [-3.0, -2.0]], [[1.0, 1.0], [-1.0, -3.0]])

3. two coincident lines
line_intersect([[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]])

4. lines that share one value (that will be the point of intersection)

5. lines with two equal points (dots)

6. negative numbers

"""