#ifndef FILE_UTILS_H
#define FILE_UTILS_H
#include <string>

class FileUtils {
public:
    static void viewLog(const std::string& logPath);
    static void exportLog(const std::string& logPath, const std::string& exportPath);
};

#endif
