# AI Game Referee – Rock–Paper–Scissors–Plus

## Overview
This project is a command-line AI referee chatbot for a modified version of the
Rock–Paper–Scissors game. The bot manages the entire game flow, enforces all rules,
keeps track of scores and rounds, and provides clear feedback after each round.
The overall design follows Google ADK principles by separating agent behavior,
tool-based logic, and game state management.

---

## State Model
The game state is maintained using a persistent Python dictionary that exists
throughout the game session. This state stores the current round number (up to
three rounds), the scores of both the user and the bot, and whether each player
has already used the bomb move. Storing state in this way ensures that the game
progresses correctly across turns without relying only on prompts or responses.

---

## Agent and Tool Design
The solution is structured with a clear separation of responsibilities.

The **GameRefereeAgent** controls the conversation flow. It explains the rules at
the start, prompts the user for input each round, invokes the appropriate tools
to process game logic, and generates responses that are shown to the user.

The core logic is handled through explicit tools:
- `validate_move` is responsible for interpreting the user’s input and validating
  it, including enforcing the one-time bomb usage rule.
- `resolve_round` contains the game rules and determines the winner of each round.
- `update_game_state` updates the persistent state by modifying scores, round
  count, and bomb usage flags.

This design closely follows the tool-driven approach encouraged by Google ADK.

---

## Tradeoffs
A command-line interface was chosen to keep the project simple and focused on core
logic rather than user interface design. The bot’s move selection is randomized
to maintain simplicity and clarity instead of implementing a complex strategy.
Additionally, Google ADK concepts are represented using a lightweight structure
since the official SDK is not publicly available at this time.

---

## Future Improvements
With additional time, the system could be improved by supporting natural language
inputs instead of fixed commands, adding a smarter bot strategy based on previous
rounds, producing structured JSON outputs for easier integration, and allowing
users to replay the game without restarting the program.

---

## Google ADK Usage Note
The official Google ADK SDK is not publicly available via pip at the time of
development. This project demonstrates ADK-style architecture by clearly
separating agent logic, tool-based validation and state updates, and persistent
game state management.
