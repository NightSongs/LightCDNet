## Introduction

The Pytorch implementation for: "LightCDNet: Lightweight Change Detection Network Based on VHR Images" ([IEEE GRSL' 2023](https://ieeexplore.ieee.org/document/10214556))

![LightCDNet](https://github.com/NightSongs/LightCDNet/assets/73015485/d675eeca-665d-43ca-bbe5-9d744cc7d226)

## Abstract
LEVIR-CD
|      Method      | Crop Size | Lr schd | \#Param (M) | MACs (G) | Precision | Recall | F1-Score |  IoU  |
| :--------------: | :-------: | :-----: | :---------: | :------: | :-------: | :----: | :------: | :---: |
| LightCDNet-small |  256x256  |  40000  |    0.35     |   1.65   |   91.36   | 89.81  |  90.57   | 82.77 |
| LightCDNet-base  |  256x256  |  40000  |    1.32     |   3.22   |   92.12   | 90.43  |  91.27   | 83.94 |
| LightCDNet-large |  256x256  |  40000  |    2.82     |   5.94   |   92.43   | 90.45  |  91.43   | 84.21 |

## Notice

The code is being sorted out, and it will be integrated in [Open-CD](https://github.com/likyoo/open-cd/tree/main) later, so stay tuned!

## Environment installation

This project is implemented based on Open-CD, please refer to the installation method of [Open-CD](https://github.com/likyoo/open-cd/tree/main) 0.x version.

## Usage

(eg: LightCDNet-small)

Train:
```
python tools/train.py configs/lightcdnet/lightcdnet_s_256x256_40k_levircd.py --work-dir ./exp/lightcdnet_s_levir_workdir --gpu-id 0 --seed 602
```

Eval:

```
python tools/test.py configs/lightcdnet/lightcdnet_s_256x256_40k_levircd.py ./exp/lightcdnet_s_levir_workdir/latest.pth --eval mFscore mIoU
```

Visualization:

```
python tools/test.py configs/lightcdnet/lightcdnet_s_256x256_40k_levircd.py ./exp/lightcdnet_s_levir_workdir/latest.pth --format-only --eval-options "imgfile_prefix=tmp_infer"
```

## Citation

If you find this project useful in your research, please consider cite:
```
@ARTICLE{10214556,
  author={Xing, Yuanjun and Jiang, Jiawei and Xiang, Jun and Yan, Enping and Song, Yabin and Mo, Dengkui},
  journal={IEEE Geoscience and Remote Sensing Letters}, 
  title={LightCDNet: Lightweight Change Detection Network Based on VHR Images}, 
  year={2023},
  volume={},
  number={},
  pages={1-1},
  doi={10.1109/LGRS.2023.3304309}}
```
(We will supplement the citation information after the official publication of the article.)
