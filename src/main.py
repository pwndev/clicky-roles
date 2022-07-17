import discord
import os
import signal

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

client = discord.Client(intents=intents)

roles_channel_id = 474976442212679710
roles = {
  # Regions
  '🇪🇺': 497368201055961110,
  '🇺🇸': 497368361580232714,
  '🇭🇰': 497368469776367627,
  # Roles
  '497118267232616448': 501069872067772446,
  '497118266498482186': 501068690083545088,
  '497118266381041674': 501068938478747657,
  # Special
  '🏆': 474891702386163722
}


@client.event
async def on_ready():
  print(f'Logged in as {client.user}', flush=True)


@client.event
async def on_raw_reaction_add(event):
  if event.user_id == client.user.id:
    return

  if event.channel_id != roles_channel_id:
    return
  
  if event.emoji.id == None:
    reaction_reference = event.emoji.name
  else:
    reaction_reference = str(event.emoji.id)

  try:
    role_id = roles[reaction_reference]
  except KeyError:
    return
  
  guild = client.get_guild(event.guild_id)
  if guild == None:
    return
  
  role = guild.get_role(role_id)
  if role == None:
    return
  
  await event.member.add_roles(role)


@client.event
async def on_raw_reaction_remove(event):
  if event.user_id == client.user.id:
    return

  if event.channel_id != roles_channel_id:
    return
  
  if event.emoji.id == None:
    reaction_reference = event.emoji.name
  else:
    reaction_reference = str(event.emoji.id)

  try:
    role_id = roles[reaction_reference]
  except KeyError:
    return

  guild = client.get_guild(event.guild_id)
  if guild == None:
    return
  
  role = guild.get_role(role_id)
  if role == None:
    return

  member = guild.get_member(event.user_id)
  if member == None:
    return
  
  await member.remove_roles(role)


BOT_TOKEN = os.environ['BOT_TOKEN']
client.run(BOT_TOKEN)
