#include<iostream.h>
#include<stdio.h>
using namespaces std;
class film {
private:
char nume[35];
char actp[35];
char acts[35];

public:
film()
{
cout<<"\n S-a apelat constructorul clasei film";
cout<<"\n Introduceti numele filmului: ";
gets(nume);
cout<<" Actorul principal: "; gets(actp);
cout<<" Actorul secundar: "; gets(acts);
}

~film()
{
cout<<"\n Se trece prin destructorul clasei
film";
}

void afisare_film()
{
cout<<"\n Nume film: "<<nume;
cout<<"\n Actor principal: "<<actp;
cout<<"\n Actor secundar: "<<acts<<endl;
}
};
