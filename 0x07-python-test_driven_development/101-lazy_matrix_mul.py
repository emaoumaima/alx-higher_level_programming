#!/usr/bin/python3
"""
Module composed by a function that multiplies 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies two matrices using numpy

    Arguments:
        m_a, m_b: lists of lists of integers or floats

    Returns:
        A new matrix resulted from the multiplication of m_a and m_b
    """
    return (np.matmul(m_a, m_b))
