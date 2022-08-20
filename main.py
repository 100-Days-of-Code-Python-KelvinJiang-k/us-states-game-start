import pandas
import turtle

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("USA States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.Turtle(image)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()


def check_correct_state(guess_state):  # can replace with if... in
    for state in data["state"]:
        if guess_state.lower() == state.lower():
            return True
    return False
    # less readability
    # return len(data[data["state"] == state]) > 0


def check_duplicate_state(guess_state):
    for state in guessed_states:
        if guess_state == state:
            return True
    return False


def update_map(guess_state):
    update_state = data[data["state"] == guess_state]
    pen.goto(update_state.x.item(), update_state.y.item())
    pen.write(f"{answer_state.title()}", False, "center", ("Arial", 8, "normal"))


correct_count = 0
guessed_states = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{correct_count}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # Generate learning file
    if answer_state.lower() == "exit":
        missing_states = [state for state in data["state"] if state not in guessed_states]

        # missing_states = []
        # for state in data["state"]:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        data_dict = {
            "missed states": missing_states
        }

        df = pandas.DataFrame(data_dict)
        df.to_csv("states_to_learn.csv")
        break

    if check_correct_state(answer_state) and not check_duplicate_state(answer_state):
        guessed_states.append(answer_state)
        update_map(answer_state.title())
        correct_count += 1

    if correct_count >= 50:
        game_is_on = False


turtle.mainloop()
