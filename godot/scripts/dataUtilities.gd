extends Reference

class_name DataUtilities

# - Looks at all the files in a directory and return them as a list 
static func get_all_files_dir(path, filter_import = true):
	var list = []
	
	var dir = Directory.new()
	
	assert(dir.open(path) == OK, "ERROR: get_all_files_dir() invalid path : " + str(path));
	
	dir.list_dir_begin()
	var file_name = dir.get_next()
	while file_name != "":
		if dir.current_is_dir():
			pass
		else:
			list.append(file_name)
		file_name = dir.get_next()
	
	if filter_import: list = filter_by_extension(list)
	
	return list

# - Remove files with a specific extension from a list (positive/negative filter)
static func filter_by_extension(list_of_files, list_of_extensions_positive = ["*"], list_of_extensions_negative = [".import"]):
	var filtered_list = []
	
	for i in range(len(list_of_files)):

		var negatived = false
		for b in list_of_extensions_negative:
			if list_of_files[i].ends_with(b):
				negatived = true
				break
		
		if negatived:
			continue
		
		for b in list_of_extensions_positive:
			if list_of_files[i].ends_with(b) or b == "*":
				filtered_list.append(list_of_files[i])
				break
	
	return filtered_list

# - Remove extension from a list of file names
static func remove_extension(list_of_files):
	var list = []
	for file in list_of_files:
		list.append(file.split(".")[0])
	return list

# - Read text file, ignoring comments, outputs array of all the lines
static func read_file(path, dedent = true):
	var allthelines = []        
	
	var file = File.new()
	file.open(path, file.READ)
	
	while file.get_position() < file.get_len():
		var line = file.get_line()
		if line.dedent() != "":
			if line.dedent()[0] != "#":
				if dedent: line = line.dedent()
				allthelines.append(line)
	
	file.close()
	
	return allthelines

# - Scans a directory and returns a model in arr form
# format for each molecule : [NAME, POSITION, PRODUCTS]
static func read_model_dir(path):
	var all_molecule_files = get_all_files_dir(path)
	var arr = []
	
	for file in all_molecule_files:
		var mol = ["No Name", Vector2.ZERO, {}]
		var content = read_file(path + "/" + file)
		var reading_products = false
		
		for i in range(len(content)):
			if !reading_products:
				if content[i] == "NAME":
					mol[0] = content[i + 1]
				
				elif content[i] == "POSITION":
					var num = content[i + 1].split(" ")
					mol[1] = Vector2(float(num[0]), float(num[1]))
				
				elif content[i] == "PRODUCTS":
					reading_products = true
			else:
				mol[2][len(mol[2])] = content[i].split(" ")
		
		arr.append(mol)
	
	return arr
