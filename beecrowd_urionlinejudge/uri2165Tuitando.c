#include <stdio.h>
#include <string.h>
int main() {
char linha[10000];


 scanf(" %[^(\n)]s",linha);

if(strlen(linha)==0 || strlen(linha)>500)
{
    printf("(1 = |T| = 500)");
    return 0;
}
if(strlen(linha)<=140)
    printf("TWEET\n");
else
    printf("MUTE\n");
    
	return 0;
}
