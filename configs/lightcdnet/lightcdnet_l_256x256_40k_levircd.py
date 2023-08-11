# -*- coding: utf-8 -*-
"""
@Time    : 2023/4/23/023 13:29
@Author  : NDWX
@File    : lightcdnet_l_256x256_40k_levircd.py
@Software: PyCharm
"""
_base_ = ['./lightcdnet_s_256x256_40k_levircd.py']

# model settings
norm_cfg = dict(type='BN', requires_grad=True)
model = dict(
    type='DIEncoderDecoder',
    pretrained=None,
    backbone=dict(
        type='LightCDNet',
        stage_repeat_num=[4, 8, 4],
        net_type="large"
    ),
    neck=dict(
        type='DS_FPN',
        in_channels=[24, 176, 352, 704],
        out_channels=48,
        num_outs=4),
    decode_head=dict(
        type='DS_FPNHead',
        in_channels=[48, 48, 48, 48],
        in_index=[0, 1, 2, 3],
        channels=48,
        dropout_ratio=0.,
        num_classes=2,
        norm_cfg=norm_cfg,
        align_corners=False,
        loss_decode=dict(
            type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0)),
    auxiliary_head=dict(
        type='FCNHead',
        in_channels=24,
        in_index=0,
        channels=24,
        num_convs=1,
        concat_input=False,
        dropout_ratio=0.,
        num_classes=2,
        norm_cfg=norm_cfg,
        align_corners=False,
        loss_decode=dict(
            type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
    # model training and testing settings
    train_cfg=dict(),
    test_cfg=dict(mode='whole'))