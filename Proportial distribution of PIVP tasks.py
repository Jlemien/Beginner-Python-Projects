# population and weights taken from https://stackoverflow.com/questions/4265988/generate-random-numbers-with-a-given-numerical-distribution

from random import choices

while True:
    try:
        task_to_be_assigned = str(input("Which task do you need to assign? Type the name of one of the following PIVP steps: QR, NPC, M&U, FC, or IQC: ")).upper()
    except ValueError:
        print("Please type the name of one of the following PIVP steps: QR, NPC, M&U, FC, or IQC.")
        continue
    # if task_to_be_assigned not in ("QR", "NPC", "M&U", "FC", "IQC"):
    #     print("Please type the name of one of the following PIVP steps: QR, NPC, M&U, FC, or IQC.")
    #     continue

    else:
        if task_to_be_assigned == str("QR"):
            population = ["Intern #1", "Intern #2", "Lara", "Caitlin", "Joseph", "Rachel"]
            weights = [0.33, 0.30, 0.21, 0.1, 0.05, 0.01]
            result = (choices(population, weights))
            print("You should assign this QR to", result)

        if task_to_be_assigned == str("NPC"):
            population = ["Intern #1", "Intern #2", "Lara", "Caitlin", "Joseph", "Rachel"]
            weights = [0.33, 0.30, 0.21, 0.1, 0.05, 0.01]
            result = (choices(population, weights))
            print("You should assign this NPC to", result)

        if task_to_be_assigned == str("M&U"):
            population = ["Intern #1", "Intern #2", "Lara", "Caitlin", "Joseph", "Rachel"]
            weights = [0.33, 0.30, 0.21, 0.1, 0.05, 0.01]
            result = (choices(population, weights))
            print("You should assign this M&U to", result)

        if task_to_be_assigned == str("FC"):
            population = ["Intern #1", "Intern #2", "Lara", "Caitlin", "Joseph", "Rachel"]
            weights = [0.33, 0.30, 0.21, 0.1, 0.05, 0.01]
            result = (choices(population, weights))
            print("You should assign this FC to", result)

        if task_to_be_assigned == str("IQC"):
            population = ["Intern #1", "Intern #2", "Lara", "Caitlin", "Joseph", "Rachel"]
            weights = [0.33, 0.30, 0.21, 0.1, 0.05, 0.01]
            result = (choices(population, weights))
            print("You should assign this IQC to", result)
