using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace exercise11
{
    class Program
    {
        static void DoTest(URLStorageInterface storageTypeToTest, URLList urlList)
        {
            foreach (string url in urlList.GetURLs())
            {
                storageTypeToTest.AddURL(url);
            }

            Process currentProcess = System.Diagnostics.Process.GetCurrentProcess();
            long totalBytesOfMemoryUsed = currentProcess.WorkingSet64;
            Console.WriteLine("Memory used: " + (totalBytesOfMemoryUsed / 1024 / 1024).ToString() + "MB");
        }

        static void Main(string[] args)
        {
            //Create list of URLs
            URLList urlList = new URLList();
            urlList.BuildURLList();

            /*Console.WriteLine("Testing Trie");
            URLStorageInterface urlStorage = new URLStorageTrie();
            Program.DoTest(urlStorage, urlList);

            Console.WriteLine("Testing DAWG");
            urlStorage = new URLStorageDAWG();
            Program.DoTest(urlStorage, urlList);*/

            Console.WriteLine("Testing BloomFilter");
            URLStorageInterface urlStorage = new URLStorageBloomFilter(urlList.GetURLs().Count);
            Program.DoTest(urlStorage, urlList);
        }
    }
}
