# Work is in progress
Traceback (most recent call last):
  File "ex43.py", line 238, in <module>
    a_game.play()
  File "ex43.py", line 20, in play
    current_scene = self.scene_map.opening_scene()
  File "ex43.py", line 234, in opening_scene
    return self.next_scene(self.start_scene)
  File "ex43.py", line 230, in next_scene
    val = Map.scenes.get(scene.name)
NameError: global name 'scene' is not defined
