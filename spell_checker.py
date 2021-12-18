from spellchecker import SpellChecker 
import re 

spell = SpellChecker(language='pt') 
sentences = [" As feramentas tradicionais de negócios não são capases de processar uma enorme quantdade de dados não estruturados. Dessa forma, a ciência de dados oferece soluções mais avançadas para analisar grandes volumes de informações provenientes de diferentes tipos de fontes, como registros financeiros, arquivos multimídia, formulários de marketing, sensores, instrumentos e arquivos de texto.",
            'Este e umm tsto qe demonstra cmo o algoritimo funciona', 
            'O Pojeto Acadêmico da UFABC pocura levar em conta as mudancas no canpo da ciênsia, propondo uma matris interdicipinar']
for sentence in sentences:
    print(f"SENTENCE: {sentence}")
    print(f'CORRECT SENTENCE:', end=' ')
    sentence = re.findall("[-'A-Za-zÀ-ÿ]+", sentence) 
    misspelled = spell.unknown(sentence) 
    for word in sentence: 
        if(word in spell.unknown(sentence)):
            print(spell.correction(word), end=" ")
            # print(spell.candidates(word),end="\n\n")
        else:
            print(word, end=" ")
    print("\n")
