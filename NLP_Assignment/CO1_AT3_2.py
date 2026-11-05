
states = ["q0", "q1", "q2"]
alphabet = ["a", "b"]

transition = {
    "q0": {"a": "q1", "b": "q0"},
    "q1": {"a": "q1", "b": "q2"},
    "q2": {"a": "q1", "b": "q0"}
}

initial_state = "q0"
final_states = ["q2"]

n = int(input("Enter number of strings: "))

for i in range(n):
    string = input("Enter string: ")

    current_state = initial_state
    path = [current_state]

    for symbol in string:
        if symbol in alphabet:
            current_state = transition[current_state][symbol]
            path.append(current_state)
        else:
            current_state = "Invalid"
            break

    print("Transition Path:")

    if current_state != "Invalid":
        print(" -> ".join(path))

    if current_state in final_states:
        print("Accepted")
    else:
        print("Rejected")
