class State:

    def __init__(self, state_id, state_name, affected_count, days_of_lockdown):
        self.state_id = state_id
        self.state_name = state_name
        self.affected_count = affected_count
        self.days_of_lockdown = days_of_lockdown

    def increase_lockdown(self, number_of_weeks):
        if number_of_weeks >= 0:
            self.days_of_lockdown += (number_of_weeks * 7)
        return self.days_of_lockdown
