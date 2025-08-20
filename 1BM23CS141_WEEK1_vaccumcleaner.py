import random


environment = {
    "A": "Dirty",
    "B": "Dirty"
}


def simple_reflex_agent(location, environment):
    actions_taken = []
    current_location = location

    for _ in range(2):  
        status = environment[current_location]
        if status == "Dirty":
            actions_taken.append(f"Clean {current_location}")
            environment[current_location] = "Clean"
        else:
            actions_taken.append(f"No cleaning needed at {current_location}")

        
        if current_location == "A":
            actions_taken.append("Move Right to B")
            current_location = "B"
        else:
            actions_taken.append("Move Left to A")
            current_location = "A"

    return actions_taken, environment


def goal_based_agent_simulation(environment, start_location):
    actions = []
    env = environment.copy()
    current_location = start_location

    
    if env[current_location] == "Dirty":
        actions.append(f"Clean {current_location}")
        env[current_location] = "Clean"
    else:
        actions.append(f"No cleaning needed at {current_location}")

    
    other_location = "B" if current_location == "A" else "A"
    actions.append(f"Move to {other_location}")
    current_location = other_location

    if env[current_location] == "Dirty":
        actions.append(f"Clean {current_location}")
        env[current_location] = "Clean"
    else:
        actions.append(f"No cleaning needed at {current_location}")

    return actions, env


def run_simulation():
    print("Initial Environment:", environment)

    # Start location randomly chosen
    start_location = random.choice(["A", "B"])
    print(f"\nSimple Reflex Agent starts at {start_location}")
    reflex_actions, reflex_env = simple_reflex_agent(start_location, environment.copy())
    for step, action in enumerate(reflex_actions, 1):
        print(f"Step {step}: {action}")
    print("Environment after Reflex Agent:", reflex_env)

    print(f"\nGoal-Based Agent starts at {start_location}")
    goal_actions, goal_env = goal_based_agent_simulation(environment, start_location)
    for step, action in enumerate(goal_actions, 1):
        print(f"Step {step}: {action}")
    print("Environment after Goal-Based Agent:", goal_env)

run_simulation()

