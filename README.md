## Introduction

The Pytorch implementation for: "LightCDNet: Lightweight Change Detection Network Based on VHR Images" (IEEE GRSL' 2023)

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

[Early Access](https://ieeexplore.ieee.org/document/10214556) (We will add citation information after official publication.)