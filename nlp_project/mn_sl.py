import re


def sem_analyze(text_in):
    text = text_in.lower()
    text = re.sub('[0-9!.,?;:\-()\']+', ' ', text)
    text = re.sub('\s+', ' ', text)
    word_list = text.split(' ')
    result = []
    argumentation = []
    for word in word_list:
        match_1 = re.fullmatch('(машин|тян|подня|комет|поезд|дым|состав|пыл).*', word)
        match_2 = re.fullmatch('(заня|вста|пристрои|оказа|вырос|очеред|отряд|станови).*', word)
        match_3 = re.fullmatch('(волос|собра|завя|запле|потян|голов|высок|небрежн|резин|бант|дерн).*', word)
        match_4 = re.fullmatch('(нос|огненн|самолет|ракет).*', word)
        match_5 = re.fullmatch(
            '(ухват|удач|пистолет|собак|виля|кончик|пушист|задр|махну|собач|распуст|облезл|схват|спойм|слов|лов|рыб|наступ).*',
            word)
        if match_1:
            argumentation.append(' обнаружено слово "' + word+'"')
            result.append(' часть движущегося объекта')
        elif match_2:
            argumentation.append(' обнаружено слово "' + word+'"')
            result.append(' очередь людей')
        elif match_3:
            argumentation.append(' обнаружено слово "' + word+'"')
            result.append(' причёска')
        elif match_4:
            argumentation.append(' обнаружено слово "' + word+'"')
            result.append(' часть летательного объекта')
        elif match_5:
            argumentation.append(' обнаружено слово "' + word+'"')
            result.append(' часть тела животного')
    if len(result) < 1:
        argumentation.append('отсутствуют показатели для определения значения')
        result.append(' не определено')
        return argumentation, result[0]
    elif len(result) == 1:
        return argumentation, result[0]
    elif len(result) == 2:
        if result[0] == result[1]:
            return argumentation, result[0]
        else:
            result_two_values = str(result[0])+' или '+str(result[1])
            return argumentation, result_two_values
    else:
        return argumentation, max(result)

