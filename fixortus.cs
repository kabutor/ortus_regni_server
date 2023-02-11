// C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /t:exe /out:fixortus.exe fixortus.cs

using System;
using System.Text;
using Microsoft.Win32;
using System.IO;
using System.Collections.Generic;


public class Program
{
    public static void Main(string[] args)
    {
        string filename = @"C:\\Users\\Administrador\\Documents\\Assembly-CSharp.dll";

        using (FileStream stream = File.Open(filename, FileMode.Open))
        {
            stream.Position = 3;
            stream.WriteByte(0x50);
        }


    }
    
}

