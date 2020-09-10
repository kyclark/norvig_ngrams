from ngrams import segment, Pw, shift, shift2, decode_shift2, \
    decode_subst, edits, cPw, segment2, correct


def test_segment():
    assert segment('choosespain') == ['choose', 'spain']
    assert segment('thisisatest') == ['this', 'is', 'a', 'test']
    assert segment('wheninthecourseofhumaneventsitbecomesnecessary') == [
        'when', 'in', 'the', 'course', 'of', 'human', 'events', 'it',
        'becomes', 'necessary'
    ]
    assert segment('whorepresents') == ['who', 'represents']
    assert segment('expertsexchange') == ['experts', 'exchange']
    assert segment('speedofart') == ['speed', 'of', 'art']
    assert segment('nowisthetimeforallgood') == [
        'now', 'is', 'the', 'time', 'for', 'all', 'good'
    ]
    assert segment('itisatruthuniversallyacknowledged') == [
        'it', 'is', 'a', 'truth', 'universally', 'acknowledged'
    ]
    assert segment(
        'itwasabrightcolddayinaprilandtheclockswerestrikingthirteen') == [
            'it', 'was', 'a', 'bright', 'cold', 'day', 'in', 'april', 'and',
            'the', 'clocks', 'were', 'striking', 'thirteen'
        ]
    assert segment('itwasthebestoftimesitwastheworstoftimes'
                   'itwastheageofwisdomitwastheageoffoolishness') == [
                       'it', 'was', 'the', 'best', 'of', 'times', 'it', 'was',
                       'the', 'worst', 'of', 'times', 'it', 'was', 'the',
                       'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of',
                       'foolishness'
                   ]
    assert segment('asgregorsamsaawokeonemorningfromuneasydreamshefound'
                   'himselftransformedinhisbedintoagiganticinsect') == [
                       'as', 'gregor', 'samsa', 'awoke', 'one', 'morning',
                       'from', 'uneasy', 'dreams', 'he', 'found', 'himself',
                       'transformed', 'in', 'his', 'bed', 'into', 'a',
                       'gigantic', 'insect'
                   ]
    assert segment('inaholeinthegroundtherelivedahobbitnotanastydirtywet'
                   'holefilledwiththeendsofwormsandanoozysmellnoryetadry'
                   'baresandyholewithnothinginittositdownonortoeatitwasa'
                   'hobbitholeandthatmeanscomfort') == [
                       'in', 'a', 'hole', 'in', 'the', 'ground', 'there',
                       'lived', 'a', 'hobbit', 'not', 'a', 'nasty', 'dirty',
                       'wet', 'hole', 'filled', 'with', 'the', 'ends', 'of',
                       'worms', 'and', 'an', 'oozy', 'smell', 'nor', 'yet',
                       'a', 'dry', 'bare', 'sandy', 'hole', 'with', 'nothing',
                       'in', 'it', 'to', 'sitdown', 'on', 'or', 'to', 'eat',
                       'it', 'was', 'a', 'hobbit', 'hole', 'and', 'that',
                       'means', 'comfort'
                   ]
    assert segment('faroutintheunchartedbackwatersoftheunfashionablee'
                   'ndofthewesternspiralarmofthegalaxyliesasmallunreg'
                   'ardedyellowsun') == [
                       'far', 'out', 'in', 'the', 'uncharted', 'backwaters',
                       'of', 'the', 'unfashionable', 'end', 'of', 'the',
                       'western', 'spiral', 'arm', 'of', 'the', 'galaxy',
                       'lies', 'a', 'small', 'un', 'regarded', 'yellow', 'sun'
                   ]


def test_Pw():
    # Pw['unregarded'] == 7557
    # assert segment('faroutintheunchartedbackwatersoftheunfashionableendofthewesternspiralarmofthegalaxyliesasmallunregardedyellowsun') == ['far', 'out', 'in', 'the', 'uncharted', 'backwaters', 'of', 'the', 'unfashionable', 'end', 'of', 'the', 'western', 'spiral', 'arm', 'of', 'the', 'galaxy', 'lies', 'a', 'small', 'unregarded', 'yellow', 'sun']
    pass


def test_cPw():
    assert cPw('sit', 'to') * cPw('down', 'sit') / cPw(
        'sitdown', 'to') == 1698.0002330199263


## Now let's try segment2


