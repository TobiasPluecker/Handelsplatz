# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/odin/Schreibtisch/poose3

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/odin/Schreibtisch/poose3/build

# Utility rule file for demo_qt_1_autogen.

# Include any custom commands dependencies for this target.
include CMakeFiles/demo_qt_1_autogen.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/demo_qt_1_autogen.dir/progress.make

CMakeFiles/demo_qt_1_autogen:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/odin/Schreibtisch/poose3/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Automatic MOC and UIC for target demo_qt_1"
	/usr/bin/cmake -E cmake_autogen /home/odin/Schreibtisch/poose3/build/CMakeFiles/demo_qt_1_autogen.dir/AutogenInfo.json ""

demo_qt_1_autogen: CMakeFiles/demo_qt_1_autogen
demo_qt_1_autogen: CMakeFiles/demo_qt_1_autogen.dir/build.make
.PHONY : demo_qt_1_autogen

# Rule to build all files generated by this target.
CMakeFiles/demo_qt_1_autogen.dir/build: demo_qt_1_autogen
.PHONY : CMakeFiles/demo_qt_1_autogen.dir/build

CMakeFiles/demo_qt_1_autogen.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/demo_qt_1_autogen.dir/cmake_clean.cmake
.PHONY : CMakeFiles/demo_qt_1_autogen.dir/clean

CMakeFiles/demo_qt_1_autogen.dir/depend:
	cd /home/odin/Schreibtisch/poose3/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/odin/Schreibtisch/poose3 /home/odin/Schreibtisch/poose3 /home/odin/Schreibtisch/poose3/build /home/odin/Schreibtisch/poose3/build /home/odin/Schreibtisch/poose3/build/CMakeFiles/demo_qt_1_autogen.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/demo_qt_1_autogen.dir/depend

