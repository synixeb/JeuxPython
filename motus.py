import random

#liste de mots francais en 5 lettres
ListeMots = ["abats","abbes","abele","abime","abois","abuse","abute","acare","accru","acere","acheb","acide","acore","acres","acyle","adage","adent","adept","adire","admis","adore","adret","adule","affut","agace","agami","agile","agios","agite","agora","agres","agron","aguti","aider","aigre","aigri","aigue","ailes","aille","aimer","ainez","ainou","airai","airer","ajour","ajout","ajute","alain","alang","alcal","alcool","aldol","aleas","alems","alese","aleve","algue","alios","alite","allez","allia","allie","allou","aloes","alors","alose","alter","alune","aluns","alvin","amant","amene","amere","amers","amibe","amict","amide","amine","amont","amour","amphi","ample","amuse","anars","ancra","ancre","andin","anier","anima","anime","anion","anise","anode","anoli","anona","anone","anons","anote","ansee","anser","antre","anuit","aorte","aphte","apide","aplat","apres","aptes","arabe","aracs","araki","arase","arbre","arcus","ardue","ardus","arecs","arene","argan","argil","argol","argot","argue","argus","aride","arisa","arise","arome","arret","arsin","artel","arums","arval","arver","aryen","asale","asana","asile","asine","aspir","assai","assit","astre","atlas","atome","atone","atour","atout","atres","attif","attir","attis","attre"
             ,"aubes","aubin","aubre","aucun","audon","augee","auges","aunes","aunis","aupar","aures","auric","auris","auror","aussy","autan","autel","autre","auxin","avais","avait","avala","avale","avant","avare","avent","avenu","avere","avide","aviez","avili","avine","avion","avisa","avise","aviva","avive","avoir","avons","avort","avoua","avoue","avril","axais","axait","axant","axeas","axees","axels","axene","axent","axera","axial","axiez","axile","axils","axion","axite","axone","axons","ayant","ayons","azyme","babel","babes","babir","babol","babou","babys","bacas","bache","bacho","bachs","bacle","bacul","badas","bader","bades","badge","badin","baffe","baffy","bagad","bagel","bagne","bagou","bagua","bagui","bahut","baies","baign","baila","baile","bails","bains","baise","baisu","baiss","baits","bajou","baker","balai","balan","balay","balbu","balda","balde","balec","balee","baler","bales","baleu","baley","balis","baliv","balle","balne","balte","balus","bambu","banal","banat","banco","banda","bande","banjo","banne","banni","banon","banza","banze","baoul","bapta","bapti","barat","barbe","barbu","barde","barge","baril","barjo","baron","barot","barre","barye","baryt","basai","basal","basan","basas","basat","basco","basel","baser","bases","basez","basil","basin","basis","bassa","basse","basta","baste","batai","batar","batas","batat","batch","bates","batet","batie","batik","batir","batis","batit","baton","batto",
             "battu","bauds","baume","baura","bavai","bavas","bavat","bavee","baver","baves","bavez","bavon","bayer","bayes","bayez","bayle","bayou","bazan","bazou","beant","beate","beats","beaux","becot","becqu","bedon","beige","beija","beira","belai","belas","belat","belee","beler","beles","belez","belge","belin","belon","belou","bemba","bemol","benet","benin","benir","benis","benit","benny","benton","benzo","berce","beret","berge","berme","berne","beryl","besas","besat","beser","beses","beset","besse","bette","beure","beurs","bevue","bezef","bezes","bezil","bezit","biais","biait","biant","biaus","bibel","bible","biche","bichu","bidet","bidon","bidou","bidul","bienz","biffe","biffi","biffy","bifle","bigle","bigor","bigot","bigre","bijou","bikie","biles","billa","bille","billy","bimbo","bimup","binai","binas","binat","biner","bines","binez","bingo","binon","biome","biote","bipai","bipas","bipat","bippe","bipus","biqua","bique","birbe","birse","bises","bison","bisou","bisse","bites","bitos","bitte","bittu","bitue","bitus","bival","bivou","bizet","bizou","bizut","blabl","black","blaff","blanc","bland","blase","blaze","bleme","blene","blida","blime","blini","blitz","blocs","blond","blues","bluff","blush","board","bobos","bocle","bodes","bodhi","bogie","boira",
                "boire","boisa","boise","boita","boite","boive","bolos","bombe","bomby","bonde","bondi","bondu","bonhe","bonis","bonne","bonze","boome","boost","boots","borda","borde","bords","boree","bores","borne","boron","bosco","bosse","botas","botte","bouca","boucs","bouee","bouet","bouge","bouie","bouin","boula","boule","boume","boums","boune","bouon","bouqu","bours","bouse","bouts","bovid","bowal","bowie","boxai","boxas","boxat","boxee","boxer","boxes","boxez","boxon","boyau","boyaux","brace","brade","bragu","braie","brame","branc","brand","brans","brant","brasa","brase","brave","braya","braye","brede","brele","breme","brent","bresa","breve","briai","brias","briat","bride","briez","brige","brigu","brima","brime","brins","brion","brios","brique","brisa","brise","broda","brode","broie","brome","bronc","bronz","bross","broue","broum","brous","brout","bruay","bruit","brume","brune","bruni","bruns","bruta","brute","bruts","bubon","bucco","buche",
                "bucol","budd"]

def ChoisirMots():
    mot = ListeMots[random.randint(0, len(ListeMots) - 1)]
    return mot

def DemanderMots():
    mot = input("Entrez un mot : ")
    if len(mot) != 5:
        return DemanderMots()
    return mot

def DecompostionMot(mot):
    liste = []
    for lettre in mot:
        liste.append(lettre)
    return liste
        
def lettresbienplaces(mot1, mot2):
    bp = 0
    for i in range(0, len(mot1)):
        if mot1[i] == mot2[i]:
            bp += 1
    return bp

def lettresmalplaces(mot1, mot2):
    mp = 0
    for i in range(0, len(mot1)):
        if mot1[i] != mot2[i]:
            if mot2[i] in mot1:
                mp += 1
    return mp

def jeux():
    if input("Voulez vous jouer ? (o/n) : ") == "o":
        mot1 = ChoisirMots()
        print("le mot est ",mot1)
        mot1 = DecompostionMot(mot1)
        while True:
            mot2 = DecompostionMot(DemanderMots())
            if mot1 == mot2:
                print("Bravo tu as gagné")
                break
            else:
                mp = lettresmalplaces(mot1, mot2)
                bp = lettresbienplaces(mot1, mot2)
                #mp -= bp
                print("Lettres bien placées : ", bp)
                print("Lettres mal placées : ", mp)

