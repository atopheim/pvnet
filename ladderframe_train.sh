#!/bin/bash

python tools/train_homemade_render.py --cfg_file configs/homemade_train.json --homemade_cls ladderframe --batch_size 32 --no-occluded --no-truncated



