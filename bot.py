import os
import platform

import discord
from discord import Client, app_commands, guild, Embed
from dotenv import load_dotenv

import btnExample

load_dotenv()
# These should be assigned in the ".env" file
TOKEN = os.getenv('TOKEN') # Bot token
guildId = os.getenv('GUILDID') # The bot will only work for guild with this id, it is faster
adminRoleId = int(os.getenv('ADMINROLE')) # Can be checked to see if person hes the permission

intents = discord.Intents.all()
client = Client(intents=intents) # classic client
tree = app_commands.CommandTree(client) # For commands
guild = discord.Object(id=guildId, type=guild)

embNoPerms = Embed(title="Permission", description="You do not have the permissions to do this!", color=discord.Color.red()) # Embed sent if the cmd sender has not the role to use this bot


# Adds a command to the bot
@tree.command(name="ping", description="Example cmd")
async def ping(ctx: discord.Interaction): # The ctx is your way of interacting with the message, and getting info like its author or content
    view = btnExample.Buttons() # View is discords built-in handling of buttons
    embeddedResponse = Embed(title="Embed title", description="Click a button", color=discord.Color.yellow()) # This makes the response fancier, the color is the stripe on the left of the embed
    await ctx.response.send_message(embed=embeddedResponse, view=view) # This sends a response, note: needs to be awaited

@tree.command(name="test", description="Needs admin role to be executed")
async def test(ctx: discord.Interaction):
    adRole = ctx.guild.get_role(adminRoleId) # Cannot be initialized outside of command because it uses "ctx", which is passed in on command
    if ctx.user.roles.__contains__(adRole): # This checks if the command initializer has the role with the inputted id(in .env file)
        view = btnExample.Buttons()
        embeddedResponse = Embed(title="Embed title", description="Click a button", color=discord.Color.yellow())
        await ctx.response.send_message(embed=embeddedResponse, view=view)
    else:
        await ctx.response.send_message(embed=embNoPerms)

# On bot loaded
@client.event
async def on_ready():
    await tree.sync(guild=guild) # Essential for this cmd system, if removed it probably wont work
    print(f"Logged in as {client.user.name}")
    print(f"discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()}, {platform.release()}, ({os.name})")
client.run(TOKEN)