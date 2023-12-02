def sum_of_possible_games(games: str, constraints: dict[str, int]) -> int:
    games = {
        int((a := l.split(": "))[0].split(" ")[1]): [
            {(d := c.split(" "))[1]: int(d[0]) for c in b.split(", ")}
            for b in a[1].split("; ")
        ]
        for l in games.splitlines()
    }

    possible_games = 0
    for game, sets in games.items():
        ok = True
        for game_set in sets:
            for color, amount in game_set.items():
                if constraints[color] < amount:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            possible_games += game

    return possible_games


TEST_GAMES = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

TEST_CONSTRAINTS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

assert sum_of_possible_games(TEST_GAMES, TEST_CONSTRAINTS) == 8

day02_input = open("day02.txt", "r").read()

print(sum_of_possible_games(day02_input, TEST_CONSTRAINTS))

from math import prod

def sum_of_powers(games: str) -> int:
    games = {
        int((a := l.split(": "))[0].split(" ")[1]): [
            {(d := c.split(" "))[1]: int(d[0]) for c in b.split(", ")}
            for b in a[1].split("; ")
        ]
        for l in games.splitlines()
    }

    powers = []
    for game, sets in games.items():
        mins = {
            "blue": 0,
            "red": 0,
            "green": 0,
        }
        for game_set in sets:
            for color, amount in game_set.items():
                if mins[color] < amount:
                    mins[color] = amount
        powers.append(prod(mins.values()))

    return sum(powers)

assert sum_of_powers(TEST_GAMES) == 2286

print(sum_of_powers(day02_input))