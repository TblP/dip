_base_ = '../base/crowdhuman_1x_setting.py'

model = dict(
    type='ATSS',
    backbone=dict(
        type='ResNet',
        depth=50,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=-1,
        norm_cfg=dict(type='BN', requires_grad=False),
        norm_eval=True,
        style='pytorch',
        init_cfg=dict(type='Pretrained', checkpoint='data/pretrain_models/resnet50-0676ba61.pth')),
    neck=dict(
        type='FPN',
        in_channels=[256, 512, 1024, 2048],
        out_channels=256,
        start_level=1,
        add_extra_convs='on_output',
        num_outs=5),
    bbox_head=dict(
        type='DDOD_Distill_Head',
        num_classes=1,
        in_channels=256,
        stacked_convs=4,
        feat_channels=256,
        anchor_generator=dict(
            type='AnchorGenerator',
            ratios=[1.0],
            octave_base_scale=8,
            scales_per_octave=1,
            strides=[8, 16, 32, 64, 128]),
        bbox_coder=dict(
            type='DeltaXYWHBBoxCoder',
            target_means=[.0, .0, .0, .0],
            target_stds=[0.1, 0.1, 0.2, 0.2]),
        loss_cls=dict(
            type='FocalLoss',
            use_sigmoid=True,
            gamma=2.0,
            alpha=0.25,
            loss_weight=1.0),
        loss_bbox=dict(type='GIoULoss', loss_weight=2.0),
        loss_iou=dict(
            type='CrossEntropyLoss', use_sigmoid=True, loss_weight=1.0),
        identity_pos=0),
    # training and testing settings
    train_cfg=dict(
        assigner=dict(type='DDODTopkAssigner', topk=9, alpha=0.8, is_atss=False),
        reg_assigner=dict(type='DDODTopkAssigner', topk=9, alpha=0.6, is_atss=False),
        kd_assigner=dict(
            cls_assigner=dict(
                type='GaussianMLEWeightCalculator',
                topk=30,
                alpha=0.8,
                low_bound=0.),
            reg_assigner=dict(
                type='GaussianMLEWeightCalculator',
                topk=30,
                alpha=0.6,
                low_bound=0.)),
        allowed_border=-1,
        pos_weight=-1,
        debug=False),
    test_cfg=dict(
        nms_pre=1000,
        min_bbox_size=0,
        score_thr=0.05,
        nms=dict(type='nms', iou_threshold=0.6),
        max_per_img=500))


work_dir = 'work_dirs/crowd_ddod_r50_1x'

