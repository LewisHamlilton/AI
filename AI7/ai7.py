events = input("Enter events separated by space (Example: B E A J M): ").split()

print("\nEvents in the Network:")
for e in events:
    print(e)

print("\nEnter Prior Probabilities")
P_B = float(input("P(Burglary): "))
P_E = float(input("P(Earthquake): "))

print("\nEnter Alarm Conditional Probabilities")
P_A = {
    (True, True): float(input("P(A|B,E): ")),
    (True, False): float(input("P(A|B,~E): ")),
    (False, True): float(input("P(A|~B,E): ")),
    (False, False): float(input("P(A|~B,~E): "))
}

print("\nEnter Call Probabilities")
P_J = {
    True: float(input("P(J|A): ")),
    False: float(input("P(J|~A): "))
}

P_M = {
    True: float(input("P(M|A): ")),
    False: float(input("P(M|~A): "))
}

print("\nConditional Probability Table Stored Successfully")

print("\nCPT Values")
print(f"P(B) = {P_B}")
print(f"P(E) = {P_E}")
print(f"P(A|B,E) = {P_A[(True, True)]}")
print(f"P(A|B,~E) = {P_A[(True, False)]}")
print(f"P(A|~B,E) = {P_A[(False, True)]}")
print(f"P(A|~B,~E) = {P_A[(False, False)]}")
print(f"P(J|A) = {P_J[True]}")
print(f"P(J|~A) = {P_J[False]}")
print(f"P(M|A) = {P_M[True]}")
print(f"P(M|~A) = {P_M[False]}")

def joint_prob(B, E, A, J, M):
    prob_B = P_B if B else (1 - P_B)
    prob_E = P_E if E else (1 - P_E)
    prob_A = P_A[(B, E)] if A else (1 - P_A[(B, E)])
    prob_J = P_J[A] if J else (1 - P_J[A])
    prob_M = P_M[A] if M else (1 - P_M[A])
    
    return prob_B * prob_E * prob_A * prob_J * prob_M

print("\nSample Query")
print("Alarm sounded but no burglary, no earthquake, John and Mary called")
print("Probability =", joint_prob(False, False, True, True, True))

print("\nEnter 5 Queries")
for i in range(1, 6):
    print(f"\nQuery {i}")
    B = bool(int(input("Burglary occurred? (1/0): ")))
    E = bool(int(input("Earthquake occurred? (1/0): ")))
    A = bool(int(input("Alarm sounded? (1/0): ")))
    J = bool(int(input("John called? (1/0): ")))
    M = bool(int(input("Mary called? (1/0): ")))
    print("Joint Probability =", joint_prob(B, E, A, J, M))