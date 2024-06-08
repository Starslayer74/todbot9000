import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

truths = [
   "Have you ever hooked up with someone you met at a party?",
   "Have you ever hooked up with someone on the server?",
"What's the most awkward thing you've done while trying to impress someone?",
"Have you ever been caught in a compromising position by a friend?",
"Have you ever had a crush on someone you've never met in person?",
"Have you ever been caught doing something inappropriate at work?",
"Have you ever had a crush on a fictional character?",
"Have you ever hooked up with someone much older than you?",
"Have you ever hooked up with someone much younger than you?",
"What's the most outrageous thing you've done while traveling?",
"Have you ever had a crush on a friend's parent?",
"Have you ever hooked up with someone who was off limits (friend's parent, friend's sibling, priest, your doctor, married friend)?",
"What's the most embarrassing thing you've done while trying to be sexy?",
"Have you ever been caught doing something inappropriate at a family gathering?",
"What's the most intimate thing you've done at a friend's house?",
"Have you ever had a crush on a stranger you saw in public?",
"What's the most embarrassing thing you've done to get out of trouble?",
"Have you ever had a crush on a neighbor?",
"What's the most embarrassing thing you've done while flirting?",
"Have you ever been caught doing something inappropriate at a wedding?",
"What's the most intimate thing you've done in a public place?",
"Have you ever had a crush on a celebrity?",
"Have you ever been caught doing something inappropriate at school?",
"What's the most outrageous thing you've done in a classroom?",
"Have you ever had a crush on a friend's partner?",
"What's the most embarrassing thing you've done to get someone's number?",
"What's the most intimate thing you've done in a movie theater?",
"Have you ever had a crush on a family member's friend?",
"What's the most embarrassing thing you've done to impress someone?",
"Have you ever been caught doing something inappropriate at a friend's house?",
"What's the most outrageous thing you've done in a hotel room?",
"Have you ever had a crush on a friend's sibling?",
"What's the most embarrassing thing you've done to get out of a bad date?",
"Have you ever hooked up with someone you met online?",
"What's the most intimate thing you've done in a public restroom?",
"Have you ever had a crush on someone you've never met in person?",
"What's the most embarrassing thing you've done to avoid a date?",
"Have you ever been caught doing something inappropriate at work?",
"What's the most outrageous thing you've done to get someone's attention?",
"Have you ever been arrested or warned by authorities for lewed behavior?",
"What's the most intimate thing you've done on a first date?",
"Have you ever been caught doing something inappropriate in a car?",
"What's the most outrageous thing you've done while traveling?",
"Have you ever had a crush on a stranger you saw in public?",
"Have you ever been caught doing something inappropriate at a concert?",
"What's the most outrageous thing you've done at a music festival?",
"Have you ever had a crush on a neighbor?",
"What's the most intimate thing you've done in a public place?",
"Have you ever had a crush on a celebrity?",
"Have you ever had a crush on a friend's partner?",
"Have you ever had a crush on a family member's friend?",
"Have you ever had a crush on a friend's sibling?",
"Have you ever been caught in a compromising position by a friend?",
"Have you ever had a crush on someone you've never met in person?",
"What is your biggest turn-on?",
"What is your biggest turn-off",
"What sex act are you the best at?",
"Are you a part of the mile high club?", 
"What is your favorite body part?",
"Have you ever gone skinny dipping?", 
"Have you ever gone streaking?", 
"Name the weirdest place you've had sex",
"Have you ever faked an orgasm?",
"Tell us your most embarrasing sexual story",
"Tell us about your fetishes. Use /spoiler tags if you feel it is appropriate",
"Lights on or lights off during sex?",
"Have you ever had a one night stand?", 
"What is your guilty pleasure in the bedroom?", 
"What is the weirdest place you've peed?",
"Do you like watersports?",
"Have you ever tasted your own fluids?",
"What is the kinkiest thing you've ever tried/done?",
"Does size really matter?",
"Favorite sexual position",
"Have you ever filmed a sex tape?", 
"Loud and in your face, or silent but deadly?",
"What nonsexual thing turns you on?",
"Have you ever had sex with multiple partners in one day? If so, did you bathe in between partners?",
"Have you ever turned down sex and regretted it?", 
"Have you ever accidentally sent a sext to the wrong person? If so, who, and what happened?",
"What is the sexiest song you've ever heard?", 
"What is the highest number of orgasms that you personally have achieved in one day?", 
"What is the weirdest sexual dream you've ever had?",
"What is your favorite sex toy?",
"Have you ever masturbated using something that wasn't intended for masturbation? What was it?", 
"What is your fantasy?",
"Have you ever been to a sex club?",
"Have you ever caught someone having sex and then joined in?",
"What is your favorite porn genre?",
"What sex act do you believe is overrated?",
"What sex act do you believe is underrated?", 
"Are you dominant, submissive, or a switch?", 
"Which is your favorite kind of sex: soft, slow, and sweet or aggressive, fast, and feisty?",
"If you were to create an original sex move, what would you call it?",
"If you could only have sex in one position for a month, what position would you pick?",
"How often do you masturbate?", 
"How do you feel about threesomes? Ever had one? If not, would you?",
"Have you ever fallen asleep during sex?",
"Where do you like to cum/be cummed on?"

]

