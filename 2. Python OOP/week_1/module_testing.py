import unittest


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        self.error = ('string', 1.5)
        for err in self.error:
            with self.subTest(err=err):
                self.assertRaises(TypeError, factorize, err)

    def test_negative(self):
        self.error = (-1, -10, -100)
        for err in self.error:
            with self.subTest(err=err):
                self.assertRaises(ValueError, factorize, err)

    def test_zero_and_one_cases(self):
        self.error = (0, 1)
        for err in self.error:
            with self.subTest(err=err):
                self.assertTupleEqual(factorize(err), (err,))

    def test_simple_numbers(self):
        self.error = (3, 13, 29)
        for err in self.error:
            with self.subTest(err=err):
                self.assertTupleEqual(factorize(err), (err,))

    def test_two_simple_multipliers(self):
        self.error = (6, 26, 121)
        value = ((2, 3), (2, 13), (11, 11))
        for i, err in enumerate(self.error):
            with self.subTest(err=err):
                self.assertTupleEqual(factorize(err), value[i])

    def test_many_multipliers(self):
        self.error = (1001, 9699690)
        value = ((7, 11, 13), (2, 3, 5, 7, 11, 13, 17, 19))
        for i, err in enumerate(self.error):
            with self.subTest(err=err):
                self.assertTupleEqual(factorize(err), value[i])


# if __name__ == '__main__':
#     unittest.main()
