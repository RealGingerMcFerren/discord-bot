import discord
import time

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Game('Powering On...'))
        time.sleep(5)
        await client.change_presence(activity=discord.Game('Waiting on Gingers Devices...'))
        time.sleep(3)
        await client.change_presence(activity=discord.Game('Logging in...'))
        time.sleep(10)
        await client.change_presence(activity=discord.Game('Ready to help!'))

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'E':
            await message.channel.send('E')
        if message.content == 'Hey System, Update.':
            await message.channel.send('System 12.6\nIt looks like I\'m already updated.')










client = MyClient()
client.run('TOKEN')
