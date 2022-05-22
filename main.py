# This Program was made for the HighTechHacks Hackathon
import discord
from discord.ext import commands

channel_id = 977649964660457503

Vishnu = commands.Bot(command_prefix = "$") # requires dollar sign before command execution. Vishnu is also the god of Karma in Hindu 

good_Karma = ["congrats", "well done", "great job", "amazing", "awesome", "nice", "superb"]

bad_Karma = ["you suck", "hate you", "screw", "frick", "arse"]

counter = 0

@Vishnu.event
async def on_ready():
  print("He has awakened...")
  await Vishnu.change_presence(activity=discord.Game(name='Constantly Judging'))

# function that adds words to the good karma list
@Vishnu.command(pass_context=True)
async def addGoodWord(ctx, word):
    good_Karma.append(word)
    await ctx.author.send(word + " has been added to the good karma list")
    await ctx.message.delete()

# function that removes words from the good karma lsit
@Vishnu.command(pass_context=True)
async def delGoodWord(ctx, word):
    good_Karma.remove(word)
    await ctx.author.send(word + " has been removed from the good karma list.")
    await ctx.message.delete()

# function that adds words to the bad karma list
@Vishnu.command(pass_context=True)
async def adBadWord(ctx, word):
    bad_Karma.append(word)
    await ctx.author.send(word + " has been added to the bad karma list")
    await ctx.message.delete()

# function that removes words from the bad karma lsit
@Vishnu.command(pass_context=True)
async def delBadWord(ctx, word):
    bad_Karma.remove(word)
    await ctx.author.send(word + " has been removed from the bad karma list.")
    await ctx.message.delete()

#sends good karma words to user
@Vishnu.command(pass_context=True)
async def goodWordsList(ctx):
    await ctx.author.send("The good words are: " + str(good_Karma))

#sends bad karma words to user
@Vishnu.command(pass_context=True)
async def badWordsList(ctx):
    await ctx.author.send("The good words are: " + str(bad_Karma))

@Vishnu.command(pass_context=True)
async def displayKarma(ctx):
  await ctx.author.send("Karma count: " + str(counter))

#sents list of commands to user
@Vishnu.command(pass_context=True)
async def displayCommands(ctx):
    await ctx.author.send("Commands list: \n" 
    " - $addGoodWord (desired word) - adds the word that you want in the good karma list \n"
    " - $removeGoodWord (desired word) - removes the word that you want in the good karma list \n"
    " - $addBadWord (desired word) - adds the word that you want in the bad karma list \n"
    " - $removeBadWord (desired word) - removes the word that you want in the bad karma list \n"
    " - $goodWordsList - prints the good karma list \n"
    " - $badWordsList - prints the bad karma list \n"
    " - $displayCommands - prints the list of commands")

# automatically tallies karma
@Vishnu.event
async def on_message(message):
  global counter
  author_id = message.author.id
  delGoodKeyword = "#delGoodWord"
  delBadKeyword = '#delBadWord'
  if(author_id != channel_id):
      for word in good_Karma:
          if((word in message.content) and (delGoodKeyword not in     message.content)):
            counter += 1
      for word in bad_Karma:
          if((word in message.content) and (delBadKeyword not in     message.content)):
            counter -= 1
      await Vishnu.process_commands(message)

Vishnu.run("TOKEN")
