
def update_bar(bar, countdown_time):
    if countdown_time > 0:
        countdown_time -= 1
        bar["value"] = countdown_time
        bar.after(1000, lambda: update_bar(bar, countdown_time))
    else:
        bar["value"] = 0

def add_to_bar(bar, increase):

    new_value = min(bar["value"] + increase, 100)
    bar["value"] = new_value

    update_bar(bar, new_value)

