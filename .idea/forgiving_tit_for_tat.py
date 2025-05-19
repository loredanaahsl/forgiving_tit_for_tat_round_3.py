def strategy(my_history: list[int], opponent_history: list[int], rounds: int | None) -> int:
    """
    Forgiving Tit for Tat Strategy for Round 1.

    - Starts by cooperating
    - Reciprocates the opponent’s last move
    - Occasionally forgives defections to break retaliation cycles
    - More forgiving if the opponent has been generally cooperative
    """

    # Default to cooperate on the first move
    if not opponent_history:
        return 1

    # Get last opponent move
    last_opponent_move = opponent_history[-1]

    # Calculate opponent cooperation rate
    total_moves = len(opponent_history)
    coop_rate = sum(opponent_history) / total_moves if total_moves > 0 else 1

    # Default to mirror (Tit for Tat behavior)
    next_move = last_opponent_move

    # Only consider forgiveness after a few moves
    if last_opponent_move == 0 and total_moves > 3:
        # The more cooperative the opponent, the more forgiving we are
        forgiveness_chance = 0.1 + (coop_rate * 0.2)

        # Deterministic fake-random mechanism based on history sum
        deterministic_seed = sum(my_history) + sum(opponent_history)
        pseudo_random_percent = deterministic_seed % 100

        if pseudo_random_percent < forgiveness_chance * 100:
            next_move = 1  # Forgive

    # In case of inconsistent or unexpected behavior, fall back to cooperation
    if next_move not in (0, 1):
        next_move = 1

    return next_move
