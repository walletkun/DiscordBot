import discord
from discord.ext import commands
import csv
import datetime

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

workout_file = "WorkOutLogs.csv"
user_file = "Users.csv"


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.command()
async def log_workouts(ctx, workout_names = "No Name",sets = 0,weights =0,reps=0):
    workout_data = [workout_names,sets,weights,reps, datetime.datetime.now().strftime("%m-%d-%Y")]

    #open csv 
    with open(workout_file, "a", newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(workout_data)

    await ctx.send(f"Workout for the day:\nWorkout: {workout_names}\nSets: {sets}\nWeights: {weights}\nReps: {reps}\nLogged Time: {workout_data[4]}")

@bot.command()
async def view_workouts(ctx):
    #read and send all logged workouts from the CSV file
    workouts = []
    with open(workout_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            workouts.append(row)

    if not workouts:
        await ctx.send("No workouts logged yet.")
    else:
        message = "Logged workouts:\n"
        for workout in workouts:
            message += f"Workout: {workout[0]}\nSets: {workout[1]}\nWeight: {workout[2]} lbs\nReps: {workout[3]}\nLogged at: {workout[4]}\n\n"
        await ctx.send(message)


@bot.command()
async def remove_workout(ctx, workout_name_remove,workout_date):
    workout = []
    workout_to_remove = []

    #read the csv
    with open(workout_file, 'r',newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)


        for row in data:
            if row[0].strip().lower() == workout_name_remove.strip().lower():
                if row[4] == workout_date:
                    workout_to_remove.append(row)
            else:
                workout.append(row)
        
    if not workout:
        await ctx.send(f"No workouts found with the name '{workout_name_remove}' for the date: {workout_date}")
    
    else:
        with open(workout_file, 'w', newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(workout)
        if workout:
            message = "Removed the following workouts:\n"
            for workout in workout_to_remove:
                message += f"Workout: {workout[0]}\nSets: {workout[1]}\nWeight: {workout[2]} lbs\nReps: {workout[3]}\nLogged at: {workout[4]}\n\n"

            await ctx.send(message)

@bot.command()
async def get_help(ctx):
    help_message = "Here's how to use the bot:\n\n" \
                   "To log a workout, use the command:\n" \
                   "`!log_workouts workout_name sets weight reps`\n" \
                   "For example: `!log_workout BenchPress 3 135 10`\n" \
                   "Make sure to provide valid integers for sets, weight, and reps.\n\n" \
                   "To view your logged workouts, use the command:\n" \
                   "`!view_workouts`\n\n" \
                   "To remove a workout, use the command:\n" \
                   "`!remove_workout index`\n" \
                   "For example, to remove the first workout, use `!remove_workout 1`.\n" \
                   "Make sure to provide a valid index.\n\n" \
                   "To get help, simply type `!get_help`."

    await ctx.send(help_message)




bot.run("BotToken")

