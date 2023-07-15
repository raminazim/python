import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_member_join(member):
    role_id = 1129185154741583873

    try:
        role = member.guild.get_role(role_id)
        await member.add_roles(role)
        print(f'Assigned role {role.name} to {member.name}')
    except Exception as e:
        print(f'Error assigning role: {e}')

bot.run('MTEyOTE5OTEyMzcyMDA0NDU3NA.Gk3f9R.Byu9PFv-DdibSi5s4Ts1kJak47hAni7VX_3EOo')
#Under Ramin Azim Enterspise