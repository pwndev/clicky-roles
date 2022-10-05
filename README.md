<div align="center">
  <h3 align="center">Clicky Roles</h3>
  <p>A Discord integration that allows members to select roles by reacting to a message</p>
  <p><a href="#overview">Overview</a> • <a href="#installation">Installation</a></p>
</div>

> ⚠️ Project might be deprecated once the Discord onboarding screen is globally released.

## Overview

It is common to have multiple roles for personalisation on a Discord server. Usually this includes roles for different name colors, pings, hidden categories and more. This bot gives your members the ability to select the preferred roles themselves by simply reacting to a message.

## Installation

The deployment can be done by building and using the app as a Docker image or via a traditional Python environment. For the traditional installation, make sure `python-3.9` & `pip` are installed on your system.

### Create a bot user

1. Create an application on the [Discord Development Portal](https://discord.com/developers/applications)
2. Add a bot user to that application
3. Regenerate a token for the bot user

### Environment variables

| VARIABLE  | DESCRIPTION                                                                               |
| --------- | ----------------------------------------------------------------------------------------- |
| BOT_TOKEN | The bot token of your [Discord application](https://discord.com/developers/applications). |
