def walk(steps):
    if steps == 0:  # base case
        return
    walk(steps - 1)  # recursive case
    print(f'Step {steps}')

walk(10)