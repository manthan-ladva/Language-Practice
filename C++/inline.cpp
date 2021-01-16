// Inline Function
#include<iostream>
using namespace std;
class demo
{
    int x,y,z;
public:
    void in();
    void display();
    void output();
};

inline void demo::in()
{
    cin>>x>>y;
}
inline void demo::display()
{
    cout<<x<<y;
}
inline void demo::output()
{
    z=x+y;
    cout<<"\nAddition ="<<z;
}

int main()
{
    demo s;
    s.in();
    s.display();
    s.output();
    return 0;
}
