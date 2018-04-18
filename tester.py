import os
import sys

fname = "configuration"
config_source_dir = ""
config_output_dir = ""
config_recursive_pattern = ""
exe_location = ""
with open(fname) as f:
	for line in f:
		if line.startswith("SOURCE_DIR"):
			li = line.strip().split("::")
			config_source_dir = li[1].strip()
			if config_source_dir[-1] != "\\":
				config_source_dir += "\\"
			# config_source_dir = li[1].strip("\\")
			# config_source_dir = li[1].strip("/")
		if line.startswith("OUTPUT_DIR"):
			li = line.strip().split("::")
			config_output_dir = li[1].strip()
			if config_output_dir[-1] != "\\":
				config_output_dir += "\\"
		if line.startswith("DICOM2NIIEXE_LOCATION"):
			li = line.strip().split("::")
			exe_location = li[1].strip()
		if line.startswith("TARGET_RECURSIVE_PATTERN"):
			li = line.strip().split("::")
			config_recursive_pattern = li[1].strip()
			config_recursive_pattern_trim = config_recursive_pattern.strip("xxx")

if config_source_dir == "" or config_output_dir == "" or config_recursive_pattern == "" or exe_location == "":
	print("Check your configuration file!")
	sys.exit(0)

from sys import platform
# TODO !=
if platform == "win32":
	print("We only support windows as for now!")
	sys.exit(0)
else:

	# getting exe location
	exe_location_li = exe_location.split("\\")
	if len(exe_location_li) < 1:
		print("Check your configuration file!")
		sys.exit(0)
	exe_location_li[0] = exe_location_li[0] + "\\"
	exe_path_recursive = os.path.join("")
	for i in exe_location_li:
		exe_path_recursive = os.path.join(exe_path_recursive, i)
	print exe_path_recursive

	config_source_dir_li = config_source_dir.split("\\" + config_recursive_pattern + "\\")
	if config_source_dir_li[0] == "" or len(config_source_dir_li) > 2:
		print("Check your configuration file!")
		sys.exit(0)

	# config_source_dir_pre
	config_source_dir_pre_li = config_source_dir_li[0].split("\\")
	if len(config_source_dir_pre_li) < 1:
		print("Check your configuration file!")
		sys.exit(0)
	config_source_dir_pre_li[0] = config_source_dir_pre_li[0] + "\\"
	pre_path_recursive = os.path.join("")
	for i in config_source_dir_pre_li:
		pre_path_recursive = os.path.join(pre_path_recursive, i)
	print pre_path_recursive
	# config_source_dir_pro
	config_source_dir_pro_li = config_source_dir_li[1].split("\\")
	pro_path_recursive = os.path.join("")
	for i in config_source_dir_pro_li:
		pro_path_recursive = os.path.join(pro_path_recursive, i)
	print pro_path_recursive

	# config_output_dir_pre
	config_output_dir_li = config_output_dir.split("\\" + config_recursive_pattern + "\\")
	if config_output_dir_li[0] == "" or len(config_output_dir_li) > 2:
		print("Check your configuration file!")
		sys.exit(0)
	# config_output_dir_pre
	config_output_dir_pre_li = config_output_dir_li[0].split("\\")
	if len(config_output_dir_pre_li) < 1:
		print("Check your configuration file!")
		sys.exit(0)
	config_output_dir_pre_li[0] = config_output_dir_pre_li[0] + "\\"
	output_pre_path_recursive = os.path.join("")
	for i in config_output_dir_pre_li:
		output_pre_path_recursive = os.path.join(output_pre_path_recursive, i)
	print output_pre_path_recursive
	# config_output_dir_pro
	config_output_dir_pro_li = config_output_dir_li[1].split("\\")
	if len(config_output_dir_pro_li) < 1:
		print("Check your configuration file!")
		sys.exit(0)
	output_pro_path_recursive = os.path.join("")
	for i in config_output_dir_pro_li:
		output_pro_path_recursive = os.path.join(output_pro_path_recursive, i)
	print output_pro_path_recursive

print config_recursive_pattern_trim
    