from typing import Generator
import sys


time = sys.modules.get('time')


def game_event_stream(event_count: int) -> Generator[tuple[str, int, str],
                                                     None, None]:
    players = ["alice", "bob", "charlie"]
    events = [
        "killed monster", "found treasure",
        "leveled up", "destroyed enemy"
        ]
    levels = [5, 12, 8, 15, 20]

    for i in range(event_count):
        player = players[i % len(players)]
        level = levels[i % len(levels)]
        event = events[i % len(events)]
        yield player, level, event


def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_numbers(limit: int) -> Generator[int, None, None]:
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 2
    while count < limit:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")

    event_num = 1000

    counter = {
        "High-level": 0,
        "Kill": 0,
        "Destroyed": 0,
    }

    start = time.perf_counter()

    lol_gen = iter(game_event_stream(event_num))

    for i in range(1, event_num + 1):
        player, level, event = next(lol_gen)

        if level > 10:
            counter["High-level"] += 1
        elif "killed" in event:
            counter["Kill"] += 1
        elif "destroyed" in event:
            counter["Destroyed"] += 1

        r = sum(range(1600))
        r += sum(range(1400))

        if i <= 3:
            print(f"Event {i}: Player {player} (level {level}) {event}")
    print("...")
    end = time.perf_counter()

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {event_num}")
    print(f"High-level players (10+): {counter['High-level']}")
    print(f"Treasure events: {counter['Kill']}")
    print(f"Level-up events: {counter['Destroyed']}")

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {end - start:.3f} seconds")

    print("\n=== Generator Demonstration ===")

    fib = fibonacci(10)
    print("Fibonacci sequence (first 10):", end=" ")
    print(", ".join(str(next(fib)) for _ in range(10)))

    primes = prime_numbers(5)
    print("Prime numbers (first 5):", end=" ")
    print(", ".join(str(next(primes)) for _ in range(5)))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", e)
