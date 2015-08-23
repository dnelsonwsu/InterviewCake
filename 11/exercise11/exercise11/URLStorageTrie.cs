using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace exercise11
{
    class TrieNode
    {
        public void AddString(string stringToAdd)
        {
            if (stringToAdd.Length == 0)
            {
                this.isTerminusNode = true;
                return;
            }

            char nextChar = stringToAdd[0];
            if (children.ContainsKey(nextChar))
            {
                children[nextChar].AddString(stringToAdd.Substring(1));
            }
            else
            {
                TrieNode newChildNode = new TrieNode();
                children.Add(nextChar, newChildNode);
                newChildNode.AddString(stringToAdd.Substring(1));
            }
        }

        public bool IsStringPresent(string stringToFind)
        {
            if (stringToFind.Length == 0            //If there are no more chacters left to find, and this i
                && isTerminusNode == true)    
            {
                return true;
            }

            char nextChar = stringToFind[0];
            if (children.ContainsKey(nextChar))
            {
                return children[nextChar].IsStringPresent(stringToFind.Substring(1));
            }
            else
            {
                return false;
            }
        }

        private bool isTerminusNode = false;
        private Dictionary<char, TrieNode> children = new Dictionary<char,TrieNode>();
    }

    class URLStorageTrie : URLStorageInterface
    {
        public void AddURL(string URL)
        {
            rootNode.AddString(URL);
        }
        public bool IsURLInList(string url)
        {
            return rootNode.IsStringPresent(url);
        }

       private TrieNode rootNode = new TrieNode ();
    }
}
