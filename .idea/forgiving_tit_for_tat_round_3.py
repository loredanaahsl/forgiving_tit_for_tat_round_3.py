def strategy_round_3(opponent_id: int, my_history: dict[int, list[int]], opponents_history: dict[int, list[int]]) -> tuple[int, int]:
    # Get current opponent's history with me
    current_opponent_moves = opponents_history.get(opponent_id, [])

    # Default to cooperate if no history
    if not current_opponent_moves:
        next_move = 1
    else:
        last_opponent_move = current_opponent_moves[-1]

        # Calculate opponent's cooperation rate
        coop_rate = sum(current_opponent_moves) / len(current_opponent_moves)

        # Standard Tit for Tat
        next_move = last_opponent_move

        # 10% chance to forgive if opponent defected (adjusted by their cooperation rate)
        if last_opponent_move == 0 and len(current_opponent_moves) > 3:
            forgiveness_chance = 0.1 + (coop_rate * 0.2)
            deterministic_seed = sum([sum(v) for v in opponents_history.values()]) + sum([sum(v) for v in my_history.values()])
            if deterministic_seed % 100 < forgiveness_chance * 100:
                next_move = 1

    # Select next opponent (prefer those who cooperated the most)
    potential_opponents = []
    for opp_id in opponents_history:
        if opp_id == opponent_id or len(my_history.get(opp_id, [])) >= 200:
            continue
        opp_moves = opponents_history.get(opp_id, [])
        coop_rate = sum(opp_moves) / len(opp_moves) if opp_moves else 1
        potential_opponents.append((opp_id, coop_rate))

    potential_opponents.sort(key=lambda x: x[1], reverse=True)

    if potential_opponents:
        next_opponent = potential_opponents[0][0]
    else:
        next_opponent = opponent_id  # Stay with current if no better options

    return (next_move, next_opponent)
