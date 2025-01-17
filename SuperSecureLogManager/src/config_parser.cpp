#include "config_parser.h"
#include <iostream>
#include <fstream>
#include <string>

std::string ConfigParser::getExportPath(const std::string& configPath) {
    std::ifstream file(configPath);
    if (!file.is_open()) {
        std::cerr << "Error: Could not open config file." << std::endl;
        return "/tmp/exported_logs.zip"; // Default export path
    }

    std::string line;
    while (std::getline(file, line)) {
        // Trim leading/trailing spaces (if needed, can implement a trim function)
        if (line.find("export_path=") == 0) {
            // Extract the value after 'export_path='
            std::string path = line.substr(std::string("export_path=").length());
            file.close();
            return path.empty() ? "/tmp/exported_logs.zip" : path;
        }
    }

    file.close();
    // If no 'export_path=' line is found, return the default path
    return "/tmp/exported_logs.zip";
}

