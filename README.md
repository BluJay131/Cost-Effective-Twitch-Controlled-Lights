# Cost Effective Twitch Chat Controlled Lights
[![Official Website](https://img.shields.io/badge/Official%20Website-blujay131.com-blue?style=flat&logo=world&logoColor=white)](https://blujay131.com/)
[![Socials](https://img.shields.io/badge/Socials-linktr.ee/blujay131-purple?style=flat&logo=world&logoColor=white)](https://linktr.ee/blujay_131)
[![GitHub Repo stars](https://img.shields.io/github/stars/BluJay131/Cost-Effective-Twitch-Chat-Controlled-Lights?style=social)](https://github.com/BluJay131/Cost-Effective-Twitch-Chat-Controlled-Lights/stargazers)

<hr/>

### ![image](https://github.com/BluJay131/Cost-Effective-Twitch-Controlled-Lights/assets/80910384/346dc2a9-45f3-4372-8e4c-de62a3bc5e3f) Make sure to use ChatLightsV2.py for the latest code and quality of life.

** (Youtube video coming)

<hr/>

Table of Contents

Description
Prerequisites
Installation
Configuration
Usage
Bot Commands
Customization
Credits
License
Description
This repository contains a Python script that allows you to create a Twitch bot capable of controlling an RGB LED using commands from the Twitch chat. The script interfaces with an Arduino board through the pyfirmata library and handles Twitch interactions using the twitchio library.

Prerequisites
Python 3.x
Arduino board (tested with Arduino Mega)
RGB LED connected to the specified pin on the Arduino board
Twitch account and an OAuth token for the bot
Installation
Clone this repository to your local machine or download the script.

Install the required Python libraries using the following command:

bash
Copy code
pip install pyfirmata twitchio
Configuration
Create a CSV file named config.csv in the same directory as the script.

Add the following fields to the CSV file and provide appropriate values:

csv
Copy code
token,oauth_token_here
prefix,lights
initial_channel,your_channel_name
com_port,/dev/ttyUSB0
led_pin,digital:13:o
token: OAuth token for your bot account.
prefix: Command prefix for the bot (default: "lights").
initial_channel: The Twitch channel where the bot will operate.
com_port: The COM port your Arduino board is connected to.
led_pin: The pin configuration of the LED on the Arduino board.
Usage
Connect the Arduino board to your computer.

Upload the StandardFirmata sketch to your Arduino board using the Arduino IDE.

Run the bot script using the following command:

bash
Copy code
python bot_script.py
In your Twitch chat, use the following commands to change the LED color:

!lights red
!lights yellowgreen
!lights orange
... (similar commands for other colors)
Bot Commands
!lights help: Display the available color options.
Color-specific commands (e.g., !lights red, !lights green, etc.) to change the LED color.
Customization
You can modify the bot script to add more color commands or customize the behavior according to your preferences.

Credits
This bot script was inspired by the idea of integrating Twitch chat with Arduino control, using the pyfirmata and twitchio libraries.

License
This project is licensed under the MIT License.
