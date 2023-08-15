# Cost Effective Twitch Chat Controlled Lights
[![Official Website](https://img.shields.io/badge/Official%20Website-blujay131.com-blue?style=flat&logo=world&logoColor=white)](https://blujay131.com/)
[![Socials](https://img.shields.io/badge/Socials-linktr.ee/blujay131-purple?style=flat&logo=world&logoColor=white)](https://linktr.ee/blujay_131)
[![GitHub Repo stars](https://img.shields.io/github/stars/BluJay131/Cost-Effective-Twitch-Chat-Controlled-Lights?style=social)](https://github.com/BluJay131/Cost-Effective-Twitch-Chat-Controlled-Lights/stargazers)

<hr/>

### ![image](https://github.com/BluJay131/Cost-Effective-Twitch-Controlled-Lights/assets/80910384/346dc2a9-45f3-4372-8e4c-de62a3bc5e3f) Make sure to use ChatLightsV2.py for the latest code and quality of life.

**(Youtube video coming)**

## Description

A Python script that enables a Twitch bot capable of controlling an RGB LED strip through commands from the Twitch chat. The script interfaces with an Arduino board via the `pyfirmata` library and manages Twitch interactions using the `twitchio` library.

## Prerequisites

- Python 3.x
- Arduino board (tested with a pro micro atmega32u4)
- RGB LED Strip Controller (tested with <a target="_blank" href="https://www.amazon.com/Lights-ehomful-Changing-Bedroom-Decoration/dp/B089YPWZKY?pd_rd_w=1UL1g&amp;content-id=amzn1.sym.e8faeee7-63c9-4cb3-96e0-e50a41f3b35b&amp;pf_rd_p=e8faeee7-63c9-4cb3-96e0-e50a41f3b35b&amp;pf_rd_r=XRHVTHYP8DZBCGCFPS86&amp;pd_rd_wg=sRwms&amp;pd_rd_r=d78b57fd-3202-4e1b-9504-ec35e67118ea&amp;pd_rd_i=B089YPWZKY&amp;ref_=pd_bap_d_grid_rp_0_6_t&amp;th=1&_encoding=UTF8&tag=blujay131-20&linkCode=ur2&linkId=6b8e047959132aa333bb5414e58410ca&camp=1789&creative=9325">RGB LED Strip Lights</a>, affiliate btw)
- Photoresistor and a singular LED (or just get a night light from the dollar store)
- Twitch account and an OAuth token for the bot which you can get from here: https://twitchapps.com/tmi/

## Installation and Usage

1. Clone this repository to your local machine or download the script.
2. Install the required Python libraries using the following command:
   ```
   pip install pyFirmata twitchio
   ```
3. Upload the StandardFirmata sketch to your Arduino board using the Arduino IDE.\
   (Simple and easy to follow video here: https://www.youtube.com/watch?v=KPfBOGjJdqE&t=526s)
4. Configure the config.csv file with your details, it goes in the format of:\
   `token` (OAuth token from the twitchapps website above),\
   `prefix` (Word or symbol used for the bot to recognize your command),\
   `initial_channel` (Name of your twitch channel),\
   `com_port` (USB port of the arduino eg. 'COM5'),\
   `led_pin` (Pin on arduino to use eg. 'd:3:o')\
5. Physical Setup\
   ![CircuitDiagram](https://github.com/BluJay131/Cost-Effective-Twitch-Controlled-Lights/assets/80910384/23c4d0f4-2f49-4beb-b63e-dc70ad49fe09)\
   As shown in the diagram above, the button to change the color of the lights is replaced with a photoresistor. On the Arduino side, a white LED is used on pin 3 in order to complete the circuit that the original button     controlled. (You can go to the dollar tree and get a night light to harvest both of these parts.)\
   <img src="https://github.com/BluJay131/Cost-Effective-Twitch-Controlled-Lights/assets/80910384/def9b3ee-ed59-4e38-8121-f70b747a77c2" data-canonical-src="https://github.com/BluJay131/Cost-Effective-Twitch-Controlled-Lights/assets/80910384/def9b3ee-ed59-4e38-8121-f70b747a77c2" width="250" height="250" />
   <img src="https://github.com/BluJay131/Cost-Effective-Twitch-Controlled-Lights/assets/80910384/fa515666-607c-433e-a6eb-3efa8096c375" data-canonical-src="https://github.com/BluJay131/Cost-Effective-Twitch-Controlled-Lights/assets/80910384/fa515666-607c-433e-a6eb-3efa8096c375" width="250" height="250" />
   <img src="https://github.com/BluJay131/Cost-Effective-Twitch-Controlled-Lights/assets/80910384/fbbd58a4-6be0-4956-8ce9-2a94b0ce734a" data-canonical-src="https://github.com/BluJay131/Cost-Effective-Twitch-Controlled-Lights/assets/80910384/fbbd58a4-6be0-4956-8ce9-2a94b0ce734a" width="250" height="250" />\
   For my real life implementation, I desoldered the 'color' button and replaced the 2 contacts with wire to feed through the shell to the breadboard. Also, I got a large straw an cut a small piece down one side so I could fit it over the photoresistor and LED to stop excess light pollution from external sources such as the LED strips themselves.

7. Run and have fun streaming! (Commands in the code are in the format of "lights red" or "lights help")

## Side Notes

- You can modify the bot script to add more color commands easily or customize the behavior according to your preferences.
- This project is licensed under the MIT License.
