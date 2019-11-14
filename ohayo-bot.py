ohayo-bot.py
#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = "NjQ0NTQ2ODE3MDE4NTYwNTQ0.Xc1x_Q.X81fW0SH6iXMlHWlL7yOwa5Jx4g" #トークン
CHANNEL_ID =483886909873979394#チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '07:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
