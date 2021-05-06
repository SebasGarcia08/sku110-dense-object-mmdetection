# Data

This module was created with the purpose of convert raw annotations from original SKU-110 dataset into a COCO standard 
format. This is why it expected a directory "images" where all train, test, and validation images are and 
another directory "annotations" that contains CSV files with annotations as described [here](https://github.com/SebasGarcia08/sku110-dense-object-mmdetection/tree/develop/dataset/README.md).
The output of this script is the creation of train.json, test.json and val.json, the annotations in COCO format.

Because it is not required anymore, will be deleted in the next commits.