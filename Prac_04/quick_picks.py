import random

NUM_QUICK_PICKS = 5
NUM_PER_QUICK_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def generate_quick_picks(num_quick_picks, num_per_quick_pick):
    quick_picks = []
    for _ in range(num_quick_picks):
        quick_pick = sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), num_per_quick_pick))
        quick_picks.append(quick_pick)
    return quick_picks

def main():
    num_quick_picks = int(input("How many quick picks? "))
    quick_picks = generate_quick_picks(num_quick_picks, NUM_PER_QUICK_PICK)

    for quick_pick in quick_picks:
        print(" ".join(str(number).rjust(2) for number in quick_pick))

if __name__ == "__main__":
    main()
