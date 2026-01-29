# Geometry utilities for transformations and calculations

import numpy as np


def distance_point_to_line_segment(point, line_start, line_end):
    # Calculate minimum distance from a point to a line segment
    # TODO: Implement
    pass


def heading_between_points(p1, p2):
    # Calculate heading angle (radians) from p1 to p2
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return np.arctan2(dy, dx)


def transform_points(points, translation, rotation):
    # Apply 2D transformation (translation + rotation) to a set of points
    # TODO: Implement
    pass
