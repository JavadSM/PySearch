#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
using namespace std;

int main( int argc, char** argv )
  {
  if (argc != 3)
    {
    cout << "usage:\n  " << argv[ 0 ] << " TEXT FILE\n\n" << "Search for TEXT in FILE.\n" << "Reports the line number of each occurrence.\n\n";
    return 1;
    }

  const char* text = argv[ 1 ];
  const char* filename   = argv[ 2 ];
  ifstream f( filename );
  if (!f)
    {
    cerr << "Could not open file " << filename << endl;
    return 1;
    }
  // Read the entire file into memory
  string s;
  string t;
  while (getline( f, t ))
    s += t + '\n';
  f.close();
  // For each match, print line number
  for (string::size_type index = s.find( text, 0 );
       index != string::npos;
       index = s.find( text, index + 1 ))
    {
    string::size_type line   = count( s.begin(), s.begin() + index, '\n' ) + 1;
    /*If you want to find the Precise location of the word*/

    //string::size_type column = index - s.rfind( '\n', index );
    cout << line << "\n";
    }
  return 0;
  }