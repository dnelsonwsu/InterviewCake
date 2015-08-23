using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace exercise11
{
   
    class URLStorageBloomFilter : URLStorageInterface
    {
        public URLStorageBloomFilter(int maxItems)
        {
            bloomFilter = new BloomFilter.Filter<string>(maxItems);
        }

        public void AddURL(string URL)
        {
            bloomFilter.Add(URL);
        }
        public bool IsURLInList(string url)
        {
            return bloomFilter.Contains(url);
        }

        private BloomFilter.Filter<string> bloomFilter;
    }
}
