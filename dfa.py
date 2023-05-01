# define the DFA
dfa = {
    'q0': {'0': 'q0', '1': 'q1'},
    'q1': {'0': 'q1', '1': 'q2'},
    'q2': {'0': 'q2', '1': 'q3'},
    'q3': {'0': 'q3', '1': 'q4'},
    'q4': {'0': 'q4', '1': 'q1'},
}

# define the accepting state
accepting_state = 'q4'

def simulate_dfa(dfa, accepting_state, input_string):
    current_state = 'q0'
    for symbol in input_string:
        if symbol not in dfa[current_state]:
            return False
        current_state = dfa[current_state][symbol]
    return current_state == accepting_state

# test the DFA
input_string = str(input("Enter a string with 0 and 1"))
if simulate_dfa(dfa, accepting_state, input_string):
    print(f"The input string '{input_string}' is accepted.")
else:
    print(f"The input string '{input_string}' is rejected.")
