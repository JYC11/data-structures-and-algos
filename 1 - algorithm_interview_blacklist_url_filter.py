class UrlTrieNode:
    def __init__(self, element):
        self.element = element 
        self.children = {}
        self.end_of_url = False

class BlacklistUrlTrie(object):
    def __init__(self):
        self.root = UrlTrieNode("")
    
    def split_and_reverse_url(self,url):
        split_and_reversed_url = url.split(".")
        split_and_reversed_url.reverse()
        return split_and_reversed_url

    def insert_url(self,url):
        node = self.root
        split_and_reversed_url = self.split_and_reverse_url(url)

        for element in split_and_reversed_url:
            if element in node.children:
                node = node.children[element]
            else:
                new_node = UrlTrieNode(element)
                node.children[element] = new_node
                node = new_node
        
        node.end_of_url = True

    def is_blacklist_url(self,url,blacklist):
        split_and_reversed_url = self.split_and_reverse_url(url)

        node = self.root
        matches = []
        for element in split_and_reversed_url:
            if element in node.children:
                matches.append(element)
                if '.'.join(matches[::-1]) in blacklist:
                    return True
                node = node.children[element]
            else:
                continue
        return False

def contains_blacklist_url(blacklist, user_urls): #returns false if not okay(if containing blacklist)
    url_trie = BlacklistUrlTrie() #initialises a trie
    
    for url in blacklist: #populates trie with blacklist url
        url_trie.insert_url(url)
    
    for url in user_urls: #starts search each url in the trie
        result = url_trie.is_blacklist_url(url,blacklist)
        if result:
            return result
    return False

blacklist1 = ["google.com"]
user_urls1 = ["google.co.kr","google.co.jp"]

blacklist2 = ["images.google.com"]
user_urls2 = ["google.com"]

blacklist3 = ["google.com"]
user_urls3 = ["bing.com","askjeeves.com"]

blacklist4 = ["google.com"]
user_urls4 = ["images.google.com","askjeeves.com"]

print(contains_blacklist_url(blacklist1, user_urls1)) #false
print(contains_blacklist_url(blacklist2, user_urls2)) #false
print(contains_blacklist_url(blacklist3, user_urls3)) #false
print(contains_blacklist_url(blacklist4, user_urls4)) #true
