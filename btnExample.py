# btnExample.py

import os
import discord
from dotenv import load_dotenv
load_dotenv()


print("y")
class Buttons(discord.ui.View):
    global view
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    
    @discord.ui.button(label="Red button",style=discord.ButtonStyle.red)
    async def red_btn(self, ctx: discord.Interaction, button: discord.ui.Button):
            view=Buttons() # So you can remove the buttons
            view.clear_items() # removes the buttons
            embeddedResponse = discord.Embed(title="Embed title", description="Clicked red button", color=discord.Color.red())
            await ctx.response.edit_message(embed=embeddedResponse, view=view)
    @discord.ui.button(label="Green button",style=discord.ButtonStyle.green)
    async def green_btn(self, ctx: discord.Interaction, button: discord.ui.Button):
            view=Buttons()
            view.clear_items()
            embeddedResponse = discord.Embed(title="Embed title", description="Clicked green button", color=discord.Color.green())
            await ctx.response.edit_message(embed=embeddedResponse, view=view)