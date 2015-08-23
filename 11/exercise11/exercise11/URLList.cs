using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;



namespace exercise11
{
    class URLList
    {
        //max number of total "children" url's that can appear in a site
        const int maxTotalChildrenPerSite = 500;

        const int urlsToGenerate = 100000; 


        public URLList()
        { 
            //
        }

        private string GenerateRandomString(uint minLength, uint maxLength)
        {
            const string charsToUse = "abcdefghijklmnopqrstuvwxyz0123456789";
            int stringLength = rand.Next((int)minLength, (int)maxLength);
            char [] stringChars = new char[stringLength];

            for(int curCharIndex = 0; curCharIndex < stringLength; curCharIndex++)
            {
                stringChars[curCharIndex] = charsToUse[rand.Next(charsToUse.Length)];
            }
            return new string(stringChars);
        }


        private List<string> BuildChildURLs(string siteURL, ref int numURLsGeneratedForThisDomain)
        {
            const uint maxNumChildren = 7;
            const uint maxStringLen = 10;
            string randomString = this.GenerateRandomString(1, maxStringLen);
            string curURL = siteURL + '/' + randomString;

            List<string> urlsGenerated = new List<string>();
            urlsGenerated.Add(curURL);
            
            numURLsGeneratedForThisDomain++;
            totalURLsGenerated++;


            bool shouldGenerateChildren = this.rand.Next(0, 3) == 0;
            if (shouldGenerateChildren)
            {
                uint numChildrenToGenerate = (uint)rand.Next((int)maxNumChildren);

                for (int i = 0; i < numChildrenToGenerate; i++)
                {
                    List<string> childrenURLs = BuildChildURLs(curURL, ref numURLsGeneratedForThisDomain);
                    urlsGenerated.AddRange(childrenURLs);

                    if (numURLsGeneratedForThisDomain >= maxTotalChildrenPerSite || totalURLsGenerated >= urlsToGenerate)
                    {
                        return urlsGenerated;
                    }
                }
            }

            return urlsGenerated;
        }

        public void BuildURLList()
        {
            urlList = new List<string>();
            totalURLsGenerated = 0;

            while(totalURLsGenerated < urlsToGenerate)
            {
                string domainName = this.GenerateRandomString(1, 10);
                bool hasWWWInFront = rand.Next(0, 1) == 0;
                if (hasWWWInFront)
                {
                    domainName = "www." + domainName;
                }
                domainName += ".com";

                int urlsGeneratedForDomain = 0;
                List<string> domainURLs = BuildChildURLs(domainName, ref urlsGeneratedForDomain);
                urlList.AddRange(domainURLs);
            }
        }

        public List<string> GetURLs()
        {
            return urlList;
        }

        private Random rand = new Random();
        private List<string > urlList;
        private uint totalURLsGenerated = 0;
    }
}
