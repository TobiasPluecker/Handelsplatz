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

# Include any dependencies generated for this target.
include CMakeFiles/markt.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/markt.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/markt.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/markt.dir/flags.make

CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.o: CMakeFiles/markt.dir/flags.make
CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.o: markt_autogen/mocs_compilation.cpp
CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.o: CMakeFiles/markt.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/odin/Schreibtisch/poose3/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.o -MF CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.o.d -o CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.o -c /home/odin/Schreibtisch/poose3/build/markt_autogen/mocs_compilation.cpp

CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/odin/Schreibtisch/poose3/build/markt_autogen/mocs_compilation.cpp > CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.i

CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/odin/Schreibtisch/poose3/build/markt_autogen/mocs_compilation.cpp -o CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.s

CMakeFiles/markt.dir/extra/markt_pybind.cpp.o: CMakeFiles/markt.dir/flags.make
CMakeFiles/markt.dir/extra/markt_pybind.cpp.o: ../extra/markt_pybind.cpp
CMakeFiles/markt.dir/extra/markt_pybind.cpp.o: CMakeFiles/markt.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/odin/Schreibtisch/poose3/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/markt.dir/extra/markt_pybind.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/markt.dir/extra/markt_pybind.cpp.o -MF CMakeFiles/markt.dir/extra/markt_pybind.cpp.o.d -o CMakeFiles/markt.dir/extra/markt_pybind.cpp.o -c /home/odin/Schreibtisch/poose3/extra/markt_pybind.cpp

CMakeFiles/markt.dir/extra/markt_pybind.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/markt.dir/extra/markt_pybind.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/odin/Schreibtisch/poose3/extra/markt_pybind.cpp > CMakeFiles/markt.dir/extra/markt_pybind.cpp.i

CMakeFiles/markt.dir/extra/markt_pybind.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/markt.dir/extra/markt_pybind.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/odin/Schreibtisch/poose3/extra/markt_pybind.cpp -o CMakeFiles/markt.dir/extra/markt_pybind.cpp.s

CMakeFiles/markt.dir/src/artikel.cpp.o: CMakeFiles/markt.dir/flags.make
CMakeFiles/markt.dir/src/artikel.cpp.o: ../src/artikel.cpp
CMakeFiles/markt.dir/src/artikel.cpp.o: CMakeFiles/markt.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/odin/Schreibtisch/poose3/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/markt.dir/src/artikel.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/markt.dir/src/artikel.cpp.o -MF CMakeFiles/markt.dir/src/artikel.cpp.o.d -o CMakeFiles/markt.dir/src/artikel.cpp.o -c /home/odin/Schreibtisch/poose3/src/artikel.cpp

CMakeFiles/markt.dir/src/artikel.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/markt.dir/src/artikel.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/odin/Schreibtisch/poose3/src/artikel.cpp > CMakeFiles/markt.dir/src/artikel.cpp.i

CMakeFiles/markt.dir/src/artikel.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/markt.dir/src/artikel.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/odin/Schreibtisch/poose3/src/artikel.cpp -o CMakeFiles/markt.dir/src/artikel.cpp.s

CMakeFiles/markt.dir/src/haendler.cpp.o: CMakeFiles/markt.dir/flags.make
CMakeFiles/markt.dir/src/haendler.cpp.o: ../src/haendler.cpp
CMakeFiles/markt.dir/src/haendler.cpp.o: CMakeFiles/markt.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/odin/Schreibtisch/poose3/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/markt.dir/src/haendler.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/markt.dir/src/haendler.cpp.o -MF CMakeFiles/markt.dir/src/haendler.cpp.o.d -o CMakeFiles/markt.dir/src/haendler.cpp.o -c /home/odin/Schreibtisch/poose3/src/haendler.cpp

CMakeFiles/markt.dir/src/haendler.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/markt.dir/src/haendler.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/odin/Schreibtisch/poose3/src/haendler.cpp > CMakeFiles/markt.dir/src/haendler.cpp.i

CMakeFiles/markt.dir/src/haendler.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/markt.dir/src/haendler.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/odin/Schreibtisch/poose3/src/haendler.cpp -o CMakeFiles/markt.dir/src/haendler.cpp.s

CMakeFiles/markt.dir/src/handelsplatz.cpp.o: CMakeFiles/markt.dir/flags.make
CMakeFiles/markt.dir/src/handelsplatz.cpp.o: ../src/handelsplatz.cpp
CMakeFiles/markt.dir/src/handelsplatz.cpp.o: CMakeFiles/markt.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/odin/Schreibtisch/poose3/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/markt.dir/src/handelsplatz.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/markt.dir/src/handelsplatz.cpp.o -MF CMakeFiles/markt.dir/src/handelsplatz.cpp.o.d -o CMakeFiles/markt.dir/src/handelsplatz.cpp.o -c /home/odin/Schreibtisch/poose3/src/handelsplatz.cpp

CMakeFiles/markt.dir/src/handelsplatz.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/markt.dir/src/handelsplatz.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/odin/Schreibtisch/poose3/src/handelsplatz.cpp > CMakeFiles/markt.dir/src/handelsplatz.cpp.i

CMakeFiles/markt.dir/src/handelsplatz.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/markt.dir/src/handelsplatz.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/odin/Schreibtisch/poose3/src/handelsplatz.cpp -o CMakeFiles/markt.dir/src/handelsplatz.cpp.s

# Object files for target markt
markt_OBJECTS = \
"CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.o" \
"CMakeFiles/markt.dir/extra/markt_pybind.cpp.o" \
"CMakeFiles/markt.dir/src/artikel.cpp.o" \
"CMakeFiles/markt.dir/src/haendler.cpp.o" \
"CMakeFiles/markt.dir/src/handelsplatz.cpp.o"

# External object files for target markt
markt_EXTERNAL_OBJECTS =

markt.cpython-310-x86_64-linux-gnu.so: CMakeFiles/markt.dir/markt_autogen/mocs_compilation.cpp.o
markt.cpython-310-x86_64-linux-gnu.so: CMakeFiles/markt.dir/extra/markt_pybind.cpp.o
markt.cpython-310-x86_64-linux-gnu.so: CMakeFiles/markt.dir/src/artikel.cpp.o
markt.cpython-310-x86_64-linux-gnu.so: CMakeFiles/markt.dir/src/haendler.cpp.o
markt.cpython-310-x86_64-linux-gnu.so: CMakeFiles/markt.dir/src/handelsplatz.cpp.o
markt.cpython-310-x86_64-linux-gnu.so: CMakeFiles/markt.dir/build.make
markt.cpython-310-x86_64-linux-gnu.so: CMakeFiles/markt.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/odin/Schreibtisch/poose3/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Linking CXX shared module markt.cpython-310-x86_64-linux-gnu.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/markt.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/markt.dir/build: markt.cpython-310-x86_64-linux-gnu.so
.PHONY : CMakeFiles/markt.dir/build

CMakeFiles/markt.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/markt.dir/cmake_clean.cmake
.PHONY : CMakeFiles/markt.dir/clean

CMakeFiles/markt.dir/depend:
	cd /home/odin/Schreibtisch/poose3/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/odin/Schreibtisch/poose3 /home/odin/Schreibtisch/poose3 /home/odin/Schreibtisch/poose3/build /home/odin/Schreibtisch/poose3/build /home/odin/Schreibtisch/poose3/build/CMakeFiles/markt.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/markt.dir/depend
