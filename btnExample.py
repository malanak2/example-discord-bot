# btnExample.py

import os
import discord
from dotenv import load_dotenv
load_dotenv()

class Buttons(discord.ui.View): # This class inherits from discord.ui.View so it can handle them
    global view
    def __init__(self, *, timeout=180): # Maybe needed, maybe not but it shouldn't cause any harm
        super().__init__(timeout=timeout)
    
    @discord.ui.button(label="Red button",style=discord.ButtonStyle.red) # Specifies the button name, etc
    async def red_btn(self, ctx: discord.Interaction, button: discord.ui.Button): # ctx here is mainly about the person who clicked the button, the name has to be original in the context of buttons, if there are multiple with the same name, they WILL conflict
            view=Buttons() # Makes it so you can do edit the view
            view.clear_items() # Removes the buttons
            embeddedResponse = discord.Embed(title="Embed title", description="Clicked red button", color=discord.Color.red())
            await ctx.response.edit_message(embed=embeddedResponse, view=view)
    @discord.ui.button(label="Green button",style=discord.ButtonStyle.green)
    async def green_btn(self, ctx: discord.Interaction, button: discord.ui.Button):
            view=Buttons()
            view.clear_items()
            embeddedResponse = discord.Embed(title="Embed title", description="Clicked green button", color=discord.Color.green())
            await ctx.response.edit_message(embed=embeddedResponse, view=view)