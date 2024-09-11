# import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# define functions
def read_csv_ncvoterdata(voterdata):
    return pd.read_csv(voterdata, sep="\t", header=0, encoding="unicode_escape")


def mean_age(df):
    # calculate mean of column with "age" in it
    age_column = [col for col in df.columns if "age" in col]
    if age_column:
        # Assuming there's only one age column in NC voter file data
        column_name = age_column[0]
        # Calculate the mean of the identified column
        result = df[column_name].mean()
        return result
    else:
        result = print("No column containing 'age' found.")
    return result


def median_age():
    # calculate median of column with "age" in it
    age_column = [col for col in df.columns if "age" in col]
    if age_column:
        # Assuming there's only one age column in NC voter file data
        column_name = age_column[0]
        # Calculate the mean of the identified column
        result = df[column_name].median()
        return result
    else:
        result = print("No column containing 'age' found.")
    return  # pandas.median


def std_age():
    # calculate standard deviation of column with "age" in it
    age_column = [col for col in df.columns if "age" in col]
    if age_column:
        # Assuming there's only one age column in NC voter file data
        column_name = age_column[0]
        # Calculate the mean of the identified column
        result = df[column_name].median()
        return result
    else:
        result = print("No column containing 'age' found.")    return  # pandas.std


def generate_histogram_age():
    # create a histogram of age distribution
    return  # histogram, to be saved to an object?


def main():
    # do test
    df = read_csv_ncvoterdata(
        "/Users/pdeguz01/Documents/git/Data/durhamco_voterfile_sep2024/ncvoter32.txt"
    )
    print(mean_age(df))
    print(median_age(df))
    print(std_age(df))
    # summary statistics


main()

# generate mean, median, standard deviation

# plot

# plot distribution of age
# print(df.head())
