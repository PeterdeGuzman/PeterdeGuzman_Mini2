# Test function created in main.py script

from main import mean_age, median_age, std_age, generate_histogram_age
import os
import numpy as np
import pandas as pd

num_rows = 100
data = pd.DataFrame(
    {
        "RowID": np.random.randint(0, 201, size=num_rows),
        "age": np.random.randint(18, 102, size=num_rows),
    }
)


def test_mean_age(data):
    result1 = mean_age(data)
    assert 18 <= result1 <= 65


def test_median_age(data):
    result2 = mean_age(data)
    assert 18 <= result2 <= 65


def test_std_age(data):
    result3 = std_age(data)
    assert 10 <= result3 <= 25


def test_generate_histogram_age(data):
    result4 = generate_histogram_age(data)
    assert result4 is None


if __name__ == "__main__":
    test_mean_age(data)
    test_median_age(data)
    test_std_age(data)
    test_generate_histogram_age(data)
