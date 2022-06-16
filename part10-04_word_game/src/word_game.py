# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        return None

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        vowel_count1 = 0
        vowel_count2 = 0

        for x in player1_word:
            if x in "aeiou":
                vowel_count1 += 1
        
        for y in player2_word:
            if y in "aeiou":
                vowel_count2 += 1
        
        if vowel_count2 > vowel_count1:
            return 2
        elif vowel_count1 > vowel_count2:
            return 1
        else:
            return None
    


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        if player2_word == player1_word:
            return None

        valid_words = ["rock", "paper", "scissors"]

        player1_word = player1_word.lower()
        player2_word = player2_word.lower()
        if not player2_word in valid_words and not player1_word in valid_words:
            return None
            
        if player2_word not in valid_words:
            return 1
        if player1_word not in valid_words:
            return 2
                
        if player1_word == "rock":
            if player2_word == "scissors":
                return 1
            return 2
        elif player1_word == "scissors":
            if player2_word == "paper":
                return 1
            return 2
        else:
            if player2_word == "rock":
                return 1
            return 2






