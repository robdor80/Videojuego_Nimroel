cmake_minimum_required(VERSION 3.25)
project(NimroelCoreRPGBridge LANGUAGES CXX)
# Production and reference lab share pins, ABI and binding profile.
include(../cmake/dependencies.cmake)
add_library(nimroel_core SHARED src/bridge.cpp)
target_link_libraries(nimroel_core PRIVATE CoreRPG::CoreRPG godot::cpp)
target_compile_features(nimroel_core PRIVATE cxx_std_20)
set_target_properties(nimroel_core PROPERTIES
    CXX_EXTENSIONS OFF CXX_VISIBILITY_PRESET hidden VISIBILITY_INLINES_HIDDEN ON
    MSVC_RUNTIME_LIBRARY MultiThreaded
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/../../Host2D/native/bin"
    RUNTIME_OUTPUT_DIRECTORY_RELEASE "${CMAKE_CURRENT_SOURCE_DIR}/../../Host2D/native/bin"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/../../Host2D/native/bin")
if(MSVC)
    target_link_options(nimroel_core PRIVATE "/MAP:${CMAKE_CURRENT_BINARY_DIR}/nimroel.map")
else()
    target_link_options(nimroel_core PRIVATE "-Wl,-Map,${CMAKE_CURRENT_BINARY_DIR}/nimroel.map" -Wl,--no-undefined)
endif()
if(ANDROID)
    if(NOT ANDROID_ABI STREQUAL "arm64-v8a")
        message(FATAL_ERROR "Only Android ARM64 is supported")
    endif()
    set_target_properties(nimroel_core PROPERTIES OUTPUT_NAME nimroel_core.android.arm64)
    target_link_options(nimroel_core PRIVATE -Wl,-z,max-page-size=16384)
elseif(WIN32 AND CMAKE_SIZEOF_VOID_P EQUAL 8)
    set_target_properties(nimroel_core PROPERTIES OUTPUT_NAME nimroel_core.windows.x86_64)
elseif(CMAKE_SYSTEM_NAME STREQUAL "Linux" AND CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64")
    set_target_properties(nimroel_core PROPERTIES OUTPUT_NAME nimroel_core.linux.x86_64)
else()
    message(FATAL_ERROR "Unsupported bridge platform")
endif()
