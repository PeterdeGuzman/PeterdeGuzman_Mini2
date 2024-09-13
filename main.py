# import packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os


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


def median_age(df):
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
    return result


def std_age(df):
    # calculate standard deviation of column with "age" in it
    age_column = [col for col in df.columns if "age" in col]
    if age_column:
        # Assuming there's only one age column in NC voter file data
        column_name = age_column[0]
        # Calculate the mean of the identified column
        result = df[column_name].std()
        return result
    else:
        result = print("No column containing 'age' found.")
    return result


def generate_histogram_age(df):
    age_column = [col for col in df.columns if "age" in col]
    plt.figure(figsize=(10, 6))
    bins = 6
    plt.hist(df[age_column], color="orange", bins=bins, edgecolor="black")
    plt.title("Age Distribution for Registered Voters in Durham County, NC")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.gca().yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"{int(x):,}")
    )
    filename = "output.png"
    output_folder = "output"
    filepath = os.path.join(output_folder, filename)
    plt.savefig(filepath)
    plt.show()
    plt.close()


# def save_histogram(filename="output.png", output_folder="output"):
#     filepath = os.path.join(output_folder, filename)
#     plt.savefig(filepath)
#     plt.close()
#     print(f"Histogram saved to {filepath}")


def main():
    df = read_csv_ncvoterdata(
        "/Users/pdeguz01/Documents/git/Data/durhamco_voterfile_sep2024/ncvoter32.txt"
    )
    # summary statistics
    print(mean_age(df))
    print(median_age(df))
    print(std_age(df))
    # generate histogram of age distribution
    generate_histogram_age(df)
    # write to output folder
    # save_histogram()


main()

# test
# df = read_csv_ncvoterdata(
#     "/Users/pdeguz01/Documents/git/Data/durhamco_voterfile_sep2024/ncvoter32.txt"
# )
# age_column = [col for col in df.columns if "age" in col]
# print(df[age_column])
# count_over_100 = (df[age_column] > 100).sum()
# print(count_over_100)
# # print(df)
