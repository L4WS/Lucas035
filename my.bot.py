# Import Discord Package #
import discord
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands

# Client (the bot)#
client = commands.Bot(command_prefix="--")

@client.command(name="version")
async def version(context):

    myEmbed = discord.Embed(title="Current Version", description="The Bot Is In Version 2.5.1", color=0x00ff00)
    myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released:", value="September 17th, 2021", inline=False)
    myEmbed.set_footer(text="This is a sample footer")
    myEmbed.set_author(name="Cool Bot")

    await context.message.channel.send(embed=myEmbed)


@client.event
async def on_ready():
    # Do stuff #
    general_channel = client.get_channel(887377402743910401)
    await general_channel.send("Hello, World!")


@client.event
async def on_disconnect():
    general_channel = client.get_channel(887377402743910401)
    await general_channel.send("Goody bye!")

@client.event
async def on_message(message):

    if message.content == "what is the version":
        general_channel = client.get_channel(887377402743910401)

        myEmbed = discord.Embed(title="Current Version", description="The Bot Is In Version 2.5.1", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date Released:", value="September 17th, 2021", inline=False)
        myEmbed.set_footer(text="This is a sample footer")
        myEmbed.set_author(name="Cool Bot")

        await general_channel.send(embed=myEmbed)

    await client.process_commands(message)

# Run the client on the server #
client.run("")