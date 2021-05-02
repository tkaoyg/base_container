from slacker import Slacker
import slackbot_settings

def getid():
    slacker = Slacker(slackbot_settings.API_TOKEN)

    res = slacker.users.list()
    for member in res.body["members"]:
        print(member["name"])
        print(member["id"])
        print()
        

