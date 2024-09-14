import nashpy as nash
import numpy as np

# prisoners dilemma
# # Define the payoff matrices for the players
A = np.array([[10, 0], [0, 5]])  # Payoff matrix for Player 1
B = np.array([[5, 0], [0, 10]])  # Payoff matrix for Player 2

# # Create the game
bos = nash.Game(A, B)

# Find the Nash Equilibria
equilibria = bos.support_enumeration()
for eq in equilibria:
    if all(p in [0, 1] for p in eq[0]) and all(p in [0, 1] for p in eq[1]):
        print(f"Nash Equilibrium: {eq}")