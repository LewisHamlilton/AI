def run_cleaning_bot():
    current_room = input("Enter start room (A/B): ").strip().upper()
    if current_room not in ['A', 'B']:
        print("Invalid start room. Defaulting to A.")
        current_room = 'A'
    status = {
        'A': input("Room A dirty? (1=Yes, 0=No): ").strip(),
        'B': input("Room B dirty? (1=Yes, 0=No): ").strip()
    }
    if status['A'] not in ['0', '1'] or status['B'] not in ['0', '1']:
        print("Invalid dirt input detected. Setting both rooms as dirty (1).")
        status['A'], status['B'] = '1', '1'
    total_cost = 0
    CLEAN_COST = 7
    MOVE_COST = 1
    while '1' in status.values():
        print("\n---------------------------------")
        print(f"Position: {current_room} | A={status['A']} B={status['B']} | Cost={total_cost}")

        if status[current_room] == '1':
            status[current_room] = '0'
            total_cost += CLEAN_COST
            print(f"Operation: CLEAN {current_room} (+{CLEAN_COST})")
        else:
            if current_room == 'A':
                current_room = 'B'
                print(f"Operation: MOVE RIGHT to B (+{MOVE_COST})")
            else:
                current_room = 'A'
                print(f"Operation: MOVE LEFT to A (+{MOVE_COST})")
            total_cost += MOVE_COST

    print("\nFinished Cleaning Process.")
    print(f"Total Cost: {total_cost}")

if __name__ == "__main__":
    run_cleaning_bot()
