#include <iostream>

extern "C" void filterLogs(const char* logPath) {
    std::cout << "Filtering logs for: " << logPath << std::endl;
}
