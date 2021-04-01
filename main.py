import dbdmusic
import os
bot_ = dbdmusic.Bot(prefix = "!", lavalinkpass = "yourpass", lavalinkport = 6969)

bot = bot_.bot

@bot.event
async def on_ready():
	bot.load_extension("extension")
	print("Extension Loaded.")

@bot.command()
async def reload(ctx):
	bot.reload_extension("extension")
	await ctx.send("Reloaded Extension.")

bot_.connect(os.environ.get("TOKEN"))