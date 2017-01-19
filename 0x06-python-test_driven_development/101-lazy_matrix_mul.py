#!/usr/bin/python3
"""
This is the 101-lazy_matrix_mul module

matrix multiplication with NumPy
This module contains only one function 101-lazy_matrix_mul

A test suite has been created for that file in the ./tests directory
you can run it with python3 -m doctest ./tests/101-lazy_matrix_mul.txt
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiply matrixes with numpy

    Arguments:
        m_a: must be a matrix of numbers
        m_b: must be a matrix of numbers

    Returns:
        a matrix, the product of the arguments
    """
    a_np = np.matrix(m_a)
    b_np = np.matrix(m_b)

    p_np = a_np * b_np

    return (p_np)
