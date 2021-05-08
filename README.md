<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Discord-Bot-Amazon-Price-Tracker</h3>

  <p align="center">
    A Discord bot that tracks Amazon item prices and alerts you when there is a price drop!
    <br />
    <a href="https://github.com/ryanhejs/discord-bot-amazon/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


[![Product Name Screen Shot][product-screenshot]](https://github.com/ryanhejs/discord-bot-amazon)

This is a fun little project I built to track some of my favourite Amazon items with my friends. While there are many other tools that do the same (namely CamelCamelCamel), I prefer to be notified on Discord, where I can also monitor certain items with my friends!


### Built With

* [Discird.py](https://pypi.org/project/discord.py/)
* [Nest-Asyncio](https://pypi.org/project/nest-asyncio/)


<!-- GETTING STARTED -->
## Getting Started

Refer to the following and install the following packages:
* [requirements.txt](https://github.com/ryanhejs/discord-bot-amazon/blob/main/requirements.txt)


### Prerequisites

You MUST install the following:
* requests-html
  ```sh
  pip install requests-html
  ```
  * nest-asyncio
  ```sh
  pip install nest-asyncio
  ```


### Usage

1. Create a new Discord Bot Application at [https://discord.com/developers/applications](https://discord.com/developers/applications)
2. Clone the repo
   ```sh
   git clone https://github.com/ryanhejs/discord-bot-amazon.git
   ```
3. Create an .env and add:
  * DISCORD_TOKEN
    ```sh
    DISCORD_TOKEN = YOUR_TOKEN_AS_IS
    ```
4. Add the Discord bot to your server with (REPLACE: YOUR_ID_HERE with your bot token) [https://discord.com/api/oauth2/authorize?client_id=YOUR_ID_HERE&permissions=523328&scope=bot](https://discord.com/api/oauth2/authorize?client_id=YOUR_ID_HERE&permissions=523328&scope=bot)
5. Run the bot
   ```Run the bot locally
   python panda.py
   ```


<!-- USAGE EXAMPLES -->
## Usage

use !help in the server for instructions


<!-- CONTACT -->
## Contact

Project Link: [https://github.com/ryanhejs/discord-bot-amazon](https://github.com/ryanhejs/discord-bot-amazon)








<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/ryanhejs/discord-bot-amazon/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/ryanhejs/discord-bot-amazon/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/ryanhejs/discord-bot-amazon/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/ryanhejs/discord-bot-amazon/blob/main/README.md
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/ryanhejs/discord-bot-amazon/blob/main/README.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/ryanhejs
[product-screenshot]: images/screenshot.png

