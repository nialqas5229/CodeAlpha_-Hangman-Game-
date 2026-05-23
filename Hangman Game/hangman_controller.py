# IMPORT REQUIRED FILES
from hangman_model import HangmanGameModel
from hangman_view import HangmanGameView

# HANGMAN CONTROLLER CLASS
class HangmanGameController:
    def __init__(self) -> None:
        self.game_model = HangmanGameModel()
        self.game_view = HangmanGameView()

    def start_game(self) -> None:
        self.game_view.display_game_title()
        while True:
            self.game_model.start_new_game()
            self.run_single_game()
            restart_choice = (
                self.game_view
                .prompt_restart_game()
                .strip()
                .lower()
            )
            while restart_choice not in ["yes", "no", "y", "n"]:

                self.game_view.display_error_message(
                    "Please enter only yes or no."
                )

                restart_choice = (
                    self.game_view
                    .prompt_restart_game()
                    .strip()
                    .lower()
                )

            if restart_choice in ["no", "n"]:

                self.game_view.display_message(
                    "Thank you for playing Hangman Game!"
                )

                break

    def run_single_game(self) -> None:
        while self.game_model.get_game_status() == "playing":
            self.game_view.display_game_status(
                hidden_word_display=(
                    self.game_model.get_hidden_word_display()
                ),
                remaining_guesses=(
                    self.game_model.get_remaining_guesses()
                ),
                used_letters_display=(
                    self.game_model.get_used_letters_display()
                )
            )
            player_guess = (
                self.game_view
                .prompt_player_guess()
            )

            is_correct_guess, result_message = (
                self.game_model.process_guess(player_guess)
            )
            if is_correct_guess:

                self.game_view.display_message(result_message)
            else:

                if (
                    "already guessed" in result_message.lower()
                    or
                    "please enter" in result_message.lower()
                    or
                    "only alphabet" in result_message.lower()
                    or
                    "must be text" in result_message.lower()
                ):
                    self.game_view.display_error_message(
                        result_message
                    )

                else:

                    self.game_view.display_message(
                        result_message
                    )

            self.game_view.display_separator()

        self.display_final_result()

    def display_final_result(self) -> None:

        # Player won
        if self.game_model.has_player_won():

            self.game_view.display_winning_message(
                self.game_model.selected_word
            )

        # Player lost
        else:

            self.game_view.display_losing_message(
                self.game_model.selected_word
            )