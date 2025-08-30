from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("US States guessing game")
image = "C:/Users/mdeha/OneDrive/Masaüstü/python/day25/us_states/blank_states_img.gif"
screen.addshape(image)
turt = Turtle()
turt.shape(image)
data = pd.read_csv("C:/Users/mdeha/OneDrive/Masaüstü/python/day25/us_states/50_states.csv")
turtle_for_writing = Turtle()
guessed_state = []
score = 0
while len(guessed_state) <= 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States correct" , prompt="What is another state's name?").title()
    data_of_state = data[data.state == answer_state]
    print(answer_state)
    if answer_state.lower() == "exit":
        missed_states = []
        for state in data.state:
            if state not in guessed_state:
                missed_states.append(state)
        missing_data = pd.DataFrame(missed_states)
        missing_data.to_csv("C:/Users/mdeha/OneDrive/Masaüstü/python/day25/us_states/states_to_learn.csv")
        break
    if not data_of_state.empty: # empty kullanımı
        if answer_state in guessed_state:
            print("The state you entered has already been entered ")
            continue
        coor_x = int(data_of_state.x)
        coor_y = int(data_of_state.y)
        print(coor_x , coor_y)
        turtle_for_writing.hideturtle()
        turtle_for_writing.penup()
        turtle_for_writing.goto(coor_x , coor_y)
        turtle_for_writing.write(answer_state , align="center" , font=("Arial" , 8 , "normal"))
        guessed_state.append(answer_state)
        score += 1
        print(f"Your current score is {score}")
    else:
        print("Invalid state")



screen.mainloop() # ekran tıklama ile kapanmasın diye