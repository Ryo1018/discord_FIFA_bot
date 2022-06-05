# pip install pynacl, libffi-dev, ffmpeg

import time
import discord
import random
from decimal import Decimal, ROUND_HALF_UP

TOKEN = 'OTQ0NjIxOTA4NjczMDU2Nzg4.GcilVp.K3S_h8ITgszm0INySXO1-Zb5d7q6OU1W-8amMk'

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.content == '$FIFA':
        '''
        TODO
        - get mentions in message
        - create new voicechannel
        - The user in new voicechannel, after return before voicechannel
        '''

        if message.author.voice is None:
            await message.channel.send(f'{message.author.mention} あなたは会場に入っていません。帰れ！バケモノ')
            return
        else:
            await message.author.voice.channel.connect()
            await message.channel.send('開場')
            
            message.guild.voice_client.play(discord.FFmpegPCMAudio('FIFA.mp3'))

            time.sleep(20)

            await message.guild.voice_client.disconnect()
            await message.channel.send('閉場')

    if message.content == '$SLM':
        if message.author.voice is None:
            await message.channel.send(f'{message.author.mention} 虫けらはお帰りくださいまし～！')
            return
        else:
            await message.author.voice.channel.connect()
            message.guild.voice_client.play(discord.FFmpegPCMAudio('salome.mp3'))
            time.sleep(15)
            await message.guild.voice_client.disconnect()

    if message.content == '$OMIKUJI':
        if message.author.voice is None:
            await message.channel.send(f'{message.author.mention} 虫けらはお帰りくださいまし～！')
            return
        else:
            await message.author.voice.channel.connect()
            rnd = random.uniform(0, 3)
            rundrnd = Decimal(rnd*100).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            await message.channel.send(f'{message.author.mention} {rundrnd}%ですわよ～！')
            message.guild.voice_client.play(
                discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('salome.mp3'), volume=rundrnd)
                )
            time.sleep(15)
            await message.guild.voice_client.disconnect()
    
    if message.content == '$TEXT':
        text = input()
        # await message.delete()
        await message.channel.send(text)

    if message.content == '$KILL':
        await message.channel.send('⏰')
        await client.close()

client.run(TOKEN)