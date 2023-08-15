import pyfirmata
import time
import csv
from twitchio.ext import commands

# Define a custom Twitch bot class that inherits from commands.Bot
class Bot(commands.Bot):

    def __init__(self, token, prefix, initial_channel, com_port, led_pin):
        super().__init__(token=token, prefix=prefix, initial_channels=[initial_channel])

        # Initialize Arduino board and LED pin
        self.board = pyfirmata.ArduinoMega(com_port)
        self.pin = self.board.get_pin(led_pin)

        # Initialize color index for cycling
        self.color = 0

    # Event handler when the bot is ready
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    # Function to change LED color by toggling the pin
    def change_color(self):
        self.pin.write(1)
        time.sleep(0.1)
        self.pin.write(0)
        time.sleep(0.3)

    # Cycle through LED colors based on the current color index
    def cycle(self):
        print(self.color)
        latest = 12 - self.color
        for _ in range(latest):
            self.change_color()

    # Set the global color index to a specified value
    def globally_change(self, val):
        self.color = val

    # Help command to display color options
    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send('Use the prefix "lights " followed by one of the following colors to change the background LEDs! (ex. red, yellowgreen, orange, green, cyan, lightblue, darkblue, violet, purple, offwhite, pink, lightpurple)')

    # Common function to handle color change commands
    def color_command(self, ctx, color_num):
        self.cycle()
        self.globally_change(color_num)
        for _ in range(color_num):
            self.change_color()

    # Map out colors (in order) below
    # Color-specific commands
    # Similar structure for other color commands
    @commands.command()
    async def red(self, ctx: commands.Context):
        self.color_command(ctx, 0)

    @commands.command()
    async def yellowgreen(self, ctx: commands.Context):
        self.color_command(ctx, 1)

    @commands.command()
    async def orange(self, ctx: commands.Context):
        self.color_command(ctx, 2)

    @commands.command()
    async def green(self, ctx: commands.Context):
        self.color_command(ctx, 3)

    @commands.command()
    async def cyan(self, ctx: commands.Context):
        self.color_command(ctx, 4)

    @commands.command()
    async def lightblue(self, ctx: commands.Context):
        self.color_command(ctx, 5)

    @commands.command()
    async def darkblue(self, ctx: commands.Context):
        self.color_command(ctx, 6)

    @commands.command()
    async def violet(self, ctx: commands.Context):
        self.color_command(ctx, 7)

    @commands.command()
    async def purple(self, ctx: commands.Context):
        self.color_command(ctx, 8)

    @commands.command()
    async def offwhite(self, ctx: commands.Context):
        self.color_command(ctx, 9)

    @commands.command()
    async def pink(self, ctx: commands.Context):
        self.color_command(ctx, 10)

    @commands.command()
    async def lightpurple(self, ctx: commands.Context):
        self.color_command(ctx, 11)

# Function to read configuration from CSV file
def read_config(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        config = next(reader)  # Read the first (and only) row
        return (
            config['token'],
            config['prefix'],
            config['initial_channel'],
            config['com_port'],
            config['led_pin']
        )

# Main function to run the bot
def main():
    token, prefix, initial_channel, com_port, led_pin = read_config('config.csv')
    bot = Bot(token, prefix, initial_channel, com_port, led_pin)
    bot.run()

# Entry point of the script
if __name__ == "__main__":
    main()
