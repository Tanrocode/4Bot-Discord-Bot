import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '4 ')

@client.event
async def on_ready():
    print("Bot is Ready.")
    await client.change_presence(activity=discord.Game('being four.'))

@client.command()
async def numbergame(ctx):
    author = ctx.message.author
    channel = ctx.channel
    def msg_check(m):
        return m.author == author and m.channel == channel

    main = discord.Embed(
        title = "Number Game!",
        colour = discord.Colour.gold()
    )



    y = random.randint(1,15)
    tries=3
    done=3
    guessno=0


    for i in range(1, done+1):
        main2 = discord.Embed(
        description = "Enter a value between 1 and 15.",
        colour = discord.Colour.red()
        )
        await ctx.send(embed = main2)    

        x = await client.wait_for('message', check=msg_check)

        tries=tries-1
        guessno=guessno+1
        x = int(x.content)

        if (x < 1 or x > 15):
            main.add_field(name = "Guess #" + guessno, value = x, inline = False )
            main.set_footer(text = "The number you have chosen is not within the given range!"+" You have "+str(tries)+" more guesses.")
            await ctx.send(embed = main)


        elif x == y:
            main.add_field(name = "Guess #" + str(guessno), value = x, inline = False )
            main.set_footer(text = "You guessed it!")
            await ctx.send(embed = main)
            break
        elif(y-3<x<y+3):
            main.add_field(name = "Guess #" + str(guessno), value = x, inline = False )
            main.set_footer(text = "You were very close!"+" You have "+str(tries)+" more guesses.")
            await ctx.send(embed = main)
        elif(x<y):
            main.add_field(name = "Guess #" + str(guessno), value = x, inline = False )
            main.set_footer(text = "You were too low!"+" You have "+str(tries)+" more guesses.")
            await ctx.send(embed = main)
        elif(x>y):
            main.add_field(name = "Guess #" + str(guessno), value = x, inline = False )
            main.set_footer(text = "You were too high!"+" You have "+str(tries)+" more guesses.")
            await ctx.send(embed = main)
        else:
            main.set_footer(text = "Invalid Response!"+" You have "+str(tries)+" more guesses.")
            await ctx.send(embed = main)

    if (i==done and x != y):
        main3 = discord.Embed(
            description = f"You ran out of tries, the number was {y}",
            colour = discord.Colour.red()
        )
        await ctx.send(embed = main3)