import discord
from discord.ext import commands
from discord import app_commands
import os

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="products",
        description="View all products available on this server."
    )
    async def products(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🛒 Available Products",
            description="Here are all available products.\n\n**For prices, please open a ticket.**",
            color=discord.Color.blue()
        )

        # Adaugă produsele tale legitime aici
        embed.add_field(name="Product 1", value="Description → open a ticket", inline=False)
        embed.add_field(name="Product 2", value="Description → open a ticket", inline=False)
        embed.add_field(name="Product 3", value="Description → open a ticket", inline=False)
        embed.add_field(name="Product 4", value="Description → open a ticket", inline=False)
        embed.add_field(name="Product 5", value="Description → open a ticket", inline=False)
        embed.add_field(name="Product 6", value="Description → open a ticket", inline=False)

        embed.set_footer(text="Server Shop • Contact staff for more details.")

        # ephemeral = doar persoana care folosește comanda îl vede
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Shop(bot))
