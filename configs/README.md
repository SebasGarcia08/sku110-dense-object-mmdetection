# Models 

These models configs are provided from the following model [implementation](https://github.com/Media-Smart/SKU110K-DenseDet) 
of Cascade-R-CNN:

[DenseNet is the state-of-the-art model for SKU110 dataset so far.](https://paperswithcode.com/sota/dense-object-detection-on-sku-110k)


# Dataset configs

If you want to train, you should change the data[train] dictionary keys to point to the dataset images and annotations.

## Incompatibility issues

Why do exist "DenseDet_SKU_fusion_bfp_x101_32x4d_v1.py" and "DenseDet_SKU_fusion_bfp_x101_32x4d_v2.py"? 
Because "DenseDet_SKU_fusion_bfp_x101_32x4d_v1.py" is not compatible with the 2.x version of 
[mmdetection](https://github.com/open-mmlab/mmdetection/tree/master). Thus, "DenseDet_SKU_fusion_bfp_x101_32x4d_v2.py" 
should be used, because it is updated to the 2.x version of mmdetection.