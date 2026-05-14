# Discord_ArkServerControl

## Download
[Click](https://github.com/rainbow0210/ArkServerControl/archive/refs/heads/main.zip)

## Table of contents
[Japanese](https://github.com/rainbow0210/ArkServerControl#japanese)

[English](https://github.com/rainbow0210/ArkServerControl#english)

# Japanese

## 使用言語
Python

## 動作確認済み環境
Ubuntu

ArkManager

Screen

Python 3

discord.py

## 概要

Discord上からArkmanagerを操作し、ARKサーバーの起動、停止、状態確認、アップデート、セーブを行うためのbotです。Linux環境での利用を前提としています。

番号ごとのコマンドを追加することで、対応するサーバー数を増やせます。

## 動作方法

1. Python 3 を用意し、`discord.py` は `pip` でインストールします。
2. `bot.py` の `TOKEN` をご自身のDiscord Botトークンに置き換えます。
3. `bot.py` 内の `Server_name`、`your_link`、`your_address`、`your_password` を実際の環境に合わせて編集します。
4. Arkmanager を導入し、`arkmanager` コマンドが実行できる状態にします。
5. `python3 bot.py` を実行します。

ArkManager のインストール方法は、[こちらの README](https://github.com/arkmanager/ark-server-tools/blob/master/README.asciidoc) を参考にしてください。

`start.sh` は通常起動用、`start_screen.sh` は Screen 経由で起動するためのスクリプトです。

## 設定

このbotは設定ファイルを持たず、`bot.py` を直接編集して設定します。

主な設定項目は次の通りです。

* `TOKEN`: Discord Botトークン
* `@main` / `Server_name`: Arkmanager のサーバー識別子
* `your_link`: Steam専用招待リンク
* `your_address`: サーバーアドレス
* `your_password`: サーバーパスワード

## 利用したもの、参考にしたサイト

* コードのベースにさせていただいた方の記事：[https://qiita.com/Mikage32/items/93ffc30a62480d39e82e](https://qiita.com/Mikage32/items/93ffc30a62480d39e82e)

* Discord.py：[https://github.com/Rapptz/discord.py](https://github.com/Rapptz/discord.py)

# English

## Use Language
Python

## Operationg environment
Ubuntu 

ArkManager

Screen

Python 3

discord.py

## Expanation

This bot controls ARK servers from Discord by calling Arkmanager commands. It is intended for Linux environments where Arkmanager is already installed.

You can increase the number of supported servers by adding more numbered command blocks.

## How to use?

1. Install Python 3, and install `discord.py` with `pip`.
2. Replace `TOKEN` in `bot.py` with your Discord bot token.
3. Update `Server_name`, `your_link`, `your_address`, and `your_password` in `bot.py`.
4. Install Arkmanager and make sure the `arkmanager` command is available.
5. Run `python3 bot.py`.

For ArkManager installation instructions, refer to [this README](https://github.com/arkmanager/ark-server-tools/blob/master/README.asciidoc).

`start.sh` is for a normal launch, and `start_screen.sh` is for launching inside Screen.

## Configuration

This bot does not use a separate config file. Edit `bot.py` directly.

Main values to update:

* `TOKEN`: Discord bot token
* `@main` / `Server_name`: Arkmanager server identifiers
* `your_link`: Steam invite link
* `your_address`: Server address
* `your_password`: Server password

## Extension library and use data

* This bot code base article：[https://qiita.com/Mikage32/items/93ffc30a62480d39e82e](https://qiita.com/Mikage32/items/93ffc30a62480d39e82e)

* Discord.py：[https://github.com/Rapptz/discord.py](https://github.com/Rapptz/discord.py)
