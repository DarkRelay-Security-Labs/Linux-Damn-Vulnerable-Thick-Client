#include <iostream>
#include <fstream>
#include <dlfcn.h>
#include "config_parser.h"
#include "file_utils.h"
#include <filesystem>
#include <cstdlib>
#include <sstream>
#include <unistd.h>
#include <dlfcn.h>
#include <stdio.h>

#define LIBRARY_PATH "liblogprocessor.so"

void displayMenu() {
    std::cout << "\nSuperSecureLogManager" << std::endl;
    std::cout << "1. View Logs" << std::endl;
    std::cout << "2. Export Logs" << std::endl;
    std::cout << "3. Exit" << std::endl;
    std::cout << "Choose an option: ";
}

int main() {
    int choice;
    std::string configPath = "/etc/logmanager.conf";

    if (seteuid(0) != 0) {  // Switch back to root if possible
        perror("seteuid failed");
        return -1;
    }
    // Dynamically load the library
    void* handle = dlopen(LIBRARY_PATH, RTLD_LAZY);
    if (!handle) {
        std::cerr << "Error loading library: " << dlerror() << std::endl;
        return 1;
    }

    auto filterLogs = (void (*)(const char*))dlsym(handle, "filterLogs");
    if (!filterLogs) {
        std::cerr << "Error loading function: " << dlerror() << std::endl;
        dlclose(handle);
        return 1;
    }

    while (true) {
        displayMenu();
        std::cin >> choice;
        std::cin.ignore();

        switch (choice) {
            case 1: {
                std::cout << "Enter log file path: ";
                std::string logPath;
                std::cin >> logPath;
                FileUtils::viewLog(logPath);
                break;
            }
            case 2: {
                std::string exportPath = ConfigParser::getExportPath(configPath);
                std::cout << "Exporting /var/log directory to: " << exportPath << std::endl;

                // Use the export path from the configuration file
                std::ostringstream command;
                command << "zip -r " << exportPath << " /var/log";
                std::cout << command.str();
                int result = std::system(command.str().c_str());

                if (result != 0) {
                    std::cerr << "Error compressing /var/log directory." << std::endl;
                } else {
                    std::cout << "Logs exported successfully to: " << exportPath << std::endl;
                }
                break;
            }
            case 3:
                std::cout << "Exiting..." << std::endl;
                dlclose(handle);
                return 0;
            default:
                std::cout << "Invalid choice. Try again." << std::endl;
        }
    }
}
