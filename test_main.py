# Test function created in main.py script

from main import mean_age, median_age, std_age, generate_histogram_age


def test_mean_age():
    result1 = mean_age()
    assert result1 is not None


def test_median_age():
    result2 = median_age()
    assert result2 is not None


def test_std_age():
    result3 = std_age()
    assert result3 is not None


def test_generate_histogram_age():
    # test if a plot is generated in output folder
    result_hist = generate_histogram_age()
    assert result_hist is None


if __name__ == "__main__":
    mean_age()
    median_age()
    std_age()
    generate_histogram_age()
