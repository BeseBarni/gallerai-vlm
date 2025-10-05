# %%
import kagglehub
import pandas as pd
import numpy as np
import os

def load_ava_dataset():
    """
    Loads the AVA dataset and returns paths and dataframes.
    
    Returns:
        dict: Contains 'df', 'tag_map', 'images_path', 'dataset_path'
    """

    dataset_handle="nicolacarrassi/ava-aesthetic-visual-assessment"

    dataset_path = kagglehub.dataset_download(dataset_handle)
    ava_folder_path = f"{dataset_path}/AVA_Files"
    images_path = os.path.join(dataset_path, 'images')
    ava_path = os.path.join(ava_folder_path, 'AVA.txt')
    tags_path = os.path.join(ava_folder_path, 'tags.txt')
    
    # Load tag map
    tag_map = {}
    with open(tags_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            tag_map[int(parts[0])] = parts[1].strip()
    
    # Load AVA data
    ava_columns = ['index', 'image_id'] + [f'votes_{i}' for i in range(1, 11)] + \
                  ['tag_1', 'tag_2', 'challenge_id']
    df = pd.read_csv(ava_path, sep=' ', header=None, names=ava_columns)
    
    return df, tag_map, images_path
# %%
def get_processed_dataset():
    df, tag_map,images_path = load_ava_dataset()

    vote_columns = [f"votes_{i}" for i in range(1,11)]
    ratings = np.arange(1, 11)
    df['mean_score'] = df[vote_columns].apply(
        lambda row: np.average(ratings, weights=row), 
        axis=1
    ).round(2)
    df = df.drop(columns=vote_columns)
    df['tag_1'] = df['tag_1'].map(tag_map)
    df['tag_2'] = df['tag_2'].map(tag_map)

    df['categories'] = df[['tag_1','tag_2']].apply(lambda x : ', '.join(x.dropna()), axis=1)
    df = df.drop(columns=['tag_1', 'tag_2'])
    df['image_path'] = df['image_id'].apply(lambda x : f"{images_path}/{x}")
    df = df.drop(columns=['image_id', 'challenge_id'])

    return df
# %%
