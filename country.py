class Country:
    def __init__(self, state_list, country_name="India"):
        self.country_name = country_name
        self.state_list = state_list

    def calculate_increase_in_lockdown_period(self, state_id, increase_number_of_lockdown_weeks):
        for i in self.state_list:
            if state_id == i.state_id:
                i.increase_lockdown(increase_number_of_lockdown_weeks)
                return i.state_name, i.days_of_lockdown

        return "No State Exists", -1
