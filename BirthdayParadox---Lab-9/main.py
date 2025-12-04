from birth_paradox import BirthdayParadox

if __name__ == "__main__":
    bp = BirthdayParadox(repeat=1000)

    for n in range(5, 105, 5):
        prob = bp.run(n)
        print(f"For {n} people, probability of shared birthday = {prob:.3f}")
