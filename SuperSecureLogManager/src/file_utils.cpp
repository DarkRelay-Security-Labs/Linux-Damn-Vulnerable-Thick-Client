#include "file_utils.h"
#include <fstream>
#include <iostream>

void FileUtils::viewLog(const std::string& logPath) {
    std::ifstream file(logPath);
    if (!file.is_open()) {
        std::cerr << "Error: Could not open log file." << std::endl;
        return;
    }

    std::string line;
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
    }
    file.close();
}

void FileUtils::exportLog(const std::string& logPath, const std::string& exportPath) {
    std::ifstream src(logPath, std::ios::binary);
    std::ofstream dst(exportPath, std::ios::binary);

    if (!src.is_open() || !dst.is_open()) {
        std::cerr << "Error: Could not open source or destination file." << std::endl;
        return;
    }

    dst << src.rdbuf();
    src.close();
    dst.close();
    std::cout << "Logs exported successfully to: " << exportPath << std::endl;
}
