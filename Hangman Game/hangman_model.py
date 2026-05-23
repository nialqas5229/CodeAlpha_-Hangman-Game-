from __future__ import annotations
import random
from dataclasses import dataclass, field
from typing import Iterable

# Small predefined list of words as required by the internship task.
DEFAULT_HANGMAN_WORDS = ["python", "apple", "tiger", "chair", "ocean"]

# Maximum wrong attempts allowed in the game.
DEFAULT_MAX_WRONG_GUESSES = 6
# HANGMAN MODEL CLASS
@dataclass
class HangmanGameModel:
    hangman_words: list[str] = field(default_factory=lambda: DEFAULT_HANGMAN_WORDS.copy())
    max_wrong_guesses: int = DEFAULT_MAX_WRONG_GUESSES
    selected_word: str = ""
    guessed_letters: set[str] = field(default_factory=set)
    wrong_guess_count: int = 0

    def __post_init__(self) -> None:
        """Validate initial data and start the first game."""
        self._validate_hangman_words(self.hangman_words)
        self._validate_max_wrong_guesses(self.max_wrong_guesses)
        self.start_new_game()

    @staticmethod
    def _validate_hangman_words(hangman_words: Iterable[str]) -> None:
        word_list = list(hangman_words)

        if not word_list:
            raise ValueError("Hangman word list cannot be empty.")

        for word in word_list:
            if not isinstance(word, str):
                raise TypeError("Every hangman word must be a string.")

            cleaned_word = word.strip().lower()
            if not cleaned_word:
                raise ValueError("Hangman words cannot be blank.")

            if not cleaned_word.isalpha():
                raise ValueError(
                    f"Invalid word '{word}'. Hangman words must contain letters only."
                )

    @staticmethod
    def _validate_max_wrong_guesses(max_wrong_guesses: int) -> None:
        if not isinstance(max_wrong_guesses, int):
            raise TypeError("max_wrong_guesses must be an integer.")

        if max_wrong_guesses < 1:
            raise ValueError("max_wrong_guesses must be at least 1.")

    def start_new_game(self) -> None:
        self.selected_word = random.choice(self.hangman_words).lower()
        self.guessed_letters.clear()
        self.wrong_guess_count = 0

    def update_word_list(self, hangman_words: Iterable[str]) -> None:
        cleaned_word_list = [word.strip().lower() for word in hangman_words]
        self._validate_hangman_words(cleaned_word_list)
        self.hangman_words = cleaned_word_list
        self.start_new_game()

    def get_hidden_word_display(self) -> str:
        return " ".join(
            letter if letter in self.guessed_letters else "_"
            for letter in self.selected_word
        )

    def get_used_letters_display(self) -> str:
        if not self.guessed_letters:
            return "None"
        return ", ".join(sorted(self.guessed_letters))

    def is_valid_guess(self, player_guess: str) -> tuple[bool, str]:

        if not isinstance(player_guess, str):
            return False, "Guess must be text."

        player_guess = player_guess.strip().lower()

        if not player_guess:
            return False, "Please enter a letter."

        if len(player_guess) != 1:
            return False, "Please enter only one letter."

        if not player_guess.isalpha():
            return False, "Only alphabet letters are allowed."

        if player_guess in self.guessed_letters:
            return False, f"You already guessed '{player_guess}'."

        return True, ""

    def process_guess(self, player_guess: str) -> tuple[bool, str]:

        player_guess = player_guess.strip().lower()
        is_valid, error_message = self.is_valid_guess(player_guess)

        if not is_valid:
            return False, error_message

        self.guessed_letters.add(player_guess)

        if player_guess in self.selected_word:
            return True, f"Good job! '{player_guess}' is in the word."

        self.wrong_guess_count += 1
        return False, f"Wrong guess! '{player_guess}' is not in the word."

    def has_player_won(self) -> bool:
        return all(letter in self.guessed_letters for letter in self.selected_word)

    def has_player_lost(self) -> bool:
        return self.wrong_guess_count >= self.max_wrong_guesses

    def get_remaining_guesses(self) -> int:
        return max(0, self.max_wrong_guesses - self.wrong_guess_count)

    def get_game_status(self) -> str:
        if self.has_player_won():
            return "won"
        if self.has_player_lost():
            return "lost"
        return "playing"
