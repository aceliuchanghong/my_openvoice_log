# 本机测试
import os
import torch
import se_extractor
from api import BaseSpeakerTTS, ToneColorConverter
from task import config

ckpt_config_base = config.ckpt_config_base
ckpt_pth_base = config.ckpt_pth_base
ckpt_config_converter = config.ckpt_config_converter
ckpt_pth_converter = config.ckpt_pth_converter
ckpt_pth2_base = config.ckpt_pth2_base
device = 'cuda:0'
output_dir = 'testfile/out'

base_speaker_tts = BaseSpeakerTTS(ckpt_config_base, device=device)
base_speaker_tts.load_ckpt(ckpt_pth_base)

tone_color_converter = ToneColorConverter(ckpt_config_converter, device=device)
tone_color_converter.load_ckpt(ckpt_pth_converter)

os.makedirs(output_dir, exist_ok=True)
source_se = torch.load(ckpt_pth2_base).to(device)
