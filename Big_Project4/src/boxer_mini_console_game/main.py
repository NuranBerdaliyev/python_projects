import sys
from box_model import Boxer
from box_view import Input, Output
from box_controller import Fight

def main():
    response:int=Input.the_main_question()
    if response not in [0, 1]:
        raise ValueError("Invalid answer")
    if response == 0:
        print(Output.user_stop_the_game())
        sys.exit()


    name=input("Enter the name of the first boxer: ")
    b1=Boxer(name, 1)
    name=input("Enter the name of the second boxer: ")
    b2=Boxer(name, 2)

    fight=Fight(b1, b2)

    print(Output.greetings())


    while True:
        try:
            first=Input.first_boxer_choice()
            if first.lower() not in [b1.name.lower(), b2.name.lower()]:
                raise ValueError("Invalid boxer")
            if first.lower()==b1.name.lower():
                turn_order=[b1, b2]
            else:
                turn_order=[b2, b1]
            break
        except ValueError:
            print("Invalid boxer")
            
            
    while True:
        for boxer in turn_order:
            print(Output.whosturn(boxer))
            while True:
                print(Output.choices())
                defence=Input.boxer_defence_choice()
                attack=Input.boxer_attack_choice()
                try:
                    fight.set_boxer_defence_attack(boxer, defence, attack)
                    break
                except ValueError as e:
                    print(e)
            

            result_num=fight.hp_damage(boxer)
            print(Output.the_result_of_choices(result_num))
            
            print(Output.boxer_hp(b1))
            print(Output.boxer_hp(b2))

            winner=fight.game_finished()
            if winner:
                print(Output.game_finished(winner))
                sys.exit()

if __name__=='__main__':
    main()