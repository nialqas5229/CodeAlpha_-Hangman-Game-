from hangman_controller import HangmanGameController
def main() -> None:
    try:
        hangman_game_controller = HangmanGameController()
        hangman_game_controller.start_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user.")
    except Exception as unexpected_error:
        print("\nAn unexpected error occurred.")
        print(f"Error Details: {unexpected_error}")
    finally:
        print("\nThank you for using CodeAlpha Hangman Game.")

if __name__ == "__main__":
    main()