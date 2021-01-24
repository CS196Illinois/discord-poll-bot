from discord.ext import commands, tasks
import discord
import os

from src.cogs.poll import Poll

TOKEN = os.environ['POLL_TOKEN'].strip()
# print(TOKEN.strip())

bot = commands.Bot(command_prefix='poll', case_insensitive=True, help_command=None)


@bot.event
async def on_ready():
    # Log events to console.
    print('Bot online.')
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    await bot.process_commands(message)


@bot.command(name='set')
async def set_target_channel(ctx: discord.ext.commands.Context, args):
    bot.add_cog(Poll(bot, args[0]))
    await ctx.send(f'Bound to <#{ctx.channel.id}>.')

bot.run(TOKEN)