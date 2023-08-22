import pyfirmata
import time
from time import sleep
from twitchio.ext import commands

board = pyfirmata.ArduinoMega('com7')
pin3 = board.get_pin('d:3:o')
color = 0
token='Your_Token_Here'
prefix='lights'
initial_channels=['BluJay132']

def changeColor():
    pin3.write(1)
    time.sleep(0.1)
    pin3.write(0)
    time.sleep(0.3)

def cycle():
    print(color)
    latest = 12 - color
    for x in range(latest):
        changeColor()

def globallyChange(val):
    global color
    color = val

def red():
    globallyChange(0)
    for x in range(0):
        changeColor()

def yellowgreen():
    globallyChange(1)
    for x in range(1):
        changeColor()

def orange():
    globallyChange(2)
    for x in range(2):
        changeColor()


def green():
    globallyChange(3)
    for x in range(3):
        changeColor()

def cyan():
    globallyChange(4)
    for x in range(4):
        changeColor()

def lightblue():
    globallyChange(5)
    for x in range(5):
        changeColor()

def darkblue():
    globallyChange(6)
    for x in range(6):
        changeColor()

def violet():
    globallyChange(7)
    for x in range(7):
        changeColor()

def purple():
    globallyChange(8)
    for x in range(8):
        changeColor()

def offwhite():
    globallyChange(9)
    for x in range(9):
        changeColor()

def pink():
    globallyChange(10)
    for x in range(10):
        changeColor()

def lightpurple():
    globallyChange(11)
    for x in range(11):
        changeColor()



class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token = token, prefix = prefix, initial_channels = initial_channels)

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send(f'Use the prefix "lights " followed by one of the following colors to change my background LEDs! (ex. red, yellowgreen, orange, green, cyan, lightblue, darkblue, violet, purple, offwhite, pink, lightpurple)')

    @commands.command()
    async def red(self, ctx: commands.Context):
        cycle()
        red()

    @commands.command()
    async def yellowgreen(self, ctx: commands.Context):
        cycle()
        yellowgreen()

    @commands.command()
    async def orange(self, ctx: commands.Context):
        cycle()
        orange()

    @commands.command()
    async def green(self, ctx: commands.Context):
        cycle()
        green()

    @commands.command()
    async def cyan(self, ctx: commands.Context):
        cycle()
        cyan()

    @commands.command()
    async def lightblue(self, ctx: commands.Context):
        cycle()
        lightblue()

    @commands.command()
    async def darkblue(self, ctx: commands.Context):
        cycle()
        darkblue()

    @commands.command()
    async def violet(self, ctx: commands.Context):
        cycle()
        violet()

    @commands.command()
    async def purple(self, ctx: commands.Context):
        cycle()
        purple()

    @commands.command()
    async def offwhite(self, ctx: commands.Context):
        cycle()
        offwhite()

    @commands.command()
    async def pink(self, ctx: commands.Context):
        cycle()
        pink()

    @commands.command()
    async def lightpurple(self, ctx: commands.Context):
        cycle()
        lightpurple()

bot = Bot()
bot.run()
