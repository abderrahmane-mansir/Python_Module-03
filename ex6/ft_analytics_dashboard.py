def main() -> None:

    print("=== Game Analytics Dashboard ===")

    players = ["alice", "bob", "charlie", "diana"]

    scores = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050
    }

    active_players = {
        "alice": True,
        "bob": True,
        "charlie": True,
        "diana": False
    }

    achievements = {
        "alice": ["first_kill", "level_10", "level_10",
                  "boss_slayer", "boss_slayer"],
        "bob": ["level_10", "first_kill", "boss_slayer"],
        "charlie": ["first_kill", "first_kill", "level_10", "level_10",
                    "boss_slayer", "boss_slayer", "boss_slayer"],
        "diana": ["boss_slayer", "first_kill", "level_10"]
    }

    regions = ["north", "east", "central", "north"]

    print("\n=== List Comprehension Examples ===")

    high_scorers = [p for p in players if scores[p] > 2000]

    scores_doubled = [scores[p] * 2 for p in players]

    active_players = [p for p in players if active_players[p]]

    print("High scorers (>2000):", sorted(high_scorers))
    print("Scores doubled:", scores_doubled)
    print("Active players:", sorted(active_players))

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {p: scores[p] for p in players}

    score_categories = {
        "high": len([p for p in players if scores[p] > 2000]),
        "medium": len([p for p in players if 2000 <= scores[p] <= 2200]),
        "low": len([p for p in players if scores[p] < 2000])
    }

    achievement_counts = {p: len(achievements[p]) for p in players[:3]}

    print("Player scores:", player_scores)
    print("Score categories:", score_categories)
    print("Achievement counts:", achievement_counts)

    print("\n=== Set Comprehension Examples ===")

    unique_players = {p for p in players}

    unique = {a for ach_list in achievements.values() for a in ach_list}

    active_regions = {r for r in regions}

    print("Unique players:", unique_players)
    print("Unique achievements:", unique)
    print("Active regions:", active_regions)

    print("\n=== Combined Analysis ===")

    skills = [
        a
        for player, score in scores.items()
        if score > 2100
        for a in achievements[player]
    ]
    total_players = len(players)
    total_unique_achievements = len(skills)
    average_score = (sum(scores.values())-50) / len(scores)
    top_player = max(scores, key=scores.get)

    print("Total players:", total_players)
    print("Total unique achievements:", total_unique_achievements)
    print("Average score:", average_score)
    print(
        "Top performer:", top_player,
        f"({scores[top_player]} points,",
        f"{len(achievements[top_player])} achievements)"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
