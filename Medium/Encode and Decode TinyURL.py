import random


class Codec:
    def __init__(self):
        self.length = 6
        self.encode_list = [{}] * 6
        self.decode_list = [{}] * 6

    def gen_index(self, strlen, lastTwo):

        return (strlen + sum ([ord (x) for x in lastTwo])) % self.length

    def gen_value(self, index):

        s = []
        for i in range (self.length):
            if (random.randint (0, 1)):
                if (random.randint (0, 1)):
                    s.append (chr (random.randint (97, 123)))
                else:
                    s.append (chr (random.randint (65, 91)))
            else:
                s.append (str (random.randint (0, 9)))

        s.insert (3, str (index))
        return "".join (s)

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        index = self.gen_index (len (longUrl), longUrl[-2:])
        value = "http://tinyurl.com/" + self.gen_value (index)
        self.encode_list[index][longUrl] = value
        self.decode_list[index][value] = longUrl
        print ("value:{}".format (value))
        print ("ll:{}".format (longUrl))

        return value

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        print ("sl:{}".format (shortUrl))
        index = int (shortUrl[-4])
        if (shortUrl in self.decode_list[index]):
            return self.decode_list[index][shortUrl]
        else:
            return None


            # Your Codec object will be instantiated and called as such:
            # codec = Codec()
            # codec.decode(codec.encode(url))