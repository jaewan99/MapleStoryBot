"""A collection of all commands that Adele can use to interact with the game. 	"""

from src.common import config, settings, utils
import time
import math
from src.routine.components import Command
from src.common.vkeys import press, key_down, key_up

import random
# List of key mappings
class Key:
    # important keys
    JUMP = 'c'
    FLASH_JUMP = 'c'
    HIGH_RISE = 'shift'
    Attack = 'a'
    
# Buffs
    큰칼 = 'f1'
    루나 = 'f2'
    SPEED_INFUSION = 'f3'
    NOTHING = 'f4'
    코스모스 = 'f5'
    코샤워 = 'e'
    에샤워 = '2'
    COMBAT_ORDERS = 'f6'
    ADVANCED_BLESSING = 'f7'
    CONVERSION_OVERDRIVE = 'f8'
    WEAPON_AURA = 'f9'
    DIVINE_WRATH = 'end'
    GRANDIS_GODDESS = 'page up'
    LEGACY_RESTORATION = 'page down'



    # Buffs Toggle
    AETHER_FORGE = 'f10'
    AETHERIAL_ARMS = 'f11'

    # Skills
    CLEAVE = 'q'
    HUNTING_DECREE = 'w'
    RUIN = 'e'
    STORM = 't'
    NOBLE_SUMMONS = 'a'
    AETHER_BLOOM = 's'
    REIGN_OF_DESTRUCTION = 'd'
    SHARDBREAKER = 'g'
    MAGIC_DISPATCH = 'shift'
    TRUE_NOBILITY = 'x'
    GRAVE_PROCLAMATION = 'c'
    BLADE_TORRENT = 'b'
    INFINITY_BLADE = 'home'
    LUCID_SOUL = '3'
    ARACHNID = '4'
    ERDA_SHOWER = 'h'
    BLESSING = 'q'
    PORTAL = 'up'
    RESTART = 'f6'
    

#########################
#       Commands        #
#########################

def step(direction, target):
    """
    Performs one movement step in the given DIRECTION towards TARGET.
    Should not press any arrow keys, as those are handled by Auto Maple.
    """

    num_presses = 2
    
    if direction == 'up' or direction == 'down':
        num_presses = 1
    if config.stage_fright and direction != 'up' and utils.bernoulli(0.75):
        time.sleep(utils.rand_float(0.1, 0.3))
    d_y = target[1] - config.player_pos[1]
    if abs(d_y) > settings.move_tolerance * 1.5:
        if direction == 'down':
            press(Key.JUMP, 3)
        elif direction == 'up':
            # time.sleep(3)
            # print('jump')
            press(Key.JUMP, 2)
    else:
        press(Key.Attack, 1)

        #for adele
        # time.sleep(.6)
        

    # time.sleep(0.1)
    press(Key.FLASH_JUMP, num_presses)


class Adjust(Command):
    """Fine-tunes player position using small movements."""

    def __init__(self, x, y, max_steps=5):
        super().__init__(locals())
        self.target = (float(x), float(y))
        self.max_steps = settings.validate_nonnegative_int(max_steps)

    def main(self):
        counter = self.max_steps
        toggle = True
        error = utils.distance(config.player_pos, self.target)
        while config.enabled and counter > 0 and error > settings.adjust_tolerance:
            if toggle:
                d_x = self.target[0] - config.player_pos[0]
                threshold = settings.adjust_tolerance / math.sqrt(2)
                if abs(d_x) > threshold:
                    walk_counter = 0
                    if d_x < 0:
                        key_down('left')
                        while config.enabled and d_x < -1 * threshold and walk_counter < 60:
                            time.sleep(random.uniform(.3,.8))
                            walk_counter += 1
                            d_x = self.target[0] - config.player_pos[0]
                        key_up('left')
                    else:
                        key_down('right')
                        while config.enabled and d_x > threshold and walk_counter < 60:
                            time.sleep(random.uniform(.3,.8))
                            walk_counter += 1
                            d_x = self.target[0] - config.player_pos[0]
                        key_up('right')
                    counter -= 1
            else:
                d_y = self.target[1] - config.player_pos[1]
                if abs(d_y) > settings.adjust_tolerance / math.sqrt(2):
                    if d_y < 0:
                        time.sleep(random.uniform(.3,.8))
                        print('upjump')
                        FlashJump('up').main()
                    else:
                        key_down('down')
                        time.sleep(random.uniform(.3,.8))
                        press(Key.JUMP, 3, down_time=0.1)
                        key_up('down')
                        time.sleep(1)
                    counter -= 1
            error = utils.distance(config.player_pos, self.target)
            toggle = not toggle


