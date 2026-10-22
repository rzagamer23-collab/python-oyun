

print("kimlik doğrulama")

while True:
    cavab1 = input("sən həqiqətən Asimansan? hə yoxsa yox? ")
    if cavab1 == "hə":
        print("kimlik doğrulandı. xoş gəldin ASİMAN bəy")
        break
    else:
        print("kimlik doğrulanmadı. sən asik deyilsən")
        

while True:
    print("sən amerikanın prüzidenti seçildin")
    cavab2 = input("Rusiyaya bomba göndərək yoxsa koreyaya? Cavabı belə yaz: rusiya və ya koreya: ")
    if cavab2 == "rusiya":
        print("Rusiya partladı. Artıq RUSİYA SƏNİNDİR")
        break
    elif cavab2 == "koreya":
        print("KOREYA SƏNİNDİR. Amma Rusiya daha güclü olduğu üçün sənin ölkəni partlatdı. Birinci RUSİYANI partlatmalıydın!")

print("KOREYA QALDI")

while True:
    cavab3 = input("Koreyanı partladırsan yoxsa onu bağışlayıb əvəzində 1 MANAT pul alırsan? Cavabı belə yaz: partladıram və ya partlatmıram: ")
    if cavab3 == "partladıram":
    	print("sən partlatdığın üçün koreyadan 1 manat ala bilmədin")
    	break
    elif cavab3 == "partlatmıram":
    	print("sən koreyadan 1 manat aldın.sonra getdin semiçka aldın.semiçkanın içindən 100000 manat kuponu çıxdı")
    	break