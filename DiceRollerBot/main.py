import discord
import re
import random

token = 'ODAxNjM2NzYzNDI0MzkxMTY4.YAjkag.fB8pfCxsX66vil0pE8vkJIBIau4'

client = discord.Client()

@client.event
async def on_message(message):
    channels = ["geral"]
    if str(message.channel) in channels:
        nTotal=0
        if re.search(r'\d+d\d+', message.content):
            await message.channel.send(f"<@{message.author.id}> rolled:\n")
            numbers = re.findall('\d+d\d+', message.content)
            numbers = [j for sub in [x.split('d') for x in numbers] for j in sub]
            while numbers!=[]:
                diceNumber = numbers[0]
                rollType = numbers[1]
                total = []
                for i in range(int(diceNumber)):
                    number = random.randint(1,int(rollType))
                    if number == int(rollType):
                        total.append(f'#{rollType}')
                    elif number == 1:
                        total.append('[1]')
                    else:
                        total.append(f'{number}')
                nTotal += sum([int(re.findall('\d+', x)[0]) for x in total])
                [numbers.pop(0) for x in range(2)]
                await message.channel.send(f"```CSS\n.{diceNumber}D{rollType}:  {str([x for x in total])[1:-1]}\n```")
            Message = message.content.replace(' ', '').replace('+',' ')
            bonus = sum([int(x) for x in Message.split() if 'd' not in x and x.isnumeric()])
            nTotal+=bonus
            await message.channel.send(f"Result: `{nTotal}`")






client.run(token)
