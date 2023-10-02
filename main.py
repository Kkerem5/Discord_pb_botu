import discord
from main2 import gen_pass



#ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
#Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
#client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Çalışmaya hazırım {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Meksikaya gidiyoruz'):
        await message.channel.send("Fernando Sucre'ye selam söyle")
    elif message.content.startswith('Hapishane hayatı çok zor'):
        await message.channel.send("\U0001f642 Hapishaneye abim lincoln geldi artık kolay")
    elif message.content.startswith('sarah'):
        gif1 = 'https://tenor.com/view/michaelsarascofield-michaelscofield-wentworthmiller-misascofield-prison-gif-23074518'
        await message.channel.send(gif1)
    elif message.content.startswith('En sevdiğim pb karakteri'):
        gif2 = 'https://tenor.com/view/michael-scolfield-wentworth-miller-wade-gif-21957458'
        await message.channel.send(gif2)
    elif message.content.startswith('sifre_olustur'):
        password = gen_pass(10)
        await message.channel.send(f"Oluşturulan şifre: {password}")
    else:
        await message.channel.send(message.content)

client.run("TOKEN")
