import numpy as np
from groebner.multi_cheb import MultiCheb
from groebner.multi_power import MultiPower
from groebner.convert_poly import poly2cheb, cheb2poly
import pytest
import pdb
import random


def test_add():
    """Test Multivariate Chebyshev polynomial addition."""
    t = np.arange(27).reshape((3,3,3))
    poly1 = MultiCheb(t)
    poly2 = MultiCheb(np.ones((3,3,3)))
    S = poly1 + poly2 # the sum of the polynomials
    result = (S.coeff == (poly1.coeff + poly2.coeff))
    assert result.all()

<<<<<<< HEAD
def test_mult():
    """Test Multivariate Chebyshev polynomial multiplication."""
    test1 = np.array([[0,1],[2,1]])
    test2 = np.array([[2,2],[3,0]])
    cheb1 = MultiCheb(test1)
    cheb2 = MultiCheb(test2)
    new_cheb = cheb1*cheb2
    truth = MultiCheb(np.array([[4, 3.5, 1],[5,9,1],[3,1.5,0]]))
    assert np.allclose(new_cheb.coeff, truth.coeff)
"""
def test_mult_diff():
    '''
    Test Multivariate Chebyshev polynomial multiplication.
    Test implementation with different shape sizes
    '''
    c1 = MultiCheb(np.arange(0,4).reshape(2,2))
    c2 = MultiCheb(np.ones((2,1)))
    p = c1*c2
    truth = MultiCheb(np.array([[1,2.5,0],[2,4,0],[1,1.5,0]]))
    assert np.allclose(p.coeff,truth.coeff)
"""

=======
>>>>>>> 31746bd7c94315f0cfa00bcfe2784160c46b31e4
def test_mon_mult():
    """
    Tests monomial multiplication using normal polynomial multiplication.
    """

    #Simple 2D test cases
    cheb1 = MultiCheb(np.array([[0,0,0],[0,0,0],[0,0,1]]))
    mon1 = (1,1)
    result1 = cheb1.mon_mult(mon1)
    truth1 = np.array([[0,0,0,0],[0,0.25,0,0.25],[0,0,0,0],[0,0.25,0,0.25]])

    assert np.allclose(result1.coeff, truth1)



    #test with random matrices
    cheb2 = np.random.randint(-9,9, (4,4))
    C1 = MultiCheb(cheb2)
    C2 = cheb2poly(C1)
    C3 = MultiCheb.mon_mult(C1, (1,1))
    C4 = MultiPower.mon_mult(C2, (1,1))
    C5 = poly2cheb(C4)

    assert np.allclose(C3.coeff, C5.coeff)

    # test results of chebyshev mult compared to power multiplication
    cheb3 = np.random.randn(5,4)
    c1 = MultiCheb(cheb3)
    c2 = MultiCheb(np.ones((4,2)))
    for index, i in np.ndenumerate(c2.coeff):
        if sum(index) == 0:
            c3 = c1.mon_mult(index)
        else:
            c3 = c3 + c1.mon_mult(index)
    p1 = cheb2poly(c1)
    p2 = cheb2poly(c2)
    p3 = p1*p2
    p4 = cheb2poly(c3)
    assert np.allclose(p3.coeff, p4.coeff)

    # test results of chebyshev mult compared to power multiplication in 3D
    cheb4 = np.random.randn(3,3,3)
    a1 = MultiCheb(cheb4)
    a2 = MultiCheb(np.ones((3,3,3)))
    for index, i in np.ndenumerate(a2.coeff):
        if sum(index) == 0:
            a3 = a1.mon_mult(index)
        else:
            a3 = a3 + a1.mon_mult(index)
    q1 = cheb2poly(a1)
    q2 = cheb2poly(a2)
    q3 = q1*q2
    q4 = cheb2poly(a3)
    assert np.allclose(q3.coeff, q4.coeff)

def test_evaluate_at():
    cheb = MultiCheb(np.array([[0,0,0,1],[0,0,0,0],[0,0,1,0]]))
    value = cheb.evaluate_at((2,5))
    assert(value == 828)

    value = cheb.evaluate_at((.25,.5))
    assert(np.isclose(value, -.5625))

def test_evaluate_at2():
    cheb = MultiCheb(np.array([[0,0,0,1],[0,0,0,0],[0,0,.5,0]]))
    value = cheb.evaluate_at((2,5))
    assert(np.isclose(value, 656.5))
