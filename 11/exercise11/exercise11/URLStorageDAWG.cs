using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using DawgSharp;

namespace exercise11
{
    class URLStorageDAWG : URLStorageInterface
    {
        public void AddURL(string URL)
        {
            dawgBuilder.Insert(URL, true);
        }

        public bool IsURLInList(string url)
        {
            if (dawg == null)
            {
                dawg = dawgBuilder.BuildDawg();
                dawgBuilder = null;
            }
            return dawg["url"];
        }

        private DawgBuilder<bool> dawgBuilder = new DawgBuilder<bool>();
        private Dawg<bool> dawg = null;
    }
}
