from rt_pie_lib import converters
import numpy as np


def test_1d():
    vector = np.ones(360)
    res = converters.convert_bin_to_local_average_cents_lowest_maxima(vector)
    print(res)


def test_2d():
    vector_2d = np.ones((10, 360))
    res = converters.convert_bin_to_local_average_cents_lowest_maxima(vector_2d)
    print(res)


def main():
    test_1d()
    test_2d()


if __name__ == "__main__":
    main()
