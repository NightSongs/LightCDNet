# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/28/028 15:01
@Author  : NDWX
@File    : lightcdnet_s_256x256_40k_levircd.py
@Software: PyCharm
"""
_base_ = [
    '../_base_/models/lightcdnet.py', '../common/standard_256x256_40k_levircd.py'
]

crop_size = (256, 256)
model = dict(
    decode_head=dict(
        num_classes=2,
        sampler=dict(type='OHEMPixelSampler', thresh=0.7, min_kept=100000)),
)

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='MultiImgLoadImageFromFile'),
    dict(type='MultiImgLoadAnnotations'),
    dict(type='MultiImgRandomRotate', prob=0.5, degree=180),
    dict(type='MultiImgRandomCrop', crop_size=(256, 256)),
    dict(type='MultiImgRandomFlip', prob=0., direction='horizontal'),
    dict(
        type='MultiImgPhotoMetricDistortion',
        brightness_delta=10,
        contrast_range=(0.8, 1.2),
        saturation_range=(0.8, 1.2),
        hue_delta=10),
    dict(type='MultiImgNormalize', **img_norm_cfg),
    dict(type='MultiImgDefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_semantic_seg']),
]
test_pipeline = [
    dict(type='MultiImgLoadImageFromFile'),
    dict(
        type='MultiImgMultiScaleFlipAug',
        img_scale=(1024, 1024),
        # img_ratios=[0.75, 1.0, 1.25],
        flip=False,
        transforms=[
            dict(type='MultiImgResize', keep_ratio=True),
            dict(type='MultiImgRandomFlip'),
            dict(type='MultiImgNormalize', **img_norm_cfg),
            dict(type='MultiImgImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=8,
    workers_per_gpu=4,
    train=dict(
        img_dir='train',
        ann_dir='train/label',
        pipeline=train_pipeline),
    val=dict(
        img_dir='val',
        ann_dir='val/label',
        pipeline=test_pipeline),
    test=dict(
        img_dir='test',
        ann_dir='test/label',
        pipeline=test_pipeline))

log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook', by_epoch=False),
        dict(type='TensorboardLoggerHook')
    ])

# optimizer
optimizer = dict(
    _delete_=True,
    type='AdamW',
    lr=0.003,
    betas=(0.9, 0.999),
    weight_decay=0.05)

runner = dict(type='IterBasedRunner', max_iters=40000)
checkpoint_config = dict(by_epoch=False, interval=4000)
evaluation = dict(interval=4000, metric=['mFscore', 'mIoU'], pre_eval=True, save_best='Fscore.changed',
                  greater_keys=['Fscore'])
