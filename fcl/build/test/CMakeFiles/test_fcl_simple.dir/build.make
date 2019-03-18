# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

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
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/ccmake

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /data/simulated_morph_data/fcl

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /data/simulated_morph_data/fcl/build

# Include any dependencies generated for this target.
include test/CMakeFiles/test_fcl_simple.dir/depend.make

# Include the progress variables for this target.
include test/CMakeFiles/test_fcl_simple.dir/progress.make

# Include the compile flags for this target's objects.
include test/CMakeFiles/test_fcl_simple.dir/flags.make

test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o: test/CMakeFiles/test_fcl_simple.dir/flags.make
test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o: ../test/test_fcl_simple.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /data/simulated_morph_data/fcl/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o"
	cd /data/simulated_morph_data/fcl/build/test && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o -c /data/simulated_morph_data/fcl/test/test_fcl_simple.cpp

test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.i"
	cd /data/simulated_morph_data/fcl/build/test && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /data/simulated_morph_data/fcl/test/test_fcl_simple.cpp > CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.i

test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.s"
	cd /data/simulated_morph_data/fcl/build/test && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /data/simulated_morph_data/fcl/test/test_fcl_simple.cpp -o CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.s

test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o.requires:
.PHONY : test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o.requires

test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o.provides: test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o.requires
	$(MAKE) -f test/CMakeFiles/test_fcl_simple.dir/build.make test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o.provides.build
.PHONY : test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o.provides

test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o.provides.build: test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o

# Object files for target test_fcl_simple
test_fcl_simple_OBJECTS = \
"CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o"

# External object files for target test_fcl_simple
test_fcl_simple_EXTERNAL_OBJECTS =

test/test_fcl_simple: test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o
test/test_fcl_simple: test/CMakeFiles/test_fcl_simple.dir/build.make
test/test_fcl_simple: lib/libfcl.so.0.6.0
test/test_fcl_simple: lib/libtest_fcl_utility.a
test/test_fcl_simple: lib/libgtest.a
test/test_fcl_simple: lib/libfcl.so.0.6.0
test/test_fcl_simple: /usr/local/lib64/libccd.so.2.0
test/test_fcl_simple: /usr/lib64/libm.so
test/test_fcl_simple: test/CMakeFiles/test_fcl_simple.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable test_fcl_simple"
	cd /data/simulated_morph_data/fcl/build/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_fcl_simple.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/CMakeFiles/test_fcl_simple.dir/build: test/test_fcl_simple
.PHONY : test/CMakeFiles/test_fcl_simple.dir/build

test/CMakeFiles/test_fcl_simple.dir/requires: test/CMakeFiles/test_fcl_simple.dir/test_fcl_simple.cpp.o.requires
.PHONY : test/CMakeFiles/test_fcl_simple.dir/requires

test/CMakeFiles/test_fcl_simple.dir/clean:
	cd /data/simulated_morph_data/fcl/build/test && $(CMAKE_COMMAND) -P CMakeFiles/test_fcl_simple.dir/cmake_clean.cmake
.PHONY : test/CMakeFiles/test_fcl_simple.dir/clean

test/CMakeFiles/test_fcl_simple.dir/depend:
	cd /data/simulated_morph_data/fcl/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /data/simulated_morph_data/fcl /data/simulated_morph_data/fcl/test /data/simulated_morph_data/fcl/build /data/simulated_morph_data/fcl/build/test /data/simulated_morph_data/fcl/build/test/CMakeFiles/test_fcl_simple.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/CMakeFiles/test_fcl_simple.dir/depend
