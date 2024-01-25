import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

state_info = pandas.read_csv("50_states.csv")
game_on = True
guessed_states = []
all_states = state_info.state.tolist()
while game_on:

    answer_state = screen.textinput(title="Guess the state", prompt="Can you name another state?")

    if answer_state:

        if answer_state.title() == "Exit":
        #     missing_states = []
        #     for state in all_states:
        #         if state not in guessed_states:
        #             missing_states.append(state)
            missing_states = [state for state in all_states if state not in guessed_states]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("States_to_learn.csv")
            break
        if answer_state.title() in (state_info.state.tolist()):
            guessed_states.append(answer_state.title())
            correct_state_info = state_info[state_info.state == answer_state.title()]
            x_cor = int(correct_state_info.x)
            y_cor = int(correct_state_info.y)
            state = turtle.Turtle()
            state.penup()
            state.hideturtle()
            state.goto(x_cor, y_cor)
            state.write(answer_state, align="center")
        else:
            continue
        print(guessed_states)

    else:
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

screen.exitonclick()

# coordinaten op een afbeelding printen (voor copy pasta):
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()