dares = [
    "Post an implied nude selfie in the appropriate channel",
    "Post a nude selfie in the appropriate channel",
    "Share what you love the most about the owner of the server",
    "Write a message in this channel using only your penis or nipple",
    "Only use GIFs to communicate on the server for the next hour",
    "Pretend to be one of the last person who took a truth question",
    "Send your ex a message that you miss them",
    "Ask Wisteria Nyx to look at pictures of a mysterious rash you have on your balls/vagina",
    "Find something phallic shaped, suck on it and post a picture",
    "Take a photo of yourself sucking your fingers",
    "Use the microphone to post an audio message of yourself faking an orgasm",
    "Use the microphone to say something sexy and post it in this channel", 
    "Put an ice cube on your nipple and post a photo of your now engorged nippynoppy",
    "Find the most disturbing definition you can think of on Urban Dictionary and post a link to it here", 
    "Tell us a dirty secret about yourself", 
    "Share your phones search history", 
    "Try to sell us a sex toy that scares you personally", 
    "Write LIME GANG 4 LYFE on your body somewhere and post a picture",
    "Use the microphone to post an audio message of yourself talking in an accent other than your own",
    "Using the microphone, sing us a song that you made up on the spot",
    "Go visit www.chickenonaraft.com and come back and tell us how long you could last",
    "Post a video of yourself twerking in the appropriate channel",
    "Post a picture of your foot in the appropriate channel", 
    "Give us your cheesiest pick up line",
    "Give us the best pick up line that has worked for you", 
    "Flirt, poorly, with the person who posted above you",
    "Using remix, change one of your photos and post it here", 
    "Use the microphone and read us the last naughty message you sent/received", 
    "Imagine the last 4 people to post in this channel in an orgy. Now tell us about how it all goes down", 
    "Link us to your favorite porn genre on pornhub",
    "Tell us how to make you cum", 
    "Fuck, Marry, Kill - last three people to post in the channel",
    "Missionary, Doggy, or Double Reverse Piledriver with a sparkler in their ass - last three people in to post in the channel",
    "Touch yourself for three minutes, then come back and tell us what you touched and how it felt",
    "Use the microphone and imitate what you think the last person to post in the channel sounds like when they have an orgasm",
    "Post a selfie of your O Face in the appropriate channel",
    "Put whipped cream and sprinkles on the body part of your choosing and then take a photo of yourself (or someone else) licking it off",
    "Two words: ANAL HIJINKS. You decide what that means"    
    
]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='t')
async def truth(ctx):
    await ctx.send(random.choice(truths))

@bot.command(name='d')
async def dare(ctx):
    await ctx.send(random.choice(dares))

@bot.command()
async def truth(ctx):
    await ctx.send(random.choice(truths))

@bot.command()
async def dare(ctx):
    await ctx.send(random.choice(dares))

bot.run('MTE5NDM5ODY5MTE3NjQ4NDkzNg.G36h9v.oZzyz8JD2x0EHjuoMHjiHJIqcrV0tgbVx4-Uo4')
