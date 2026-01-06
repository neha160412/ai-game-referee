import random
from typing import Dict, Callable


def tool(func: Callable):
    """
    Simulated Google ADK @tool decorator.
    """
    return func

game_state = {
    "round": 1,
    "user_score": 0,
    "bot_score": 0,
    "user_bomb_used": False,
    "bot_bomb_used": False
}

@tool
def validate_move(move: str, bomb_used: bool) -> Dict:
    valid_moves = ["rock", "paper", "scissors", "bomb"]

    if move not in valid_moves:
        return {"valid": False, "reason": "Invalid move"}

    if move == "bomb" and bomb_used:
        return {"valid": False, "reason": "Bomb already used"}

    return {"valid": True}

@tool
def resolve_round(user_move: str, bot_move: str) -> str:
    if user_move == bot_move:
        return "draw"

    if user_move == "bomb":
        return "user"
    if bot_move == "bomb":
        return "bot"

    rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    return "user" if rules[user_move] == bot_move else "bot"

@tool
def update_game_state(
    state: Dict,
    winner: str,
    user_move: str,
    bot_move: str
) -> Dict:

    if user_move == "bomb":
        state["user_bomb_used"] = True
    if bot_move == "bomb":
        state["bot_bomb_used"] = True

    if winner == "user":
        state["user_score"] += 1
    elif winner == "bot":
        state["bot_score"] += 1

    state["round"] += 1
    return state

class GameRefereeAgent:

    def explain_rules(self):
        print(
            "Rock–Paper–Scissors–Plus Rules:\n"
            "• Best of 3 rounds\n"
            "• Moves: rock, paper, scissors, bomb (u can choose bomb only once)\n"
            "• Bomb beats everything\n"
            "• Invalid input wastes the round\n"
        )

    def play(self):
        global game_state
        self.explain_rules()

        while game_state["round"] <= 3:
            print(f"\nRound {game_state['round']}")
            user_move = input("Your move: ").strip().lower()

            validation = validate_move(user_move, game_state["user_bomb_used"])

            bot_move = random.choice(
                ["rock", "paper", "scissors", "bomb"]
                if not game_state["bot_bomb_used"]
                else ["rock", "paper", "scissors"]
            )

            if not validation["valid"]:
                print("Invalid input. Round wasted.")
                game_state["round"] += 1
                continue

            winner = resolve_round(user_move, bot_move)

            game_state = update_game_state(
                game_state, winner, user_move, bot_move
            )

            print(f"\nUser Move: {user_move}")
            print(f"Bot Move: {bot_move}")
            print(f"Round Winner: {winner}")
            print(
                f"Score → User: {game_state['user_score']} | "
                f"Bot: {game_state['bot_score']}"
            )

        print("\nFinal Result:")
        if game_state["user_score"] > game_state["bot_score"]:
            print("User wins")
        elif game_state["bot_score"] > game_state["user_score"]:
            print("Bot wins")
        else:
            print("Draw")

if __name__ == "__main__":
    agent = GameRefereeAgent()
    agent.play()

