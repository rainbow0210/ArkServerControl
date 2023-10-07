#! /usr/bin/env python
import discord
import os
import subprocess

flag_ark1 = 0
flag_ark2 = 0
flag_ark3 = 0

client = discord.Client()
TOKEN = 'your_bot_token'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name="ARK Server"))

@client.event
async def on_message(message):
    global flag_ark1
    global flag_ark2
    global flag_ark3

    if message.author == client.user:
        return
    
    #Server start Command
    if message.content == '.ark 1 start':
        if flag_ark1 == 1:
                await message.channel.send('既に起動しています。')
        elif flag_ark == 0:
                flag_ark1 = 1
                stream = os.popen('arkmanager start @main')
                output = stream.read()
                await message.channel.send('No.1 ARKサーバーを起動します、起動まで10分お待ちください。')

    if message.content == '.ark 2 start':
        if flag_ark2 == 1:
                await message.channel.send('既に起動しています。')
        elif flag_ark2 == 0:
                flag_ark2 = 1
                stream = os.popen('arkmanager start @"Server_name"')
                output = stream.read()
                await message.channel.send('No.2 ARKサーバーを起動します、起動まで10分お待ちください。')

    if message.content == '.ark 3 start':
        if flag_ark3 == 1:
                await message.channel.send('既に起動しています。')
        elif flag_ark3 == 0:
                flag_ark3 = 1
                stream = os.popen('arkmanager start @"Server_name"')
                output = stream.read()
                await message.channel.send('"No.3 ARKサーバーを起動します、起動まで10分お待ちください。')


    #Server stop Command
    if message.content == '.ark 1 stop':
        if flag_ark1 == 0:
                await message.channel.send('既に停止しています。')
        elif flag_ark1 == 1:
                flag_ark1 = 2
                await message.channel.send('このコマンドではセーブデータの保存を行いません。セーブデータは15分おきに自動セーブしているので, 現在の進行度を確実に保存するには15分待機してください。サーバを停止する場合はもう一度コマンドを入力してください。')
        elif flag_ark1 == 2:
                flag_ark1 = 0
                stream = os.popen('arkmanager stop @main')
                output = stream.read()
                await message.channel.send('No.1 ARKサーバを停止します。')
       
    if message.content == '.ark 2 stop':
        if flag_ark2 == 0:
                await message.channel.send('既に停止しています。')
        elif flag_ark2 == 1:
                flag_ark2 = 2
                await message.channel.send('このコマンドではセーブデータの保存を行いません。セーブデータは15分おきに自動セーブしているので, 現在の進行度を確実に保存するには15分待機してください。サーバを停止する場合はもう一度コマンドを入力してください。')
        elif flag_ark2 == 2:
                flag_ark2 = 0
                stream = os.popen('arkmanager stop @"Server_name"')
                output = stream.read()
                await message.channel.send('No.2 ARKサーバを停止します。')

    if message.content == '.ark 3 stop':
        if flag_ark3 == 0:
                await message.channel.send('既に停止しています。')
        elif flag_ark3 == 1:
                flag_ark_UD1 = 2
                await message.channel.send('このコマンドではセーブデータの保存を行いません。セーブデータは15分おきに自動セーブしているので, 現在の進行度を確実に保存するには15分待機してください。サーバを停止する場合はもう一度コマンドを入力してください。')
        elif flag_ark3 == 2:
                flag_ark_3 = 0
                stream = os.popen('arkmanager stop @"Server_name"')
                output = stream.read()
                await message.channel.send('No.3 ARKサーバを停止します。')


    #Server status check command
    if message.content == '.ark 1 status':
        stream = os.popen('arkmanager status @main')
        output = stream.read()
        result = '[0;39m Server listening:  [1;32m Yes [0;39m' in output
        if result == True:
            await message.channel.send('No.1 ARKサーバーはオンラインです')
        elif result == False:
            await message.channel.send('No.1 ARKサーバーはオフラインです')

    if message.content == '.ark 2 status':
        stream = os.popen('arkmanager status @"Server_name"')
        output = stream.read()
        result = '[0;39m Server listening:  [1;32m Yes [0;39m' in output
        if result == True:
            await message.channel.send('No.2 ARKサーバーはオンラインです')
        elif result == False:
            await message.channel.send('No.2ARKサーバーはオフラインです')

    if message.content == '.ark 3 status':
        stream = os.popen('arkmanager status @"Server_name"')
        output = stream.read()
        result = '[0;39m Server listening:  [1;32m Yes [0;39m' in output
        if result == True:
            await message.channel.send('No.3 ARKサーバーはオンラインです')
        elif result == False:
            await message.channel.send('No.3 ARKサーバーはオフラインです')


    #Server version update Command
    if message.content == '.ark 1 update':
        stream = os.popen('arkmanager update @main')
        await message.channel.send('No.1 ARKサーバーのアップデートを行います、完了メッセージが出るまで1~5分ほどお待ちください。')
        output = stream.read()
        await message.channel.send('アップデートの確認または、アップデートが完了しました。')

    if message.content == '.ark 2 update':
        stream = os.popen('arkmanager update @"Server_name"')
        await message.channel.send('No.2 ARKサーバーのアップデートを行います、完了メッセージが出るまで1~5分ほどお待ちください。')
        output = stream.read()
        await message.channel.send('アップデートの確認または、アップデートが完了しました。')

    if message.content == '.ark 3 update':
        stream = os.popen('arkmanager update @"Server_name"')
        await message.channel.send('No.3 ARKサーバーのアップデートを行います、完了メッセージが出るまで1~5分ほどお待ちください。')
        output = stream.read()
        await message.channel.send('アップデートの確認または、アップデートが完了しました。')


    #Server save Command
    if message.content == '.ark 1 save':
        stream = os.popen('arkmanager saveworld @main')
        output = stream.read()
        result = 'World Saved' in output
        if result == True:
            await message.channel.send('No.1 ARKサーバーのセーブが無事完了しました')
        elif result == False:
            await message.channel.send('No.1 ARKサーバーのセーブに失敗しました。')
    
    if message.content == '.ark 2 save':
        stream = os.popen('arkmanager saveworld @"Server_Name"')
        output = stream.read()
        result = 'World Saved' in output
        if result == True:
            await message.channel.send('No.2 ARKサーバーのセーブが無事完了しました')
        elif result == False:
            await message.channel.send('No.2 ARKサーバーのセーブに失敗しました。')

    if message.content == '.ark 3 save':
        stream = os.popen('arkmanager saveworld @"Server_Name"')
        output = stream.read()
        result = 'World Saved' in output
        if result == True:
            await message.channel.send('No.3 ARKサーバーのセーブが無事完了しました')
        elif result == False:
            await message.channel.send('No.3 ARKサーバーのセーブに失敗しました。')


    #Server invite information Command
    if message.content == '.ark 1 invite':
        embed=discord.Embed(title="No.1 ARKサーバー情報", color=0xffffff)
        embed.add_field(name="Steam専用招待リンク", value="your_link", inline=True)
        embed.add_field(name="サーバーアドレス", value="your_address", inline=False)
        embed.add_field(name="パスワード", value="your_password", inline=True)
        await message.reply(embed=embed)

    if message.content == '.ark 2 invite':
        embed=discord.Embed(title="No.2 ARKサーバー情報", color=0xffffff)
        embed.add_field(name="Steam専用招待リンク", value="your_link", inline=True)
        embed.add_field(name="サーバーアドレス", value="your_address", inline=False)
        embed.add_field(name="パスワード", value="your_password", inline=True)
        await message.reply(embed=embed)

    if message.content == '.ark 3 invite':
        embed=discord.Embed(title="No.3 ARKサーバー情報", color=0xffffff)
        embed.add_field(name="Steam専用招待リンク", value="your_link", inline=True)
        embed.add_field(name="サーバーアドレス", value="your_address", inline=False)
        embed.add_field(name="パスワード", value="your_password", inline=True)
        await message.reply(embed=embed)


    #All server information Command
    if message.content == ".ark info":
        embed=discord.Embed(title="登録ARKサーバー一覧", color=0xffffff)
        embed.add_field(name="No.1", value="Server_name", inline=True)
        embed.add_field(name="No.2", value="Server_name", inline=False)
        embed.add_field(name="No.3", value="Server_name", inline=True)
        await message.reply(embed=embed)

client.run(TOKEN)
