import random

def simulate_game(rounds=1000000):
    jack_wins = 0
    rose_wins = 0

    for _ in range(rounds):
        jack_choice = random.choice(['H', 'T'])


        rose_choice = 'H' if random.random() < 3/8 else 'T'

        if jack_choice == 'H' and rose_choice == 'H':
            jack_wins += 3
        elif jack_choice == 'T' and rose_choice == 'T':
            jack_wins += 1
        else:
            rose_wins += 2

    return jack_wins, rose_wins

jack_score, rose_score = simulate_game()

print(f"Jack's total score: {jack_score}")
print(f"Rose's total score: {rose_score}")