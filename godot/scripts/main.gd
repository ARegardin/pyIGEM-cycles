extends Node2D

var molecule_scene = preload("res://scenes/molecule.tscn")
var molecules = []

func _ready():
	create_model("../data")

# - Create the model from a directory
func create_model(dir):
	var data = DataUtilities.read_model_dir(dir)
	for mol in data:
		var a = molecule_scene.instance()
		self.add_child(a)
		a.set_molname(mol[0])
		a.position = mol[1]
		a.set_products(mol[2])
		
		molecules.append(a)

	# First I wanted to have every molecules know it's inputs but it's not needed (yet... maybe)
#	for mol1 in molecules:
#		for key in mol1.products:
#			for mol2 in molecules:
#				if mol2.molname == mol1.products[key][0]:
#					mol2.inputs[len(mol2.inputs)] = mol1.molname

	for mol in molecules:
		mol.establish()

# - Move the model foward delta amount
func model_step(dt):
	var previous_quantities = {}
	
	for mol in molecules:
		previous_quantities[mol.molname] = mol.quantity
	
	for mol1 in molecules:
		for key in mol1.products:
			for mol2 in molecules:
				if mol2.molname == mol1.products[key][0]:
					
					# Linear
					if mol1.products[key][1] == "linear":
						var net = previous_quantities[mol1.molname] * dt * float(mol1.products[key][2])
						mol1.quantity -= net
						mol2.quantity += net
					
					# Michaelis
					elif mol1.products[key][1] == "michaelis" or mol1.products[key][1] == "micha":
						var net = (previous_quantities[mol1.molname] / (previous_quantities[mol1.molname] + float(mol1.products[key][2]))) * dt * float(mol1.products[key][3])
						mol1.quantity -= net
						mol2.quantity += net
	
		if mol1.quantity < 0:
			mol1.quantity = 0

func _process(delta):
	model_step(delta)
	update()
