from http import server
from discord import Client
from argparse import ArgumentParser,Namespace
import discord

class MyBot(Client):
    def __init__(self):
        super().__init__()
        
    async def on_ready(self):
         print("Le cameroun est dans la place!")
    async def on_message(ctx,message):
        if message.content == "salut":
            await message.channel.send("le cameroun a éléminé l'algerie de la coupe du monde")
    
    #default_intents = discord.Intents.default()
    #default_intents.members = True
    #client = discord.Client(intents=default_intents)
    @client.event
    async def on_member_join(member):
        general_channel: discord.TextChannel = client.get_channel(958698262842445836)
        await general_channel.send(content=f"Bienvenue au cameroun {member.display_name}!")
    @client.event
    async def on_message(message):
        if message.content.startswith("!del"):
            number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()

def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-c", "--config", help="Config file", required=True, dest="config"
    )
    #return parser.parse_args()

    
client = MyBot()
client.run("OTU4NjkzNjI1NjY2MDg5MDMx.YkRDBA.tZEQNNE4cKmF9ooAR-Ibk1btHWU")

       
