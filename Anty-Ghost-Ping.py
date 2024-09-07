import discord
from discord.ext import commands
from datetime import datetime
import pytz 

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Login: {bot.user}')

@bot.event
async def on_message_delete(message):
    if message.author.bot:
        return

    if message.mentions:
        channel = message.channel
        embed = discord.Embed(
            title="Ghost Ping Detected",
            color=discord.Color.red()
        )
        
        embed.add_field(name="Author", value=message.author.mention, inline=False)
        mentioned_users = ', '.join(user.mention for user in message.mentions)
        embed.add_field(name="Pinged User(s)", value=mentioned_users, inline=False)
        
        local_timezone = pytz.timezone("Europe/Warsaw")
        local_time = datetime.now(local_timezone).strftime("%Y-%m-%d %H:%M:%S %Z")
        embed.set_footer(text=f"Detected at: {local_time}")

        await channel.send(embed=embed)

bot.run('your bot token')
