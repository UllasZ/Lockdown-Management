import state
import country


def main():
    states_list = []
    test_case = int(input("Number of state objects : "))

    for x in range(test_case):
        s_id = int(input("Enter State_Id: "))
        s_name = input("Enter State_Name : ")
        affected = int(input("Affected Count : "))
        days = int(input("Lockdown Days : "))
        print("\n")
        s = state.State(s_id, s_name, affected, days)
        states_list.append(s)

    c = country.Country(states_list)
    select_state_id = int(input("Enter State ID : "))
    increased_weeks = int(input("Increased weeks : "))

    state_name, updated_days = c.calculate_increase_in_lockdown_period(select_state_id, increased_weeks)
    if updated_days == -1:
        print(state_name)
    else:
        print(state_name, updated_days)


if __name__ == "__main__":
    main()
