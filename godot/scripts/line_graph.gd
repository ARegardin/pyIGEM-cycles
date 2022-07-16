extends Node2D

onready var main = get_parent()
var moving = false

func _process(delta):
	if Input.is_action_just_pressed("open_lines"):
		self.visible = !self.visible
	if moving:
		self.position = get_global_mouse_position() - $ui/move.rect_position - $ui/move.rect_size/2

func _draw():
	for i in range(len(main.molecules)):
		draw_string(Control.new().get_font("font"), Vector2(50, 400 + 15 * i), main.molecules[i].molname, main.molecules[i].color)

func _on_exit_pressed():
	self.visible = false

func _on_move_button_down():
	moving = true

func _on_move_button_up():
	moving = false
