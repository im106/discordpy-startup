tasksloop.py
#coding:UTF-8
import discord
from discord.ext import tasks

TOKEN = "NjQ0NTQ2ODE3MDE4NTYwNTQ0.Xc1vHA.9OV7gI6bcSsBSdSXbWiXE4xB2C8" #トークン
CHANNEL_ID = 483886909873979392#チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
