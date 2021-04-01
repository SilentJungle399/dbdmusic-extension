from discord.ext import commands

class Exten(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		# we need to grab the lavalink instance first
		self.lavalink = self.bot.get_cog("Music").bot.lavalink

	@commands.command()
	async def volume(self, ctx, vol = None):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")

		if not vol:
			await ctx.send(f"Volume: {player.volume}")
		elif 0 <= int(vol) <= 100:
			await player.set_volume(int(vol))
			await ctx.send(f"Set volume to {vol}")

	@commands.command()
	async def pause(self, ctx):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")

		await player.set_pause(True)
		await ctx.send("Paused the music.")

	@commands.command()
	async def resume(self, ctx):
		player = self.lavalink.player_manager.get(ctx.guild.id)

		if not player:
			return await ctx.send('Not connected!')
		
		elif not ctx.author.voice or (int(ctx.author.voice.channel.id) != int(player.channel_id)):
			return await ctx.send("You are not in my voice channel.")

		await player.set_pause(False)
		await ctx.send("Resumed the music.")

	# that was it for this video, keep watching for more

def setup(bot):
	bot.add_cog(Exten(bot))