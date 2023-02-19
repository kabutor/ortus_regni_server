// C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /t:exe /out:fixortus.exe fixortus.cs
// This will fix the Assembly-Csharp.dll on the "Ortus Regni\OrtusRegni_Data\Managed" directory
// the url is on UTF16LE format it will remove S of the secure url. From https://prod.ortusregnicloud.com/api to http://prod.etc... 
// you can use another url , just create it below as the decimal values in utf16le format (a 0 byte between each normal byte)
using System;
using System.Text;
using Microsoft.Win32;
using System.IO;
using System.Collections.Generic;


public class Program
{
    public static void Main(string[] args)
    {
        string filename = @"Assembly-CSharp.dll";

	byte[] newurl={104,0,116,0,116,0,112,0,0,58,0,47,0,47,0,112,0,114,0,111,0,100,0,46,0,111,0,114,0,116,0,117,0,115,0,114,0,101,0,103,0,110,0,105,0,99,0,108,0,111,0,117,0,100,0,46,0,99,0,111,0,109,0,47,0,97,0,112,0,105,0,47,0,0};
        using (FileStream stream = File.Open(filename, FileMode.Open))
        {
	        stream.Position = 2426953;

		stream.Write(newurl,0,73);
		//Console.WriteLine(string.Join(",", newurl));
		
        }
    }  
}

