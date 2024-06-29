import pandas as pd
import os

def save_model_results(file_name, model, n_images, n_dogs_img, n_notdogs_img, results_stats_dic):
    """
    Saves the results of a model evaluation to a CSV file. If the file does not exist, it creates the file and writes
    the headers. If the file exists, it appends the new data without headers.
    
    Parameters:
    file_name (str): The name of the CSV file where results will be saved.
    model (str): The name of the model.
    n_images (int): The total number of images evaluated.
    n_dogs_img (int): The number of dog images in the dataset.
    n_notdogs_img (int): The number of non-dog images in the dataset.
    results_stats_dic (dict): A dictionary containing the results statistics, where keys starting with 'p' are considered.
    """
    # Create a DataFrame for the data
    data = {
        'Model': [model],
        'N Images': [n_images],
        'N Dog Images': [n_dogs_img],
        'N Not-Dog Images': [n_notdogs_img]
    }
    # Add results statistics to the data dictionary if the key starts with 'p'
    for key, value in results_stats_dic.items():
        if key.startswith('p'):
            data[key] = [value]
    
    # Convert the data dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Check if the file already exists to decide whether we need to write headers
    if os.path.isfile(file_name):
        # Append data without headers if the file exists
        df.to_csv(file_name, mode='a', header=False, index=False)
    else:
        # Write data with headers if the file does not exist
        df.to_csv(file_name, mode='w', header=True, index=False)