def check_string(s):
    state = 0

    for ch in s:
        if state == 0:
            state = 1 if ch == 'a' else 0
        elif state == 1:
            state = 2 if ch == 'b' else (1 if ch == 'a' else 0)
        elif state == 2:
            state = 1 if ch == 'a' else 0

    return state == 2

s = input("Enter a string: ")

if check_string(s):
    print("String Accepted")
else:
    print("String Rejected")