def test_seg2():
    def seg2(s):
        return segment2(s)[1]

    assert seg2('choosespain') == ['choose', 'spain']
    assert seg2('thisisatest') == ['this', 'is', 'a', 'test']
    # assert seg2('wheninthecourseofhumaneventsitbecomesnecessary') == [
    #     'when', 'in', 'the', 'course', 'of', 'human', 'events', 'it',
    #     'becomes', 'necessary'
    # ]
    # assert seg2('whorepresents') == ['who', 'represents']
    # assert seg2('expertsexchange') == ['experts', 'exchange']
    # assert seg2('speedofart') == ['speed', 'of', 'art']
    # assert seg2('nowisthetimeforallgood') == [
    #     'now', 'is', 'the', 'time', 'for', 'all', 'good'
    # ]
    # assert seg2('itisatruthuniversallyacknowledged') == [
    #     'it', 'is', 'a', 'truth', 'universally', 'acknowledged'
    # ]
    # assert seg2(
    #     'itwasabrightcolddayinaprilandtheclockswerestrikingthirteen') == [
    #         'it', 'was', 'a', 'bright', 'cold', 'day', 'in', 'april', 'and',
    #         'the', 'clocks', 'were', 'striking', 'thirteen'
    #     ]
    # assert seg2('itwasthebestoftimesitwastheworstoftimesitwastheageof'
    #             'wisdomitwastheageoffoolishness') == [
    #                 'it', 'was', 'the', 'best', 'of', 'times', 'it', 'was',
    #                 'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age',
    #                 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of',
    #                 'foolishness'
    #             ]
    # assert seg2('asgregorsamsaawokeonemorningfromuneasydreamshefoundh'
    #             'imselftransformedinhisbedintoagiganticinsect') == [
    #                 'as', 'gregor', 'samsa', 'awoke', 'one', 'morning', 'from',
    #                 'uneasy', 'dreams', 'he', 'found', 'himself',
    #                 'transformed', 'in', 'his', 'bed', 'into', 'a', 'gigantic',
    #                 'insect'
    #             ]
    # assert seg2('inaholeinthegroundtherelivedahobbitnotanastydirtywet'
    #             'holefilledwiththeendsofwormsandanoozysmellnoryetadry'
    #             'baresandyholewithnothinginittositdownonortoeatitwasa'
    #             'hobbitholeandthatmeanscomfort') == [
    #                 'in', 'a', 'hole', 'in', 'the', 'ground', 'there', 'lived',
    #                 'a', 'hobbit', 'not', 'a', 'nasty', 'dirty', 'wet', 'hole',
    #                 'filled', 'with', 'the', 'ends', 'of', 'worms', 'and',
    #                 'an', 'oozy', 'smell', 'nor', 'yet', 'a', 'dry', 'bare',
    #                 'sandy', 'hole', 'with', 'nothing', 'in', 'it', 'to',
    #                 'sit', 'down', 'on', 'or', 'to', 'eat', 'it', 'was', 'a',
    #                 'hobbit', 'hole', 'and', 'that', 'means', 'comfort'
    #             ]

    # ### Notice that segment2 got "sit down" right, where segment did not.
    # ### It gets "unregarded" right only when Pw['unregarded'] is given a value.
    # assert seg2(
    #     'faroutintheunchartedbackwatersoftheunfashionableendo'
    #     'fthewesternspiralarmofthegalaxyliesasmallunregardedyellowsun') == [
    #         'far', 'out', 'in', 'the', 'uncharted', 'backwaters', 'of', 'the',
    #         'unfashionable', 'end', 'of', 'the', 'western', 'spiral', 'arm',
    #         'of', 'the', 'galaxy', 'lies', 'a', 'small', 'unregarded',
    #         'yellow', 'sun'
    #     ]


################ Secret Codes (p. 228-229)


def test_shift():
    assert shift('Listen, do you want to know a secret?'
                 ) == 'Yvfgra, qb lbh jnag gb xabj n frperg?'

    assert shift('HAL 9000 xyz', 1) == 'IBM 9000 yza'

    # for i in range(26):
    #     msg = shift('Yvfgra, qb lbh jnag gb xabj n frperg?', i)
    #     print(msg, int(logPwords(msg)))
    #     Yvfgra, qb lbh jnag gb xabj n frperg? -84
    #     Zwghsb, rc mci kobh hc ybck o gsqfsh? -83
    #     Axhitc, sd ndj lpci id zcdl p htrgti? -83
    #     Byijud, te oek mqdj je adem q iushuj? -77
    #     Czjkve, uf pfl nrek kf befn r jvtivk? -85
    #     Daklwf, vg qgm osfl lg cfgo s kwujwl? -91
    #     Eblmxg, wh rhn ptgm mh dghp t lxvkxm? -84
    #     Fcmnyh, xi sio quhn ni ehiq u mywlyn? -84
    #     Gdnozi, yj tjp rvio oj fijr v nzxmzo? -86
    #     Heopaj, zk ukq swjp pk gjks w oaynap? -93
    #     Ifpqbk, al vlr txkq ql hklt x pbzobq? -84
    #     Jgqrcl, bm wms uylr rm ilmu y qcapcr? -76
    #     Khrsdm, cn xnt vzms sn jmnv z rdbqds? -92
    #     Listen, do you want to know a secret? -25
    #     Mjtufo, ep zpv xbou up lopx b tfdsfu? -89
    #     Nkuvgp, fq aqw ycpv vq mpqy c ugetgv? -87
    #     Olvwhq, gr brx zdqw wr nqrz d vhfuhw? -85
    #     Pmwxir, hs csy aerx xs orsa e wigvix? -77
    #     Qnxyjs, it dtz bfsy yt pstb f xjhwjy? -83
    #     Royzkt, ju eua cgtz zu qtuc g ykixkz? -85
    #     Spzalu, kv fvb dhua av ruvd h zljyla? -85
    #     Tqabmv, lw gwc eivb bw svwe i amkzmb? -84
    #     Urbcnw, mx hxd fjwc cx twxf j bnlanc? -92
    #     Vscdox, ny iye gkxd dy uxyg k combod? -84
    #     Wtdepy, oz jzf hlye ez vyzh l dpncpe? -91
    #     Xuefqz, pa kag imzf fa wzai m eqodqf? -83


