# TextRephraser
This project aims to generate videos from text and images with text rephrasing. [ToonCrafter](https://github.com/Doubiiu/ToonCrafter/tree/main) is used as the video generation model, which creates videos by interpolating frames between the first and last frames. Text rephrasing is performed using [ollama](https://github.com/ollama/ollama) with the [Llama 3.2](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md) model.

Prompts play an important role in video generation models. To enhance the quality of the generated videos, I tried manipulating the style and length of prompts. 

The inspiration for this approach came from 'Diversity is all you need (DIAYN)'*, a search algorithm in reinforcement learning that seeks to discover a various of strategies. Although it idffers from DIAYN, focusing on diversity, I took a different approach by manually designing and testing a variety of strategies.

This project is one of the individial projects conducted as part of [Pseudo-Lab 9th - 모여봐요 강화학숲](https://github.com/Pseudo-Lab/9th-together-RL). 

_\* Eysenbach, Benjamin, et al. "Diversity is all you need: Learning skills without a reward function." arXiv preprint arXiv:1802.06070 (2018)._
<br/><br/>

## Setup
  ```bash
  conda create -n rephraser python=3.10
  conda activate rephraser
  git clone https://github.com/chointer/TextRephraser.git
  cd TextRephraser
  pip install -r requirments.txt
  ```
<br/>

## Usage - Rephraser
  ```python
  from RephraseText import Rephrase

  # Initialize
  rephrase = Rephrase()

  # Input and setup
  input_prompt = "I found a book in his dark room."
  style = "narrative"      # Choose from "narrative", "emotional", "objective"
  length = "compress"      # Choose from "compress", "maintain", "expand"

  # Perform rephrasing
  output = rephrase(input_prompt, style, length)
  ```
<br/>

##  Usage - Video Generation with Rephrasing
