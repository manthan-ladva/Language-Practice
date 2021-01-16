// Constructor
#include<iostream>
using namespace std;
class demo
{
private:
    int x,y,z;
public:
    demo()
    {
        cin>>x>>y;
    }
    void display();
    void add();
    ~demo()
    {
        cout<<"Destructor has called";
    }
};

inline void demo::display()
{
    cout<<"\n"<<x<<y;
}
inline void demo::add()
{
    z=x+y;
    cout<<"\nAdd ="<<z;
}

int main()
{
    demo d1;
    d1.display();
    d1.add();
    return 0;
}
