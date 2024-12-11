#Dictionary that tracks current instances of the health bars
active_updates = {}

# For checking if the pet should faint
hungerBarValueZero = False
energyBarValueZero = False

def update_bar(bar, countdown_time):
    global hungerBarValueZero, energyBarValueZero
    bar_id = id(bar) #Gives each instance unique ID
    
    if countdown_time > 0:
        countdown_time -= 1
        bar["value"] = countdown_time
        #Adds bar to active updates
        active_updates[bar_id] = bar.after(1000, lambda: update_bar(bar, countdown_time))
    else:
        bar["value"] = 0

        if str(bar) == ".!mainscreen.!progressbar2":
            hungerBarValueZero = True
        if str(bar) == ".!mainscreen.!progressbar3":
            energyBarValueZero = True

        active_updates.pop(bar_id, None)  #Removes the bar from active updates

def add_to_bar(bar, increase):
    global hungerBarValueZero, energyBarValueZero
    bar_id = id(bar)

    if str(bar) == ".!mainscreen.!progressbar2":
            hungerBarValueZero = False
    if str(bar) == ".!mainscreen.!progressbar3":
            energyBarValueZero = False
    
    #Cancels any current countdown for this bar
    if bar_id in active_updates:
        bar.after_cancel(active_updates[bar_id])
        active_updates.pop(bar_id, None)
    
    #Updates the bar and start a new countdown
    new_value = min(bar["value"] + increase, 21600)
    bar["value"] = new_value
    update_bar(bar, new_value)

# If both true, the pet will faint
def faintCheck():
    if hungerBarValueZero and energyBarValueZero:
        #print("fainted!")
        return True
    else:
        #print("alive")
        return False
