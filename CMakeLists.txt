#----------------------------------------------#
#-----Konfiguration des Buildsystems CMake-----#
#----------------------------------------------#

# Minimale Version des Buildsystems
cmake_minimum_required(VERSION 3.14)
# Name des Projekts
project(stockmarket)


#----------------------------------------------#
#-------------------Optionen-------------------#
#----------------------------------------------#

# Setzte verwendeten C++-Standard auf C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Prüfe ob Heapspeicher gefunden wird,
# der nicht freigegeben wurde
# add_compile_options(-fsanitize=address)
# add_link_options(-fsanitize=address)

# Füge selbsgeschriebene Includes hinzu
include_directories(include)
# Füge externe Includes hinzu
include_directories(external)


#----------------------------------------------#
#----------Download and use GoogleTest---------#
#----------------------------------------------#

# Use CMakes FetchContent
include(FetchContent)
# Workaround for CMake >= 3.24
# Avoid warning about DOWNLOAD_EXTRACT_TIMESTAMP
if (CMAKE_VERSION VERSION_GREATER_EQUAL "3.24.0")
  cmake_policy(SET CMP0135 NEW)
endif()

# Download GoogleTest (we use version 1.12.1)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
# Workaround for Windows:
# Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

# GoogleTest soll nur lokal, in diesem Projekt verwendet werden.
option(INSTALL_GTEST "Enable installation of googletest." OFF)

# Include CMake configuration of GoogleTest
FetchContent_MakeAvailable(googletest)
include(GoogleTest)

# Enable GoogleTest
enable_testing()


#----------------------------------------------#
#---------------Verwende Pybind11--------------#
#----------------------------------------------#
find_package(pybind11 REQUIRED)


#----------------------------------------------#
#------------------Verwende Qt-----------------#
#----------------------------------------------#
# Die folgenden drei Befehle sind für QT < 6.3 nötig.
# Ab QT >= 6.3 können diese durch 'qt_standard_project_setup()' ersetzt werden.
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

# Falls eine Klasse beim Bauen nicht gefunden wird, lohnt ein Blick in die entsprechende Qt6-Dokumenation unter
#     https://doc.qt.io/
# Dort steht
#    welche C++Header eingebunden werden müssen,
#    welche CMake-Packages eingebunden werden müssen und
#    welche Bibliotheken gelinkt werden müssen
# Die letzten beiden Punkte müssen hier unter
#    find_package und
#    target_link_libraries
# ergänzt werden
find_package(Qt6 REQUIRED COMPONENTS Core)
find_package(Qt6 REQUIRED COMPONENTS Widgets)


#----------------------------------------------#
#---------------Erzeuge Projekt----------------#
#----------------------------------------------#
# Legt die Variable SRC_FILES an, die alle
# .cpp-Dateien des Projekts benennt,
# die in Verzeichnis src/ liegen.
file(GLOB SRC_FILES ${PROJECT_SOURCE_DIR}/src/*.cpp)

add_executable(demo_qt_1
    examples/demo_qt_1.cpp
)
# Baue pybind11-Schnittstelle
pybind11_add_module(markt
  extra/markt_pybind.cpp
  ${SRC_FILES}
)

target_link_libraries(demo_qt_1 PRIVATE Qt6::Core Qt6::Widgets)


#----------------------------------------------#
#----------Installation des Projekts-----------#
#----------------------------------------------#
install(TARGETS markt
  COMPONENT python
  LIBRARY DESTINATION "${PROJECT_SOURCE_DIR}/extra")
