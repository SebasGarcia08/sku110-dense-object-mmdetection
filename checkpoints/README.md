# Model weights

These models weights are provided from the following model [implementation](https://github.com/Media-Smart/SKU110K-DenseDet) 
of Cascade-R-CNN:

[DenseNet is the state-of-the-art model for SKU110 dataset so far.](https://paperswithcode.com/sota/dense-object-detection-on-sku-110k)


## Incompatibility issues

Why do exist "DenseDet_SKU_fusion_bfp_x101_32x4d_v1.pth" and "DenseDet_SKU_fusion_bfp_x101_32x4d_v2.pth."? 
Because "DenseDet_SKU_fusion_bfp_x101_32x4d_v1.pth" is not compatible with the 2.x version of 
[mmdetection](https://github.com/open-mmlab/mmdetection/tree/master). Thus, "DenseDet_SKU_fusion_bfp_x101_32x4d_v2.pth" 
should be used, because it is updated to the 2.x version of mmdetection via a utility function.