class Buff(Command):
    """Uses each of Adele's buffs once."""

    def __init__(self):
        super().__init__(locals())
        self.cd120_buff_time = 0
        # self.cd180_buff_time = 0
        # self.cd200_buff_time = 0
        # self.cd240_buff_time = 0
        # self.cd900_buff_time = 0
        # self.decent_buff_time = 0

    
    def main(self):

        buffs = [Key.SPEED_INFUSION, Key.NOTHING, Key.코스모스, Key.COMBAT_ORDERS, Key.ADVANCED_BLESSING]
        now = time.time()
        
        if self.cd120_buff_time == 0 or now - self.cd120_buff_time > 90:
            press(Key.루나, 2)
            # press(Key.큰칼, 2)
            press(Key.코스모스, 2)
            self.cd120_buff_time = now
        
        # if self.cd180_buff_time == 0 or now - self.cd180_buff_time > 180:
	    #     press(Key.WEAPON_AURA, 2)
	    #     press(Key.LEGACY_RESTORATION, 2)
	    #     self.cd180_buff_time = now
        # if self.cd200_buff_time == 0 or now - self.cd200_buff_time > 100:
	    #     press(Key.큰칼, 2)
	    #     press(Key.CONVERSION_OVERDRIVE, 2)
	    #     self.cd200_buff_time = now
        # if self.cd240_buff_time == 0 or now - self.cd240_buff_time > 240:
	    #     press(Key.GRANDIS_GODDESS, 2)
	    #     self.cd240_buff_time = now
        # if self.cd900_buff_time == 0 or now - self.cd900_buff_time > 100:
	    #     press(Key.루나, 2)
	    #     self.cd900_buff_time = now
        # if self.decent_buff_time == 0 or now - self.decent_buff_time > settings.buff_cooldown:
	    #     for key in buffs:
		#         press(key, 3, up_time=0.3)
	    #     self.decent_buff_time = now		

            
        
        

class FlashJump(Command):
    """Performs a flash jump in the given direction."""

    def __init__(self, direction):
        super().__init__(locals())
        self.direction = settings.validate_arrows(direction)

    def main(self):
        key_down(self.direction)
        
        press(Key.FLASH_JUMP, 1)
        
        randomJump = (random.uniform(.3,.6))
        if self.direction == 'up':
            
            press(Key.FLASH_JUMP, randomJump)
        else:
            press(Key.FLASH_JUMP, randomJump)
        key_up(self.direction)
        time.sleep(0.2)
		
class Attack(Command):
    """Uses 'Attack' once."""

    def main(self):
        uptimeRand = (random.uniform(.03,.07))
        press(Key.Attack, 1, up_time=uptimeRand)
		
class JUMPING(Command):
    """Uses 'Noble summons' once."""

    def main(self):
        uptimeRand = (random.uniform(.03,.07))
        press(Key.JUMP, 1, up_time=uptimeRand)


class coShower(Command):
    """Uses 'Noble summons' once."""

    def main(self):
        time.sleep(.5)
        press(Key.코샤워, 5)

class eShower(Command):
    """Uses 'Noble summons' once."""

    def main(self):
        time.sleep(.5)
        key_down('down')
        time.sleep(.3)
        press(Key.에샤워, 5)
        time.sleep(.05)
        key_up('down')
class RopeConnect(Command):
    """Uses 'Attack' once."""

    def main(self):
        press(Key.HIGH_RISE, 3, up_time=0.05)






