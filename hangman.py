mport discord
import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '4 ')

@client.event
async def on_ready():
    print("Bot is Ready.")
    await client.change_presence(activity=discord.Game('being four.'))

@client.command()
async def hangman(ctx):
    author = ctx.message.author
    channel = ctx.channel
    def msg_check(m):
        return m.author == author and m.channel == channel

    lst_of_words=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "canyon", "dinosaur", "volcano", "fungus", "cabinet", "laptop", "goldfish", "pistachio", "electricity", "television",  "coffee"]
    word=random.choice(lst_of_words)
    counter=len(word)
    letters_guessed=[]
    word_formation=[]
    num_of_tries=len(word)+2
    checker=0
    f = num_of_tries

    for t in range(counter):
        word_formation.append(" _ ")

    for i in range(num_of_tries):
        theguess = discord.Embed(
        title = "Hangman",
        description = "What is your guess?",
        colour = discord.Colour.red()
        )
        await ctx.send(embed = theguess)
        guess=(await client.wait_for("message", check=msg_check)).content

        f = f-1


        if(guess == "end"):
            end = discord.Embed(
            description = "Thanks for playing!",
            colour = discord.Colour.gold()
            )
            await ctx.send(embed = end)
            checker = 1
            break

        if(len(guess)>1 and guess==word):
            correct = discord.Embed(
                title = "You Win!",
                description = "The word was: "+str(word),
                colour = discord.Colour.green()
            )
            await ctx.send(embed = correct)
            checker=1
            break

        letters_guessed.append(guess)
        description = discord.Embed(
            title = "Letters Guessed", 
            description = str(letters_guessed), 
            colour = discord.Colour.red()
            )

        description.add_field(name = "Number of Tries Left", value = f, inline = False)


        if(guess in word and len(guess)==1):
            correctletter = discord.Embed(
            description = str(guess)+" is correct.",
            colour = discord.Colour.green()
            )
            await ctx.send(embed = correctletter)
            counter=counter-word.count(guess)

            for n in range(0,len(word)):
                if(word[n]==guess):
                    word_formation[n]=guess
        else:
            wrongletter = discord.Embed(
            description = "wrong.",
            colour = discord.Colour.red()
            )
            await ctx.send(embed = wrongletter)

        if(counter==0):
            correct2 = discord.Embed(
                title = "You Win!",
                description = "The word was: "+str(word),
                colour = discord.Colour.green()
            )
            await ctx.send(embed = correct2)
            break

        description.add_field(name = "The Word", value = word_formation, inline = True)
        await ctx.send(embed = description)


    if(checker==0 and counter != 0):
        ranout = discord.Embed(
            description = "you are out of tries, the word was: "+str(word),
            colour = discord.Colour.red()
        )
        await ctx.send(embed = ranout)