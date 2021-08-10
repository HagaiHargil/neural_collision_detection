# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

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

# Suppress display of executed commands.
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
CMAKE_SOURCE_DIR = /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build

# Include any dependencies generated for this target.
include src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/depend.make

# Include the progress variables for this target.
include src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/progress.make

# Include the compile flags for this target's objects.
include src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/flags.make

src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/lib/alpha_shapes_3_bindings.cpp.o: src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/flags.make
src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/lib/alpha_shapes_3_bindings.cpp.o: ../src/libs/tri3/lib/alpha_shapes_3_bindings.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/lib/alpha_shapes_3_bindings.cpp.o"
	cd /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/src/libs/tri3 && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CGALPY_TRI3.dir/lib/alpha_shapes_3_bindings.cpp.o -c /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/src/libs/tri3/lib/alpha_shapes_3_bindings.cpp

src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/lib/alpha_shapes_3_bindings.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CGALPY_TRI3.dir/lib/alpha_shapes_3_bindings.cpp.i"
	cd /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/src/libs/tri3 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/src/libs/tri3/lib/alpha_shapes_3_bindings.cpp > CMakeFiles/CGALPY_TRI3.dir/lib/alpha_shapes_3_bindings.cpp.i

src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/lib/alpha_shapes_3_bindings.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CGALPY_TRI3.dir/lib/alpha_shapes_3_bindings.cpp.s"
	cd /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/src/libs/tri3 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/src/libs/tri3/lib/alpha_shapes_3_bindings.cpp -o CMakeFiles/CGALPY_TRI3.dir/lib/alpha_shapes_3_bindings.cpp.s

src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/lib/export_module.cpp.o: src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/flags.make
src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/lib/export_module.cpp.o: ../src/libs/tri3/lib/export_module.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/lib/export_module.cpp.o"
	cd /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/src/libs/tri3 && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CGALPY_TRI3.dir/lib/export_module.cpp.o -c /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/src/libs/tri3/lib/export_module.cpp

src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/lib/export_module.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CGALPY_TRI3.dir/lib/export_module.cpp.i"
	cd /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/src/libs/tri3 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/src/libs/tri3/lib/export_module.cpp > CMakeFiles/CGALPY_TRI3.dir/lib/export_module.cpp.i

src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/lib/export_module.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CGALPY_TRI3.dir/lib/export_module.cpp.s"
	cd /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/src/libs/tri3 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/src/libs/tri3/lib/export_module.cpp -o CMakeFiles/CGALPY_TRI3.dir/lib/export_module.cpp.s

src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/__/cgalpy/lib/kernel_bindings.cpp.o: src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/flags.make
src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/__/cgalpy/lib/kernel_bindings.cpp.o: ../src/libs/cgalpy/lib/kernel_bindings.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/__/cgalpy/lib/kernel_bindings.cpp.o"
	cd /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/src/libs/tri3 && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CGALPY_TRI3.dir/__/cgalpy/lib/kernel_bindings.cpp.o -c /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/src/libs/cgalpy/lib/kernel_bindings.cpp

src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/__/cgalpy/lib/kernel_bindings.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CGALPY_TRI3.dir/__/cgalpy/lib/kernel_bindings.cpp.i"
	cd /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/src/libs/tri3 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/src/libs/cgalpy/lib/kernel_bindings.cpp > CMakeFiles/CGALPY_TRI3.dir/__/cgalpy/lib/kernel_bindings.cpp.i

src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/__/cgalpy/lib/kernel_bindings.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CGALPY_TRI3.dir/__/cgalpy/lib/kernel_bindings.cpp.s"
	cd /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/src/libs/tri3 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/src/libs/cgalpy/lib/kernel_bindings.cpp -o CMakeFiles/CGALPY_TRI3.dir/__/cgalpy/lib/kernel_bindings.cpp.s

# Object files for target CGALPY_TRI3
CGALPY_TRI3_OBJECTS = \
"CMakeFiles/CGALPY_TRI3.dir/lib/alpha_shapes_3_bindings.cpp.o" \
"CMakeFiles/CGALPY_TRI3.dir/lib/export_module.cpp.o" \
"CMakeFiles/CGALPY_TRI3.dir/__/cgalpy/lib/kernel_bindings.cpp.o"

# External object files for target CGALPY_TRI3
CGALPY_TRI3_EXTERNAL_OBJECTS =

src/libs/tri3/tri3_epic.so: src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/lib/alpha_shapes_3_bindings.cpp.o
src/libs/tri3/tri3_epic.so: src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/lib/export_module.cpp.o
src/libs/tri3/tri3_epic.so: src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/__/cgalpy/lib/kernel_bindings.cpp.o
src/libs/tri3/tri3_epic.so: src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/build.make
src/libs/tri3/tri3_epic.so: /usr/lib/x86_64-linux-gnu/libmpfr.so
src/libs/tri3/tri3_epic.so: /usr/lib/x86_64-linux-gnu/libgmpxx.so
src/libs/tri3/tri3_epic.so: /usr/lib/x86_64-linux-gnu/libgmp.so
src/libs/tri3/tri3_epic.so: /usr/local/lib/libCGAL_Core.so.13.0.3
src/libs/tri3/tri3_epic.so: /usr/local/lib/libCGAL.so.13.0.3
src/libs/tri3/tri3_epic.so: /usr/local/lib/libboost_system.so.1.72.0
src/libs/tri3/tri3_epic.so: /usr/local/lib/libboost_thread.so.1.72.0
src/libs/tri3/tri3_epic.so: /usr/local/lib/libboost_python37.so.1.72.0
src/libs/tri3/tri3_epic.so: /usr/lib/x86_64-linux-gnu/libpython3.7m.so
src/libs/tri3/tri3_epic.so: /usr/lib/x86_64-linux-gnu/libmpfr.so
src/libs/tri3/tri3_epic.so: /usr/lib/x86_64-linux-gnu/libgmpxx.so
src/libs/tri3/tri3_epic.so: /usr/lib/x86_64-linux-gnu/libgmp.so
src/libs/tri3/tri3_epic.so: src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX shared library tri3_epic.so"
	cd /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/src/libs/tri3 && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/CGALPY_TRI3.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/build: src/libs/tri3/tri3_epic.so

.PHONY : src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/build

src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/clean:
	cd /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/src/libs/tri3 && $(CMAKE_COMMAND) -P CMakeFiles/CGALPY_TRI3.dir/cmake_clean.cmake
.PHONY : src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/clean

src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/depend:
	cd /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/src/libs/tri3 /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/src/libs/tri3 /data/MatlabCode/PBLabToolkit/External/cgal-python-bindings/build/src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/libs/tri3/CMakeFiles/CGALPY_TRI3.dir/depend

