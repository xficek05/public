from binance.client import Client
import time

def data(pair):
    for ticker, values in pair.items():
        list = client.get_ticker(symbol=ticker)
        value = float(list['priceChangePercent'])
        price = float(list['lastPrice'])
        pair[ticker] = { 'percent' : value, 'price' : price}
    return pair

# binance api
api_key_Binance = 'geM8dY8xZG02nYuFVVpay2asDhGMhJn24sKTgLLH5isIBGtiAC5pp5pJ2CZIlHnp'
api_secret_Binance = 'geM8dY8xZG02nYuFVVpay2asDhGMhJn24sKTgLLH5isIBGtiAC5pp5pJ2CZIlHnp'

client = Client(api_key_Binance, api_secret_Binance)
print('\x1bc')
i = 0
while True:
    #začátek timeru
    startTime = time.time()
    #hlavni dict nic neupravovat !!!!!!
    pair = {'BTCUSDT': '', 'ETHUSDT': '', 'BNBUSDT': '', 'BCCUSDT': '', 'NEOUSDT': '', 'LTCUSDT': '', 'QTUMUSDT': '', 'ADAUSDT': '', 'XRPUSDT': '', 'EOSUSDT': '', 'TUSDUSDT': '', 'IOTAUSDT': '', 'XLMUSDT': '', 'ONTUSDT': '', 'TRXUSDT': '', 'ETCUSDT': '', 'ICXUSDT': '', 'VENUSDT': '', 'NULSUSDT': '', 'VETUSDT': '', 'PAXUSDT': '', 'BCHABCUSDT': '', 'BCHSVUSDT': '', 'USDCUSDT': '', 'LINKUSDT': '', 'WAVESUSDT': '', 'BTTUSDT': '', 'USDSUSDT': '', 'ONGUSDT': '', 'HOTUSDT': '', 'ZILUSDT': '', 'ZRXUSDT': '', 'FETUSDT': '', 'BATUSDT': '', 'XMRUSDT': '', 'ZECUSDT': '', 'IOSTUSDT': '', 'CELRUSDT': '', 'DASHUSDT': '', 'NANOUSDT': '', 'OMGUSDT': '', 'THETAUSDT': '', 'ENJUSDT': '', 'MITHUSDT': '', 'MATICUSDT': '', 'ATOMUSDT': '', 'TFUELUSDT': '', 'ONEUSDT': '', 'FTMUSDT': '', 'ALGOUSDT': '', 'USDSBUSDT': '', 'GTOUSDT': '', 'ERDUSDT': '', 'DOGEUSDT': '', 'DUSKUSDT': '', 'ANKRUSDT': '', 'WINUSDT': '', 'COSUSDT': '', 'NPXSUSDT': '', 'COCOSUSDT': '', 'MTLUSDT': '', 'TOMOUSDT': '', 'PERLUSDT': '', 'DENTUSDT': '', 'MFTUSDT': '', 'KEYUSDT': '', 'STORMUSDT': '', 'DOCKUSDT': '', 'WANUSDT': '', 'FUNUSDT': '', 'CVCUSDT': '', 'CHZUSDT': '', 'BANDUSDT': '', 'BUSDUSDT': '', 'BEAMUSDT': '', 'XTZUSDT': '', 'RENUSDT': '', 'RVNUSDT': '', 'HCUSDT': '', 'HBARUSDT': '', 'NKNUSDT': '', 'STXUSDT': '', 'KAVAUSDT': '', 'ARPAUSDT': '', 'IOTXUSDT': '', 'RLCUSDT': '', 'MCOUSDT': '', 'CTXCUSDT': '', 'BCHUSDT': '', 'TROYUSDT': '', 'VITEUSDT': '', 'FTTUSDT': '', 'EURUSDT': '', 'OGNUSDT': '', 'DREPUSDT': '', 'BULLUSDT': '', 'BEARUSDT': '', 'ETHBULLUSDT': '', 'ETHBEARUSDT': '', 'TCTUSDT': '', 'WRXUSDT': '', 'BTSUSDT': '', 'LSKUSDT': '', 'BNTUSDT': '', 'LTOUSDT': '', 'EOSBULLUSDT': '', 'EOSBEARUSDT': '', 'XRPBULLUSDT': '', 'XRPBEARUSDT': '', 'STRATUSDT': '', 'AIONUSDT': '', 'MBLUSDT': '', 'COTIUSDT': '', 'BNBBULLUSDT': '', 'BNBBEARUSDT': '', 'STPTUSDT': '', 'WTCUSDT': '', 'DATAUSDT': '', 'XZCUSDT': '', 'SOLUSDT': '', 'CTSIUSDT': '', 'HIVEUSDT': '', 'CHRUSDT': '', 'BTCUPUSDT': '', 'BTCDOWNUSDT': '', 'GXSUSDT': '', 'ARDRUSDT': '', 'LENDUSDT': '', 'MDTUSDT': '', 'STMXUSDT': '', 'KNCUSDT': '', 'REPUSDT': '', 'LRCUSDT': '', 'PNTUSDT': '', 'COMPUSDT': '', 'BKRWUSDT': '', 'SCUSDT': '', 'ZENUSDT': '', 'SNXUSDT': '', 'ETHUPUSDT': '', 'ETHDOWNUSDT': '', 'ADAUPUSDT': '', 'ADADOWNUSDT': '', 'LINKUPUSDT': '', 'LINKDOWNUSDT': '', 'VTHOUSDT': '', 'DGBUSDT': '', 'GBPUSDT': '', 'SXPUSDT': '', 'MKRUSDT': '', 'DAIUSDT': '', 'DCRUSDT': '', 'STORJUSDT': '', 'BNBUPUSDT': '', 'BNBDOWNUSDT': '', 'XTZUPUSDT': '', 'XTZDOWNUSDT': '', 'MANAUSDT': '', 'AUDUSDT': '', 'YFIUSDT': '', 'BALUSDT': '', 'BLZUSDT': '', 'IRISUSDT': '', 'KMDUSDT': '', 'JSTUSDT': '', 'SRMUSDT': '', 'ANTUSDT': '', 'CRVUSDT': '', 'SANDUSDT': '', 'OCEANUSDT': '', 'NMRUSDT': '', 'DOTUSDT': '', 'LUNAUSDT': '', 'RSRUSDT': '', 'PAXGUSDT': '', 'WNXMUSDT': '', 'TRBUSDT': '', 'BZRXUSDT': '', 'SUSHIUSDT': '', 'YFIIUSDT': '', 'KSMUSDT': '', 'EGLDUSDT': '', 'DIAUSDT': '', 'RUNEUSDT': '', 'FIOUSDT': '', 'UMAUSDT': '', 'EOSUPUSDT': '', 'EOSDOWNUSDT': '', 'TRXUPUSDT': '', 'TRXDOWNUSDT': '', 'XRPUPUSDT': '', 'XRPDOWNUSDT': '', 'DOTUPUSDT': '', 'DOTDOWNUSDT': '', 'BELUSDT': '', 'WINGUSDT': '', 'LTCUPUSDT': '', 'LTCDOWNUSDT': '', 'UNIUSDT': '', 'NBSUSDT': '', 'OXTUSDT': '', 'SUNUSDT': '', 'AVAXUSDT': '', 'HNTUSDT': '', 'FLMUSDT': '', 'UNIUPUSDT': '', 'UNIDOWNUSDT': '', 'ORNUSDT': '', 'UTKUSDT': '', 'XVSUSDT': '', 'ALPHAUSDT': '', 'AAVEUSDT': '', 'NEARUSDT': '', 'SXPUPUSDT': '', 'SXPDOWNUSDT': '', 'FILUSDT': '', 'FILUPUSDT': '', 'FILDOWNUSDT': '', 'YFIUPUSDT': '', 'YFIDOWNUSDT': '', 'INJUSDT': '', 'AUDIOUSDT': '', 'CTKUSDT': '', 'BCHUPUSDT': '', 'BCHDOWNUSDT': '', 'AKROUSDT': '', 'AXSUSDT': '', 'HARDUSDT': '', 'DNTUSDT': '', 'STRAXUSDT': '', 'UNFIUSDT': '', 'ROSEUSDT': '', 'AVAUSDT': '', 'XEMUSDT': '', 'AAVEUPUSDT': '', 'AAVEDOWNUSDT': '', 'SKLUSDT': '', 'SUSDUSDT': '', 'SUSHIUPUSDT': '', 'SUSHIDOWNUSDT': '', 'XLMUPUSDT': '', 'XLMDOWNUSDT': '', 'GRTUSDT': '', 'JUVUSDT': '', 'PSGUSDT': '', '1INCHUSDT': '', 'REEFUSDT': '', 'OGUSDT': '', 'ATMUSDT': '', 'ASRUSDT': '', 'CELOUSDT': '', 'RIFUSDT': '', 'BTCSTUSDT': '', 'TRUUSDT': '', 'CKBUSDT': '', 'TWTUSDT': '', 'FIROUSDT': '', 'LITUSDT': '', 'SFPUSDT': '', 'DODOUSDT': '', 'CAKEUSDT': '', 'ACMUSDT': '', 'BADGERUSDT': '', 'FISUSDT': '', 'OMUSDT': '', 'PONDUSDT': '', 'DEGOUSDT': '', 'ALICEUSDT': '', 'LINAUSDT': '', 'PERPUSDT': '', 'RAMPUSDT': '', 'SUPERUSDT': '', 'CFXUSDT': '', 'EPSUSDT': '', 'AUTOUSDT': '', 'TKOUSDT': '', 'PUNDIXUSDT': '', 'TLMUSDT': '', '1INCHUPUSDT': '', '1INCHDOWNUSDT': '', 'BTGUSDT': '', 'MIRUSDT': '', 'BARUSDT': '', 'FORTHUSDT': '', 'BAKEUSDT': '', 'BURGERUSDT': '', 'SLPUSDT': '', 'SHIBUSDT': '', 'ICPUSDT': '', 'ARUSDT': '', 'POLSUSDT': '', 'MDXUSDT': '', 'MASKUSDT': '', 'LPTUSDT': '', 'NUUSDT': '', 'XVGUSDT': '', 'ATAUSDT': '', 'GTCUSDT': '', 'TORNUSDT': '', 'KEEPUSDT': '', 'ERNUSDT': '', 'KLAYUSDT': '', 'PHAUSDT': '', 'BONDUSDT': '', 'MLNUSDT': '', 'DEXEUSDT': '', 'C98USDT': '', 'CLVUSDT': '', 'QNTUSDT': '', 'FLOWUSDT': '', 'TVKUSDT': '', 'MINAUSDT': '', 'RAYUSDT': '', 'FARMUSDT': '', 'ALPACAUSDT': '', 'QUICKUSDT': '', 'MBOXUSDT': '', 'FORUSDT': '', 'REQUSDT': '', 'GHSTUSDT': '', 'WAXPUSDT': '', 'TRIBEUSDT': '', 'GNOUSDT': '', 'XECUSDT': '', 'ELFUSDT': '', 'DYDXUSDT': '', 'POLYUSDT': '', 'IDEXUSDT': '', 'VIDTUSDT': '', 'USDPUSDT': '', 'GALAUSDT': '', 'ILVUSDT': '', 'YGGUSDT': '', 'SYSUSDT': '', 'DFUSDT': '', 'FIDAUSDT': '', 'FRONTUSDT': '', 'CVPUSDT': '', 'AGLDUSDT': '', 'RADUSDT': '', 'BETAUSDT': '', 'RAREUSDT': '', 'LAZIOUSDT': '', 'CHESSUSDT': '', 'ADXUSDT': '', 'AUCTIONUSDT': '', 'DARUSDT': '', 'BNXUSDT': '', 'RGTUSDT': '', 'MOVRUSDT': '', 'CITYUSDT': '', 'ENSUSDT': '', 'KP3RUSDT': '', 'QIUSDT': '', 'PORTOUSDT': '', 'POWRUSDT': '', 'VGXUSDT': '', 'JASMYUSDT': '', 'AMPUSDT': '', 'PLAUSDT': '', 'PYRUSDT': '', 'RNDRUSDT': '', 'ALCXUSDT': '', 'SANTOSUSDT': '', 'MCUSDT': '', 'ANYUSDT': '', 'BICOUSDT': '', 'FLUXUSDT': '', 'FXSUSDT': '', 'VOXELUSDT': '', 'HIGHUSDT': '', 'CVXUSDT': '', 'PEOPLEUSDT': '', 'OOKIUSDT': '', 'SPELLUSDT': '', 'USTUSDT': '', 'JOEUSDT': '', 'ACHUSDT': '', 'IMXUSDT': '', 'GLMRUSDT': '', 'LOKAUSDT': '', 'SCRTUSDT': '', 'API3USDT': '', 'BTTCUSDT': '', 'ACAUSDT': '', 'ANCUSDT': '', 'XNOUSDT': '', 'WOOUSDT': ''}
    #nahravání 1.dat
    pair = data(pair)
    first = pair.copy()
    #výpočet sleep time aby bylo co 5 min jeden cyklus
    endTime = time.time()
    endTime = 300 - (2 * (endTime - startTime))
    #time to sleep
    time.sleep(endTime)
    #nahravání 1.dat
    pair = data(pair)
    second = pair.copy()
    #kontrola dat
    for firstTicker, firstValues in first.items():
        for secondTicker, secondValues in second.items():
            if firstTicker == secondTicker:
                jump = abs(secondValues['percent']) - abs(firstValues['percent'])
                if jump >= 3.00:
                    print("{} : 1.cena {}   %skok {}    2.cena {} zkouknout".format(firstTicker,firstValues['price'], jump, secondValues['price']))
                    jump = 0
                    break
                else:
                    jump = 0
                    break
    i += 1
    print(i)
