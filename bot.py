# pip install pynacl, libffi-dev, ffmpeg

import time
import discord

TOKEN = ''

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
            await message.channel.send('あなたは会場に入っていません。')
            return
        else:
            await message.author.voice.channel.connect()
            await message.channel.send('開場')
            
            message.guild.voice_client.play(discord.FFmpegPCMAudio('FIFA.mp3'))

            time.sleep(20)

            await message.guild.voice_client.disconnect()
            await message.channel.send('閉場')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)