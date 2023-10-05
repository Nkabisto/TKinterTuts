#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;

void didFileOpen(const ifstream&);
void didFileOpen(const ofstream&);
void printError(const string);

int main()
{
    const string INFILE = "Time and attendance.txt";
    const string OUTFILE = "Time and attendance.csv";

    const string C = ",";

    ifstream inFile;
    ofstream outFile;

    string _userID, _date, _time, _staff, _io; // variables to store input data from file.

    inFile.open(INFILE, ios::in);
    didFileOpen(inFile);
    outFile.open(OUTFILE, ios::out);
    didFileOpen(outFile);

    inFile>>_date>>_time>>_staff; // First read reads headers which should be discarded,

    while(inFile>>_userID>>_date>>_time>>_staff>>_io)
    {
        _userID.append(C);
        _date.append(C);
        _time.append(C);
        _staff.append(C);

        outFile<<_userID<<_date<<_time<<_staff<<_io<<endl;
    }

    inFile.close();
    outFile.close();

    return 0;
}

void didFileOpen(const ifstream& fileStream)
{
    if(fileStream.fail())
    {
        printError("Input");
    }
}

void didFileOpen(const ofstream& fileStream)
{
    if(fileStream.fail())
    {
        printError("Output");
    }
}

void printError(const string fileType)
{
    cerr<<fileType +  " file opening failed! Program shutting down... \n";
    exit(EXIT_FAILURE);
}
