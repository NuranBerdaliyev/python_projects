

from box_model import Boxer

class Fight:
    def __init__(self, boxer1, boxer2):
        self.boxer1: Boxer = boxer1
        self.boxer2: Boxer = boxer2
    
    def set_boxer_defence_attack(self, boxer: Boxer, defence_type, attack_type):
        '''
        This function sets defence and attack type to the boxer from params if he is the one of two boxers in class Fight.
        '''
        if defence_type not in Boxer.defence_types:
            raise ValueError("Invalid defence type")
        if attack_type not in Boxer.attack_types:
            raise ValueError("Invalid attack type")
       
        boxer.defence_type=defence_type; boxer.attack_type=attack_type
    
    def hp_damage(self, boxer: Boxer):
        '''
        After checking that boxer is one of the two boxers in the fight class, this function decides if this boxer hit his rival or he doesn't.
        If boxer's rival chose defence that was boxer's attack, he doesn't get hp damage, otherwise -5 hp. 
        '''
        
        boxer_enemy = self.boxer1 if boxer is self.boxer2 else self.boxer2
        if boxer.attack_type!=boxer_enemy.defence_type:
            boxer_enemy.hp=max(boxer_enemy.hp-5, 0)
            return 1
        return 0
    
        
    def game_finished(self):
        if self.boxer1.hp==0:
            return self.boxer2
        if self.boxer2.hp==0:
            return self.boxer1
        return None
        
            

