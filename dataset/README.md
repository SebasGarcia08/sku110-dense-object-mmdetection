# SKU 110 dataset

We have 2940 images in the test set, 8232 images in the train set and 587 images in the validation set. Each image can have varying number of objects, hence, varying number of bounding boxes.

------------
    └── dataset
            └── images       <- Images folder
            │    │── train        <- 8232 test images with filenames "train_{image_number}.jpg"
            │    │── val        <- 587 val images with filenames "val_{image_number}.jpg"
            │    └── test         <- 2940 test images with filenames "test_{image_number}.jpg"
            │
            └── annotations       <- Annotations folder
                    │── csv        <- Original annotations in csv format. Contains: "train.csv", "test.csv" and "val.csv"
                    └── coco        <- Annotations in COCO format. Contains: "train.json", "test.json" and "val.json"
--------

## csv
The CSV columns are: image_name,x1,y1,x2,y2,class,image_width,image_height

x1 and y1 are top left coordinates
x2 and y2 are bottom right coordinates

## COCO 

You can learn more about COCO format [here](https://www.immersivelimit.com/tutorials/create-coco-annotations-from-scratch)
