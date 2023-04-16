import pandas
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()


class SingleState:
    def __init__(self, state):
        self.single_state = state

    def get_x(self):
        return data[data.state == self.single_state].x.to_list()[0]

    def get_y(self):
        return data[data.state == self.single_state].y.to_list()[0]
