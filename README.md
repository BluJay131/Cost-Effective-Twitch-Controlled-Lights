# Cost Effective Twitch Chat Controlled Lights
[![Official Website](https://img.shields.io/badge/Official%20Website-blujay131.com-blue?style=flat&logo=world&logoColor=white)](https://blujay131.com/)
[![Socials](https://img.shields.io/badge/Socials-linktr.ee/blujay131-purple?style=flat&logo=world&logoColor=white)](https://linktr.ee/blujay_131)
[![GitHub Repo stars](https://img.shields.io/github/stars/BluJay131/Cost-Effective-Twitch-Chat-Controlled-Lights?style=social)](https://github.com/BluJay131/Cost-Effective-Twitch-Chat-Controlled-Lights/stargazers)

<hr/>

### ![image](https://github.com/BluJay131/Cost-Effective-Twitch-Controlled-Lights/assets/80910384/346dc2a9-45f3-4372-8e4c-de62a3bc5e3f) Make sure to use ChatLightsV2.py for the latest code and quality of life.

** (Youtube video coming)

## Description

This repository contains a Python script that enables the creation of a Twitch bot capable of controlling an RGB LED through commands from the Twitch chat. The script interfaces with an Arduino board via the `pyfirmata` library and manages Twitch interactions using the `twitchio` library.

## Prerequisites

- Python 3.x
- Arduino board (tested with a pro micro atmega32u4)
- RGB LED Strip Controller (tested with <a target="_blank" href="https://www.amazon.com/Lights-ehomful-Changing-Bedroom-Decoration/dp/B089YPWZKY?pd_rd_w=1UL1g&amp;content-id=amzn1.sym.e8faeee7-63c9-4cb3-96e0-e50a41f3b35b&amp;pf_rd_p=e8faeee7-63c9-4cb3-96e0-e50a41f3b35b&amp;pf_rd_r=XRHVTHYP8DZBCGCFPS86&amp;pd_rd_wg=sRwms&amp;pd_rd_r=d78b57fd-3202-4e1b-9504-ec35e67118ea&amp;pd_rd_i=B089YPWZKY&amp;ref_=pd_bap_d_grid_rp_0_6_t&amp;th=1&_encoding=UTF8&tag=blujay131-20&linkCode=ur2&linkId=6b8e047959132aa333bb5414e58410ca&camp=1789&creative=9325">RGB LED Strip Lights</a>, affiliate btw)
- Twitch account and an OAuth token for the bot which you can get from here: https://twitchapps.com/tmi/

## Installation

1. Clone this repository to your local machine or download the script.
2. Install the required Python libraries using the following command:
   '''
   pip install pyfirmata twitchio
   '''
