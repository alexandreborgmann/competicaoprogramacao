#include <iostream>
#include<iomanip>
using namespace std;


int main() {
    
double PI = 3.14159,raio,area;

cin >>raio;

area = PI*(raio*raio);

cout<<fixed<<setprecision(4);
 cout << "A="<<area<<endl;


    
	return 0;
}