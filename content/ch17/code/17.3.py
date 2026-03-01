fread=open('weibocontent.txt')
fwrite=open('weibocontent2.txt', 'w')

try:
    for line in fread:
        text = line.strip()
        if("" == text):
            continue
        if( 5 >= len(text)): #一般来说都是四位数
            continue
        if(-1 != text.find("转发理由")):
            continue
        if(-1 != text.find("原图")):
            continue

        string_1 = 0
        if("发布了" in text or "转发了" in text):
            if(-1 != text.find("：")):
                string_1 = text.find("：") + 1
            elif(-1 != text.find(":")):
                string_1 = text.find(":") + 1
        string_2 = len(text)
        if(-1 != text.find("http")):
            string_2 = text.find("http")
        elif(-1 != text.find("全文")):
            string_2 = text.find("全文")
        elif (-1 != text.find("赞")):
            string_2 = text.find("赞")
        elif(-1 != text.find("[组图共")):
            string_2 = text.find("[组图共")

        content = text[string_1 : string_2]
        fwrite.write(content + '\r\n')
finally:
    fread.close()
    fwrite.close()