import discord


#id  = 641887039578701834
def read_token():
    with open("token.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()



token = read_token()




#Connect with the bot
client = discord.Client()
id = client.get_guild(641887039578701834)

@client.event
async def on_member_update(before,after):
    nickname = after.nick
    if nickname:
        if nickname.lower().count("anson") > 0:
            last = before.nick
            if last:
                await after.edit(nick = last)
            else:
                await after.edit(nick = "random name")





@client.event
async def member_join(member):
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome!! {member.mention}!""")

valid_users = ["AChristo01#1943"]




@client.event
async def on_message(message):
    id = client.get_guild(641887039578701834)
    valid_users = ["AChristo01#1943"]
    bad_words = ['damn','holy','shoot']
    #print(message.content)

    for word in bad_words:
        if message.content.count(word) > 0:
            print("A bad word was said man!")
            await message.channel.purge(limit = 1)

    if message.content == "!help":
        embed = discord.Embed(title= "Help on BOT", description="Some useful commands")
        embed.add_field(name='!hello', value = 'Greeting the user')
        embed.add_field(name='!users', value = "Print # of users")
        await message.channel.send(content=None,embed=embed)
    if str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("hi")
        elif message.content == '!users':
            await message.channel.send(f"""# of users: {id.member_count}""")
    else:
        print(f"""User: {message.author} tried to do command {message.content}""")

client.run(token)
