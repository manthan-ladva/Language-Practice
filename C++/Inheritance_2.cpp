/*Complete Inheritance Program*/

#include<iostream>
using namespace std;
class enter1  //--------------------------------------------Base class
{
protected:
    int a,b,f,g;
};

class enter2  //--------------------------------------------Base Class
{
protected:
    int c,d,e,h;
};

class value_ab:public enter1
{
protected:
    int sum,mul,sub;
public:
    int val_ab()
    {
        cout<<"Give the value of a and b\n";
        cin>>a>>b;
    }
};//----------------------------------------------------------------Single

class value_cd:public enter2
{
public:
    int val_cd()
    {
        cout<<"\n\nGive the value of c and d\n";
        cin>>c>>d;
    }
}; //----------------------------------------------------------------Single

class addition:public value_ab
{
public:
    int add()
    {
        sum=a+b;
        cout<<"\nAddition ="<<sum;
    }
}; //-------------------------------------------------------------Multilevel

class subtraction:public value_ab, public value_cd
{
public:
    int subt()
    {
        sub=c-d;
        cout<<"\nSubtraction="<<sub<<"\n";
    }
}; //---------------------------------------------------------------Multiple

class multiplication:public value_ab,public enter2
{
public:
    int multi()
    {
        cout<<"\nGive the value of e and h\n";
        cin>>e>>h;
        mul = e*h;
        cout<<"\nMultiplication= "<<mul<<"\n";
    }
}; //-------------------------------------------------------------------Hybrid

class division:public enter1
{
public:
    int div()
    {
        int divide;
        cout<<"\nGive the value of f and g\n";
        cin>>f>>g;
        divide= f/g;
        cout<<"\nDivides="<<divide;
    }
}; //--------------------------------------------------------------Heirarchical

/*Main Function Starts*/
int main()
{
    addition x;
    subtraction y;
    multiplication z;
    division w;
    x.val_ab();
    x.add();
    y.val_cd();
    y.subt();
    z.multi();
    w.div();
    return 0;
}

