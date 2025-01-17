# Makefile for SuperSecureLogManager

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -Werror
LDFLAGS = -Wl,-rpath,/tmp,-ldl

# Directories
SRC_DIR = src
INCLUDE_DIR = include
LIB_DIR = lib
BUILD_DIR = build

# Files
TARGET = $(BUILD_DIR)/SuperSecureLogManager
LIBRARY = $(LIB_DIR)/liblogprocessor.so
SRC_FILES = $(wildcard $(SRC_DIR)/*.cpp)
OBJ_FILES = $(patsubst $(SRC_DIR)/%.cpp, $(BUILD_DIR)/%.o, $(SRC_FILES))

# Build targets
all: $(TARGET) $(LIBRARY)

# Ensure the build directory exists
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

# Target for the main application
$(TARGET): $(OBJ_FILES) | $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) $(OBJ_FILES) -o $@ $(LDFLAGS)

# Rule for compiling source files into object files
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp | $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) -I$(INCLUDE_DIR) -c $< -o $@

# Rule for building the shared library
$(LIBRARY): $(LIB_DIR)/liblogprocessor.cpp
	$(CXX) -shared -fPIC $< -o $@

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR) $(LIBRARY)

.PHONY: all clean

