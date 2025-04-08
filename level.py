class Level:
    def __init__(self, level=1):
        self.level = level
        self.enemy_speed_multiplier = 1
        self.spawn_rate = 1
        self.set_level_attributes()
        
    def set_level_attributes(self):    
        self.enemy_threshold = int(20 * self.level **1.5)
        self.enemy_points = self.enemy_threshold // 20
        self.enemies_killed_this_round = 0
        self.enemy_count = 0
        self.enemy_speed_multiplier += .25
        self.spawn_rate += .1*self.level
    
    def level_up(self):
        self.level += 1
        self.set_level_attributes()