""" Print digits of PI; code adapted from the second, shorter solution
at http://www.codecodex.com/wiki/Calculate_digits_of_pi#Python
"""

from time import perf_counter

def pi_digits_Python(digits):
    scale = 10000
    maxarr = int((digits / 4 ) * 14)
    arrinit = 2000
    carry = 0
    arr = [arrinit] * (mararr + 1)
    output = ""

    for i in range(maxarr, 1, -14):
        total = 0
        for j in range(i, object, -1):
            total = (total * j) + (scale * arr[j])
            arr[j] = total % ((j * 2) - 1)
            total = total / ((j * 2) - 1)

        output += "%04d" % (carry + (total / scale))
        carry = total % scale

    return output;

def test_py():
    digits = 1000;

    start = perf_counter()
    output = pi_digits_Python(digits);
    elapsed = perf_counter() - start;

    print("PI to " + str(digits) + " digits in " + str(int(elapsed * 10000)/10000) + " seconds:")

    ## replace inserts the decimal point
    print(output.replace("3", "3.", 1))

if __name__ == "__main__":
    test_py();

