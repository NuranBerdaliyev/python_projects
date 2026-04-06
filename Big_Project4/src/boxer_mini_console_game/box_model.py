class Boxer:
    attack_types=['jab', 'cross', 'uppercut', 'hook', 'nothing']
    defence_types=['jab', 'cross', 'uppercut', 'hook', 'nothing']
    def __init__(self, name: str, player_id):
        '''
        When boxer is created, we can set only his name and id.
        '''
        self.name=name.capitalize()
        self.player_id=player_id
        self.attack_type=None
        self.defence_type=None
        self.hp=100
    
    
      