extends Node2D

var totaldelta = 0
onready var main = get_parent().get_parent().get_parent().get_parent()

# FORMAT : [y : quantity, x : time, color]
var points = []
var reset = false
var graph_scaling = Vector2(5, 15)
var graph_offset = Vector2(50, 360)

func _draw():
	if reset:
		for point in points:
			var v = point[0]
			draw_circle(v, 1, point[1])
		reset = false
	for molecule in main.molecules:
		var v = Vector2(totaldelta, -molecule.quantity) * graph_scaling + graph_offset
		draw_circle(v, 1, molecule.color)

func _process(delta):
	for molecule in main.molecules:
		points.append([Vector2(totaldelta, -molecule.quantity) * graph_scaling + graph_offset, molecule.color])
	
	if Input.is_action_pressed("open_lines"):
		reset = true
	
	totaldelta += delta
	update()

