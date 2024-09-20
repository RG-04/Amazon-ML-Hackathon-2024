from src.utils import download_images
import pandas as pd
import sys
sys.path.append('src')

for dataset in ["train", "test"]:
    df = pd.read_csv(f"./dataset/{dataset}.csv")
    df = df.iloc[:10]
    download_images(df["image_link"], f"./images/{dataset}/", True)