# import packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os


# define functions
def read_csv_ncvoterdata(voterdata):
    return pd.read_csv(
        voterdata, sep="\t", header=0, encoding="unicode_escape", low_memory=False
    )


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

    plt.savefig("output.png")
    # plt.show()


def save_to_markdown(df):
    """save summary report to markdown"""
    # Write the markdown table to a file
    with open("tyrellco_voter.md", "w", encoding="utf-8") as file:
        file.write("Mean Age of Sample of Registered Voters in Tyrell County\n")
        file.write("mean_age(df)")
        file.write("\n\n")  # Add a new line
        file.write("Median Age of Sample of Registered Voters in Tyrell County\n")
        file.write("median_age(df)")
        file.write("\n\n")  # Add a new line
        file.write("Standard Deviation of Age of Registered Voters in Tyrell County\n")
        file.write("std_age(df)")
        file.write("\n\n")  # Add a new line
        file.write("!/output/output.png\n")


def main():
    # load data
    df = read_csv_ncvoterdata("ncvoter89.txt")
    # summary statistics
    print(mean_age(df))
    print(median_age(df))
    print(std_age(df))
    # generate histogram of age distribution
    # and save to output folder
    generate_histogram_age(df)
    save_to_markdown(df)


main()
