import gzip
import time

if __name__ == '__main__':
    start = time.time()
    filename = "data/01302019.NASDAQ_ITCH50.gz"
    headers = set()

    with gzip.open(filename, 'rb') as datafile:
        temp = datafile.readline()
        while temp:
            try:
                # print(temp[0])
                headers.add(chr(temp[0]))
                temp = datafile.readline()
            except Exception as e:
                print("Cannot understand line:", i+1, " Error : ", e.__class__)
                print(e)
            
    datafile.close()
    end = time.time()
    print(headers)
    print("Time taken : ", (end - start)*(10**3), "ms")


"""
apple@Apples-MacBook-Air trexquant % python3 rough-work/read-and-decode/extract-header.py
{'¨', 'Õ', 'à', 'ã', '\x86', 'ÿ', ']', '\x99', 'a', '\x10', '\x08', 'Á', 'N', 'ì', 'Î', 'ù', '.', 
'\x0c', '\x14', '~', 'Ñ', '\x0e', '4', 'Ö', '\x81', 'æ', 'È', 'M', 'P', '\x83', '\x88', 'Ü', '7', 
'ª', 'º', '\t', '*', 'Ä', '\x0f', 'Ô', 'R', 'ï', 'ü', '½', '\x1c', 'Ù', 'D', 'G', '\x1a', 'ç', '{', 
'é', '3', '÷', '\r', '\x00', '"', 'Ý', '\x7f', 'ø', '+', '\x82', 'ä', 'ý', 'r', '©', 'Ç', 'X', 'ô', 
'm', '\x1d', 'u', '¶', 'ß', 'E', '[', '´', '\x92', '\x96', 'µ', '\x05', 'ñ', '®', 'Â', '¡', '6', 'V', 
'\x8a', 'v', '#', '¸', 'I', 'l', '¬', 'J', 'Ê', ' ', '\x8c', '\x02', '\x80', '¼', 'L', '(', 'Q', 'c', 
'U', '<', '\x87', '\x9d', '\x85', 'Ú', 'O', 'n', '¥', '\x9f', 'q', '¤', '>', '|', '?', ',', 'Ã', '²', 
'8', '¢', 'b', 'è', 'ë', 'i', 'þ', 'ú', '\x90', '9', 'T', 'o', 'û', 's', '\x1f', 'Ì', '^', 'K', '_', 
'\x93', '»', 'ò', '`', '×', '5', '\x07', 'â', '\x98', '\x8e', '±', '\x15', '\x9b', 'Ë', 'Z', 'Í', 
'\x9a', '\xa0', 'd', 'f', '\x12', 'y', '\x97', '\x84', '\x06', '\\', 'Ó', '\x13', '%', '\x18', "'", 
'\xad', 't', 'w', 'A', '$', '\x89', 'Ò', '\x8d', '\x8b', '1', '³', 'k', ')', 'õ', '\x8f', 'Ð', '\x16', 
'&', '\x94', '\x01', '\x95', '\x9c', '°', 'g', '¦', '\n', '§', 'ó', 'ö', '2', 'Þ', 'h', '\x9e', 'Ø', 
'\x04', '£', '/', '\x0b', 'z', 'ê', ';', '¹', 'H', 'e', 'S', '¿', 'å', '\x11', ':', 'x', 'W', 'Y', 
'\x19', '@', '¾', 'á', '\x1b', '«', '\x03', 'Æ', 'j', 'í', '=', '\x91', 'ð', '!', 'î', '¯', '·', 'Ï', 
'0', 'Û', 'À', 'C', '\x1e', '\x17', '}', 'É', 'B', '-', 'Å', 'p', 'F'}
Time taken :  83156.93306922913 ms
apple@Apples-MacBook-Air trexquant % 
"""