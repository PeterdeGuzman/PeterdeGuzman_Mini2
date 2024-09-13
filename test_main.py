# Test function created in main.py script

from main import read_csv_ncvoterdata, mean_age, median_age, std_age
import os

df = read_csv_ncvoterdata(
    "/Users/pdeguz01/Documents/git/Data/durhamco_voterfile_sep2024/ncvoter32.txt"
)


def test_mean_age(df):
    result1 = mean_age(df)
    assert result1 is not None


def test_median_age(df):
    result2 = median_age(df)
    assert result2 is not None


def test_std_age(df):
    result3 = std_age(df)
    assert result3 is not None


def test_histogram_output():
    # test if a plot is generated in output folder
    filename = "output.png"
    output_folder = "output"
    filepath = os.path.join(output_folder, filename)
    if not filepath:
        raise FileNotFoundError(
            f"The directory {filepath} to store the histogram does not exist."
        )
    for file_name in filepath:
        if file_name.lower().endswith("png"):
            return True
    return False


if __name__ == "__main__":
    test_mean_age(df)
    test_median_age(df)
    test_std_age(df)
    test_histogram_output()