def test_shift2():
    assert shift2('Listen, do you want to know a secret?'
                  ) == 'yvfgraqblbhjnaggbxabjnfrperg'


def test_decode_shift2():
    pass
    # assert decode_shift2('yvfgraqblbhjnaggbxabjnfrperg'
    #                      ) == 'listen do you want to know a secret'

    # assert decode_shift2(shift2('Rosebud')) == 'rosebud'

    # assert decode_shift2(shift2("Is it safe?")) == 'is it safe'

    # assert decode_shift2(shift2(
    #     "What's the frequency, Kenneth?")) == 'whats the frequency kenneth'

    # msg = 'General Kenobi: Years ago, you served my father in the Clone Wars; now he begs you to help him in his struggle against the Empire.'
    # assert decode_shift2(
    #     shift2(msg)
    # ) == 'general kenobi years ago you served my father in the clone wars now he begs you to help him in his struggle against the empire'

    # L = list(sorted(P3l, key=P3l, reverse=True))
    # assert L[:10] == [
    #     'the', 'ing', 'and', 'ion', 'tio', 'ent', 'for', 'ati', 'ter', 'ate'
    # ]
    # assert L[-10:] == [
    #     'fzq', 'jvq', 'jnq', 'zqh', 'jqx', 'jwq', 'jqy', 'zqy', 'jzq', 'zgq'
    # ]


def test_decode_subst():
    pass
    # msg = ('DSDRO XFIJV DIYSB ANQAL TAIMX VBDMB GASSA QRTRT CGGXJ MMTQC '
    #        'IPJSB AQPDR SDIMS DUAMB CQCMS AQDRS DMRJN SBAGC IYTCY ASBCS '
    #        'MQXKS CICGX RSRCQ ACOGA SJPAS AQHDI ASBAK GCDIS AWSJN CMDKB '
    #        'AQHAR RCYAE')

    # assert decode_subst(msg) == (
    #     'it is by knowing the frequency which letters usually '
    #     'occur and other distinctive characteristics of the language '
    #     'that crypt analysts are able to determine the plain text of '
    #     'a cipher message j')

    # msg = ('NKDIF SERLJ MIBFK FKDLV NQIBR HLCJU KFTFL KSTEN YQNDQ NTTEB '
    #        'TTENM QLJFS NOSUM MLQTL CTENC QNKRE BTTBR HKLQT ELCBQ QBSFS '
    #        'KLTML SSFAI NLKBR RLUKT LCJUK FTFLK FKSUC CFRFN KRYXB')

    # assert decode_subst(msg) == (
    #     'english complaining over lack of munitions they regret '
    #     'that the promised support of the french attack north of '
    #     'arras is not possible on account of munition insufficiency wa')

    # msg = ('CNLGV QVELH WTTAI LEHOT WEQVP CEBTQ FJNPP EDMFM LFCYF SQFSP '
    #        'NDHQF OEUTN PPTPP CTDQN IFSQD TWHTN HHLFJ OLFSD HQFED HEGNQ '
    #        'TWVNQ HTNHH LFJWE BBITS PTHDT XQQFO EUTYF SLFJE DEFDN IFSQG '
    #        'NLNGN PCTTQ EDOED FGQFI TLXNI')

    # assert decode_subst(msg) == (
    #     'march third week bridge with smile to pass info from you '
    #     'to us and to give assessment about new dead drop ground '
    #     'to indicate what dead drop will be used next to give your '
    #     'opinion about caracas meeting in october xab')

    # msg = ('WLJIU JYBRK PWFPF IJQSK PWRSS WEPTM MJRBS BJIRA BASPP '
    #        'IHBGP RWMWQ SOPSV PPIMJ BISUF WIFOT HWBIS WBIQW FBJRB '
    #        'GPILP PXLPM SAJQQ PMJQS RJASW LSBLW GBHMJ QSWIL PXWOL')

    # assert decode_subst(msg) == (
    #     'a cony ov is headed northeast take up positions fifteen '
    #     'miles apart between point yd and bu maintain radio silence '
    #     'except for reports of tactical importance x abc')


################ Spelling Correction (p. 237)


def test_edits():
    assert edits('adiabatic', 2) == {
        'adiabatic': '',
        'diabetic': '<a|<+a|e',
        'diabatic': '<a|<'
    }

    assert correct('vokabulary') == 'vocabulary'

    assert correct('embracable') == 'embraceable'

    assert corrections(
        'thiss is a teyst of acommodations for korrections '
        'of mispellings of particuler wurds.') == (
            'this is a test of acommodations for corrections of '
            'mispellings of particular words.')
