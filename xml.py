import xmltodict, json

def getdata(xml_file):
    try:
        with open('data/'+xml_file, 'r', encoding='utf8') as myfile:
            obj = xmltodict.parse(myfile.read(), strip_whitespace = False)
        
        return obj
    except BaseException:
        raise BaseException('Invalid data.')