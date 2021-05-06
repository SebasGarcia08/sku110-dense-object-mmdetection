import os
import pandas as pd
import json
import datetime
from argparse import ArgumentParser


def generate_coco_dataset(path):
    """
    Generates COCO annotations for SKU110 dataset
    :param path:
    :return:
    """
    # TODO: DEPRECATED method, Code refactoring to work with newer code pending
    df = pd.read_csv(path,
                     names=['img','x1','y1','x2','y2','class','imgw','imgh'])

    df["img_id"] = df['img'].apply(lambda s: s.split(".jpg")[0].split("_")[1])

    images = []
    annotations = []
    categories = []

    imgs_set = set()
    categories_ids_set = set()

    category2id = dict((category,id_) for id_,category in enumerate(df["class"].unique().tolist()))

    df['bboxh'] = df['y2']-df['y1']
    df['bboxw'] = df['x2']-df['x1']
    df["category_id"] = df["class"].apply(category2id.get)

    print("Generating tree...")
    for i, row in  df.iterrows():
        if row['category_id'] not in categories_ids_set:
            category_record = {
                'name': row['class'],
                'id': row['category_id'],
                'supercategory': 'none',
            }
            categories.append(category_record)
            categories_ids_set.add(row['category_id'])

        if row['img'] not in imgs_set:
            record = {
                'id': row['img_id'],
                'license': 0,
                'file_name': row['img'],
                'height': row['imgh'],
                'width': row['imgw'],
            }
            images.append(record)
            imgs_set.add(row['img'])

        annotation_record = {
            'id': i,
            'image_id': row['img_id'],
            'category_id': row['category_id'],
            'bbox': [row["x1"], row["y1"], row['bboxw'], row['bboxh']],
            'area': row['bboxh'] * row['bboxw'],
            'segmentation': [],
            'iscrowd': 0,
        }

        annotations.append(annotation_record)

    data_set = {
        'licenses': [
            {
                "id": 1,
                "url": "https://creativecommons.org/publicdomain/zero/1.0/",
                "name": "Public Domain"
            }
        ],
        "info": {
            "year": "2021",
            "version": "1",
            "description": "SKU 110 is an open-source dataset",
            "contributor": "Sebastián García Acosta",
            "url": "https://github.com/SebasGarcia08/",
            "date_created": datetime.datetime.utcnow().isoformat()
        },
        'images' : images,
        'annotations': annotations,
        'categories': categories,
    }
    return data_set


def run_labelling(dataset_dir="./"):
    for filename in os.listdir(dataset_dir):
        if filename.endswith(".csv"):
            path = f"{dataset_dir}{filename}"
            print(f"Generating json dataset for {path}")
            dataset = generate_coco_dataset(path)
            dest = f'{filename.split(".csv")[0]}.json'
            print(f"Writing json to {dest}")
            with open(dest, 'w') as fp:
                json.dump(dataset, fp, indent=4)


if __name__ == "__main__":
    parser = ArgumentParser()
    #TODO: Pending receive arguments from shell