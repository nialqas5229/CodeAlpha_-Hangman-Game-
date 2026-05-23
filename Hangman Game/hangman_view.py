# HANGMAN VIEW CLASS
class HangmanGameView:
    @staticmethod
    def display_game_title() -> None:

        print("\n" + "=" * 50)
        print("WELCOME TO THE HANGMAN GAME")
        print("=" * 50)

    # GAME STATUS DISPLAY
    @staticmethod
    def display_game_status(
        hidden_word_display: str,
        remaining_guesses: int,
        used_letters_display: str
    ) -> None:
        print("\nCurrent Word:")
        print(hidden_word_display)

        print(f"\nRemaining Guesses: {remaining_guesses}")

        print(f"Used Letters: {used_letters_display}")

    # PLAYER MESSAGE DISPLAY
    @staticmethod
    def display_message(message: str) -> None:

        print(f"\n{message}")
    # ERROR MESSAGE DISPLAY
    @staticmethod
    def display_error_message(error_message: str) -> None:
        """
        Display error messages clearly.
        """
        print(f"\n[ERROR] {error_message}")

    # WIN MESSAGE
    @staticmethod
    def display_winning_message(selected_word: str) -> None:
        print("\n" + "=" * 50)
        print("CONGRATULATIONS! YOU WON THE GAME")
        print(f"The word was: {selected_word}")
        print("=" * 50)

    # LOSE MESSAGE
    @staticmethod
    def display_losing_message(selected_word: str) -> None:

        print("\n" + "=" * 50)
        print("GAME OVER! YOU LOST")
        print(f"The correct word was: {selected_word}")
        print("=" * 50)

    # INPUT MESSAGE
    @staticmethod
    def prompt_player_guess() -> str:
        return input("\nEnter a letter: ")
    # RESTART MESSAGE
    @staticmethod
    def prompt_restart_game() -> str:
        return input("\nDo you want to play again? (yes/no): ")

    # SEPARATOR
    @staticmethod
    def display_separator() -> None:
        """
        Display a visual separator line.
        """
        print("-" * 50)