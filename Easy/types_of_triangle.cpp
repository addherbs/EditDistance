#include <iostream>
#include <string>
#include <sstream>
#include <iterator>
#include <vector>

using namespace std;
int getResult(int x, int y, int z){

    if((x<=0) || (y<=0) || (z<=0)) return 0;
    if(x+y<=z || x+z<=y || z+y<=x) return 0;
    if(x == y && y == z) return 1;
    if((x==y) || (x==z) || (y==z)) return 2;
}

char const* checkTriangle (int a, int b, int c){

    int res = getResult(a,b,c);
    switch(res) {
      case 0 : return "None of these";
      case 1 : return "Equilatrel";
      case 2 : return "Isosceles";
   }
}

vector<string> getType(vector<string> abc){

    std::vector<std::string> finalResult;

    for (int i = 0; i < abc.size(); ++i) {

        string temp = abc[i];
        std::istringstream buf(temp);
        std::istream_iterator<std::string> beg(buf), end;
        std::vector<std::string> tokens(beg, end); // done!
        string result = checkTriangle(stoi(tokens[0]), stoi(tokens[1]), stoi(tokens[2]));
        finalResult.push_back(result);
    }

    return finalResult;
}

int main()
{
    string t = "36 36 24";
    vector<string> abc;
    abc.push_back(t);
    vector<string> res = getType(abc);
    cout << res[0] << "\n";
    return 0;
}
