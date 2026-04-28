# -------- Experiment 1 : Create Belief Network --------

events = input("Enter events separated by space (Example: B E A J M): ").split()

print("\nEvents in the Network:")
for e in events:
    print(e)

# -------- Store Conditional Probability Tables --------

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
print("P(B) =", P_B)
print("P(E) =", P_E)
for k in P_A:
    print(f"P(A|{'B' if k[0] else '~B'},{'E' if k[1] else '~E'}) =", P_A[k])
print("P(J|A) =", P_J[True])
print("P(J|~A) =", P_J[False])
print("P(M|A) =", P_M[True])
print("P(M|~A) =", P_M[False])


# -------- Joint Probability Function --------

def joint_prob(B, E, A, J, M):
    pB = P_B if B else 1 - P_B
    pE = P_E if E else 1 - P_E

    pA = P_A[(B, E)]
    pA = pA if A else 1 - pA

    pJ = P_J[A] if J else 1 - P_J[A]
    pM = P_M[A] if M else 1 - P_M[A]

    return pB * pE * pA * pJ * pM


# -------- Sample Query --------

print("\nSample Query")
print("Alarm sounded but no burglary, no earthquake, John and Mary called")

result = joint_prob(False, False, True, True, True)
print("Probability =", result)


# -------- User Queries --------

print("\nEnter 5 Queries")

for i in range(5):
    print("\nQuery", i+1)

    B = bool(int(input("Burglary occurred? (1/0): ")))
    E = bool(int(input("Earthquake occurred? (1/0): ")))
    A = bool(int(input("Alarm sounded? (1/0): ")))
    J = bool(int(input("John called? (1/0): ")))
    M = bool(int(input("Mary called? (1/0): ")))

    print("Joint Probability =", joint_prob(B, E, A, J, M))