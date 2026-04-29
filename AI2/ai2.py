def run_cleaning_bot():
    r = input("Enter start room (A/B): ").strip().upper()
    if r not in ['A', 'B']:
        print("Invalid start room. Defaulting to A.")
        r = 'A'

    s = {k: input(f"Room {k} dirty? (1=Yes, 0=No): ").strip() for k in ['A', 'B']}
    if any(v not in ['0', '1'] for v in s.values()):
        print("Invalid dirt input detected. Setting both rooms as dirty (1).")
        s = {'A': '1', 'B': '1'}

    cost = 0
    while '1' in s.values():
        print(f"\n---------------------------------\nPosition: {r} | A={s['A']} B={s['B']} | Cost={cost}")
        if s[r] == '1':
            s[r] = '0'
            cost += 7
            print(f"Operation: CLEAN {r} (+7)")
        else:
            direction = "RIGHT to B" if r == 'A' else "LEFT to A"
            r = 'B' if r == 'A' else 'A'
            cost += 1
            print(f"Operation: MOVE {direction} (+1)")

    print(f"\nFinished Cleaning Process.\nTotal Cost: {cost}")

if __name__ == "__main__":
    run_cleaning_bot()
