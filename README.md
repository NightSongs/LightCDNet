The Pytorch implementation for: "LightCDNet: Lightweight Change Detection Network Based on VHR Images"

![LightCDNet](https://github.com/NightSongs/LightCDNet/assets/73015485/93b8171f-4d12-4232-af3b-a5452c50b4e4)

The code is being sorted out, and it will be integrated in [Open-CD](https://github.com/likyoo/open-cd/tree/main) later, so stay tuned!

[Early Access](https://ieeexplore.ieee.org/document/10214556)

train(Example: LightCDNet-small)
```
python tools/train.py configs/lightcdnet/lightcdnet_s_256x256_40k_levircd.py --work-dir ./exp/lightcdnet_s_levir_workdir --gpu-id 0 --seed 602
```
