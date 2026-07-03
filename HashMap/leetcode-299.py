'''Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.'''

#Time Complexity O(n^2)
def getHint(secret: str, guess: str) -> str:
    hm1 = {}
    hm2 = {}
    for i in range(0, len(secret)):
        hm1[i] = secret[i]
    for i in range(0, len(guess)):
        hm2[i] = guess[i]

    bulls = 0
    cows = 0

    # Loop 1: Find bulls and eliminate them from both hash maps
    for j in range(len(guess)):
        if hm1[j] == hm2[j]:
            bulls += 1
            hm1[j] = None  # Mark as used so it won't be counted as a cow
            hm2[j] = None  # Mark as used

    # Loop 2: Find cows from the remaining unmatched digits
    for i in range(len(guess)):
        if hm2[i] is not None:  # Skip digits that were already bulls
            for key, val in hm1.items():
                if val == hm2[i]:
                    cows += 1
                    hm1[key] = None  # Consume this secret digit so it's not reused
                    break  # Stop looking for this specific guess digit

    final = str(bulls) + "A" + str(cows) + "B"
    return final

#Time Complexity - O(n)

def getHint(self, secret: str, guess: str) -> str:
    bulls = 0
    cows = 0
    
    # Arrays to keep track of frequencies for digits '0' through '9'
    secret_counts = [0] * 10
    guess_counts = [0] * 10
    
    # Single pass to find bulls and populate frequency arrays for non-bulls
    for s, g in zip(secret, guess):
        if s == g:
            bulls += 1
        else:
            secret_counts[int(s)] += 1
            guess_counts[int(g)] += 1
            
    # Calculate cows by finding overlapping frequencies
    for i in range(10):
        cows += min(secret_counts[i], guess_counts[i])
        
    return f"{bulls}A{cows}B"