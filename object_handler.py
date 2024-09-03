from sprite_object import *
from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.1, 1.1)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.9, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(game, pos=(7.1, 5.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 7.9))) 

        #npc map
        add_npc(NPC(game))
        add_npc(NPC(game, pos=(11.5, 4.5)))
        add_npc(CacoDemonNPC(game, pos=(21.3,10.5)))
        add_npc(CyberDemonNPC(game, pos=(25.3, 6.5)))
        # add_npc(NPC(game, pos=(35.5, 6.5)))
        # add_npc(NPC(game, pos=(35.5, 7.5)))
        # add_npc(NPC(game, pos=(35.5, 8.5)))
        # add_npc(NPC(game, pos=(36.5, 6.5)))
        # add_npc(NPC(game, pos=(36.5, 7.5)))
        # add_npc(NPC(game, pos=(36.5, 8.5)))
        # add_npc(NPC(game, pos=(37.5, 6.5)))
        # add_npc(NPC(game, pos=(36.5, 7.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))
        add_npc(NPC(game, pos=(36.5, 8.5)))


    def update(self):
        #calculando a distancia do NPC com o jogador
        # distance = self.npc.check_distance()[1]
        # print('distasce', distance)
        # player_pos = self.game.player.map_pos
        # npc_distances = [(npc, self.game.distance(npc.map_pos, player_pos)) for npc in self.npc_list if npc.alive]

        # #organizando NPCs pela distancia do jogador
        # npc_distances.sort(key=lambda x: x[1])

        # #atualizando somente os NPCs top N que estão na tela
        # max_npcs_on_screen = 10
        # for npc, _ in npc_distances[:max_npcs_on_screen]:
        #     if self.game.is_on_screen(npc.map_pos):
        #         npc.update()

        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)