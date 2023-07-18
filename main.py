import gzip
import zlib

if __name__ == '__main__':
    # filename = "rough-work/sample.txt.gz"
    filename = "01302019.NASDAQ_ITCH50.gz"
    dataObj = zlib.decompressobj()

    with gzip.open(filename, 'rb') as datafile:
        for i in range(1980):
            try:
                datafile.readline()
            except Exception as e:
                print("Cannot understand line:", i+1, " Error : ", e.__class__)
                print(e)
        for i in range(20):
            try:
                temp = datafile.readline()
                print("Raw content: ", temp)
                decodedString = temp.decode("unicode_escape")
                print("Size:        ", temp.__sizeof__(), len(decodedString))
                print("Decoded cont:", decodedString, end='')
                # print(temp.decode('utf-16'))
                # print(temp.decode('utf-8'))
                # print(temp.decode('ascii'))

            except Exception as e:
                print("Cannot understand line:", i+1, " Error : ", e.__class__)
                print(e)
        # CHUNKSIZE = 1024
        # buffer_value = datafile.read(CHUNKSIZE)
        # # while buffer_value and i < 100:
        # try:
        #     print("Compressed:", buffer_value)
        #     decompressed_data = dataObj.decompress(buffer_value)
        #     print("Decompressed:", decompressed_data)
        #     # if(CHUNKSIZE > 30):
        #     #     break;
        # except:
        #     print("Cannot : ", CHUNKSIZE)
        #     pass
            
    datafile.close()


"""
apple@Apples-MacBook-Air trexquant % python3 main.py
b'\x00\x0cS\x00\x00\x00\x00\n'
b'\n'
b"`\xaa\xdb\x93O\x00'R\x00\x01\x00\x00\n"
b"JL\xeeU\x99A       N \x00\x00\x00dNCZ PN 1N\x00\x00\x00\x00N\x00'R\x00\x02\x00\x00\n"
b"JM\x06--AA      N \x00\x00\x00dNCZ PN 1N\x00\x00\x00\x01N\x00'R\x00\x03\x00\x00\n"
b"JM\x07\x01oAAAU    P \x00\x00\x00dNQI PN 2Y\x00\x00\x00\x01N\x00'R\x00\x04\x00\x00\n"
b"JM\x07\xb0\x96AABA    QN\x00\x00\x00dNCQ PNN2N\x00\x00\x00\x01N\x00'R\x00\x05\x00\x00\n"
b"JM\x08\x85lAAC     N \x00\x00\x00dNCZ PN 2N\x00\x00\x00\x00N\x00'R\x00\x06\x00\x00\n"
b"JM\ta\x10AADR    P \x00\x00\x00dNQI PN 2Y\x00\x00\x00\x00N\x00'R\x00\x07\x00\x00\n"
b'JM\n'
"""
"""
# With utf-8
apple@Apples-MacBook-Air trexquant % python3 main.py 

S



Cannot understand line: 3
Cannot understand line: 4
JM--AA      N dNCZ PN 1NN'R

JMoAAAU    P dNQI PN 2YN'R

Cannot understand line: 7
Cannot understand line: 8
JM      aAADR    P dNQI PN 2YN'R

JM

apple@Apples-MacBook-Air trexquant % 
"""
"""
# With unicode_escape
apple@Apples-MacBook-Air trexquant % python3 main.py

S



`ªÛO'R

JLîUA       N dNCZ PN 1NN'R

JM--AA      N dNCZ PN 1NN'R

JMoAAAU    P dNQI PN 2YN'R

JM°AABA    QNdNCQ PNN2NN'R

JM
lAAC     N dNCZ PN 2NN'R

JM      aAADR    P dNQI PN 2YN'R

JM

apple@Apples-MacBook-Air trexquant % 

apple@Apples-MacBook-Air trexquant % python3 main.py
74 41
JNä$¸BNFT    GNdNCZ PNN2NN'R¶
74 41
JNä
   BNGO    SNdNCZ PNN2NN'R·
74 41
JNäóýBNGOW   SNdNWZ PNN NN'R¸
74 41
JNåYBNO     P dNQI PN 1YN'R¹
74 41
JNåÄÙBNS     N dNCZ PN 2NN'Rº
74 41
JNæ*´BNSO    SNdNCZ PNN2NN'R»
74 41
JNæhBNTC    SNdNAZ PNN2NN'R¼
74 41
JNæÿ BNTCW   SNdNWZ PNN NN'R½
74 41
JNçiòBNY     N dNCQ PN 2NN'R¾
74 41
JNçÐàBOCH    GNdNCZ PNN2NN'R¿
74 41
JNè4^BOCT    Z dNQI PN 2YN'RÀ
74 41
JNèBOE     N dNSQ PN 2NN'RÁ
74 41
JNèþwBOH     N dNCZ PN 1NN'RÂ
74 41
JNé`UBOIL    P dNQI PN 2YN'RÃ
74 41
JNéÉ_BOKF    QNdNCZ PNN1NN'RÄ
74 41
JNê0BOKFL   QNdNQG PNN2NN'RÅ
74 41
JNêmBOLD    GNdNCZ PNN2NN'RÆ
74 41
JNêþÈBOM     P dNQB PN 2NN'RÇ
74 41
JNëdôBOMN    SNdNCZ PNN2NN'RÈ
74 41
JNëÎBOND    P dNQI PN 1YN'RÉ
apple@Apples-MacBook-Air trexquant % 

Raw content:  b"JN\xe7i\xf2BNY     N \x00\x00\x00dNCQ PN 2N\x00\x00\x00\x00N\x00'R\x03\xbe\x00\x00\n"
Size:         74 41
Decoded cont: JNçiòBNY     N dNCQ PN 2NN'R¾
Raw content:  b"JN\xe7\xd0\xe0BOCH    GN\x00\x00\x00dNCZ PNN2N\x00\x00\x00\x00N\x00'R\x03\xbf\x00\x00\n"
Size:         74 41
Decoded cont: JNçÐàBOCH    GNdNCZ PNN2NN'R¿
Raw content:  b"JN\xe84^BOCT    Z \x00\x00\x00dNQI PN 2Y\x00\x00\x00\x01N\x00'R\x03\xc0\x00\x00\n"
Size:         74 41
"""
"""
References:
1. https://docs.python.org/3/library/gzip.html
2. https://stackoverflow.com/questions/22216076/unicodedecodeerror-utf8-codec-cant-decode-byte-0xa5-in-position-0-invalid-s
3. https://stackoverflow.com/questions/444591/how-to-convert-a-string-of-bytes-into-an-int

"""