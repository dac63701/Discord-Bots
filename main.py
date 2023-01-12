import discord
from discord.ui import Select, View
from discord.ext import commands
import random

TOKEN = ''

botChannel = 'bot-test'

output = ''
context = ''

intents = discord.Intents().all()

gameMoves = ['rock', 'paper', 'scissor']

bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')
    
def run_game(playerMove):
    global gameMoves
    global output

    botMove = random.choices(gameMoves)

    if playerMove == 'rock':
        if botMove[0] == 'rock':
            output = 'Tie'
        if botMove[0] == 'paper':
            output = 'Player Won'
        if botMove[0] == 'scissor':
            output = 'AI Won'
    if playerMove == 'paper':
        if botMove[0] == 'rock':
            output = 'Player Won'
        if botMove[0] == 'paper':
            output = 'Tie'
        if botMove[0] == 'scissor':
            output = 'AI Won'
    if playerMove == 'scissor':
        if botMove[0] == 'rock':
            output = 'AI Won'
        if botMove[0] == 'paper':
            output = 'Player Won'
        if botMove[0] == 'scissor':
            output = 'Tie'
    

class PlayGame(discord.ui.View):

    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label='Rock', style=discord.ButtonStyle.gray, custom_id='rock') 
    async def rock_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        global context
        global output

        run_game('rock')

        e = discord.Embed(title='Rock, Paper, Scissors', description=output)

        await context.reply(embed=e)


    @discord.ui.button(label='Paper', style=discord.ButtonStyle.green, custom_id='paper') 
    async def paper_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        global context
        global output

        run_game('paper')

        e = discord.Embed(title='Rock, Paper, Scissors', description=output)

        await context.reply(embed=e)


    @discord.ui.button(label='Scissors', style=discord.ButtonStyle.red, custom_id='scissor') 
    async def paper_button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        global context
        global output

        run_game('scissor')

        e = discord.Embed(title='Rock, Paper, Scissors', description=output)

        await context.reply(embed=e)


@bot.event
async def on_ready():
    print('Bot are logged in as: {0.user}'.format(bot))

#async def send_message(message, user_message, is_private):


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Help',
        description='Here are all the commands for Rock, Paper, Scissors.',
        color=discord.Colour.blue()
    )
    embed.set_thumbnail(url='https://github.com/dac63701/Discord-Bots/blob/rock-paper-scissors/Screenshot%202023-01-08%20165313.png?raw=true')
    embed.add_field(
        name='!help',
        value='List all of the commands.',
        inline=False
    )
    embed.add_field(
        name='!play',
        value='Starts a game of rock, paper, scissors against an AI opponent.',
        inline=False
    )

    await ctx.send(embed=embed)

@bot.command()
async def play(ctx):
    global output
    global context

    context = ctx

    view = PlayGame()

    embed = discord.Embed(
        title="Rock, Paper, Scissors"
    )

    await ctx.reply(embed=embed, view=view)


bot.run(TOKEN)
