# import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
    return result


def std_age():
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


def generate_histogram_age():
    # create a histogram of age distribution
    return  # histogram, to be saved to an object?

def save_histogram(histogram, filename='output.png', output_folder='output'):




def save_histogram(data, filename='hist.png', output_folder='output'):
    """
    Creates a histogram from the provided data and saves it as a PNG file in the specified folder.

    Parameters:
    - data: List or array-like of numerical data to plot in the histogram.
    - filename: The name of the file to save the histogram as.
    - output_folder: The folder where the histogram image will be saved.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Create the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=20, edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    # Save the histogram to the specified folder
    filepath = os.path.join(output_folder, filename)
    plt.savefig(filepath)
    plt.close()

    print(f"Histogram saved to {filepath}")

def main():
    df = read_csv_ncvoterdata(
        "/Users/pdeguz01/Documents/git/Data/durhamco_voterfile_sep2024/ncvoter32.txt"
    )
    # summary statistics
    print(mean_age(df))
    print(median_age(df))
    print(std_age(df))
    # generate histogram of age distribution

    # write to output folder


main()

# generate mean, median, standard deviation

# plot

# plot distribution of age
# print(df.head())
