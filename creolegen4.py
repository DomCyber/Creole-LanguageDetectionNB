import pandas as pd
import random

# Define creoles and their example sentences
creoles = {
    "Jamaican Creole": [
        "Mi nuh si dem.",
        "Wha gwan?",
        "Mi a go a di market.",
        "Yuh done know.",
        "Dis a di best.",
        "Yuh know how fi chat Patwah",
        "Ya Mon",
        "Frah wha pawt yuh deh",
        "Mi deh",
        "Inna di morrows",
        "Mi gaan",
        "Mi irie",
        "Wha gawn bad a maanin, cyaan kum gud a evelin.",
        "Good frien’ betta dan packet money",
        "A fe mi cyar",
        "Mi ah guh lef tiday",
        "Im too haad eaize.",
        "Axe har de question.",
        "No bodda bawl im soon cum bak",
        "Dat a mi bredda",
        "Bwaay! Mi did tink de test wudda eazy.",
        "The parson sey de marriage cerfitikit soon cum inna de mail.",
        "Mi a go bak a wuk pan Chewsday.",
        "Di chuck want tree new tyres.",
        "Cuyah, she gwan lak she nice eee?",
        "Chobble nuh nice.” “Yuh inna big chobble.",
        "Mi cyan ‘elp yuh wit dat problem.",
        "De bwoy dem teif di bleach outta de wata",
        "So, one time long long ago, di Hebrew people dem did ah suffer inna Egypt under di Pharaoh. One day, a likkle baby boy named Moses born, but Pharaoh did want to kill all di baby boy dem, so Moses’ madda put him inna basket and float him down di river",
        "Well, Jah know, dat basket end up inna di hands of Pharaoh’s daughter, who take pity pon di baby and adopt him",
        "Moses grow up inna di palace, but him always know say him a Hebrew",
        "One day, Moses see one of him Hebrew bredda dem get beaten by di Egyptian overseer, and him get so mad him end up killing di overseer.",
        "So, Moses haffi run weh from Egypt and go live inna di wilderness.",
        "While him a live out deh, Moses see a burning bush, but di bush nah burn up! Jah tell Moses fi go back to Egypt and tell Pharaoh fi let di Hebrew people dem go.",
        "But Pharaoh say no, so Jah send down some big big plague dem fi force Pharaoh fi let di people dem go.",
        "After di ten plague dem, Pharaoh finally let di people dem go, but him change him mind and send him army after dem.",
        "Jah part di Red Sea fi di Hebrew people dem fi escape, and when di Egyptian army try fi follow dem, di sea come back togedda and wash dem away.",
        "Moses lead di Hebrew people dem to Mount Sinai, where Jah give him di Ten Commandments and all di laws dem fi live by",
        "Moses spend forty years leading di people dem through di wilderness, and even though him never reach di Promised Land himself, him set di foundation fi di Hebrew people dem fi years to come.",
        "So dat a di story of Moses inna Jamaican patois! Give thanks fi di blessings of Jah",
        "Fram reggae tu dub poetry tu pride in a wi culcha, nationality, and dialek, whole eep a ting bout wi Jamaican culcha wi owe nuff respek to one oman.",
        "As a poet, comedian, folklorist, television and radio personality, singer and actor, di whole a Jamaica luv har like fambily and call har Miss Lou – not Louise Bennett-Coverley.",
        " Di way how she tek pride inna wi culcha and chat di patwa mek di whole a wi feel good. Pon toppa dat she inspire a whole heap a Jamaican artists to buss out with boasiness.",
        " Mi mudda tell mi dat as a likkle girl how powaful it was fi si Miss Lou pon TV a chat patwa."
        "Baan in 1919, Miss Lou tek up writin poetry from shi a likkle pickney. ",
        "Shi quick quick luv di patwa as di language of di people betta dan di stush English dem did a teach inna school. Mi mudda explain dat"
        "Miss Lou did write har first poem at di tenda age of 14 and inna no time shi write har poem dem inna di Gleana.",
        " Pon toppa dat, shi study Jamaican folklore an den she learn more bout oral tradition, proverbs, and riddles dat shi big up in har work, chat bout.",
        " Quick quick shi gaan a foreign pon scholarship to di Royal Academy a Dramatic Art. ",
        "When shi come back a yaad shi set up har theatre, den shi guh back a foreign to England and den America where shi nuh tap educate di people dem in a di patwa through folklore and music. ",
        "When shi come back a yaad, shi would teach di young people dem at UWI bout Jamaican folklore and drama. ",
        "Shi get more famous cuz di people dem luv har, dem big har up wid har own radio show: Miss Lou’s Views.",
        "Likkle bit from dat shi get a show call Ring Ding pon di TV. ", 
        "She tell di pickney dem Anansi stories an sing an dance an dem luv it. Dis was my muddas first time wid Miss Lou. ",
        "Dis was a time when everybody si success an steppin up inna life as talkin like di Queen of England. Miss Lou dared to big up all tings Jamaican.",
        "Di way shi chat di patwa wid respectability mek har an expert til Bajan poet Kamau Braithwaite call it a “nation language.” ",
        "As oppose to di English of di Queen, Braithwaite seh “nation language” is like di English of di slaves dat was full a African speech riddims like Hausa, Yoruba, Igbo, or Twi.",
        " Di colonizers put dung di patwa – dem neva like di patwa at all, an neva seet as respectable. ",
        "But Miss Lou neva stap, and Brathwaite seh “the hurricane does not roar in pentameter” – wi kno fi sure dat di English of Shakespeare caan match di true vibe of di Caribbean people.",
        "When you see Miss Lou pon TV, sometimes shi start tings off vibin wid di audience, getting dem tu sing along: ",
        "“Come mek mi hol yuh han.” Di audience jump in, den shi cut dem off:",
        "Oh wate wate wate wate… You know dis ting a appen too offen yunnuh… somebody a seh “yOuR hAnD”. Its not your hand, its yuh han! Nuh pwoil up di culcha!”",
        "When shi duh dis, everybody laugh. Miss Lou show us what is di language and culcha of di people, an what is di colonized language. As mi mudda explain",
        "When she says something like “mi glad fi see yuh bwoi”… “I’m happy to see you, boy” does not capture “Mi glad fi see yuh bwoi”.",
        "From har poetry tu har musical tu Ring Ding, Miss Lou’s wuk fi eva fulla Jamaican vibe and culcha. ",
        "Di way shi talk wid di children, an nuh tap wear di traditional Jamaican bandana dress, and di uppity weh shi chat patwa wid pride, even when di stush people dem try tu put har dung inspire di yute dem tu walk wid pride in demself.",
        "Di way shi use di patwa wid pride an bragadoshiousness an di tings in a it like immigration, status, uppitiness, stushness, and folk antics (like di Ashanti trickster spida “Anansi always in a har stories) set up tings fi dub poetry and reggae music fi buss out wid di people. ",
        "All a dem perform in patwa an talk bout di struggle of di people, fi sure poets and artiste like Bob Marley, Linton Kwesi Johnson, and Mutabaruka owe har nuff respeck.",
        " Mi haffi mention dat Big Youth (mi favourite deejay) duh a song name “Miss Lou Ring Ding.” ",
        "Everybody know dat widdout Miss Lou, reggae and di whole a Jamaican music dat wi kno right now wouldn’t be di same.",
        "Fi sure wi wear patwa wid suh much pride dat it bleed inna other culcha. ",
        "Alla da Jamaican inna Canada bring patwa wid dem an talk it at home an at school an everywhere into di meltin pot.,"
        " When Miss Lou said “Colonization in Reverse,” dis can also reffa to di patwa of fus an secon generation Jamaicans dat is di “Toronto slang” chat by all kinda people inna Toronto.",
        "Even doe Miss Lou mek Jamaicans proud, mi mudda pine dat “patois can take you very far if you’re an artist, poet or musician, but it will not take you anywhere if you want to be a lawyer or politician ",
        "Shi seh dat, even doe tings improve di trute is yuh haffi drop di patwa an try talk proppa English if yuh waan tu move up an “navigate colonized spaces.” ",
        "Jamaicans at home and Black people all ova di worl ave to code switch, leave di language and dem tru vibe when dem seekin success.",
        "Even doe dem caana wi an wi haffi use di Queen English fi step up ina life, Miss Lou bring pride an dignity to all a wi an mek wi luv wi culcha.",
        " Shi a wi hero an wi luv har because “She wrote and spoke these poems and stories and she made us proud of our own traditions.",
        " I think that is the root of the pride that we have in Miss Lou and in ourselves. We saw ourselves reflected in her, and in a way that was very dignified and uniquely Jamaican.",
        " And so, if we could be proud of Miss Lou, then we could be proud of ourselves too.”"


        # Add more sentences as needed
    ],
    "Haitian Creole": [
        "Mwen renmen ou.",
        "Kijan ou ye?",
        "Sa a bon.",
        "Nou pral ale.",
        "Li ap mache.",
        "Divès lyen ki konekte Ayiti ak Louisiana an tèm de kilti gastronomik, langaj, achitekti, relijyon, ak mizik pèsiste jodi a.",
        "Tout moun fèt lib, egal ego pou diyite kou wè dwa. Nou gen la rezon ak la konsyans epi nou fèt pou nou aji youn ak yon lespri fwatènite.",
        "Byen venu",
        "V byenvini",
        "N bèlantre",
        "Bonjou",
        "Sa fè lontan",
        "Sa fe lon temps nou pa we",
        "Koman ou rele?,"
        "Ki jan ou rele?",
        "Ki non ou?",
        "Ki non w?",
        "Se bato mwen ki flote sou dlo a ki te ranpli avèk èèl",
        "Yon sèl lang se janm ase",
        "Felisitasyon!",
        "Bonn fèt",
        "Erez anivèsè",
        "Bònn fèt pak",
        "Bònn Ane",
        "Jwaye Nowèl",
        "Rele la polis!",
        "Rete",
        "Dife",
        "Anmwe!",
        "Ki te'm anrepo'm!",
        "Ale vou zan!",
        "Fè mye talè",
        "Mwen renmen w",
        "Mwen sonje w",
        "Eske ou vle danse?",
        "Kote twalèt la?",
        "Sa fè lontan",
        "Sa fe lon temps nou pa we",
        "Koman ou rele?",
        "Ki jan ou rele?",
        "Ki non ou?",
        "Ki non w?",
        "Anchante",
        "M'kontan fè konesans ou",
        "Mwe kontan fe konesana ou",
        "Se youn plaisir fè konesans ou!",
        "Bon maten",
        "Bon apre-midi",
        "Bonswa",
        "Adye",
        "Babay",
        "N a wè pi ta",
        "A pi ta",
        "A demen ",
        "Bòn chans",
        "Ochan!",
        "Sante!",
        "Onè Respè!",
        "Pase yon bònn jounen",
        "Bònn jounen",
        "Ou konprann?",
        "Mwen pa komprann",
        "Ou ka pale dousman souple?",
        "Nou nan yon ti bouk pa twò lwen Pòtoprens. Bouk sa a rele Fonwouj. Li gen yon pwoblèm ki gwo anpil anpil: pa gen dlo. ",
        "Pa gen dlo menm menm. Plant ap mouri, bèt ap mouri.",
        "Yon jou se moun ki ka mouri tou. Depi lontan lontan lapli pa tonbe.",
        "Tout bagay sèk, tout bagay tris.",
        "Petèt se paske yo te koupe tout pyebwa yo, men sa w vle? Yo te bezwen bwa a pou fè chabon, pou fè kay, lantiray, mèb.",
        " Epi yo te bezwen tè a tou pou plante mayi, pou plante pwa, pou yo jwenn manje. Si yo pa travay tè a, yo pap manje.",
        "Devan yon ti kay pay gen de vye granmoun ki chita: yon nèg ki rele Byenneme, ak Delira, madanm li.",
        "Byenneme: “Zafè nou pa bon. Tout bagay ap mouri. Bondye bliye nou nèt.”",
        "Delira: “Pa pale konsa. Se pa byen, non. Deja nou pa gen lespwa.",
        "Pitit gason nou an kite nou depi lontan, pou ale koupe kann nan peyi Kiba.",
        "Li pap tounen. Non, se vre, pa gen lespwa.",
        "Ki kote de vye granmoun sa yo chita?",
        "Èske yo kwè gen lespwa pou yo?",
        "Epi ki sa Delira reponn li?",
        "Si yo pa travay tè a, sa k ap rive?",
        "Ki bagay yo te plante sou tè a?",


        # Add more sentences as needed
    ],
    "Papiamento": [
        "Mi ta gusta ku bo.",
        "Kiko ta pasa?",
        "Nos ta bai.",
        "E ta bon.",
        "Bo ta bini?",
        "Yama polis!",
        "Bon pasco",
        "Bon pasco di resureccion",
        "Felis cumpleaño",
        "Un idioma nunka ta sufisiente",
        "Un lenguage nunka ta sufisiente",
        "Mi hovercraft ta yen di conglá",
        "Candela!",
        "Yudami!",
        "Pronto recuperacion",
        "Mehora pronto",
        "Bo lo kier baila cumi? ",
        "E meneer lo paga pa tur cos",
        "Masha danki",
        "Danki",
        "Porfabor",
        "Cuanto esaki ta costa?",
        "Porfabor Bo por bisami un biaha mas e mesun cos",
        "Ta un plaser di conocebo",
        "Venezuela i a traha den Kòkou. Ta di dje mi a fia e nòmber Mimina. Asin'aki e tambe por haña honor pa e kurashi ku el a demonstrá e",
        "tempu ei. Espesialmente mi ke animá tur hende yòn pa lesa e buki aki ku un aktitut di siña nos historia sin laga rabia drenta boso kurason.",
        "E personahenan di e 5 muhénan i nan shonnan ta kompletamente fiktivo. Na Boneiru tabatin un katibu muhé Mimina ku a hui bai",
        "Dje serka ei sklabitut ta di nos? E buki aki ta skibí pa yuda nos komprondé nos historia di sklabitut mas mihó. ",
        "Tur fecha i datonan den e buki aki ta histórikamente korekto.",
        "tabata katibu òf por lo ménos a biba den tempu di sklabitut!",
        "papelnan ofisial mi a ripará ku el a nase na 1913.",
        "papelnan ofisial mi a ripará ku el a nase na 1913.",
        "Esta su wela o bisa wela mester",
        "Suzanna Fransiska (Tanchi Chu) ta un di mi welanan ku a kuida mi hopi den mi bida. Dia ku el a bai sosegá i mi tabata atendiendo su",
        "Papa Bubu, di Banda Bou, tabata manera un tawela pa mi i el a konta mi mashá kos di pasado. Su mayornan a kont'é di tempu di katibu. Hopi di loke ta skibí aki ta kosnan ku el a konta mi personalmente.",
        "kuida mata i kushiná kuminda krioyo.",
        "kompletamente n'e pa su amor p'ami. El a siña mi kon ta mata galiña,",
        "Sila Kelie (Mai Sila) a kria mi hopi aña i e buki aki ta dediká",
        "Purba pone algun prosa riba pantaya, sinembargo, i nan ta meskla nan mes basta lihé. ",
        "Esaki tin hopi di haber ku e limitashonnan di tempu ku nos ta pretendé di sinti den e era digital.",
        " Nos no tin tempu pa traha karta i post nan mas–muchu ménos paga gastunan di post, kiko ku tur e bankonan kinda-sorta ta pèrdè nos sèn e dianan aki–p’esei nos ta blast algun email. ",
        "Nos no tin tempu pa papia, pues nos ta manda mensahe. Nos no tin tempu pa manda mensahe pa hende spesífiko, pues nos ta aktualisá nos status di Facebook. Nos no tin tempu pa skirbi ensayonan, pues nos ta blog.",
        "Mas importante: Kiko eksaktamente nos ta skirbiendo ora nos ta hasiendo tur e skirbimentu aki? Mi no ta bai pretendé di inventá un término kompletamente nobo aki; ",
        " Mi ta kere ainda ku e mihó ku nos por rekohé ta un análogo mas adekuá. I si nos mester haña un análogo den un unidat literario eksistente, mi ta proponé e paragraf. ",
        "Nos skirbimentu konstante a kuminsá sinti manera un paragraf digital sin fin. No un paragraf stret i hinkadó di The Sun Also Rises òf asta un paragraf grasioso, tin bia ta slip, tin bia ta bula di Absalom! Absalom!",
        "mi ke men un paragraf konvolushoná, aleatorio, ku ta serka, algu manera Kerouac su konsepto original di On the Road–solamente grabá huntu pa byte. I 1 porshento mes interesante.",
   

        # Add more sentences as needed
    ],
    "Tok Pisin": [
        "Mi likim yu.",
        "Ol i stap?",
        "Mi go long market.",
        "Yu save?",
        "Dispela em i gut.",
        "Bikpela samting tru: Wanem samting tru yumi raitim taim yumi raitim olgeta dispela samting? Mi no inap giaman long kamapim wanpela nupela tok hia;",
        " Mi ting yet olsem nambawan samting yumi ken bungim em i wanpela 'analog' we i stret moa. Na sapos yumi mas painim wanpela analog insait long wanpela 'literary unit' we i stap pinis, mi laik kamapim dispela paragraf. ",
        "Rait bilong mipela oltaim i stat long pilim olsem wanpela dijitel paragraf we i no inap pinis. I no wanpela tait, strongpela paragraf bilong The Sun Also Rises o wanpela naispela, sampela taim-slinking, sampela taim-soaring paragraf bilong",
        "Absalom! Absalom!, mi minim wanpela paragraf we i paul, i no stret, na i tantanim, samting olsem namba wan draf bilong Kerouac bilong On the Road - ol i bin pasim wantaim long ol 'bytes' tasol. Na 1 pesen em i gutpela.",
        "I no long taim i go pinis, mi luksave olsem ol sentens bilong mi i save go het taim mi raitim ol long skrin. Dispela i go long raitim planti samting na tu long raitim ol pas.",
        " (Ating Twain i bilip olsem wok bilong raitim pas, insait long wanpela gutpela wol, i nidim tu tingting gut. Tasol em i no bin yusim email.) Las wik mi painim mi yet i putim 4-pela konjunksen",
        "insait long wanpela tripela lain sentens insait long wanpela email. Em i no inap long eskius. Stat long dispela taim, mi bin traim long abrusim ol 'conjunction' taim mi inap. Ol koma, ol na, tasol, na olsem i no stap moa; insait em ol 'staccato declaratives'. ",
        "Mobeta long ritim olsem Hemingway nogut winim Faulkner nogut.",
        "Wanpela wik i go pinis wanpela pren i bin singautim tupela arapela marit long kam kaikai. Bihain, ol i rausim kaikai (tasol i no wain) long tebol bilong wanem samting i kamap olsem wanpela strongpela Scrabbling.",
        " Mipela i bihainim tingting bilong yusim sotpela, moa gutpela tok na i no longpela na i no gat bikpela pe, laspela pilai bilong mipela em ", 
        "Bon, we-olsem laki bai i stap!-i kamap olsem wanpela Japanese Buddhist festival, na i no, olsem mi bin mekim pastaim i tok strong taim em i putim ol 'tiles' long bod ",
        " wanpela hap bilong wanpela 'cherry treat' we i gat soklet long en. Maski, dispela strateji i wok gut. Tim bilong mi i lus long 53 poin tasol na i no 58.",
        "Wanem nem bilong yu?",
        "Yu whosait?",
        "Nem bilong mi",
        "sori nogut",
        "sori nogut",
        "mi orait tasol",
        "em hamas?",
        "mi laik go long Airport",
        "inap yu kam wantaim mi?",
        "plis, inap ya halivim mi wantaim dispela samting?",
        "lait malolo liklik",
        "mi laikim planti plis",
        "Dispela man bai i bekim pe long olgeta samting",
        "Bikpela hamamas blong dispela Krismas go long yu Meri Krismas",
        "Bilong me hangamapim bot stap pulap maleo",
        "Balus em i no goupim bilong me em i pullup long liklik pela snek bilong solwarra",
        "Meri i gat liklik sipsip",
        "Giras bilong en i waitpela tru",
        "Sapos Meri i go wokabaut",
        "Bai sipsip igo wantaim tu",
        "Papa bilong mipela, yu stap long heven.",
        "Mekim nem bilong yu i kamap bikpela.",
        "Strongim mipela long bihainim laik bilong yu long graun, olsem ol i bihainim long heven.",
        "Pogivim rong bilong mipela olsem mipela i pogivim ol arapela i mekim rong long mipela.",
        "Sambai long mipela long taim bilong traim. ",
        "Na rausim olgeta samting nogut long mipela",
        "Yu raun we",
        "Nogat. Mi siutim koronas",
        "Nau yet, ol 'virtual companions' na 'AI sexbots' i stap olsem wanpela liklik maket tru winim sosel midia, wantaim planti milion yusa na i no planti bilien.",
        " Tasol olsem histori bilong ol kampani olsem Facebook, Google na Amazon i bin lainim yumi, ol dijitel samting bilong nau inap kamap ol bikpela samting bilong wol tumora.",
        "Pasin bilong ol 'catfisher' na 'dikteta' long paulim tingting bilong ol manmeri em i samting nogut tru. ",
        "Tingim bagarap bai kamap sapos ol manmeri olsem Vladimir Putin bilong Rasia o Kim Jong-un bilong Not Korea i yusim dispela teknoloji long helpim ol kantri bilong ol long mekim bikpela wok bilong 'cyber-spionage'.",
        

        # Add more sentences as needed
    ],
    "Cape Verdean Creole": [
        "Nhu ten ki bon.",
        "Kum ta?",
        "Nos ta bai.",
        "Es ta bon.",
        "Kel é seu nome?",
        "Olá",
        "Modi bu sta?",
        "Nha nomi e ...",
        "Moki bu tchoma?",
        "Ti manham",
        "Pur favor, papia digabar",
        "Skrebe-l, pur favor",
        "Da-n lisensa",
        "Bu cre dança ku mi?",
        "Dixâ-m' em pás!",
        "D'xá-m' s'segód'!",
        "Boas Festas",
        "Modi bu sta?, Kuma ku bu sta?",
        "N´kré kumi cachupa",
        "N´ka kré más, obrigado(a)",
        "Bu sabi ki óra autokaru ta txiga?",
        "Bon dia",
        "Kuma ku bu nome?",
        "Consensa",
        "Algin li ta papia inglés?",
        "N’ka persibi (or) N’ka intindi",
        "Dja N perde nhas amiga",
        "Dja N perde avion/konboiu",
        "Patin bianda",
        "Algin li ta papia inglés?",
        "Ta fest ti koku",
       

        # Add more sentences as needed
    ]
}

# Prepare the dataset
data = []

# Generate sentences for each creole
for creole, sentences in creoles.items():
    for _ in range(2000):
        sentence = random.choice(sentences)
        data.append({"Text": sentence, "Language": creole})

# Create a DataFrame
df = pd.DataFrame(data)

# Shuffle the dataset
df = df.sample(frac=1).reset_index(drop=True)

# Save to a CSV file
df.to_csv("cgen4.csv", index=False)

print("Dataset generated with 10,000 entries.")






