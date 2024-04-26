import discord
from discord.ext import commands
import datetime
import requests
from control_BD_SQLite import Table_SQLite

TOKEN = 'MTIzMTY2NDE5NjY4NTM5ODA3Nw.Gw4IGG.V9tlrvSXdpLIO-6WeQ333Dvg5AjQujfOuA0eEw'
PREFIX = 'FH! '
intents = discord.Intents().all()

port = "192.168.0.101"
xTunnel_key = "e95eee266eb34ecda2f19c953ec945e6"

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

'''requests_события'''

send_load = {
    "content": "FH_Bot запущен!"
}

header_flag = {
    "authorization": "NTM2MjM4MzEzNDE0MzI4MzUx.GCobTt.sKasvsPzbh9lgWuEuZUCiW_nyvdMreREV0B4yY"
}

r = requests.post("https://discord.com/api/v9/channels/1231677946075549806/messages",
                  data=send_load,
                  headers=header_flag)

'''События'''


@bot.event
async def on_member_join(member):  # приветствие участника
    await member.send(f'Добро пожаловать {member}!')


'''Комманды'''


@bot.command()
async def get_commands(ctx: commands.Context):  # отправка всех комманд
    some_url = "https://fallendeity.github.io/discord.py-masterclass/"
    embed = discord.Embed(
        title="Комманды",
        description="",
        url=some_url,
        color=discord.Color.random(),
        timestamp=datetime.datetime.utcnow()
    )

    embed.add_field(name="",
                    value="get_commands - комманда, для вывода всех комманд,\n"
                          "vinipuh - комманда, для вывода изображения Винипуха,\n"
                          "hello - комманда, для вывода ответного сообщения",
                    inline=False)

    embed.set_image(
        url="https://www.w-dog.ru/wallpapers/1/17/352483019594575/geroj-multfilma-vinni-pux-na-zheltom-fone-budto-paryashhij-v-vozduxe.jpg"
    )

    await ctx.reply(embed=embed)


@bot.listen()
async def on_message(message:discord.Message): # назначение имени
    a = Table_SQLite
    if str(message.author) == "mr.oduvanchik" and str(message.content.split()[0]) == "FH?" and str(message.content.split()[1]) == "claim_name":
        a.claim_name(Table_SQLite(), str(message.content.split()[2]))
    else:
        pass



@bot.listen()
async def on_message(message:discord.Message): # получение имени
    a = Table_SQLite
    if str(message.author) == "mr.oduvanchik" and str(message.content.split()[0]) == "FH?" and str(message.content.split()[1]) == "get_name":
        mes = a.get_name(Table_SQLite())
        await message.author.send(mes)
    else:
        pass


@bot.command()
async def vinipuh(ctx):  # отправка картинки
    await ctx.reply(file=discord.File('images/vinipuh.jpg'))


@bot.command()
async def hello(ctx):  # отправка сообщения, в ответ
    await ctx.reply("hello")
    await ctx.reply('how your life?')


bot.run(TOKEN)
