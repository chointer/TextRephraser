from RephraseText.rephrase import Rephrase
from ToonCrafter.scripts.evaluation.inference import run_inference
import argparse

# [0] Inputs
# GPU
number_of_gpus = 1
rank_of_gpu = 0

# inputs
input_text = ""
input_image_pair = [None, None]

# params - rephrase
save_txt_path = "temp/rephrase.txt"
rephrase_style = 'objective'        # ['narrative', 'emotional', 'objective']
rephrase_length = 'maintain'        # ['compress', 'maintain', 'expand']
args_reph = argparse.Namespace(style=rephrase_style, length=rephrase_length, save_txt_path=save_txt_path, input_prompt=input_text)

# params - video generation
seed=123
ckpt_path="ToonCrafter/checkpoints/tooncrafter_512_interp_v1/model.ckpt"        # based on run.sh
config="ToonCrafter/configs/inference_512_v1.0.yaml"                            # based on run.sh
savedir="results/"                                                              # based on run.sh
n_samples=1
bs=1
height=320                                                                      # based on run.sh, 512: inference.py args default
width=512
unconditional_guidance_scale=7.5                                                # based on run.sh, 1.0: inference.py args default
ddim_steps=50
ddim_eta=1.0
prompt_dir=args_reph.save_txt_path
text_input=True                                                                 # based on run.sh, False: inference.py args default
video_length=16
frame_stride=10                                                                 # based on run.sh, 3: inference.py args default
timestep_spacing="uniform_trailing"                                             # based on run.sh, "uniform": inference.py args default
guidance_rescale=0.7                                                            # based on run.sh, 0.0: inference.py args default
perframe_ae=False
interp=True                                                                     # based on run.sh, False: inference.py args default

negative_prompt=False
multiple_cond_cfg=False
cfg_img=None
loop=False                                      ## currently not support looping video and generative frame interpolation

args_vid = argparse.Namespace(seed=seed, 
                              ckpt_path=ckpt_path, 
                              config=config, 
                              savedir=savedir, 
                              n_samples=n_samples, 
                              bs=bs, 
                              height=height, 
                              width=width, 
                              unconditional_guidance_scale=unconditional_guidance_scale,
                              ddim_steps=ddim_steps,
                              ddim_eta=ddim_eta,
                              prompt_dir=prompt_dir,
                              text_input=text_input,
                              video_length=video_length,
                              frame_stride=frame_stride,
                              timestep_spacing=timestep_spacing,
                              guidance_rescale=guidance_rescale,
                              perframe_ae=perframe_ae,
                              interp=interp,
                              negative_prompt=negative_prompt,
                              multiple_cond_cfg=multiple_cond_cfg,
                              cfg_img=cfg_img,
                              loop=loop
                              )


# [1] Rephrase
rephraser = Rephrase()
input_text_reph = (args_reph.input_text, args_reph.style, args_reph.length)
with open(args_reph.save_txt_path, "w") as f:
    f.write(input_text_reph)

# [2] ToonCrafter
run_inference(args_vid, number_of_gpus, rank_of_gpu)
# output is saved in "results/"