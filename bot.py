import discord, asyncio, os

client = discord.Client()

gen_channel_ids = []
for n in open('channel_ids.txt', 'r', encoding='UTF8').read().split('\n'):
    gen_channel_ids.append(n)

@client.event
async def on_ready():
    print(" ")
    print("봇 작동중")
    print(" ")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("$키젠도움말"))

@client.event
async def on_message(message):
    if message.author.bot:
       return
    try:
        open(f'{message.guild.id}.txt', 'a').write('')
    except:
        pass
    if message.content == "$키젠도움말":
        await message.reply(embed=discord.Embed(title='키젠봇', description=f'키젠을 합니다.\n\n**[명령어 안내]**\n$재고 : 현재 랜덤 키젠이 몇개 있는지 확인 합니다.\n$키젠 : 랜덤 키젠을 생성 합니다.\n\n**[현재 제공되는 키젠]**\n스팀, 로블록스, 넷플릭스, 노드VPN, 마인크래프트, 디즈니플러스, 유플레이', color=0x00ff00))
    if message.content == "$재고":
        tokens = open(f'{message.guild.id}.txt', 'r').read().split('\n')
        await message.reply(embed=discord.Embed(title=f'⏹ 현재 랜덤키젠이 {len(tokens) - 1}개 남아있습니다 !', color=0x00ff00))
    if message.author.guild_permissions.administrator:
        if message.content.startswith("$키젠추가\n"):
            count = 1
            token = []
            for d in range(len(message.content.split('\n')) - 1):
                token.append(message.content.split('\n')[count])
                count += 1
            open(f'{message.guild.id}.txt', 'a').write('\n'.join(token) + '\n')
            await message.reply(embed=discord.Embed(title='✅ 랜덤 키젠 추가 성공 !', color=0x00ff00))
        if message.content.startswith('$키젠채널 '): #명령어 설정
            channel_id = message.content.split(' ')[1]
            open('channel_ids.txt', 'a').write(channel_id + '\n')
            await message.reply(embed=discord.Embed(title='✅ 채널 추가 성공 !', color=0x00ff00))
    if message.content == '$키젠': # 명령어 설정
        if str(message.channel.id) in gen_channel_ids:
            c = 1
            token = []
            tokens = open(f'{message.guild.id}.txt', 'r').read().split('\n')
            if tokens[0] == '':
                await message.reply(embed=discord.Embed(title='❎ 재고 소진 안내', description=f'모든 재고가 소진 되었습니다.\n추후 관리자가 직접 넣을 예정 입니다.', text='제목', color=0x00ff00))
            else:
                await message.reply(embed=discord.Embed(title='✅ DM 전송 완료!', description=f'랜덤 계정을 **DM**으로 보냈습니다.\n**DM**을 확인해주세요!', text='제목', color=0x00ff00))
                try:
                    email_password_token = tokens[0].split(":")
                    sent_message = await message.author.send(embed=discord.Embed(title='랜덤키젠', description=f'```제품 분류 : {email_password_token[0]}\n아이디 : {email_password_token[1]}\n비밀번호 : {email_password_token[2]}```', color=0x00ff00))
                except:
                    sent_message = await message.author.send(embed=discord.Embed(title='랜덤키젠', description=f'```{tokens[0]}```', color=0x00ff00))
                for tokenlist in range(len(tokens) - 1):
                    token.append(tokens[c])
                    c += 1
                open(f'{message.guild.id}.txt', 'w').write('\n'.join(token))


client.run('토큰') # 토큰주소
