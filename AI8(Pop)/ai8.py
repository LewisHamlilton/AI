def partial_order_planner(initial_state, goal_state):
    plan = ["Start"]
    curr = initial_state.copy()

    print("\nInitial State:", curr)
    print("Goal State:", goal_state)

    step = 1
    for goal in goal_state:
        if goal not in curr:
            print("\nStep", step, ": Achieving goal ->", goal)
            block, pos = goal.split("-")
            
            action = f"Put {block} on table" if pos == "table" else f"Stack {block} on {pos}"
            print("Action added to plan:", action)
            
            plan.append(action)
            curr.append(goal)
            print("Current State:", curr)
            step += 1

    plan.append("Finish")
    print("\nFinal Plan:\n" + "\n".join(plan))

initial_input = input("Enter initial state (comma separated, e.g. A-table,B-A): ")
goal_input = input("Enter goal state (comma separated, e.g. C-B,A-C): ")

initial = [x.strip() for x in initial_input.split(",")]
goal = [x.strip() for x in goal_input.split(",")]

partial_order_planner(initial, goal)
