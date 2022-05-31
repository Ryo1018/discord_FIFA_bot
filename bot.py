# pip install pynacl, libffi-dev, ffmpeg


# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'OTQ0NjIxOTA4NjczMDU2Nzg4.GsFZ0a.eDg40c3vBlafKSkk4t0Eg4zo_TNAWAI9Gwr1eU'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    # if message.content == '$neko':
    #     await message.channel.send('にゃーん')

    if message.content == '$FIFA':
        '''
        TODO
        - get mentions in message
        - create new voicechannel
        - The user in new voicechannel, after return before voicechannel
        '''
        
        # voice = await client.join_voice_channel(client.get_channel("PASTE ID"))
        # player = voice.create_ffmpeg_player('fifa.mp3')
        # player.start()

        if message.author.voice is None:
            await message.channel.send('あなたは会場に入っていません。')
            return
        
        await message.author.voice.channel.connect()
        await message.channel.send('開場')
        
        await message.guild.voice_client.play(discord.FFmpegPCMAudio('FIFA.mp3'))

        await message.guild.voice_client.disconnect()
        await message.channel.send('閉場')


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)