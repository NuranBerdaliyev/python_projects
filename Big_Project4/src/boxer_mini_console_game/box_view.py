from box_model import Boxer
attacks=Boxer.attack_types
defences=Boxer.defence_types

class Input:
    @staticmethod
    def first_boxer_choice():
        '''
        Choose the name of boxer who attacks first
        '''
        boxer=input("Enter the name of the boxer who you want to choose as a boxer who starts the fight: ")
        return boxer
    @staticmethod
    def boxer_attack_choice():
        '''
        Enter the attack type for a boxer
        '''
        attack_type=input("Enter the boxer attack: ").lower()
        return attack_type
    @staticmethod
    def boxer_defence_choice():
        '''
        Enter the defence type for a boxer
        '''
        defence_type=input("Enter the boxer defence: ").lower()
        return defence_type
    @staticmethod
    def the_main_question():
        '''We ask if user really wants to play'''
        response=int(input("Do you wanna play? 1-yes; 0-no "))
        return response

    
class Output:
    @staticmethod
    def greetings():
        result="Hello! This is the mini-game \'Two boxers\'"
        return result
    @staticmethod
    def whosturn(boxer: Boxer):
        return f"{boxer.name}'s turn!"
    @staticmethod
    def boxer_hp(boxer: Boxer):
        return f"{boxer.name} number {boxer.player_id} has {boxer.hp} hp"
    @staticmethod
    def the_result_of_choices(num: int):
        return ["Rival had good defence!", "You hit your rival!"][num]
    @staticmethod
    def choices():
        result="Available types:\n"
        for number, tpe in enumerate(attacks):
            result+=f"{number}. {tpe.capitalize()}\n"
        return result
        
    @staticmethod
    def game_finished(boxer_winner: Boxer):
        return f"{boxer_winner.name} won!"

    @staticmethod
    def user_stop_the_game():
        return "Game stopped"