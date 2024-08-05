#include <iostream>
#include<fstream>
#include<iomanip>
using namespace std;

void addstudent()
{
    ofstream f("db.txt",ios::app);

    string rn,name,div,add;
    cout<<"Enter your Rollno:";
    cin>>rn;
    cout<<"Enter your Name:";
    cin>>name;
    cout<<"Enter your Division:";
    cin>>div;
    cout<<"Enter your Address:";
    cin>>add;
 f <<setw(20)<<rn<<setw(20)<<setw(20)<<name<<setw(20)<<div<<setw(20)<<add<<endl;
 f.close();
 cout<<"Student Added Successfully.";
}

void deletestudent()
{
     ifstream f("db.txt");
   string line;
   string rn;
   cout<<"Enter Student Roll no. To Delete:";
   cin>>rn;
   string fileData;

    while(getline(f,line)){
        if(line.find(rn) == string::npos){
           fileData += line;
           fileData += "\n";
        }
    }
    f.close();
    ofstream f1("db.txt",ios::out);
    f1 <<fileData;
    f1.close();
   
    
}
void searchstudent()
{
   ifstream f("db.txt");
   string line;
   string rn;
   cout<<"Enter Student Roll no. To search:";
   cin>>rn;
   bool found = false;
    while(getline(f,line)){
        if(line.find(rn) != string::npos){
            cout<<"Student Details: "<<endl;
            cout<<line<<endl;
            found = true;
            break;
        }
    }
    f.close();
    if(!found){
        cout<<"Student Doesn't Exist"<<endl;
    }
   
}

void printstudent()
{
    ifstream f("db.txt");
    string line;
    cout<<"Printing file data..."<< endl;
    while(getline(f,line))
    {
        cout<<line<<endl;
    }
    cout<<"Printing Complete.";
    f.close(); 
    
}

int main()
{
    ofstream f("db.txt",ios::out);
     f <<left<<setw(20)<<"Rollno"<<setw(20)<<setw(20)<<"Name"<<setw(20)<<"Division"<<setw(20)<<"Address"<<endl;
     f.close();
    int ip;
    while(ip !=-1)
    {
        cout<<"\nEnter your choice\n1. Add Student\n2. Delete Student\n3. Search Student\n4. Print Data\n.5 Exit\n---->";
        cin>>ip;
        switch(ip){
            case 1:
                addstudent();
                break;
            case 2:
                deletestudent();
                break;
            case 3:
                searchstudent();
                break;
            case 4:
                printstudent();  
                break;
            case 5:
            return 0;
                break;
            default:
                 cout<<"Please ReEnter your choice.";
                 break;

        }

    }
}