import discord
from discord.ext import commands
from discord import app_commands

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="products",
        description="Display available products."
    )
    async def products(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="🛒 Available Products",
            description="Here are all available products.\n\n**For prices, please open a ticket.**",
            color=discord.Color.blue()
        )

        # AICI adaugi ce produse vrei tu (legale)
        embed.add_field(name="Example Product", value="For price → open a ticket", inline=False)

        embed.set_footer(text="Server Shop")
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Shop(bot))
