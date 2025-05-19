# Forgiving Tit for Tat

This is the implementation of the `forgiving_tit_for_tat` strategy for the Iterated Prisoner's Dilemma tournament.

## Strategy Overview

This algorithm is built on the classic Tit for Tat, starting each opponent interaction with cooperation. It mirrors the opponent's last move but includes a forgiveness mechanism:
- If the opponent defects, there’s a chance to forgive and cooperate anyway, especially if the opponent has generally been cooperative.
- This breaks destructive cycles of mutual defection while still punishing consistently aggressive strategies.

## Character

- **Type**: Neat
- **Behavior**: The algorithm **never defects first** and favors long-term cooperation by default.
- Capable of **forgiving** after punishment if the opponent shows a willingness to cooperate again.

### Opponent Selection
In Round 3, the algorithm chooses its next opponent based on prior cooperation levels:
- Favors players with high cooperation rates.
- Skips players it has already faced in 200 rounds.
- If no new cooperative opponents are found, it continues with the current one.

## File Contents
- `forgiving_tit_for_tat.py` – Strategy for the first part of the tournament
- `forgiving_tit_for_tat_round_3.py` – Strategy for the second part (with opponent selection)
