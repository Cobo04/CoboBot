# IMPORTANT: Create a suggestions.txt file

@bot.command()
async def request(ctx, *, message=None):
    channel = ctx.message.channel
    person_that_sent_this = str(ctx.message.author)
    with open("suggestions.txt", "r+") as f:
        old = f.read()
        f.seek(0)
        f.write(f"{person_that_sent_this}: {message} : {datetime.now()}\n{old}")
        f.seek(0)
    await channel.send('```Thank you ' + person_that_sent_this + ', Your request has been documented!```')

@bot.command()
async def suggest(ctx, *, message=None):
    channel = ctx.message.channel
    person_that_sent_this = str(ctx.message.author)
    with open("suggestions.txt", "r+") as f:
        old = f.read()
        f.seek(0)
        f.write(f"{person_that_sent_this}: {message} : {datetime.now()}\n{old}")
        f.seek(0)
    await channel.send('```Thank you ' + person_that_sent_this + ', Your request has been documented!```')

@bot.command()
async def req(ctx, *, message=None):
    channel = ctx.message.channel
    person_that_sent_this = str(ctx.message.author)
    with open("suggestions.txt", "r+") as f:
        old = f.read()
        f.seek(0)
        f.write(f"{person_that_sent_this}: {message} : {datetime.now()}\n{old}")
        f.seek(0)
    await channel.send('```Thank you ' + person_that_sent_this + ', Your request has been documented!```')
