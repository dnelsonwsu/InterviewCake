using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace exercise11
{
    interface URLStorageInterface
    {
        void AddURL(string url);
        bool IsURLInList(string url);
    }
}
