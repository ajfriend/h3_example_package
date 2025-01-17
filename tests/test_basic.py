import numpy as np
from h3_example_package.geo import latlng_to_cell_vect


def test_cython_api():
    N = 100000
    np.random.seed(0)

    lats, lngs = np.random.uniform(0, 90, N), np.random.uniform(0, 90, N)
    res = 9

    lats = np.array(lats, dtype=np.float64)
    lngs = np.array(lngs, dtype=np.float64)
    out = np.zeros(len(lats), dtype='uint64')
    latlng_to_cell_vect(lats, lngs, res, out)

    assert out[0] == 617284541015654399
