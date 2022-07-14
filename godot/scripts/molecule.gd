extends Node2D

class_name Molecule

export var molname = ""

var products = {}
var quantity = 0

func _ready():
	randomize()
	quantity = randi() % 10 + randf()

func set_molname(n):
	molname = n
	$ui/name_label.text = n

func set_products(dict):
	products = dict

# - Called after every molecule has been created
func establish():
	for key in products:
		for mol in get_parent().molecules:
			if products[key][0] == mol.molname:
				# Create a arrow
				var a = Sprite.new()
				self.add_child(a)
				a.texture = load("res://sprites/16Arrow.png")
				a.position = (mol.global_position - self.global_position)*3.5/6
				a.rotation = (mol.global_position - self.global_position).angle()

func _process(delta):
	if Input.is_action_just_pressed("show_quantities"): print(molname + ": " + str(quantity))
	$ui/name_label.modulate = Color(1, quantity/100, quantity/10 )

func _draw():
	for key in products:
		for mol in get_parent().molecules:
			if products[key][0] == mol.molname:
				# Draw lines between molecules
				draw_line(Vector2.ZERO, mol.global_position - self.global_position, Color(255, 255, 255)) 
