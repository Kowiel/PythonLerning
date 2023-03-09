while True:
    date = input("Enter Todays Date \n")
    Mood = input("Rate your Day forom 1- 10 \n")
    Text = input("Tell me something about the day \n")

    with open(f"Jornual/Jornual-{date}-[{Mood}].txt","w") as file:
        file.writelines(Text)

    redo = input("Again? [Y / N]")
    if(redo=="Y"):
        continue
    if (redo=="N"):
        break
