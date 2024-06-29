import pandas as pd
import os
import argparse

def print_model_results(file_name):
    """
    Reads a CSV file containing model results into a DataFrame, then prints two tables:
    1. General information about the dataset, including the total number of images, dog images, and not-a-dog images.
    2. Detailed CNN model results, including the architecture and accuracy metrics.
    
    Parameters:
    file_name (str): The path to the CSV file containing the model results.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_name)
    
    # Mapping of original column names to new names for general dataset information
    column_name_mapping = {
        'N Images': '# Total Images',
        'N Dog Images': '# Dog Images',
        'N Not-Dog Images': '# Not-a-Dog Images'
    }

    # Table 1: General information
    # Extract the columns for general information based on the mapping keys
    general_info_columns = list(column_name_mapping.keys())

    # Create a DataFrame with unique rows for general information
    general_info_df = df[general_info_columns].drop_duplicates().reset_index(drop=True)

    # Rename the columns according to the defined mapping
    general_info_df_renamed = general_info_df.rename(columns=column_name_mapping)

    # Print the general dataset information
    print("Dataset Information:")
    print(general_info_df_renamed.to_string(index=False))

    # Table 2: CNN model results
    # Assuming the column names in the CSV can be directly mapped to the desired names
    # Adjust the column names as per your CSV
    results_columns_mapping = {
        'Model': 'CNN Model Architecture',
        'pct_correct_notdogs': '% Not a Dog Correct',
        'pct_correct_dogs': '% Dogs Correct',
        'pct_correct_breed': '% Breeds Correct',
        'pct_match': '% Match Labels'
    }
    # Select and rename the columns according to the mapping
    results_df = df[list(results_columns_mapping.keys())].rename(columns=results_columns_mapping)
    # Print the detailed CNN model results
    print("\nResults:")
    print(results_df.to_string(index=False))

    # Delete the CSV file after printing the results
    os.remove(file_name)


if __name__ == "__main__":
    # Parse command line arguments for the CSV file name
    parser = argparse.ArgumentParser(description='Print model results from a CSV file.')
    parser.add_argument('file_name', type=str, help='The name of the CSV file to print.')

    args = parser.parse_args()

    # Call the function to print model results
    print_model_results(args.file_name)