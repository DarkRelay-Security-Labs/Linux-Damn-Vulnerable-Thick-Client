#ifndef CONFIG_PARSER_H
#define CONFIG_PARSER_H
#include <string>

class ConfigParser {
public:
    static std::string getExportPath(const std::string& configPath);
};

#endif
