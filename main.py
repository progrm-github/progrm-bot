import discord
from discord.ext import commands
from hanspell import spell_checker
with open('db', encoding="UTF8") as open_file:
    all_data = open_file.read()
line_list = all_data.splitlines()
bot_dict = {}
for line in line_list:
    orig,trans = line.split(':')
    bot_dict[orig] = trans  
app = commands.Bot(command_prefix='!')
client = discord.Client()
@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)
 
@app.event
async def on_message(message):
    if message.author == client.user: # 만약 메시지를 보낸 사람과 봇이 서로 같을 때
        return

    if message.author.bot: # discord.User.bot 프로퍼티가 참일 때
        return

    command = message.content
    responce = ""
    for key in bot_dict:
        if key in command:
            responce = bot_dict[key]
            break
    if not responce:
        return
    await message.channel.send(responce)
      
       
       
app.run('NzYwODMwMDI2MjA3NDYxNDA2.X3RwLQ.4wSzbo4537rkMOtY9KB5_Fkzxm8')