extends Node2D

var labels = []
var moving = false

func _process(delta):
	if Input.is_action_just_pressed("open_bars"):
		self.visible = !self.visible
	if moving:
		self.position = get_global_mouse_position() - $ui/move.rect_position - $ui/move.rect_size/2
	update()

func _draw():
	if self.visible:
		draw_bars(get_parent().molecules)

func draw_bars(molecules, size = 40, n = 10):
	
	var maxquant = 0
	
	# We order the molecules
	var ordered = []
	for mol in molecules:
		maxquant += mol.quantity
		if len(ordered) < 0:
			ordered.append(mol)
			continue
		for i in range(len(ordered) + 1):
			if i == len(ordered):
				ordered.append(mol)
				continue
			if ordered[i].quantity < mol.quantity:
				ordered.insert(i , mol)
				break
	
	for label in labels:
		label.queue_free()
	labels = []
	
	# Draw a bar for each molecule
	for i in range(n):
		var color = Color(1, ordered[i].quantity/100, ordered[i].quantity/10)
		var bar = Rect2(Vector2.ZERO + Vector2(i * size + i, 0), Vector2(size, -ordered[i].quantity/maxquant * 200))
		draw_rect(bar, color, true)

		var a = Label.new()
		add_child(a)
		labels.append(a)
		a.rect_rotation = 90
		a.rect_size = Vector2(200, size)
		a.valign = Label.VALIGN_CENTER
		a.text = ordered[i].molname
#		a.mouse_filter = Control.MOUSE_FILTER_IGNORE
		a.modulate = color
		a.rect_position = Vector2(size, 30)+ Vector2(i * size + i, 0)
	
	# Set the size and position of background
	var width = size * n + n + 100
	var height = 400
	$ui/background.rect_size = Vector2(width, height)
	$ui/background.rect_position = Vector2(-50, -height/2)
	
	# Set button position
	$ui/move.rect_position = Vector2(width - 90, -height/2)
	$ui/exit.rect_position = Vector2(width - 70, -height/2)

func _on_move_button_down():
	moving = true

func _on_move_button_up():
	moving = false

func _on_exit_pressed():
	self.visible = false
