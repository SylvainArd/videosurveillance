# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.0

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

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/sylvain/Documents/VideoSurveillance/videosurveillance/cascadeclassifier

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/sylvain/Documents/VideoSurveillance/videosurveillance/cascadeclassifier

# Include any dependencies generated for this target.
include CMakeFiles/videosurveillance.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/videosurveillance.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/videosurveillance.dir/flags.make

CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o: CMakeFiles/videosurveillance.dir/flags.make
CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o: videosurveillance.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/sylvain/Documents/VideoSurveillance/videosurveillance/cascadeclassifier/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o -c /home/sylvain/Documents/VideoSurveillance/videosurveillance/cascadeclassifier/videosurveillance.cpp

CMakeFiles/videosurveillance.dir/videosurveillance.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/videosurveillance.dir/videosurveillance.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/sylvain/Documents/VideoSurveillance/videosurveillance/cascadeclassifier/videosurveillance.cpp > CMakeFiles/videosurveillance.dir/videosurveillance.cpp.i

CMakeFiles/videosurveillance.dir/videosurveillance.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/videosurveillance.dir/videosurveillance.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/sylvain/Documents/VideoSurveillance/videosurveillance/cascadeclassifier/videosurveillance.cpp -o CMakeFiles/videosurveillance.dir/videosurveillance.cpp.s

CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o.requires:
.PHONY : CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o.requires

CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o.provides: CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o.requires
	$(MAKE) -f CMakeFiles/videosurveillance.dir/build.make CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o.provides.build
.PHONY : CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o.provides

CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o.provides.build: CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o

# Object files for target videosurveillance
videosurveillance_OBJECTS = \
"CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o"

# External object files for target videosurveillance
videosurveillance_EXTERNAL_OBJECTS =

videosurveillance: CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o
videosurveillance: CMakeFiles/videosurveillance.dir/build.make
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_videostab.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_video.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_ts.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_superres.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_stitching.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_photo.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_ocl.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_objdetect.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_ml.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_legacy.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_imgproc.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_highgui.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_gpu.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_flann.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_features2d.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_core.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_contrib.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_calib3d.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_photo.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_legacy.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_video.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_objdetect.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_ml.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_calib3d.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_features2d.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_highgui.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_imgproc.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_flann.so.2.4.9
videosurveillance: /usr/lib/i386-linux-gnu/libopencv_core.so.2.4.9
videosurveillance: CMakeFiles/videosurveillance.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable videosurveillance"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/videosurveillance.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/videosurveillance.dir/build: videosurveillance
.PHONY : CMakeFiles/videosurveillance.dir/build

CMakeFiles/videosurveillance.dir/requires: CMakeFiles/videosurveillance.dir/videosurveillance.cpp.o.requires
.PHONY : CMakeFiles/videosurveillance.dir/requires

CMakeFiles/videosurveillance.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/videosurveillance.dir/cmake_clean.cmake
.PHONY : CMakeFiles/videosurveillance.dir/clean

CMakeFiles/videosurveillance.dir/depend:
	cd /home/sylvain/Documents/VideoSurveillance/videosurveillance/cascadeclassifier && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sylvain/Documents/VideoSurveillance/videosurveillance/cascadeclassifier /home/sylvain/Documents/VideoSurveillance/videosurveillance/cascadeclassifier /home/sylvain/Documents/VideoSurveillance/videosurveillance/cascadeclassifier /home/sylvain/Documents/VideoSurveillance/videosurveillance/cascadeclassifier /home/sylvain/Documents/VideoSurveillance/videosurveillance/cascadeclassifier/CMakeFiles/videosurveillance.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/videosurveillance.dir/depend

