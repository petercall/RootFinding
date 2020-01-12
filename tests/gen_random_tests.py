import numpy as np
from random_tests import save_tests

degrees = {}
degrees[2] = np.arange(2,26)
degrees[3] = np.arange(2,11)
degrees[4] = np.arange(2,6)
degrees[5] = [2,3,4]
degrees[6] = [2,3]
degrees[7] = [2]
degrees[8] = [2]
degrees[9] = [2]
degrees[10] = [2]

N = {}
N[2] = 100
N[3] = 100
N[4] = 100
N[5] = 50
N[6] = 50
N[7] = 25
N[8] = 25
N[9] = 15
N[10] = 15

if __name__ == "__main__":

    for dim in np.arange(2,11):
        save_tests(dim,degrees[dim])
    # dimension 2
    degrees = np.arange(2,26)
    save_tests(2,degrees,100)

    # dimension 3
    degrees = np.arange(2,11)
    save_tests(3,degrees,50)

    # dimension 4
    degrees = np.arange(2,6)
    save_tests(4,degrees,25)

    # dimension 5
    save_tests(5,[2,3,4],15)

    # dimension 6
    save_tests(6,[2,3],15)

    # dimension 7
    save_tests(7,[2],15)

    # dimension 8
    save_tests(8,[2],10)

    # dimension 9
    save_tests(9,[2],10)

    # dimension 10
    save_tests(10,[2],10)