import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        raise ValueError("No scores provided!")
    scores = []
    total = 0
    for i in range(1, len(sys.argv)):
        try:
            score = int(sys.argv[i])
            total += score
            scores.append(score)
        except ValueError:
            print(f"Invalid score '{sys.argv[i]}', skipping.")
    print("Scores received: ", scores)
    print("Total Players: ", len(scores))
    print("Total Score: ", total)
    print("Average Score: ", total / len(scores) if scores else 0)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
