a_map = Map('central corridor')
# creates an instance of Map named a_map and passes in variable 'central corridor'
a_map.start_scene = 'central corridor'
# assigns 'central corridor' to variable start_scene

a_game = Engine(a_map)
# creates an instance of Engine and passes in a_map and assigns the object to a_game
# this assigns a_map to a_game.scene_map

a_game.play()
# this calls the play function of a_game

current_scene = self.scene_map.opening_scene()
# current_scene = 'central corridor'

last_scene = self.scene_map.next_scene('finished')
# a_map.next_scene = 'finished'
# last_scene = 'finished'

