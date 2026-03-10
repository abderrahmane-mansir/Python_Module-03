import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided."
              " Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
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
        print("High Score: ", max(scores) if scores else 0)
        print("Low Score: ", min(scores) if scores else 0)
        print("Score Range: ", max(scores) - min(scores) if scores else 0,
              end="\n\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
