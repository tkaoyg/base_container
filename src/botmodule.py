from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slacker import Slacker
import screenshot
import slackbot_settings

# respond_to : メンションに応答
@respond_to("こんにちは")
def greeting_1(message):
    message.reply("こんにちは！")

# listen_to : メンションがなくても特定の文字列に応答する
@listen_to("あいうえお")
def greeting_2(message):
    message.reply("メンション：あいうえお　と入力されました")
    message.send("通常の投稿：aaa")
    # message.react("melon") # メロン絵文字をリアクション

@respond_to("!dam")
def greeting_2(message):
    screenshot.screen()
    slacker = Slacker(slackbot_settings.API_TOKEN)
    channel = "tst"
    file = "C:/Users/ao/Desktop/image/screen.png"

    slacker.files.upload(file_=file, channels=channel)
    message.send("file uploaded")

    