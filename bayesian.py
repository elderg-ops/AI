# 1. Create a Belief Network

# a. List all events occurring in this network (input)
events = ["Burglary", "Earthquake", "Alarm", "JohnCalls", "MaryCalls"]
print("\nEvents in the network:", events)

# b. Store Conditional probability table for each event (input)
prob_burglary = {"True": 0.001, "False": 0.999}
prob_earthquake = {"True": 0.002, "False": 0.998}
prob_alarm = {
    ("True", "True"): {"True": 0.95, "False": 0.05},  # (B=T, E=T)
    ("True", "False"): {"True": 0.94, "False": 0.06}, # (B=T, E=F)
    ("False", "True"): {"True": 0.29, "False": 0.71}, # (B=F, E=T)
    ("False", "False"): {"True": 0.001, "False": 0.999}, # (B=F, E=F)
}
prob_john_calls = {
    "True": {"True": 0.90, "False": 0.10},  # (A=T)
    "False": {"True": 0.05, "False": 0.95}, # (A=F)
}
prob_mary_calls = {
    "True": {"True": 0.70, "False": 0.30},  # (A=T)
    "False": {"True": 0.01, "False": 0.99}, # (A=F)
}

cpts = {
    "Burglary": prob_burglary,
    "Earthquake": prob_earthquake,
    "Alarm": prob_alarm,
    "JohnCalls": prob_john_calls,
    "MaryCalls": prob_mary_calls,
}

print("\nConditional Probability Tables (CPTs):")
for event, cpt in cpts.items():
    print(f"\nCPT for {event}:")
    print(cpt)

# 2. Use the created Bayesian network to answer any query about the domain by using Joint distribution.

def calculate_joint_probability(b, e, a, j, m):
    """Calculates the joint probability P(B, E, A, J, M)."""
    p_b = cpts["Burglary"][str(b)]
    p_e = cpts["Earthquake"][str(e)]
    p_a_given_be = cpts["Alarm"][(str(b), str(e))][str(a)]
    p_j_given_a = cpts["JohnCalls"][str(a)][str(j)]
    p_m_given_a = cpts["MaryCalls"][str(a)][str(m)]
    return p_m_given_a * p_j_given_a * p_a_given_be * p_e * p_b

def query_joint_distribution(query):
    """Answers a query by calculating the joint probability of the specified events."""
    if not all(event in query for event in events):
        print("Error: Query must specify the state for all events.")
        return None

    b = query["Burglary"]
    e = query["Earthquake"]
    a = query["Alarm"]
    j = query["JohnCalls"]
    m = query["MaryCalls"]
    return calculate_joint_probability(b, e, a, j, m)

# a. Calculate the probability that the alarm has sounded (A=True), but there is neither a burglary (B=False),
# nor an earthquake occurred (E=False), and John called (J=True) and Marry called (M=True).

query_a = {
    "Burglary": False,
    "Earthquake": False,
    "Alarm": True,
    "JohnCalls": True,
    "MaryCalls": True
}
probability_a = query_joint_distribution(query_a)

print("\n--- Query Results ---")
print(f"\nProbability (A=True, B=False, E=False, J=True, M=True): {probability_a:.8f}")

# b. Similarly create 5 such queries and get the answer.

# Query 1: P(B=True, E=True, A=True, J=True, M=True)
query_1 = {
    "Burglary": True,
    "Earthquake": True,
    "Alarm": True,
    "JohnCalls": True,
    "MaryCalls": True
}
probability_1 = query_joint_distribution(query_1)
print(f"Probability (B=True, E=True, A=True, J=True, M=True): {probability_1:.8f}")

# Query 2: P(B=False, E=False, A=False, J=False, M=False)
query_2 = {
    "Burglary": False,
    "Earthquake": False,
    "Alarm": False,
    "JohnCalls": False,
    "MaryCalls": False
}
probability_2 = query_joint_distribution(query_2)
print(f"Probability (B=False, E=False, A=False, J=False, M=False): {probability_2:.8f}")

# Query 3: P(B=True, E=False, A=True, J=False, M=True)
query_3 = {
    "Burglary": True,
    "Earthquake": False,
    "Alarm": True,
    "JohnCalls": False,
    "MaryCalls": True
}
probability_3 = query_joint_distribution(query_3)
print(f"Probability (B=True, E=False, A=True, J=False, M=True): {probability_3:.8f}")

# Query 4: P(B=False, E=True, A=False, J=True, M=False)
query_4 = {
    "Burglary": False,
    "Earthquake": True,
    "Alarm": False,
    "JohnCalls": True,
    "MaryCalls": False
}
probability_4 = query_joint_distribution(query_4)
print(f"Probability (B=False, E=True, A=False, J=True, M=False): {probability_4:.8f}")

# Query 5: P(B=False, E=False, A=True, J=False, M=False)
query_5 = {
    "Burglary": False,
    "Earthquake": False,
    "Alarm": True,
    "JohnCalls": False,
    "MaryCalls": False
}
probability_5 = query_joint_distribution(query_5)
print(f"Probability (B=False, E=False, A=True, J=False, M=False): {probability_5:.8f}")
