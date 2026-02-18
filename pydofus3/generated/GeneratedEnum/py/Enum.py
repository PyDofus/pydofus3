from enum import IntFlag

# .FlashFilterRenderFeature
class FlashFilterRenderFeature(IntFlag):
    dsad = 0
    dsae = 1
    dsaf = 2
    dsag = 3
    dsah = 4

# .Interop
class Interop(IntFlag):
    FileBasicInfo = 0
    FileStandardInfo = 1
    FileNameInfo = 2
    FileRenameInfo = 3
    FileDispositionInfo = 4
    FileAllocationInfo = 5
    FileEndOfFileInfo = 6
    FileStreamInfo = 7
    FileCompressionInfo = 8
    FileAttributeTagInfo = 9
    FileIdBothDirectoryInfo = 10
    FileIdBothDirectoryRestartInfo = 11
    FileIoPriorityHintInfo = 12
    FileRemoteProtocolInfo = 13
    FileFullDirectoryInfo = 14
    FileFullDirectoryRestartInfo = 15

# .Interop
class Interop(IntFlag):
    FindExInfoStandard = 0
    FindExInfoBasic = 1
    FindExInfoMaxInfoLevel = 2

# .Interop
class Interop(IntFlag):
    FindExSearchNameMatch = 0
    FindExSearchLimitToDirectories = 1
    FindExSearchLimitToDevices = 2
    FindExSearchMaxSearchOp = 3

# .Interop
class Interop(IntFlag):
    GetFileExInfoStandard = 0
    GetFileExMaxInfoLevel = 1

# .Interop
class Interop(IntFlag):
    STATUS_SUCCESS = 0
    STATUS_NOT_FOUND = 3221226021
    STATUS_INVALID_PARAMETER = 3221225485
    STATUS_NO_MEMORY = 3221225495

# .Interop
class Interop(IntFlag):
    FALSE = 0
    TRUE = 1

# .Interop
class Interop(IntFlag):
    FALSE = 0
    TRUE = 1

# .Interop
class Interop(IntFlag):
    FileDirectoryInformation = 1
    FileFullDirectoryInformation = 2
    FileBothDirectoryInformation = 3
    FileBasicInformation = 4
    FileStandardInformation = 5
    FileInternalInformation = 6
    FileEaInformation = 7
    FileAccessInformation = 8
    FileNameInformation = 9
    FileRenameInformation = 10
    FileLinkInformation = 11
    FileNamesInformation = 12
    FileDispositionInformation = 13
    FilePositionInformation = 14
    FileFullEaInformation = 15
    FileModeInformation = 16
    FileAlignmentInformation = 17
    FileAllInformation = 18
    FileAllocationInformation = 19
    FileEndOfFileInformation = 20
    FileAlternateNameInformation = 21
    FileStreamInformation = 22
    FilePipeInformation = 23
    FilePipeLocalInformation = 24
    FilePipeRemoteInformation = 25
    FileMailslotQueryInformation = 26
    FileMailslotSetInformation = 27
    FileCompressionInformation = 28
    FileObjectIdInformation = 29
    FileCompletionInformation = 30
    FileMoveClusterInformation = 31
    FileQuotaInformation = 32
    FileReparsePointInformation = 33
    FileNetworkOpenInformation = 34
    FileAttributeTagInformation = 35
    FileTrackingInformation = 36
    FileIdBothDirectoryInformation = 37
    FileIdFullDirectoryInformation = 38
    FileValidDataLengthInformation = 39
    FileShortNameInformation = 40
    FileIoCompletionNotificationInformation = 41
    FileIoStatusBlockRangeInformation = 42
    FileIoPriorityHintInformation = 43
    FileSfioReserveInformation = 44
    FileSfioVolumeInformation = 45
    FileHardLinkInformation = 46
    FileProcessIdsUsingFileInformation = 47
    FileNormalizedNameInformation = 48
    FileNetworkPhysicalNameInformation = 49
    FileIdGlobalTxDirectoryInformation = 50
    FileIsRemoteDeviceInformation = 51
    FileUnusedInformation = 52
    FileNumaNodeInformation = 53
    FileStandardLinkInformation = 54
    FileRemoteProtocolInformation = 55
    FileRenameInformationBypassAccessCheck = 56
    FileLinkInformationBypassAccessCheck = 57
    FileVolumeNameInformation = 58
    FileIdInformation = 59
    FileIdExtdDirectoryInformation = 60
    FileReplaceCompletionInformation = 61
    FileHardLinkFullIdInformation = 62
    FileIdExtdBothDirectoryInformation = 63
    FileDispositionInformationEx = 64
    FileRenameInformationEx = 65
    FileRenameInformationExBypassAccessCheck = 66
    FileDesiredStorageClassInformation = 67
    FileStatInformation = 68

# .Interop
class Interop(IntFlag):
    OBJ_INHERIT = 2
    OBJ_PERMANENT = 16
    OBJ_EXCLUSIVE = 32
    OBJ_CASE_INSENSITIVE = 64
    OBJ_OPENIF = 128
    OBJ_OPENLINK = 256

# .Interop
class Interop(IntFlag):
    FILE_SUPERSEDE = 0
    FILE_OPEN = 1
    FILE_CREATE = 2
    FILE_OPEN_IF = 3
    FILE_OVERWRITE = 4
    FILE_OVERWRITE_IF = 5

# .Interop
class Interop(IntFlag):
    FILE_DIRECTORY_FILE = 1
    FILE_WRITE_THROUGH = 2
    FILE_SEQUENTIAL_ONLY = 4
    FILE_NO_INTERMEDIATE_BUFFERING = 8
    FILE_SYNCHRONOUS_IO_ALERT = 16
    FILE_SYNCHRONOUS_IO_NONALERT = 32
    FILE_NON_DIRECTORY_FILE = 64
    FILE_CREATE_TREE_CONNECTION = 128
    FILE_COMPLETE_IF_OPLOCKED = 256
    FILE_NO_EA_KNOWLEDGE = 512
    FILE_RANDOM_ACCESS = 2048
    FILE_DELETE_ON_CLOSE = 4096
    FILE_OPEN_BY_FILE_ID = 8192
    FILE_OPEN_FOR_BACKUP_INTENT = 16384
    FILE_NO_COMPRESSION = 32768
    FILE_OPEN_REQUIRING_OPLOCK = 65536
    FILE_DISALLOW_EXCLUSIVE = 131072
    FILE_SESSION_AWARE = 262144
    FILE_RESERVE_OPFILTER = 1048576
    FILE_OPEN_REPARSE_POINT = 2097152
    FILE_OPEN_NO_RECALL = 4194304

# .Interop
class Interop(IntFlag):
    FILE_READ_DATA = 1
    FILE_LIST_DIRECTORY = 1
    FILE_WRITE_DATA = 2
    FILE_ADD_FILE = 2
    FILE_APPEND_DATA = 4
    FILE_ADD_SUBDIRECTORY = 4
    FILE_CREATE_PIPE_INSTANCE = 4
    FILE_READ_EA = 8
    FILE_WRITE_EA = 16
    FILE_EXECUTE = 32
    FILE_TRAVERSE = 32
    FILE_DELETE_CHILD = 64
    FILE_READ_ATTRIBUTES = 128
    FILE_WRITE_ATTRIBUTES = 256
    FILE_ALL_ACCESS = 983551
    DELETE = 65536
    READ_CONTROL = 131072
    WRITE_DAC = 262144
    WRITE_OWNER = 524288
    SYNCHRONIZE = 1048576
    STANDARD_RIGHTS_READ = 131072
    STANDARD_RIGHTS_WRITE = 131072
    STANDARD_RIGHTS_EXECUTE = 131072
    FILE_GENERIC_READ = 2147483648
    FILE_GENERIC_WRITE = 1073741824
    FILE_GENERIC_EXECUTE = 536870912

# .Interop
class Interop(IntFlag):
    FALSE = 0
    TRUE = 1

# .bl
class bl(IntFlag):
    ctod = 0
    ctoe = 1
    ctof = 2
    ctog = 3

# .c
class c(IntFlag):
    ctgo = 0
    ctgp = 1
    ctgq = 2
    ctgr = 3
    ctgs = 4
    ctgt = 5

# .chn
class chn(IntFlag):
    czlu = 0
    czlv = 1

# .cl
class cl(IntFlag):
    ctrj = 0
    ctrk = 1
    ctrl = 2
    ctrm = 3
    ctrn = 4
    ctro = 5
    ctrp = 6

# .cnb
class cnb(IntFlag):
    czmh = 0
    czmi = 1
    czmj = 2

# .dam
class dam(IntFlag):
    dadr = 0
    dads = 1
    dadt = 2

# .ddc
class ddc(IntFlag):
    dagz = 0
    daha = 1

# .dg
class dg(IntFlag):
    ctub = 0
    ctuc = 1
    ctud = 0

# .dke
class dke(IntFlag):
    daqj = 0
    daqk = 1

# .dkf
class dkf(IntFlag):
    daql = 0
    daqm = 1
    daqn = 2

# .dkg
class dkg(IntFlag):
    daqo = 1
    daqp = 2

# .dkh
class dkh(IntFlag):
    daqq = 0
    daqr = 1
    daqs = 2
    daqt = 3

# .dki
class dki(IntFlag):
    daqu = 0
    daqv = 1
    daqw = 2
    daqx = 3

# .dkj
class dkj(IntFlag):
    daqy = 0
    daqz = 1
    dara = 2
    darb = 3
    darc = 4

# .dkk
class dkk(IntFlag):
    dard = 0
    dare = 1
    darf = 2
    darg = 3
    darh = 4
    dari = 5

# .dkl
class dkl(IntFlag):
    darj = 0
    darl = 1
    darm = 2
    darn = 3

# .dkm
class dkm(IntFlag):
    daro = 0
    darp = 1
    darq = 2
    darr = 3
    dars = 4
    dart = 5
    daru = 6

# .dkn
class dkn(IntFlag):
    darv = 0
    darw = 1
    darx = 2
    dary = 3
    darz = 4
    dasa = 5

# .dko
class dko(IntFlag):
    dasb = 0
    dasc = 1
    dasd = 2

# .dkp
class dkp(IntFlag):
    dase = 0
    dasf = 1
    dasg = 2
    dash = 3
    dasi = 4
    dasj = 5
    dask = 6
    dasl = 7
    dasm = 8
    dasn = 9

# .dkq
class dkq(IntFlag):
    daso = 0
    dasp = 1
    dasq = 2
    dasr = 3
    dass = 4
    dast = 5
    dasu = 6

# .dkr
class dkr(IntFlag):
    dasv = 0
    dasw = 1
    dasx = 2

# .dks
class dks(IntFlag):
    dasy = 0
    dasz = 1
    datb = 2
    datc = 3
    datd = 4
    datf = 5
    datg = 6
    dath = 7
    dati = 8
    datj = 9
    datk = 10
    datl = 11
    datm = 12
    datn = 13
    dato = 14
    datp = 15

# .dkt
class dkt(IntFlag):
    datq = 0
    datr = 1
    dats = 2
    datt = 3
    datu = 4
    datv = 5

# .dku
class dku(IntFlag):
    datw = 0
    datx = 1
    daty = 2
    datz = 3
    daua = 4
    daub = 5

# .dkv
class dkv(IntFlag):
    dauc = 0
    daud = 1

# .dkw
class dkw(IntFlag):
    daue = 0
    dauf = 1

# .dkx
class dkx(IntFlag):
    daug = 0
    dauh = 1

# .dky
class dky(IntFlag):
    daui = 0
    dauj = 1
    dauk = 2
    daul = 3

# .dkz
class dkz(IntFlag):
    daum = 0
    daun = 1
    dauo = 2

# .dla
class dla(IntFlag):
    daup = 0
    dauq = 1
    daur = 2
    daus = 3
    daut = 4
    dauu = 5

# .dlb
class dlb(IntFlag):
    dauv = 0
    dauw = 1
    daux = 2

# .dlc
class dlc(IntFlag):
    dauy = 0
    dauz = 1
    dava = 2
    davb = 3
    davc = 4
    davd = 5
    dave = 6

# .dld
class dld(IntFlag):
    davf = 0
    davg = 1
    davh = 2
    davi = 3
    davj = 4
    davk = 5
    davl = 6
    davm = 7
    davn = 8
    davo = 9
    davp = 10

# .dle
class dle(IntFlag):
    davq = 0
    davr = 1

# .dlf
class dlf(IntFlag):
    davs = 0
    davt = 1
    davu = 2

# .dlg
class dlg(IntFlag):
    davv = 0
    davw = 1
    davx = 2
    davy = 3
    davz = 4
    dawa = 5

# .dlh
class dlh(IntFlag):
    dawb = 0
    dawc = 1
    dawd = 2
    dawe = 3
    dawf = 4

# .dli
class dli(IntFlag):
    dawg = 0
    dawh = 1
    dawi = 2
    dawj = 3
    dawk = 4

# .dlj
class dlj(IntFlag):
    dawl = -1
    dawm = 0
    dawn = 1
    dawo = 2
    dawp = 3
    dawq = 4
    dawr = 5
    daws = 6

# .dlk
class dlk(IntFlag):
    dawt = 0
    dawu = 1
    dawv = 2

# .dll
class dll(IntFlag):
    daww = 0
    dawx = 1
    dawy = 2
    dawz = 3

# .dlm
class dlm(IntFlag):
    daxa = 0
    daxb = 1
    daxc = 2
    daxd = 3
    daxe = 4

# .dln
class dln(IntFlag):
    daxf = 0
    daxg = 1

# .dlo
class dlo(IntFlag):
    daxh = 0
    daxi = 1
    daxj = 2
    daxk = 3

# .dlp
class dlp(IntFlag):
    daxl = 0
    daxm = 1
    daxn = 2
    daxo = 3

# .dlq
class dlq(IntFlag):
    daxp = 0
    daxq = 1
    daxr = 2
    daxs = 3
    daxt = 4
    daxu = 5
    daxv = 6
    daxw = 7
    daxx = 8
    daxy = 9
    daxz = 10
    daya = 11
    dayb = 12
    dayc = 13
    dayd = 14
    daye = 15

# .dlr
class dlr(IntFlag):
    dayf = 0
    dayg = 1
    dayh = 2
    dayi = 3
    dayj = 4
    dayk = 5
    dayl = 6
    daym = 7

# .dls
class dls(IntFlag):
    dayn = 855
    dayo = 848
    dayp = 862
    dayq = -1

# .dlt
class dlt(IntFlag):
    dayr = 0
    dayt = 1
    dayu = 2
    dayv = 3
    dayw = 4
    dayx = 5
    dayy = 6
    dayz = 7
    daza = 8
    dazb = 9
    dazc = 10

# .dlu
class dlu(IntFlag):
    dazd = -1
    daze = 0
    dazf = 1
    dazg = 2
    dazh = 3
    dazi = 4
    dazj = 5
    dazk = 6
    dazl = 7
    dazm = 8
    dazn = 9
    dazo = 10
    dazp = 11
    dazq = 12
    dazr = 13
    dazs = 14
    dazt = 15
    dazu = 16
    dazv = 17
    dazw = 18

# .dlv
class dlv(IntFlag):
    dazx = 1
    dazy = 2
    dazz = 3
    dbaa = 4

# .dlw
class dlw(IntFlag):
    dbab = -1
    dbac = 0
    dbad = 1
    dbae = 2
    dbaf = 3
    dbag = 4
    dbah = 5
    dbai = 6
    dbaj = 7
    dbak = 8
    dbal = 9
    dbam = 10
    dban = 11
    dbao = 12
    dbap = 13
    dbaq = 14
    dbar = 15
    dbas = 16
    dbat = 17
    dbau = 18
    dbav = 19
    dbaw = 20
    dbax = 21
    dbay = 22
    dbaz = 23
    dbba = 24
    dbbb = 25
    dbbc = 26
    dbbd = 27
    dbbe = 28

# .dlx
class dlx(IntFlag):
    dbbf = 0
    dbbg = 1

# .dly
class dly(IntFlag):
    dbbh = 0
    dbbi = 1
    dbbj = 2
    dbbk = 3
    dbbl = 4
    dbbm = 5
    dbbn = 6
    dbbo = 7
    dbbp = 8
    dbbq = 9
    dbbr = 10
    dbbs = 11
    dbbt = 12
    dbbu = 13
    dbbv = 14
    dbbw = 15
    dbbx = 16
    dbby = 17
    dbbz = 18
    dbca = 19
    dbcb = 20
    dbcc = 21
    dbcd = 22
    dbce = 23
    dbcf = 24
    dbcg = 25
    dbch = 26
    dbci = 27
    dbcj = 28
    dbck = 30
    dbcl = 31
    dbcm = 32
    dbcn = 33
    dbco = 34
    dbcp = 35
    dbcq = 36
    dbcr = 37
    dbcs = 38
    dbct = 39
    dbcu = 40
    dbcv = 41
    dbcw = 42
    dbcx = 43
    dbcy = 44
    dbcz = 45
    dbda = 46
    dbdb = 47
    dbdc = 48
    dbdd = 49

# .dlz
class dlz(IntFlag):
    dbde = 0
    dbdf = 1
    dbdg = 2

# .dma
class dma(IntFlag):
    dbdh = 0
    dbdi = 1
    dbdj = 2
    dbdk = 3
    dbdl = 4

# .dmb
class dmb(IntFlag):
    dbdm = 0
    dbdn = 1

# .dmc
class dmc(IntFlag):
    dbdo = 0
    dbdp = 1

# .dmd
class dmd(IntFlag):
    dbdq = 0
    dbdr = 1
    dbds = 2
    dbdt = 3
    dbdu = 4
    dbdv = 5
    dbdw = 6

# .dme
class dme(IntFlag):
    dbdx = 1
    dbdy = 2
    dbdz = 3
    dbea = 4
    dbeb = 5
    dbec = 6
    dbed = 7
    dbee = 8
    dbef = 9
    dbeg = 10
    dbeh = 11
    dbei = 12
    dbej = 13
    dbek = 14
    dbel = 15
    dbem = 16
    dben = 17
    dbeo = 18
    dbep = 19
    dbeq = 20
    dber = 21
    dbes = 22
    dbet = 99
    dbeu = 100
    dbev = 101
    dbew = 102
    dbex = 103
    dbey = 999
    dbez = 1001
    dbfa = 1002
    dbfb = 1004
    dbfc = 1005
    dbfd = 1006
    dbfe = 3001
    dbff = 3002
    dbfg = 10001
    dbfh = 11001
    dbfi = 13001

# .dmg
class dmg(IntFlag):
    dbfk = -1
    dbfl = 0
    dbfm = 1
    dbfn = 2
    dbfo = 3
    dbfp = 4
    dbfq = 5

# .dmh
class dmh(IntFlag):
    dbfr = 0
    dbfs = 1

# .dmi
class dmi(IntFlag):
    dbft = 0
    dbfu = 1

# .dmj
class dmj(IntFlag):
    dbfv = 0
    dbfw = 1
    dbfx = 2

# .dmk
class dmk(IntFlag):
    dbfy = 0
    dbfz = 1
    dbga = 2

# .dml
class dml(IntFlag):
    dbgb = -1
    dbgc = 0
    dbgd = 1
    dbge = 2

# .dmm
class dmm(IntFlag):
    dbgf = 0
    dbgg = 1

# .dmn
class dmn(IntFlag):
    dbgh = 0
    dbgi = 1
    dbgj = 2

# .dmo
class dmo(IntFlag):
    dbgk = 1
    dbgl = 2
    dbgm = 3
    dbgn = 4
    dbgo = 5
    dbgp = 6
    dbgq = 7
    dbgr = 8
    dbgs = 9
    dbgt = 10
    dbgu = 11
    dbgv = 12
    dbgw = 13
    dbgx = 14
    dbgy = 15
    dbgz = 53
    dbha = 61
    dbhb = 62
    dbhc = 99
    dbhd = 100

# .dmp
class dmp(IntFlag):
    dbhe = 0
    dbhf = 1
    dbhg = 2
    dbhh = 3
    dbhi = 4
    dbhj = 5

# .dmq
class dmq(IntFlag):
    dbhk = 0
    dbhl = 1
    dbhm = 2

# .dmr
class dmr(IntFlag):
    dbhn = 0
    dbho = 1
    dbhp = 2

# .dms
class dms(IntFlag):
    dbhq = 0
    dbhr = 1

# .dmt
class dmt(IntFlag):
    dbhs = 0
    dbht = 1
    dbhu = 2

# .dmu
class dmu(IntFlag):
    dbhv = 0
    dbhw = 1
    dbhx = 2

# .dmv
class dmv(IntFlag):
    dbhy = 0
    dbhz = 1
    dbia = 2
    dbib = 3
    dbic = 4
    dbid = 5
    dbie = 6
    dbif = 7
    dbig = 8

# .dmw
class dmw(IntFlag):
    dbih = 0
    dbii = 1
    dbij = 2
    dbik = 3

# .dmx
class dmx(IntFlag):
    dbil = 0
    dbim = 1
    dbin = 2

# .dmy
class dmy(IntFlag):
    dbio = 1
    dbip = 2
    dbiq = 3
    dbir = 4

# .dmz
class dmz(IntFlag):
    dbis = 0
    dbit = 1
    dbiu = 2
    dbiv = 3
    dbiw = 4
    dbix = 5
    dbiy = 6
    dbiz = 7
    dbja = 8
    dbjb = 9
    dbjc = 10
    dbjd = 11

# .dnb
class dnb(IntFlag):
    dbje = 0
    dbjf = 1
    dbjg = 2
    dbjh = 3
    dbji = 4
    dbjj = 5
    dbjk = 6
    dbjl = 7
    dbjm = 8
    dbjn = 9
    dbjo = 10
    dbjp = 11

# .dnc
class dnc(IntFlag):
    dbjq = 1
    dbjr = 2

# .dnd
class dnd(IntFlag):
    dbjs = -1
    dbjt = 0
    dbju = 1
    dbjv = 2
    dbjw = 3
    dbjx = 4
    dbjy = 5
    dbjz = 6
    dbka = 7
    dbkb = 8
    dbkc = 9
    dbkd = 10

# .dne
class dne(IntFlag):
    dbke = 0
    dbkf = 1
    dbkg = 2
    dbkh = 3
    dbki = 4
    dbkj = 5
    dbkk = 6
    dbkl = 7
    dbkm = 8
    dbkn = 9
    dbko = 10
    dbkp = 11
    dbkq = 12

# .dnf
class dnf(IntFlag):
    dbkr = 0
    dbks = 1

# .dng
class dng(IntFlag):
    dbkt = 0
    dbku = 1
    dbkv = 2

# .dnh
class dnh(IntFlag):
    dbkw = 0
    dbkx = 1
    dbky = 2
    dbkz = 3
    dbla = 4
    dblb = 5
    dblc = 6
    dbld = 7
    dble = 8
    dblf = 9
    dblg = 10
    dblh = 11
    dbli = 12

# .dni
class dni(IntFlag):
    dblj = 0
    dblk = 1
    dbll = 2
    dblm = 3
    dbln = 4

# .dnj
class dnj(IntFlag):
    dblo = 0
    dblp = 1
    dblq = 2
    dblr = 3
    dbls = 4

# .dnk
class dnk(IntFlag):
    dblt = 0
    dblu = 1
    dblv = 2

# .dnl
class dnl(IntFlag):
    dblw = -1
    dblx = 0
    dbly = 1
    dblz = 2
    dbma = 3
    dbmb = 4
    dbmc = 5
    dbmd = 6
    dbme = 7
    dbmf = 8
    dbmg = 9
    dbmh = 10
    dbmi = 11
    dbmj = 12
    dbmk = 13
    dbml = 14
    dbmm = 15
    dbmn = 16
    dbmo = 17
    dbmp = 18
    dbmq = 19
    dbmr = 20
    dbms = 21
    dbmt = 22
    dbmu = 23

# .dnm
class dnm(IntFlag):
    dbmv = 0
    dbmw = 1
    dbmx = 2
    dbmy = 3
    dbmz = 4
    dbna = 5
    dbnb = 6
    dbnc = 7
    dbnd = 8
    dbne = 9
    dbnf = 10
    dbng = 11
    dbnh = 12
    dbni = 13
    dbnj = 14
    dbnk = 15
    dbnl = 16
    dbnm = 17
    dbnn = 18
    dbno = 20

# .dnn
class dnn(IntFlag):
    dbnp = 0
    dbnq = 1
    dbnr = 2

# .dno
class dno(IntFlag):
    dbns = 0
    dbnt = 1
    dbnu = 2

# .dnp
class dnp(IntFlag):
    dbnv = 0
    dbnw = 1
    dbnx = 2
    dbny = 99

# .dnq
class dnq(IntFlag):
    dbnz = 0
    dboa = 1
    dbob = 2
    dboc = 3
    dbod = 4

# .dnr
class dnr(IntFlag):
    dboe = 0
    dbof = 1
    dbog = 2
    dboh = 3

# .dns
class dns(IntFlag):
    dboi = 0
    dboj = 1
    dbok = 2
    dbol = 3
    dbom = 4

# .dnt
class dnt(IntFlag):
    dbon = 0
    dboo = 1
    dbop = 2
    dboq = 3
    dbor = 4
    dbos = 5

# .dnu
class dnu(IntFlag):
    dbot = -1
    dbou = 0
    dbov = 1

# .dnv
class dnv(IntFlag):
    dbow = 0
    dbox = 1
    dboy = 2
    dboz = 3
    dbpa = 4
    dbpb = 5
    dbpc = 6
    dbpd = 7
    dbpe = 8
    dbpf = 9

# .dnw
class dnw(IntFlag):
    dbpg = 0
    dbph = 1

# .dnx
class dnx(IntFlag):
    dbpi = -1
    dbpj = 0
    dbpk = 1
    dbpl = 2
    dbpm = 3

# .dnz
class dnz(IntFlag):
    dbtc = 0
    dbtd = 1
    dbte = 2
    dbtf = 3

# .doa
class doa(IntFlag):
    dbtg = -1
    dbth = 0
    dbti = 1
    dbtj = 2

# .dob
class dob(IntFlag):
    dbtk = 0
    dbtl = 1
    dbtm = 2
    dbtn = 3
    dbto = 4
    dbtp = 5

# .doc
class doc(IntFlag):
    dbtq = 1
    dbtr = 2
    dbts = 3
    dbtt = 4
    dbtu = 5
    dbtv = 6
    dbtw = 7
    dbtx = 8
    dbty = 9

# .dod
class dod(IntFlag):
    dbtz = 0
    dbua = 1
    dbub = 2
    dbuc = 3
    dbud = 4

# .doe
class doe(IntFlag):
    dbue = 0
    dbuf = 1
    dbug = 3
    dbuh = 4
    dbui = 5
    dbuj = 6
    dbuk = 7

# .dof
class dof(IntFlag):
    dbul = 0
    dbum = 1

# .dog
class dog(IntFlag):
    dbun = 0
    dbuo = 1

# .doh
class doh(IntFlag):
    dbup = 0
    dbuq = 1
    dbur = 2

# .doi
class doi(IntFlag):
    dbus = 78
    dbut = 79
    dbuu = 80
    dbuv = 81
    dbuw = 82
    dbux = 83
    dbuy = 84
    dbuz = 85
    dbva = 86
    dbvb = 87
    dbvc = 88
    dbvd = 89
    dbve = 90
    dbvf = 91
    dbvg = 92
    dbvh = 93
    dbvi = 94
    dbvj = 95
    dbvk = 96
    dbvl = 97
    dbvm = 98
    dbvn = 99
    dbvo = 100
    dbvp = 101
    dbvq = 102
    dbvr = 103
    dbvs = 104
    dbvt = 105
    dbvu = 106
    dbvv = 107
    dbvw = 108
    dbvx = 109
    dbvy = 110
    dbvz = 111
    dbwa = 112
    dbwb = 113
    dbwc = 114
    dbwd = 115
    dbwe = 116
    dbwf = 151
    dbwg = 152
    dbwh = 544
    dbwi = 546
    dbwj = 547
    dbwk = 549
    dbwl = 550
    dbwm = 545
    dbwn = 548

# .doj
class doj(IntFlag):
    dbwo = -1
    dbwp = 0
    dbwq = 2
    dbwr = 3
    dbws = 4

# .dok
class dok(IntFlag):
    dbwt = 0
    dbwu = 1
    dbwv = 2
    dbww = 3
    dbwx = 4
    dbwy = 6
    dbwz = 8
    dbxa = 9
    dbxb = 10
    dbxc = 11
    dbxd = 12
    dbxe = 13
    dbxf = 14

# .dom
class dom(IntFlag):
    dbxh = 0
    dbxi = 1
    dbxj = 2
    dbxk = 3
    dbxl = 4
    dbxm = 5

# .don
class don(IntFlag):
    dbxn = 0
    dbxo = 1
    dbxp = 2
    dbxq = 3
    dbxr = 4

# .doo
class doo(IntFlag):
    dbxs = -1
    dbxt = 0
    dbxu = 1
    dbxv = 2
    dbxw = 3
    dbxx = 4
    dbxy = 5
    dbxz = 6
    dbya = 7
    dbyb = 9
    dbyc = 10
    dbyd = 11
    dbye = 12
    dbyf = 13

# .dop
class dop(IntFlag):
    dbyg = 0
    dbyh = 1
    dbyi = 2

# .doq
class doq(IntFlag):
    dbyj = 0
    dbyk = 1
    dbyl = 2
    dbym = 3
    dbyn = 4
    dbyo = 5
    dbyp = 6

# .dor
class dor(IntFlag):
    dbyq = 0
    dbyr = 1
    dbys = 2
    dbyt = 3
    dbyu = 4
    dbyv = 5
    dbyw = 6

# .dos
class dos(IntFlag):
    dbyx = 0
    dbyy = 1
    dbyz = 2

# .dot
class dot(IntFlag):
    dbza = 0
    dbzb = 1
    dbzc = 2
    dbzd = 3
    dbze = 4
    dbzf = 5

# .dou
class dou(IntFlag):
    dbzg = 0
    dbzh = 1
    dbzi = 2
    dbzj = 3
    dbzk = 4
    dbzl = 5

# .dov
class dov(IntFlag):
    dbzm = 0
    dbzn = 1
    dbzo = 2

# .dow
class dow(IntFlag):
    dbzp = 0
    dbzq = 1

# .dox
class dox(IntFlag):
    dbzr = 0
    dbzs = 1
    dbzt = 2

# .doy
class doy(IntFlag):
    dbzu = 0
    dbzv = 1
    dbzw = 2
    dbzx = 3
    dbzy = 4
    dbzz = 5
    dcaa = 6
    dcab = 7
    dcac = 8
    dcad = 9
    dcae = 10
    dcaf = 11
    dcag = 12
    dcah = 13

# .doz
class doz(IntFlag):
    dcai = 0
    dcaj = 1
    dcak = 2
    dcal = -1

# .dpb
class dpb(IntFlag):
    dcaw = 0
    dcax = 1
    dcay = 2
    dcaz = 3

# .dpc
class dpc(IntFlag):
    dcba = 0
    dcbb = 1
    dcbc = 2
    dcbd = 3
    dcbe = 4
    dcbf = 5
    dcbg = 6
    dcbh = 7
    dcbi = 8
    dcbj = 9
    dcbk = 10
    dcbl = 11
    dcbm = 12
    dcbn = 13
    dcbo = 14
    dcbp = 15
    dcbq = 16
    dcbr = 17
    dcbs = 18
    dcbt = 19
    dcbu = 20

# .dpd
class dpd(IntFlag):
    dcbv = 0
    dcbw = 1
    dcbx = 2

# .dpe
class dpe(IntFlag):
    dcby = 0
    dcbz = 1

# .dpf
class dpf(IntFlag):
    dcca = 0
    dccb = 1
    dccc = 2
    dccd = 4
    dcce = 8
    dccf = 16
    dccg = 32

# .dpg
class dpg(IntFlag):
    dcch = 1
    dcci = 2
    dccj = 3
    dcck = 4
    dccl = 5
    dccm = 6
    dccn = 7
    dcco = 8
    dccp = 9
    dccq = 10
    dccr = 11
    dccs = 12
    dcct = 13
    dccu = 15
    dccv = 16
    dccw = 17
    dccx = 18
    dccy = 19
    dccz = 21

# .dph
class dph(IntFlag):
    dcda = 0
    dcdb = 1
    dcdc = 2
    dcdd = 3

# .dpi
class dpi(IntFlag):
    dcde = 0
    dcdf = 1
    dcdg = 2
    dcdh = 3

# .dpj
class dpj(IntFlag):
    dcdi = 0
    dcdj = 1
    dcdk = 2
    dcdl = 3
    dcdm = 4
    dcdn = 5
    dcdo = 6

# .dpk
class dpk(IntFlag):
    dcdp = 0
    dcdq = 1
    dcdr = 2

# .dpl
class dpl(IntFlag):
    dcds = 1
    dcdt = 2
    dcdu = 3
    dcdv = 4
    dcdw = 5
    dcdx = 6
    dcdy = 7
    dcdz = 8
    dcea = 10
    dceb = 13
    dcec = 14
    dced = 15
    dcee = 20
    dcef = 21
    dceg = 23
    dceh = 24
    dcei = 25
    dcej = 26
    dcek = 27
    dcel = 38
    dcem = 39
    dcen = 40
    dceo = 41

# .dpm
class dpm(IntFlag):
    dcep = 0
    dceq = 1
    dcer = 2
    dces = 4
    dcet = 8
    dceu = 16
    dcev = 32
    dcew = 64
    dcex = 128
    dcey = 256

# .dpn
class dpn(IntFlag):
    dcez = 0
    dcfa = 1
    dcfb = 2
    dcfc = 3

# .dpo
class dpo(IntFlag):
    dcfd = 0
    dcfe = 1
    dcff = 2
    dcfg = 3
    dcfh = 4
    dcfi = 5
    dcfj = 6

# .dpp
class dpp(IntFlag):
    dcfk = 0
    dcfl = 1
    dcfm = 2

# .dpq
class dpq(IntFlag):
    dcfn = 0
    dcfo = 2
    dcfp = 3
    dcfq = 4
    dcfr = 5
    dcfs = 6

# .dpr
class dpr(IntFlag):
    dcft = 0
    dcfu = 1
    dcfv = 2
    dcfw = 3
    dcfx = 4
    dcfy = 5
    dcfz = 6
    dcga = 7

# .dps
class dps(IntFlag):
    dcgb = 0
    dcgc = 1

# .dpt
class dpt(IntFlag):
    dcgd = 0
    dcge = 1
    dcgf = 2
    dcgg = 3

# .dpu
class dpu(IntFlag):
    dcgh = 0
    dcgi = 1
    dcgj = 2
    dcgk = 3
    dcgl = 4
    dcgm = 5
    dcgn = 6
    dcgo = 7
    dcgp = 8
    dcgq = 9
    dcgr = 10
    dcgs = 11

# .dpv
class dpv(IntFlag):
    dcgt = 0
    dcgu = 1
    dcgv = 2

# .dpw
class dpw(IntFlag):
    dcgw = 0
    dcgx = 1
    dcgy = 2

# .dpx
class dpx(IntFlag):
    dcgz = 0
    dcha = 1
    dchb = 2
    dchc = 3
    dchd = 4
    dche = 5
    dchf = 6
    dchg = 7
    dchh = 8

# .dpy
class dpy(IntFlag):
    dchi = 0
    dchj = 1
    dchk = 2
    dchl = 3
    dchm = 4

# .dpz
class dpz(IntFlag):
    dchn = 0
    dcho = 1
    dchp = 2

# .dqa
class dqa(IntFlag):
    dchq = 0
    dchr = 1
    dchs = 2
    dcht = 3

# .dqb
class dqb(IntFlag):
    dchu = 0
    dchv = 1

# .dqc
class dqc(IntFlag):
    dchw = 0
    dchx = 1
    dchy = 2
    dchz = 3
    dcia = 4
    dcib = 5
    dcic = 6
    dcid = 7
    dcie = 8
    dcif = 9
    dcig = 10
    dcih = 11
    dcii = 12
    dcij = 13

# .dqd
class dqd(IntFlag):
    dcik = -1
    dcil = 0
    dcim = 1
    dcin = 2
    dcio = 3
    dcip = 4
    dciq = 5
    dcir = 6
    dcis = 7
    dcit = 8
    dciu = 9
    dciv = 10
    dciw = 11
    dcix = 12
    dciy = 13
    dciz = 14
    dcja = 15
    dcjb = 16
    dcjc = 17
    dcjd = 18
    dcje = 19
    dcjf = 20
    dcjg = 21
    dcjh = 22
    dcji = 23
    dcjj = 24
    dcjk = 25

# .dqe
class dqe(IntFlag):
    dcjl = 1
    dcjm = 2
    dcjn = 4
    dcjo = 8
    dcjq = 0

# .dqf
class dqf(IntFlag):
    dcjr = 0
    dcjs = 1
    dcjt = 2
    dcju = 3
    dcjv = 4
    dcjw = 5

# .dqg
class dqg(IntFlag):
    dcjx = 1
    dcjy = 3
    dcjz = 4
    dcka = 5
    dckb = 9
    dckc = 10
    dckd = 11
    dcke = 15
    dckf = 16

# .dqh
class dqh(IntFlag):
    dckg = 0
    dckh = 1
    dcki = 2
    dckj = 3
    dckk = 4

# .dqi
class dqi(IntFlag):
    dckl = 0
    dckm = 1
    dckn = 2
    dcko = 5
    dckp = 6

# .dqj
class dqj(IntFlag):
    dckq = 0
    dckr = 1
    dcks = 2

# .dqk
class dqk(IntFlag):
    dckt = 0
    dcku = 1
    dckv = 2

# .dqm
class dqm(IntFlag):
    dckw = 0
    dckx = 1
    dcky = 2
    dckz = 4
    dcla = 8
    dclb = 16
    dclc = 32
    dcld = 64
    dcle = 128
    dclf = 256
    dclg = 512
    dclh = 1024
    dcli = 2048

# .dqz
class dqz(IntFlag):
    dclj = 0

# .dqz
class dqz(IntFlag):
    dclk = 0
    dcll = 1
    dclm = 2
    dcln = 3
    dclo = 4
    dclp = 5
    dclq = 6
    dclr = 7
    dcls = 8
    dclt = 9

# .dqz
class dqz(IntFlag):
    dclu = 0
    dclv = 1
    dclw = 2
    dclx = 3
    dcly = 4
    dclz = 5
    dcma = 6
    dcmb = 7
    dcmc = 8
    dcmd = 9
    dcme = 10
    dcmf = 11
    dcmg = 12
    dcmh = 13
    dcmi = 14
    dcmj = 15
    dcmk = 16
    dcml = 17
    dcmm = 18
    dcmn = 19
    dcmo = 20
    dcmp = 21
    dcmq = 22

# .dqz
class dqz(IntFlag):
    dcmr = 0
    dcms = 1
    dcmt = 2
    dcmu = 3
    dcmv = 4
    dcmw = 5
    dcmx = 6

# .dqz
class dqz(IntFlag):
    dcmy = 0

# .dqz
class dqz(IntFlag):
    dcmz = 0
    dcna = 1
    dcnb = 2
    dcnc = 3
    dcnd = 4
    dcne = 5
    dcnf = 6
    dcng = 7
    dcnh = 8
    dcni = 9
    dcnj = 10
    dcnk = 11
    dcnl = 12
    dcnm = 13
    dcnn = 14
    dcno = 15
    dcnp = 16
    dcnq = 17
    dcnr = 18
    dcns = 19
    dcnt = 20
    dcnv = 21
    dcnw = 22
    dcnx = 23
    dcny = 24
    dcnz = 25

# .dqz
class dqz(IntFlag):
    dcoa = 0
    dcob = 1
    dcoc = 2

# .dqz
class dqz(IntFlag):
    dcod = 0
    dcoe = 1
    dcof = 2
    dcog = 3
    dcoh = 4
    dcoi = 5
    dcoj = 6
    dcok = 7
    dcol = 8
    dcom = 9
    dcon = 10
    dcoo = 11
    dcop = 12
    dcoq = 13
    dcor = 14
    dcos = 15
    dcot = 16

# .dqz
class dqz(IntFlag):
    dcou = 0
    dcov = 1

# .dqz
class dqz(IntFlag):
    dcow = 0

# .dqz
class dqz(IntFlag):
    dcox = 0

# .dqz
class dqz(IntFlag):
    dcoy = 0
    dcoz = 1
    dcpa = 2
    dcpb = 3
    dcpc = 4
    dcpd = 5
    dcpe = 6
    dcpf = 7

# .dra
class dra(IntFlag):
    dcpg = -1
    dcph = 0
    dcpi = 1
    dcpj = 2

# .drb
class drb(IntFlag):
    dcpk = 0
    dcpl = 1
    dcpm = 2
    dcpn = 3
    dcpo = 4
    dcpp = 5
    dcpq = 6

# .dsv
class dsv(IntFlag):
    Resources = 0
    Equipment = 1

# .dsv
class dsv(IntFlag):
    Spells = 0
    Title = 1
    ForgettableSpells = 2
    Bestiary = 3
    Alignment = 4
    Companion = 5
    Jobs = 6
    Achievement = 7
    Calendar = 8
    Quest = 9

# .dsv
class dsv(IntFlag):
    Equipment = 0
    Resource = 1
    Consumable = 2

# .dsv
class dsv(IntFlag):
    House = 0
    Paddocks = 1

# .dul
class dul(IntFlag):
    ddhg = 1
    ddhh = 2

# .duz
class duz(IntFlag):
    ddmn = 0
    ddmo = 1
    ddmp = 2
    ddmq = 4
    ddmr = 8
    ddms = 16
    ddmt = 32
    ddmu = 64
    ddmv = 128
    ddmw = 256

# .dyc
class dyc(IntFlag):
    demu = 0
    demv = 1

# .dz
class dz(IntFlag):
    ctwg = 0
    ctwh = 1
    ctwi = 2
    ctwj = 3
    ctwk = 4
    ctwl = 5
    ctwm = 6
    ctwn = 7
    ctwo = 8

# .dz
class dz(IntFlag):
    ctwp = 0
    ctwq = 1
    ctwr = 2
    ctws = 3
    ctwt = 4
    ctwu = 5
    ctwv = 6
    ctww = 7
    ctwx = 8
    ctwy = 9
    ctwz = 10
    ctxa = 11
    ctxb = 12
    ctxc = 13
    ctxd = 14
    ctxe = 15
    ctxf = 16
    ctxg = 17
    ctxh = 18
    ctxi = 19

# .dzf
class dzf(IntFlag):
    deqo = 0
    deqp = 1
    deqq = 2
    deqr = 3
    deqs = 4

# .dzx
class dzx(IntFlag):
    deux = 0
    deuy = 1
    deuz = 2
    deva = 3

# .eas
class eas(IntFlag):
    devb = 1
    devc = 2
    devd = 3
    deve = 4

# .eas
class eas(IntFlag):
    devf = 0
    devg = 1
    devh = 2

# .eas
class eas(IntFlag):
    devi = 0
    devj = 1
    devk = 2

# .ebi
class ebi(IntFlag):
    dfhk = -1
    dfhl = 0
    dfhm = 1
    dfhn = 2
    dfho = 3
    dfhp = 4
    dfhq = 5
    dfhr = 6
    dfhs = 7
    dfht = 8
    dfhu = 10
    dfhv = 11
    dfhw = 12
    dfhx = 13
    dfhy = 14
    dfhz = 15
    dfia = 16
    dfib = 17
    dfic = 18
    dfid = 19
    dfie = 20
    dfif = 21
    dfig = 22
    dfih = 23
    dfii = 24
    dfij = 25
    dfik = 26
    dfil = 27
    dfim = 28
    dfin = 29
    dfio = 30
    dfip = 31
    dfiq = 32

# .ebj
class ebj(IntFlag):
    dfir = 0
    dfis = 1
    dfit = 2
    dfiu = 3
    dfiv = 4
    dfiw = 5
    dfix = 6
    dfiy = 7
    dfiz = 8
    dfja = 9

# .ebq
class ebq(IntFlag):
    dfjb = 1
    dfjc = 2
    dfjd = 3
    dfje = 4
    dfjf = 5

# .eck
class eck(IntFlag):
    dfqg = 0
    dfqh = 1

# .edd
class edd(IntFlag):
    dfyj = 0
    dfyk = 1
    dfyl = 2
    dfym = 3

# .ede
class ede(IntFlag):
    dfzg = 0
    dfzh = 1
    dfzi = 2
    dfzj = 3

# .edf
class edf(IntFlag):
    dfzk = 0
    dfzl = 1
    dfzm = 2
    dfzn = 3

# .edi
class edi(IntFlag):
    dfzx = 0
    dfzy = 1
    dfzz = 2
    dgaa = 3
    dgab = 4
    dgac = 5
    dgad = 6
    dgae = 7
    dgaf = 8
    dgag = 9
    dgah = 10
    dgai = 11
    dgaj = 12
    dgak = 13

# .edk
class edk(IntFlag):
    dgam = 0
    dgan = 1

# .edn
class edn(IntFlag):
    dgay = 0
    dgaz = 1
    dgba = 2
    dgbb = 3
    dgbc = 4
    dgbd = 5
    dgbe = 6

# .eei
class eei(IntFlag):
    dgrx = 3
    dgry = 4
    dgrz = 5
    dgsa = 7
    dgsb = 8
    dgsc = 668
    dgsd = 669
    dgse = 670
    dgsf = 671
    dgsg = 672
    dgsh = 673
    dgsi = 676
    dgsj = 684
    dgsk = 700
    dgsl = 707
    dgsm = 713
    dgsn = 726
    dgso = 729
    dgsp = 730
    dgsq = 752

# .eej
class eej(IntFlag):
    dgsr = 0
    dgss = 1
    dgst = 2
    dgsu = 3
    dgsv = 4
    dgsw = 5
    dgsx = 6
    dgsy = 7
    dgsz = 8
    dgta = 9
    dgtb = 10
    dgtc = 11
    dgtd = 12
    dgte = 13
    dgtf = 14
    dgtg = 15
    dgth = 16

# .eew
class eew(IntFlag):
    dguq = 2
    dgur = 3
    dgus = 4
    dgut = 7
    dguu = 9

# .eez
class eez(IntFlag):
    dguz = 0
    dgva = 1
    dgvb = 2
    dgvc = 3
    dgvd = 4
    dgve = 5
    dgvf = 6
    dgvg = 7
    dgvh = 8
    dgvi = 9
    dgvj = 10
    dgvk = 11
    dgvl = 12
    dgvm = 13
    dgvn = 14
    dgvo = 15
    dgvp = 16
    dgvq = 17
    dgvr = 18
    dgvs = 19
    dgvt = 20
    dgvu = 21
    dgvv = 22
    dgvw = 23
    dgvx = 24
    dgvy = 25
    dgvz = 26
    dgwa = 27
    dgwb = 28
    dgwc = 29
    dgwd = 30
    dgwe = 31
    dgwf = 32
    dgwg = 33
    dgwh = 34

# .eft
class eft(IntFlag):
    dhdn = 0
    dhdo = 1

# .efz
class efz(IntFlag):
    dhgb = 0
    dhgc = 1
    dhgd = 2
    dhge = 3

# .ega
class ega(IntFlag):
    dhgf = 0
    dhgg = 1
    dhgh = 2

# .egb
class egb(IntFlag):
    dhgi = 0
    dhgj = 1
    dhgk = 2
    dhgl = 3
    dhgm = 4

# .egk
class egk(IntFlag):
    dhjo = 0
    dhjp = 1
    dhjq = 2

# .egm
class egm(IntFlag):
    dhkf = 0
    dhkg = 1
    dhkh = 2
    dhki = 3
    dhkj = 4
    dhkk = 5

# .ehy
class ehy(IntFlag):
    dhug = 0
    dhuh = 1
    dhui = 2
    dhuj = 4
    dhuk = 8
    dhul = 255

# .eil
class eil(IntFlag):
    dhxp = 0
    dhxq = 1
    dhxr = 2
    dhxs = 3
    dhxt = 4

# .eis
class eis(IntFlag):
    dhyl = 0
    dhym = 1

# .eji
class eji(IntFlag):
    diby = -1
    dibz = 0
    dica = 1
    dicb = 2
    dicc = 3

# .ek
class ek(IntFlag):
    ctzw = 0
    ctzx = 1
    ctzy = 2
    ctzz = 3

# .eke
class eke(IntFlag):
    diin = 0
    diio = 1
    diip = 2

# .ekf
class ekf(IntFlag):
    diiq = 0
    diir = 1
    diis = 2
    diit = 3
    diiu = 4
    diiv = 5
    diiw = 6
    diix = 7
    diiy = 8
    diiz = 9
    dija = 10
    dijb = 11
    dijc = 12
    dijd = 13
    dije = 14
    dijf = 15
    dijg = 16
    dijh = 17
    diji = 18

# .ekr
class ekr(IntFlag):
    dily = -1
    dilz = 0
    dima = 1
    dimb = 2

# .eks
class eks(IntFlag):
    dimc = 0
    dimd = 1
    dime = 2
    dimf = 3

# .ekt
class ekt(IntFlag):
    dimg = 0
    dimh = 1

# .elb
class elb(IntFlag):
    diok = 3
    diol = 4
    diom = 5

# .eln
class eln(IntFlag):
    divm = 0
    divn = 1
    divo = 2
    divp = 3

# .enf
class enf(IntFlag):
    djcq = 0
    djcr = 1
    djcs = 2

# .eng
class eng(IntFlag):
    djct = 82
    djcu = 83
    djcv = 477
    djcw = 493

# .eny
class eny(IntFlag):
    djcx = 0
    djcy = 1
    djcz = 2
    djda = 3
    djdb = 4

# .eoa
class eoa(IntFlag):
    djdc = 0
    djdd = 1

# .eoe
class eoe(IntFlag):
    djde = -1
    djdf = 0
    djdg = 1
    djdh = 2
    djdi = 3

# .eov
class eov(IntFlag):
    djdq = 0

# .eov
class eov(IntFlag):
    djdr = 0
    djds = 1
    djdt = 2
    djdu = 3

# .eoy
class eoy(IntFlag):
    ReadingBook = 0
    Scroll = 1
    ImageScroll = 2

# .epj
class epj(IntFlag):
    FightResultSimple = 0
    FightResult = 1
    EndTurnWidget = 2
    timeline = 3
    UIChallengeSelectionDisplay = 4
    BuffsUI = 5
    fighterInfo = 6
    playerTurnStart = 7
    newTurnStart = 8
    CompanionSlaveFightUI = 9
    SummonedSlaveFightUI = 10
    MonsterSlaveFightUI = 11
    SpellPicker = 12
    UIChallengeChoiceDisplay = 13
    UIChallengeSettingsDisplay = 14
    FighterInfoPlacementUI = 15
    WorldBossUi = 16
    PingWheel = 17

# .eqq
class eqq(IntFlag):
    djdv = 0
    djdw = 1
    djdx = 2

# .erg
class erg(IntFlag):
    djdy = 0
    djdz = -1
    djea = 1
    djeb = 2

# .erh
class erh(IntFlag):
    djec = 0
    djed = 1
    djee = 2
    djef = 3

# .erk
class erk(IntFlag):
    djeg = 0
    djeh = 1
    djei = 2
    djej = 3
    djek = 4
    djel = 5
    djem = 6
    djen = 7
    djeo = 8
    djep = 9
    djeq = 10

# .esx
class esx(IntFlag):
    djex = 0
    djey = 1
    djez = 2
    djfa = 3

# .ete
class ete(IntFlag):
    djfb = 2
    djfc = 46
    djfd = 56
    djfe = 69
    djff = 70
    djfg = 74
    djfh = 84
    djfi = 77
    djfj = 106

# .etf
class etf(IntFlag):
    AdminItemSelection = 0

# .eth
class eth(IntFlag):
    Login = 0
    ServerSelection = 1
    CharacterSelection = 2
    CharacterCreation = 3
    PreGameMenu = 4
    SecretPopup = 5
    PseudoChoice = 6
    CharacterHeader = 7
    ConnectionBackground = 8
    OptionLoadingError = 9

# .etj
class etj(IntFlag):
    BugReporter = 0

# .etk
class etk(IntFlag):
    CalendarUi = 0
    AlmanaxEventDetails = 1
    SeasonalEventDetails = 2
    WorldEventDetails = 3
    DungeonRusherDetails = 4

# .etm
class etm(IntFlag):
    StatSheet = 0
    StatBoostSheet = 1
    StatBoostMinimized = 2
    Alignment = 3
    CharacterPresets = 4
    Reward = 5
    RewardMinimized = 6
    WorldEventReward = 7
    LadderRewardTable = 8
    StatBoostSheetPreset = 9
    StatBoostPresetMinimized = 10
    CharaModification = 11
    CharacModificationBackground = 12
    Rename = 13

# .etr
class etr(IntFlag):
    Exchange = 0
    ExchangeNPCUI = 1
    Recycle = 2

# .ets
class ets(IntFlag):
    NONE = 0
    GaugeCharacter = 1
    GaugeGuild = 2
    GaugeMount = 4
    GaugeHonorPoints = 8
    GaugePods = 16
    GaugeEnergyPoints = 32
    GaugeJobAlchemist = 64
    GaugeJobLumberjack = 128
    GaugeJobHunter = 256
    GaugeJobMiner = 512
    GaugeJobFarmer = 1024
    GaugeJobFisherman = 2048
    GaugeJobJeweler = 4096
    GaugeJobHandyman = 8192
    GaugeJobShoemaker = 16384
    GaugeJobArtificer = 32768
    GaugeJobSmith = 65536
    GaugeJobCarver = 131072
    GaugeJobTailor = 262144
    GaugeJobShoemagus = 524288
    GaugeJobCostumagus = 1048576
    GaugeJobCraftmagus = 2097152
    GaugeJobSmithmagus = 4194304
    GaugeJobJewelmagus = 8388608
    GaugeJobCarvmagus = 16777216

# .ett
class ett(IntFlag):
    EncyclopediaBase = 0
    PlayerSpell = 1
    ModsterBase = 2
    ForgettableSpellSetCreationPopup = 3
    ForgettableSpellSetListPopup = 4
    RemoveForgettablePopup = 5
    Quests = 6
    Achievements = 7
    Expeditions = 8

# .etu
class etu(IntFlag):
    GuideBase = 0

# .etw
class etw(IntFlag):
    HavenbagManager = 0
    HavenbagFurnituresTypes = 1

# .etx
class etx(IntFlag):
    HouseUI = 0
    HouseGuildManager = 1
    HouseSalePopup = 2
    HouseEstateUI = 3

# .etz
class etz(IntFlag):
    Tracking = 0
    Shop = 1
    DropTable = 2
    Bestiary = 3
    RerollPopup = 4
    CreateNewPopup = 5
    Hub = 6
    Map = 7
    SpellBar = 8
    Result = 9

# .eua
class eua(IntFlag):
    ItemRecipes = 0
    JobUI = 1

# .euf
class euf(IntFlag):
    GameMenu = 0
    Latency = 1

# .euh
class euh(IntFlag):
    MountPaddock = 0
    MountInfo = 1
    MountAncestors = 2
    PaddockSellBuy = 3

# .eui
class eui(IntFlag):
    PauseMenu = 0
    PayZone = 1
    OptionBase = 2
    ModalCover = 3
    QualitySelection = 4
    ColorPicker = 5

# .euj
class euj(IntFlag):
    JoinParty = 0
    EndSeasonReward = 1
    Companions = 2
    PartyDisplay = 3
    PvpArenaBase = 4
    KisWarning = 5
    KisInfraction = 6
    KisPreventSanction = 7
    SurrenderPopup = 8

# .euk
class euk(IntFlag):
    CharacterInformations = 0
    ActionBar = 1
    BannerMenu = 2
    CartographyBanner = 3
    MapInfo = 4
    Chat = 5
    QuestList = 6
    Smiley = 7
    InternalNotification = 8
    BigInternalNotification = 9
    CartographyMap = 10
    CartographySearch = 11
    Alteration = 12
    PreviewAlteration = 13
    ActionBar1 = 14
    ActionBar2 = 15
    ActionBar3 = 16
    ActionBar4 = 17
    ActionBar5 = 18
    ActionBar6 = 19
    ActionBar7 = 20
    ActionBar8 = 21
    WidgetManager = 22

# .eun
class eun(IntFlag):
    LevelUp = 0
    SpectatorUi = 1
    TreasureHunt = 2
    AllianceAvA = 3
    LegendaryHunts = 4
    Alignment = 5
    CinematicPlayer = 7
    FightMapPreview = 8
    HardcoreDeath = 9

# .euo
class euo(IntFlag):
    ReportUI = 0
    AddFriend = 1
    SocialBaseUI = 2
    SpouseUI = 3
    GuildApplyUI = 4
    GuildJoinUi = 5
    AllianceJoinUi = 6
    AllianceApplyUi = 7
    EditNote = 8
    GuildPresentationUI = 9
    AlliancePresentationUI = 10
    LadderUI = 11
    CollectorLootDetail = 12
    TopTaxCollectorsUI = 13
    GuildRightsAndRanksUI = 14
    GuildPaddockInfoUI = 15
    GuildHouseManager = 16
    GuildCreateRankUi = 17
    GuildModifyRankUi = 18
    GuildRemoveRankUi = 19
    GuildApplicationsUi = 20
    AllianceApplicationsUi = 21
    GuildMemberRightsUi = 22
    AllianceMemberRightsUi = 23
    AllianceRightsAndRanksUi = 24
    CreateRankUi = 25
    ModifyRankUi = 26
    RemoveRankUi = 27
    TaxCollectorEquipmentModify = 28
    TaxCollectorEquipmentConsult = 29
    AllianceNuggetValidPopup = 30
    GuildCreatorUi = 31
    AllianceCreatorUi = 32
    GuildMissionTierOption = 33
    GuildMissionRanksAndCategoriesOption = 34
    GuildLevelRewardsUi = 35
    GuildMissionSubscribers = 36
    GuildContributionUi = 37
    GuildActivityRewards = 38
    GuildShopUi = 39
    GuildShopConfirmBuyPopup = 40

# .euq
class euq(IntFlag):
    NONE = -1
    Spells = 0
    SpecialSpells = 1
    ForgettableSpellsTab = 3

# .eus
class eus(IntFlag):
    Bank = 0
    Equipment = 1
    ItemList = 2
    LivingObjectSkinList = 3
    StorableItemGrid = 4
    StorableItemList = 5
    ItemsSet1 = 6
    ItemsSet2 = 7
    ItemsSet3 = 8
    ItemsSet4 = 9
    ItemsSet5 = 10
    ItemsSet6 = 11
    ItemsSet7 = 12
    ItemsSet8 = 13
    ItemsSet9 = 14
    ItemsSet10 = 15
    Mimicry = 16
    LivingObject = 17
    LivingObjectLook = 18
    WatchEquipment = 19
    Stock = 20
    Mount = 21
    ExchangeInventory = 22
    GuildChest = 23
    GuildChestUpdate = 24
    Storage = 25
    TrashBin = 26
    AlliancePrism = 27
    Havenbag = 28
    OfflineSales = 29
    FeedUI = 30
    TaxCollector = 31
    PlayerInventory = 32
    CosmeticStorage = 33
    TagEditor = 34
    OutfitList = 35
    CharacterPresetList = 36
    OutfitChoiceList = 37
    NpcStore = 38
    ConfirmBuy = 39
    Appearance = 40
    FittingRoom = 41
    ConfirmSell = 42

# .eut
class eut(IntFlag):
    ZaapSelection = 0
    ZaapiSelection = 1

# .euw
class euw(IntFlag):
    NONE = -1
    WebBase = 0
    AuctionHouse = 1
    ShopConfirmPurchase = 2
    BoughtPurchase = 3
    AuctionHouseSell = 4
    AuctionHouseConfirmPurchase = 5
    WebGiftCodeResult = 6
    WebGiftMysteryBox = 7
    WebBakPopUp = 8
    EstateAgency = 9
    DescriptionPopup = 10
    AuctionHouseItemsList1 = 11
    AuctionHouseItemsList2 = 12
    AuctionHouseItemsList3 = 13

# .euw
class euw(IntFlag):
    djfn = -1
    djfo = 0
    djfp = 1

# .eux
class eux(IntFlag):
    Tutorial = 0

# .euy
class euy(IntFlag):
    WidgetManager = 0
    CreatePreset = 1

# .exe
class exe(IntFlag):
    djno = 1
    djnp = 2
    djnq = 3
    djnr = 4

# .exm
class exm(IntFlag):
    djph = 1
    djpi = 3
    djpj = 6
    djpk = 4
    djpl = 9
    djpm = 10
    djpn = 11
    djpo = 12
    djpp = 13
    djpq = 1
    djpr = 2
    djps = 3
    djpt = 4

# .eyc
class eyc(IntFlag):
    djsh = 0
    djsi = 1
    djsj = 2

# .eyj
class eyj(IntFlag):
    djvh = 0
    djvi = 1
    djvj = 2

# .eyo
class eyo(IntFlag):
    djxi = -2
    djxj = -1
    djxk = 0
    djxl = 1
    djxm = 2
    djxn = 3
    djxo = 4

# .ezd
class ezd(IntFlag):
    dkbr = -1
    dkbs = 0
    dkbt = 1
    dkbu = 2
    dkbv = 3
    dkbw = 4
    dkbx = 5
    dkby = 6
    dkbz = 7
    dkca = 8
    dkcb = 9
    dkcc = 10

# .eze
class eze(IntFlag):
    dkcd = -1
    dkce = 0
    dkcf = 1
    dkcg = 2
    dkch = 3
    dkci = 4
    dkcj = 5

# .ezj
class ezj(IntFlag):
    dkds = -1
    dkdt = 0
    dkdu = 1
    dkdv = 2
    dkdw = 3

# .fax
class fax(IntFlag):
    dktp = 1
    dktq = 3
    dktr = 4
    dkts = 5
    dktt = 6

# .fay
class fay(IntFlag):
    dktu = 1
    dktv = 2
    dktw = 3
    dktx = 4

# .fbn
class fbn(IntFlag):
    dkxi = 0
    dkxj = 1
    dkxk = 2
    dkxl = 3
    dkxm = 4
    dkxn = 5
    dkxo = 6
    dkxp = 7
    dkxq = 8
    dkxr = 9
    dkxs = 10

# .fby
class fby(IntFlag):
    dlai = 1
    dlaj = 2
    dlak = 3
    dlal = 4
    dlam = 5
    dlan = 6
    dlao = 7
    dlap = 8
    dlaq = 9
    dlar = 10
    dlas = 11
    dlat = 12
    dlau = 13
    dlav = 14
    dlaw = 15
    dlax = 16
    dlay = 17
    dlaz = 18
    dlba = 19
    dlbb = 20
    dlbc = 21
    dlbd = 22
    dlbe = 23
    dlbf = 24
    dlbg = 25
    dlbh = 26
    dlbi = 27
    dlbj = 28
    dlbk = 29
    dlbl = 30

# .fcy
class fcy(IntFlag):
    dljb = 0
    dljc = 1
    dljd = 2
    dlje = 3
    dljf = 4
    dljg = 5
    dljh = 6
    dlji = 7
    dljj = 8

# .fcy
class fcy(IntFlag):
    dljk = 1
    dljl = 2
    dljm = 3

# .fdd
class fdd(IntFlag):
    dljz = 1
    dlka = 2
    dlkb = 3

# .fe
class fe(IntFlag):
    cuci = 0
    cucj = 1
    cuck = 2

# .fee
class fee(IntFlag):
    dlqn = 0
    dlqo = 1
    dlqp = 2

# .ffg
class ffg(IntFlag):
    dlvn = 3
    dlvo = 4

# .ffz
class ffz(IntFlag):
    dmad = 0
    dmae = 1

# .fj
class fj(IntFlag):
    cudk = 0
    cudl = 1
    cudm = 2

# .fkl
class fkl(IntFlag):
    dmwk = -1
    dmwl = 0
    dmwm = 0
    dmwn = 1
    dmwo = 2
    dmwp = 2
    dmwq = 0
    dmwr = 1
    dmws = 2
    dmwt = 3
    dmwu = 4
    dmwv = 5
    dmww = 0
    dmwx = 1
    dmwy = 2
    dmwz = 3
    dmxa = 4
    dmxb = 5
    dmxc = 6

# .fmw
class fmw(IntFlag):
    dnmh = 1
    dnmi = 2
    dnmj = 4
    dnmk = 8
    dnml = 16
    dnmm = 32
    dnmn = 64
    dnmo = 128
    dnmp = 256
    dnmq = 512
    dnmr = 1024
    dnms = 2048
    dnmt = 4096
    dnmu = 8192
    dnmv = 2047

# .fnl
class fnl(IntFlag):
    dnrn = 0
    dnro = 1
    dnrp = 2

# .fod
class fod(IntFlag):
    dnuu = 0
    dnuv = 1
    dnuw = 2
    dnux = 3

# .foe
class foe(IntFlag):
    Trace = 0
    Info = 1
    Debug = 2
    Warn = 3
    Error = 4
    Fatal = 5

# .foh
class foh(IntFlag):
    dnwd = 0
    dnwe = 1
    dnwf = 2
    dnwg = 4
    dnwh = 8
    dnwi = 16
    dnwj = 32
    dnwk = 64
    dnwl = 128
    dnwm = 65535

# .fqp
class fqp(IntFlag):
    dofi = 0
    dofj = 1

# .fra
class fra(IntFlag):
    doil = 0
    doim = 1

# .frg
class frg(IntFlag):
    doip = 0
    doiq = 1
    doir = 2
    dois = 3
    doit = 4
    doiu = 5

# .frg
class frg(IntFlag):
    doiv = 0
    doiw = 1
    doix = 2
    doiy = 3
    doiz = 4
    doja = 5
    dojb = 6
    dojc = 7
    dojd = 8
    doje = 9
    dojf = 10

# .frh
class frh(IntFlag):
    dokc = 0
    dokd = 1
    doke = 2

# .fri
class fri(IntFlag):
    dokf = 0
    dokg = 1

# .frj
class frj(IntFlag):
    dokh = 3
    doki = 5
    dokj = 10
    dokk = 30
    dokl = 60

# .frk
class frk(IntFlag):
    dokm = 0
    dokn = 1
    doko = 2
    dokp = 3
    dokq = 4

# .frl
class frl(IntFlag):
    dokr = 0
    doks = 1

# .frm
class frm(IntFlag):
    dokt = 0
    doku = 1
    dokv = 2

# .frn
class frn(IntFlag):
    dokw = -1
    dokx = 0
    doky = 1
    dokz = 2
    dola = 3
    dolb = 4

# .fro
class fro(IntFlag):
    dolc = 0
    dold = 1
    dole = 2

# .frp
class frp(IntFlag):
    dolf = 1
    dolg = 0
    dolh = 1
    doli = 2
    dolj = 3

# .frq
class frq(IntFlag):
    dolk = 0
    doll = 1

# .frr
class frr(IntFlag):
    dolm = 0
    doln = 1
    dolo = 2
    dolp = 3

# .fu
class fu(IntFlag):
    cueq = 0
    cuer = 1
    cues = 2
    cuet = 3

# .fwd
class fwd(IntFlag):
    domb = 0
    domc = 1
    domd = 2

# .fwt
class fwt(IntFlag):
    domw = 0
    domx = 1
    domy = 2
    domz = 3
    dona = 4
    donb = 5
    donc = 6
    dond = 7
    done = 8
    donf = 9
    dong = 10
    donh = 11
    doni = 12
    donj = 13
    donk = 14
    donl = 15
    donm = 16
    donn = 17
    dono = 18
    donp = 19
    donq = 20
    donr = 21
    dons = 22
    dont = 23
    donu = 24

# .fyp
class fyp(IntFlag):
    doqm = -5
    doqn = -3
    doqo = -2
    doqp = -1
    doqq = 0
    doqr = 1
    doqs = 2
    doqt = 3
    doqu = 5

# .gao
class gao(IntFlag):
    doxp = 0
    doxq = 1
    doxr = 2
    doxs = 3

# .gbc
class gbc(IntFlag):
    dpbu = -1
    dpbv = 0
    dpbw = 1
    dpbx = 2
    dpby = 3
    dpbz = 4
    dpca = 5
    dpcb = 6
    dpcc = 7
    dpcd = 8
    dpce = 9
    dpcf = 10
    dpcg = 11
    dpch = 12
    dpci = 13
    dpcj = 14
    dpck = 15
    dpcl = 16
    dpcm = 17
    dpcn = 18
    dpco = 19
    dpcp = 20
    dpcq = 21
    dpcr = 22
    dpcs = 23

# .gbd
class gbd(IntFlag):
    dpct = 0
    dpcu = 1
    dpcv = 2

# .gbe
class gbe(IntFlag):
    dpcw = 0
    dpcx = 1
    dpcy = 2
    dpcz = 3
    dpda = 4

# .gbf
class gbf(IntFlag):
    dpdb = 0

# .gbg
class gbg(IntFlag):
    dpdc = 0
    dpdd = 1

# .gbh
class gbh(IntFlag):
    dpde = 0
    dpdf = 1

# .gbi
class gbi(IntFlag):
    dpdg = 0
    dpdh = 1

# .gbj
class gbj(IntFlag):
    dpdi = 0
    dpdj = 1
    dpdk = 2
    dpdl = 3

# .gbk
class gbk(IntFlag):
    dpdm = 0
    dpdn = 1
    dpdo = 2
    dpdp = 3
    dpdq = 4

# .gbl
class gbl(IntFlag):
    dpdr = 0
    dpds = 1
    dpdt = 2

# .gbm
class gbm(IntFlag):
    dpdu = 0
    dpdv = 1
    dpdw = 2
    dpdx = 3

# .gbn
class gbn(IntFlag):
    dpdy = 0
    dpdz = 1
    dpea = 2
    dpeb = 3
    dpec = 4
    dped = 5
    dpee = 6
    dpef = 7
    dpeg = 8

# .gbo
class gbo(IntFlag):
    dpeh = 0
    dpei = 1
    dpej = 2
    dpek = 3
    dpel = 4
    dpem = 5
    dpen = 6
    dpeo = 7
    dpep = 8
    dpeq = 9
    dper = 10
    dpes = 11
    dpet = 12
    dpeu = 13
    dpev = 14

# .gcp
class gcp(IntFlag):
    dpgz = 0
    dpha = 1
    dphb = 2

# .gcq
class gcq(IntFlag):
    dphc = 0
    dphd = 1
    dphe = 2
    dphf = 3

# .get
class get(IntFlag):
    dpqy = 0
    dpqz = 1
    dpra = 2
    dprb = 3
    dprc = 4
    dprd = 5
    dpre = 6
    dprf = 7
    dprg = 8
    dprh = 9
    dpri = 10
    dprj = 11
    dprk = 12
    dprl = 13
    dprm = 14
    dprn = 15
    dpro = 16
    dprp = 17
    dprq = 18
    dprr = 19
    dprs = 20
    dprt = 21
    dpru = 22
    dprv = 23
    dprw = 24
    dprx = 25
    dpry = 26
    dprz = 27
    dpsa = 28
    dpsb = 29
    dpsc = 30
    dpsd = 31
    dpse = 32
    dpsf = 33
    dpsg = 34
    dpsh = 35
    dpsi = 36
    dpsj = 37
    dpsk = 38
    dpsl = 39
    dpsm = 40
    dpsn = 41
    dpso = 42
    dpsp = 43
    dpsq = 44
    dpsr = 45
    dpss = 46
    dpst = 47
    dpsu = 48
    dpsv = 49
    dpsw = 50
    dpsx = 51
    dpsy = 52
    dpsz = 53
    dpta = 54
    dptb = 55
    dptc = 56
    dptd = 57
    dpte = 58
    dptf = 59

# .gfl
class gfl(IntFlag):
    dpwc = 0
    dpwd = 1
    dpwe = 2

# .gfu
class gfu(IntFlag):
    dpyn = 0
    dpyo = 1
    dpyp = 2
    dpyq = 3

# .gfv
class gfv(IntFlag):
    dpyr = -1
    dpys = 0
    dpyt = 1
    dpyu = 2
    dpyv = 3
    dpyw = 4
    dpyx = 5
    dpyy = 6
    dpyz = 7
    dpza = 8
    dpzb = 9
    dpzc = 10
    dpzd = 11
    dpze = 12
    dpzf = 13
    dpzg = 14
    dpzh = 15
    dpzi = 16
    dpzj = 17
    dpzk = 18
    dpzl = 19
    dpzm = 20
    dpzn = 21
    dpzo = 22
    dpzp = 23
    dpzq = 24
    dpzr = 25
    dpzs = 26
    dpzt = 27
    dpzu = 28
    dpzv = 29
    dpzw = 30
    dpzx = 31
    dpzy = 32
    dpzz = 33
    dqaa = 34
    dqab = 35
    dqac = 36
    dqad = 37
    dqae = 38
    dqaf = 39
    dqag = 40
    dqah = 41
    dqai = 42
    dqaj = 43
    dqak = 44
    dqal = 45
    dqam = 46
    dqan = 47
    dqao = 48
    dqap = 49
    dqaq = 50
    dqar = 51
    dqas = 52
    dqat = 53
    dqau = 54
    dqav = 55
    dqaw = 56
    dqax = 57
    dqay = 58
    dqaz = 59
    dqba = 60
    dqbb = 61
    dqbc = 62
    dqbd = 63
    dqbe = 64
    dqbf = 65
    dqbg = 66
    dqbh = 67
    dqbi = 68
    dqbj = 69
    dqbk = 70
    dqbl = 71
    dqbm = 72
    dqbn = 73
    dqbo = 74
    dqbp = 75
    dqbq = 76
    dqbr = 77
    dqbs = 78
    dqbt = 79
    dqbu = 80
    dqbv = 81
    dqbw = 82
    dqbx = 83
    dqby = 84
    dqbz = 85
    dqca = 86
    dqcb = 87
    dqcc = 88
    dqcd = 89
    dqce = 90
    dqcf = 91
    dqcg = 92
    dqch = 93
    dqci = 94
    dqcj = 95

# .gfw
class gfw(IntFlag):
    dqck = 0
    dqcl = 1
    dqcm = 2

# .ggw
class ggw(IntFlag):
    dqjz = 0
    dqka = 1
    dqkb = 2
    dqkc = 3

# .ggz
class ggz(IntFlag):
    dqkk = 0
    dqkl = 1
    dqkm = 2
    dqkn = 3
    dqko = 4
    dqkp = 5
    dqkq = 6
    dqkr = 7
    dqks = 8
    dqkt = 9
    dqku = 10

# .gho
class gho(IntFlag):
    dqme = -1
    dqmf = 0
    dqmg = 1
    dqmh = 2
    dqmi = 42

# .gii
class gii(IntFlag):
    dqsp = -2
    dqsq = -1
    dqsr = 0
    dqss = 1
    dqst = 2
    dqsu = 3
    dqsv = 4
    dqsw = 5
    dqsx = 6
    dqsy = 7

# .gil
class gil(IntFlag):
    dqtm = 0
    dqtn = 1
    dqto = 2
    dqtp = 3
    dqtq = 4

# .gim
class gim(IntFlag):
    dqub = 0
    dquc = 1
    dqud = 2
    dque = 4
    dquf = 8
    dqug = 16
    dquh = 32
    dqui = 64
    dquj = 128
    dquk = 256
    dqul = 2147483648

# .gjb
class gjb(IntFlag):
    dqvx = 0
    dqvy = 1
    dqvz = 2
    dqwa = 255

# .gjd
class gjd(IntFlag):
    dqwg = 0
    dqwh = 1
    dqwi = 2
    dqwj = 4

# .gjf
class gjf(IntFlag):
    dqwm = 0
    dqwn = 1
    dqwo = 2
    dqwp = 3
    dqwq = 4

# .gjj
class gjj(IntFlag):
    dqxi = 0
    dqxj = 1
    dqxk = 4294967295

# .gjl
class gjl(IntFlag):
    dqxr = 0
    dqxs = 1
    dqxt = 2
    dqxu = 3

# .gka
class gka(IntFlag):
    draf = 0
    drag = 1
    drah = 2
    drai = 3

# .gkc
class gkc(IntFlag):
    draj = 0
    drak = 1
    dral = 2
    dram = 3
    dran = 4
    drao = 5

# .gkd
class gkd(IntFlag):
    drap = 0

# .gki
class gki(IntFlag):
    drby = 0
    drbz = 1
    drca = 2
    drcb = 3

# .gkk
class gkk(IntFlag):
    drcc = 0
    drcd = 1
    drce = 2
    drcf = 3
    drcg = 4
    drch = 5
    drci = 6
    drcj = 7
    drck = 8
    drcl = 9
    drcm = 10
    drcn = 11
    drco = 12
    drcp = 13
    drcq = 14
    drcr = 15
    drcs = 16
    drct = 17
    drcu = 18
    drcv = 19
    drcw = 20
    drcx = 21
    drcy = 22
    drcz = 23
    drda = 24
    drdb = 25
    drdc = 26
    drdd = 27
    drde = 28
    drdf = 29
    drdg = 30
    drdh = 31
    drdi = 32
    drdj = 33
    drdk = 34
    drdl = 35
    drdm = 36
    drdn = 37
    drdo = 38
    drdp = 39
    drdq = 40
    drdr = 41
    drds = 42
    drdt = 43
    drdu = 44
    drdv = 45
    drdw = 46
    drdx = 47
    drdy = 48
    drdz = 49
    drea = 50
    dreb = 51
    drec = 52
    dred = 53
    dree = 54
    dref = 55
    dreg = 56

# .gms
class gms(IntFlag):
    drhy = -1
    drhz = 0
    dria = 1
    drib = 2

# .gmu
class gmu(IntFlag):
    driv = -2
    driw = -1
    drix = 0
    driy = 1
    driz = 2
    drja = 3

# .gmx
class gmx(IntFlag):
    drje = 3
    drjf = 6
    drjg = 7
    drjh = 8
    drji = 9
    drjj = 42
    drjk = 56
    drjl = 76
    drjm = 95
    drjn = 96
    drjo = 101
    drjp = 218
    drjq = 244
    drjr = 250
    drjs = 251
    drjt = 659

# .gmy
class gmy(IntFlag):
    drju = 0
    drjv = 1
    drjw = 2
    drjx = 3
    drjy = 4
    drjz = 5
    drka = 6
    drkb = 7
    drkc = 8
    drkd = 9
    drke = 10
    drkf = 11
    drkg = 12
    drkh = 13
    drki = 14
    drkj = 15
    drkk = 16
    drkl = 17
    drkm = 18
    drkn = 19
    drko = 20
    drkp = 21
    drkq = 22
    drkr = 23
    drks = 24
    drkt = 25
    drku = 26
    drkv = 27
    drkw = 28
    drkx = 29
    drky = 30
    drkz = 31
    drla = 32
    drlb = 33
    drlc = 34
    drld = 35
    drle = 35

# .gmz
class gmz(IntFlag):
    drlf = 0
    drlg = 1
    drlh = 2
    drli = 4
    drlj = 8
    drlk = 16
    drll = 32
    drlm = 64
    drln = 128
    drlo = 256
    drlp = 512
    drlq = 1024
    drlr = 2048
    drls = 4096
    drlt = 8192
    drlu = 16384
    drlv = 4294967295

# .gna
class gna(IntFlag):
    drlw = 0
    drlx = 1
    drly = 2
    drlz = 3

# .gns
class gns(IntFlag):
    drne = -1
    drnf = 0
    drng = 1
    drnh = 2

# .goh
class goh(IntFlag):
    drpf = 0
    drpg = 1
    drph = 2
    drpi = 3
    drpj = 4

# .gpg
class gpg(IntFlag):
    drur = 115615
    drus = 17923
    drut = 25088
    druu = 1025

# .gph
class gph(IntFlag):
    drvg = 0
    drvh = 1
    drvi = 2
    drvj = 4
    drvk = 8
    drvl = 16
    drvm = 32
    drvn = 4294967295

# .gpi
class gpi(IntFlag):
    drvo = 0
    drvp = 1
    drvq = 2
    drvr = 4
    drvs = 8
    drvt = 16
    drvu = 32
    drvv = 64
    drvw = 4294967295

# .gpj
class gpj(IntFlag):
    drvx = 0
    drvy = 4294967295

# .gpx
class gpx(IntFlag):
    drxa = 0

# .gpx
class gpx(IntFlag):
    drxb = 0

# .gpx
class gpx(IntFlag):
    drxc = 0

# .gpx
class gpx(IntFlag):
    drxd = 0

# .gpx
class gpx(IntFlag):
    drxe = 0

# .gpx
class gpx(IntFlag):
    drxf = 0
    drxg = 1

# .gpx
class gpx(IntFlag):
    drxh = 0

# .gpx
class gpx(IntFlag):
    drxi = 0
    drxj = 1
    drxk = 2
    drxl = 3
    drxm = 4
    drxn = 5

# .gpx
class gpx(IntFlag):
    drxo = 0

# .gpx
class gpx(IntFlag):
    drxp = 0

# .gpx
class gpx(IntFlag):
    drxq = 0

# .gpx
class gpx(IntFlag):
    drxr = 0
    drxs = 1
    drxt = 2
    drxu = 3

# .gqt
class gqt(IntFlag):
    dsgj = 0
    dsgk = 1
    dsgl = 2
    dsgm = 3

# .gqu
class gqu(IntFlag):
    dsgn = 0
    dsgo = 1

# .grn
class grn(IntFlag):
    dsja = 0
    dsjb = 1
    dsjc = 2
    dsjd = 3
    dsje = 4

# .grq
class grq(IntFlag):
    dsjr = 0
    dsjs = 1
    dsjt = 2
    dsju = 3
    dsjv = 4
    dsjw = 5
    dsjx = 6
    dsjy = 7
    dsjz = 8
    dska = 9
    dskb = 10
    dskc = 11
    dskd = 12
    dske = 13
    dskf = 14
    dskg = 15

# .gsd
class gsd(IntFlag):
    dsml = 0
    dsmm = 1
    dsmn = 2

# .gsr
class gsr(IntFlag):
    dsnq = 0
    dsnr = 1
    dsns = 3
    dsnt = 4

# .gsr
class gsr(IntFlag):
    dsnu = 0
    dsnv = 1

# .gsv
class gsv(IntFlag):
    dsos = 0
    dsot = 1
    dsou = 2
    dsov = 3

# .gtr
class gtr(IntFlag):
    dsul = 0

# .gtx
class gtx(IntFlag):
    dsvg = 0
    dsvh = 1
    dsvi = 2

# .gum
class gum(IntFlag):
    dszv = 0
    dszw = 1

# .guo
class guo(IntFlag):
    dtae = 0
    dtaf = 1
    dtag = 2
    dtah = 3
    dtai = 6
    dtaj = 7

# .gva
class gva(IntFlag):
    dtbb = 0
    dtbc = 1
    dtbd = 2
    dtbe = 3
    dtbf = 4
    dtbg = 5
    dtbh = 7
    dtbi = 8
    dtbj = 9
    dtbk = 10

# .gva
class gva(IntFlag):
    dtbl = 0
    dtbm = 1
    dtbn = 2
    dtbo = 3

# .gva
class gva(IntFlag):
    dtbu = 0

# .gvf
class gvf(IntFlag):
    dtdj = 0
    dtdk = 1
    dtdl = 2
    dtdm = 3
    dtdn = 4
    dtdo = 5

# .gvf
class gvf(IntFlag):
    dtdp = 0
    dtdq = 1

# .gvh
class gvh(IntFlag):
    dtee = 0
    dtef = 1
    dteg = 2

# .gwb
class gwb(IntFlag):
    dteh = 0
    dtei = 1
    dtej = 2
    dtek = 3
    dtel = 4
    dtem = 5

# .gwb
class gwb(IntFlag):
    dtfh = 0
    dtfi = 1

# .gwb
class gwb(IntFlag):
    dtha = 0
    dthb = 1
    dthc = 2

# .gwb
class gwb(IntFlag):
    dthp = 0
    dthq = 1
    dthr = 2
    dths = 3
    dtht = 4

# .gwg
class gwg(IntFlag):
    dtiy = 0
    dtiz = 1
    dtja = 2
    dtjb = 3
    dtjc = 4
    dtjd = 5

# .gwg
class gwg(IntFlag):
    dtje = 0
    dtjf = 1
    dtjg = 2
    dtjh = 3
    dtji = 4
    dtjj = 5
    dtjk = 6
    dtjl = 7
    dtjm = 8

# .gws
class gws(IntFlag):
    dtna = 0
    dtnb = 1
    dtnc = 2
    dtnd = 3
    dtne = 4
    dtnf = 5
    dtng = 6

# .gwy
class gwy(IntFlag):
    dtoi = 0
    dtoj = 1
    dtok = 2
    dtol = 3
    dtom = 4
    dton = 5
    dtoo = 6

# .gxa
class gxa(IntFlag):
    dtoy = 0
    dtoz = 1
    dtpa = 2

# .gxg
class gxg(IntFlag):
    dtpp = 0
    dtpq = 1
    dtpr = 2
    dtps = 3
    dtpt = 4
    dtpu = 5
    dtpv = 6
    dtpw = 7

# .gxn
class gxn(IntFlag):
    dtrk = 0
    dtrl = 1
    dtrm = 2
    dtrn = 3
    dtro = 4

# .gxz
class gxz(IntFlag):
    dtur = 0
    dtus = 7

# .gyq
class gyq(IntFlag):
    dtzn = 0
    dtzo = 1
    dtzp = 2
    dtzq = 3
    dtzr = 4
    dtzs = 5
    dtzt = 6
    dtzu = 7
    dtzv = 8

# .gz
class gz(IntFlag):
    cukb = 0
    cukc = 1
    cukd = 2
    cuke = 3
    cukf = 4
    cukg = 5
    cukh = 6
    cuki = 7

# .gzw
class gzw(IntFlag):
    duhp = 0
    duhq = 1
    duhr = 2
    duhs = 3
    duht = 4

# .gzw
class gzw(IntFlag):
    duhu = 0
    duhv = 1
    duhw = 2
    duhx = 3
    duhy = 4
    duhz = 5
    duia = 6

# .hac
class hac(IntFlag):
    duiw = 0
    duix = 1

# .hah
class hah(IntFlag):
    dujx = 0
    dujy = 1
    dujz = 2
    duka = 3
    dukb = 4
    dukc = 5
    dukd = 6
    duke = 7

# .has
class has(IntFlag):
    dumc = 0

# .hav
class hav(IntFlag):
    dumu = 0
    dumv = 1
    dumw = 2
    dumx = 3
    dumy = 4
    dumz = 5

# .hb
class hb(IntFlag):
    cukn = -1
    cuko = 0
    cukp = 1
    cukq = 2
    cukr = 3
    cuks = 4

# .hba
class hba(IntFlag):
    dunm = 0
    dunn = 1
    duno = 2
    dunp = 3
    dunq = 4
    dunr = 5
    duns = 6
    dunt = 7

# .hbm
class hbm(IntFlag):
    dupq = 0
    dupr = 1
    dups = 2

# .hbm
class hbm(IntFlag):
    dupt = 0
    dupu = 1

# .hbt
class hbt(IntFlag):
    durc = 0
    durd = 1

# .hbz
class hbz(IntFlag):
    dutc = 0
    dutd = 1
    dute = 2
    dutf = 3
    dutg = 4

# .hcc
class hcc(IntFlag):
    dutq = 0
    dutr = 1
    duts = 2
    dutt = 3
    dutu = 4
    dutv = 5
    dutw = 6
    dutx = 7
    duty = 8
    dutz = 9

# .hcp
class hcp(IntFlag):
    duwz = 0
    duxa = 1
    duxb = 2

# .hdj
class hdj(IntFlag):
    dvbv = 0
    dvbw = 1
    dvbx = 2

# .hdp
class hdp(IntFlag):
    dvdo = 0
    dvdp = 1

# .hek
class hek(IntFlag):
    dvhu = 0
    dvhv = 1
    dvhw = 2
    dvhx = 3

# .hex
class hex(IntFlag):
    dvlh = 0
    dvli = 1
    dvlj = 2
    dvlk = 3
    dvll = 4
    dvlm = 5

# .hfc
class hfc(IntFlag):
    dvlt = 0
    dvlu = 1
    dvlv = 2
    dvlw = 3
    dvlx = 4
    dvly = 5
    dvlz = 6

# .hfc
class hfc(IntFlag):
    dvma = 0
    dvmb = 1
    dvmc = 2
    dvmd = 3
    dvme = 4

# .hfk
class hfk(IntFlag):
    dvoh = 0
    dvoi = 1
    dvoj = 2
    dvok = 3
    dvol = 4
    dvom = 5
    dvon = 6
    dvoo = 7
    dvop = 8

# .hfz
class hfz(IntFlag):
    dvsl = 0

# .hgv
class hgv(IntFlag):
    dvxh = 0
    dvxi = 1

# .hgv
class hgv(IntFlag):
    dvxj = 0
    dvxk = 1
    dvxl = 2
    dvxm = 3

# .hgy
class hgy(IntFlag):
    dvxz = 0
    dvya = 1
    dvyb = 2
    dvyc = 3
    dvyd = 4
    dvye = 5
    dvyf = 6
    dvyg = 7
    dvyh = 8

# .hhl
class hhl(IntFlag):
    dwag = 0
    dwah = 1
    dwai = 2

# .hhl
class hhl(IntFlag):
    dwaj = 0
    dwak = 1
    dwal = 2
    dwam = 3
    dwan = 4

# .hhu
class hhu(IntFlag):
    dwbf = 0
    dwbg = 1
    dwbh = 2
    dwbi = 3

# .hhu
class hhu(IntFlag):
    dwbj = 0
    dwbk = 1
    dwbl = 2
    dwbm = 3
    dwbn = 4
    dwbo = 5
    dwbp = 6
    dwbq = 7

# .hiy
class hiy(IntFlag):
    dwir = 0
    dwis = 1
    dwit = 2

# .hiy
class hiy(IntFlag):
    dwiu = 0
    dwiv = 1
    dwiw = 2
    dwix = 3

# .hjp
class hjp(IntFlag):
    dwnl = 0
    dwnm = 1
    dwnn = 2

# .hjp
class hjp(IntFlag):
    dwno = 0
    dwnp = 1
    dwnq = 2
    dwnr = 3
    dwns = 4
    dwnt = 5
    dwnu = 6

# .hju
class hju(IntFlag):
    dwph = 0
    dwpi = 1
    dwpj = 2
    dwpk = 3
    dwpl = 4

# .hk
class hk(IntFlag):
    cuny = 1
    cunz = 2
    cuoa = 3
    cuob = 4

# .hka
class hka(IntFlag):
    dwqm = 0

# .hkd
class hkd(IntFlag):
    dwqv = 0
    dwqw = 1
    dwqx = 2
    dwqy = 3
    dwqz = 4
    dwra = 5
    dwrb = 6

# .hkv
class hkv(IntFlag):
    dwtz = 0
    dwua = 1
    dwub = 2
    dwuc = 4
    dwud = 5

# .hkv
class hkv(IntFlag):
    dwuo = 0
    dwup = 1
    dwuq = 2
    dwur = 3
    dwus = 4
    dwut = 5
    dwuu = 6
    dwuv = 7

# .hlc
class hlc(IntFlag):
    dwwy = 0
    dwwz = 1
    dwxa = 2

# .hll
class hll(IntFlag):
    dwys = 0
    dwyt = 1
    dwyu = 2
    dwyv = 3
    dwyw = 4
    dwyx = 5
    dwyy = 6

# .hly
class hly(IntFlag):
    dxbu = 0
    dxbv = 1
    dxbw = 2
    dxbx = 3
    dxby = 4

# .hlz
class hlz(IntFlag):
    dxbz = 0
    dxca = 1
    dxcb = 2

# .hme
class hme(IntFlag):
    dxcq = 0
    dxcr = 1

# .hmh
class hmh(IntFlag):
    dxcw = 0
    dxcx = 1

# .hmm
class hmm(IntFlag):
    dxdo = 0
    dxdp = 1

# .hnb
class hnb(IntFlag):
    dxhh = 0
    dxhi = 1
    dxhj = 2
    dxhk = 3
    dxhl = 4
    dxhm = 5
    dxhn = 6
    dxho = 7
    dxhp = 8
    dxhq = 9
    dxhr = 10
    dxhs = 11
    dxht = 12

# .hng
class hng(IntFlag):
    dxik = 0
    dxil = 1

# .hnp
class hnp(IntFlag):
    dxke = 0
    dxkf = 1

# .hoc
class hoc(IntFlag):
    dxoz = 0
    dxpa = 1
    dxpb = 2
    dxpc = 3
    dxpd = 4

# .hoi
class hoi(IntFlag):
    dxqe = 0
    dxqf = 1

# .hot
class hot(IntFlag):
    dxsl = 0
    dxsm = 1

# .hpa
class hpa(IntFlag):
    dxud = 0
    dxue = 1
    dxuf = 2
    dxug = 3
    dxuh = 4
    dxui = 5
    dxuj = 6
    dxuk = 7

# .hps
class hps(IntFlag):
    dxzu = 0
    dxzv = 1

# .hqc
class hqc(IntFlag):
    dybq = 0
    dybr = 1
    dybs = 2
    dybt = 3
    dybu = 4

# .hqw
class hqw(IntFlag):
    dyhd = 0
    dyhe = 1
    dyhf = 2
    dyhg = 3
    dyhh = 4

# .hrr
class hrr(IntFlag):
    dyln = 0
    dylo = 1

# .hrv
class hrv(IntFlag):
    dyms = 0
    dymt = 1
    dymu = 2
    dymv = 3

# .hrz
class hrz(IntFlag):
    dyna = 0
    dynb = 1
    dync = 2
    dynd = 3

# .hsf
class hsf(IntFlag):
    dyow = 0
    dyox = 1

# .hsk
class hsk(IntFlag):
    dypm = 0
    dypn = 1
    dypo = 2
    dypp = 3
    dypq = 4
    dypr = 5
    dyps = 6

# .hsv
class hsv(IntFlag):
    dyru = 0
    dyrv = 1
    dyrw = 2

# .hsy
class hsy(IntFlag):
    dysb = 0
    dysc = 1
    dysd = 2
    dyse = 3

# .ht
class ht(IntFlag):
    cuqe = 1
    cuqf = 2
    cuqg = 3

# .htf
class htf(IntFlag):
    dytb = 0
    dytc = 1
    dytd = 2
    dyte = 3
    dytf = 4
    dytg = 5
    dyth = 6
    dyti = 7

# .hts
class hts(IntFlag):
    dyvo = 0
    dyvp = 1
    dyvq = 2
    dyvr = 3

# .huk
class huk(IntFlag):
    dyzt = 0
    dyzu = 1
    dyzv = 2
    dyzw = 3
    dyzx = 4
    dyzy = 5
    dyzz = 6
    dzaa = 7
    dzab = 8

# .hvl
class hvl(IntFlag):
    dzhd = 0
    dzhe = 1
    dzhf = 2
    dzhg = 3
    dzhh = 4
    dzhi = 5
    dzhj = 6
    dzhk = 7
    dzhl = 8

# .hvs
class hvs(IntFlag):
    dziq = 0
    dzir = 1
    dzis = 2
    dzit = 3

# .hwi
class hwi(IntFlag):
    dzmh = 0
    dzmi = 1
    dzmj = 2
    dzmk = 3
    dzml = 4
    dzmm = 5
    dzmn = 6
    dzmo = 7
    dzmp = 8

# .hxd
class hxd(IntFlag):
    dzqn = 0
    dzqo = 3
    dzqp = 4

# .hxd
class hxd(IntFlag):
    dzqq = 0
    dzqr = 1

# .hxg
class hxg(IntFlag):
    dzsk = 0
    dzsl = 1
    dzsm = 2

# .hxk
class hxk(IntFlag):
    dzsn = 0

# .hxr
class hxr(IntFlag):
    dzuv = 0
    dzuw = 1
    dzux = 2
    dzuy = 3
    dzuz = 4
    dzva = 5

# .hxv
class hxv(IntFlag):
    dzvr = 0
    dzvs = 1
    dzvt = 2
    dzvu = 3
    dzvv = 4

# .hyu
class hyu(IntFlag):
    eaap = 0
    eaaq = 1
    eaar = 2
    eaas = 3
    eaat = 4
    eaau = 5
    eaav = 6
    eaaw = 7

# .hyz
class hyz(IntFlag):
    eaca = 0
    eacb = 1
    eacc = 2
    eacd = 3
    eace = 4
    eacf = 5
    eacg = 6
    each = 7

# .hzk
class hzk(IntFlag):
    eaev = 0
    eaew = 1
    eaex = 2
    eaey = 3
    eaez = 4
    eafa = 5
    eafb = 6

# .hzn
class hzn(IntFlag):
    eafq = 0
    eafr = 1

# .hzu
class hzu(IntFlag):
    eahb = 0
    eahc = 1
    eahd = 2

# .hzz
class hzz(IntFlag):
    eaic = 0
    eaid = 1
    eaie = 2

# .ias
class ias(IntFlag):
    eamp = 0
    eamq = 1
    eamr = 2
    eams = 3
    eamt = 4
    eamu = 5
    eamv = 6
    eamw = 7

# .ibb
class ibb(IntFlag):
    eapw = 0
    eapx = 1
    eapy = 2
    eapz = 3
    eaqa = 4
    eaqb = 5
    eaqc = 6
    eaqd = 7

# .ibn
class ibn(IntFlag):
    eatu = 0
    eatv = 1
    eatw = 2

# .ibx
class ibx(IntFlag):
    eavk = 0

# .icb
class icb(IntFlag):
    eavz = 0
    eawa = 1
    eawb = 2
    eawc = 3

# .ics
class ics(IntFlag):
    eban = 0
    ebao = 1
    ebap = 2

# .idd
class idd(IntFlag):
    ebce = 0
    ebcf = 1
    ebcg = 2
    ebch = 3
    ebci = 4

# .idh
class idh(IntFlag):
    ebcn = 0
    ebco = 1

# .ieh
class ieh(IntFlag):
    ebgk = 0
    ebgl = 2
    ebgm = 3

# .ieq
class ieq(IntFlag):
    ebhl = 0
    ebhm = 2
    ebhn = 3

# .ieq
class ieq(IntFlag):
    ebho = 0

# .ieq
class ieq(IntFlag):
    ebht = 0
    ebhu = 1

# .ifb
class ifb(IntFlag):
    ebix = 0
    ebiy = 1
    ebiz = 2

# .ifb
class ifb(IntFlag):
    ebja = 0

# .ifj
class ifj(IntFlag):
    ebkn = 0
    ebko = 1
    ebkp = 2

# .ifu
class ifu(IntFlag):
    eblc = 0
    ebld = 1
    eble = 2
    eblf = 4

# .ifu
class ifu(IntFlag):
    eblm = 0
    ebln = 1
    eblo = 2
    eblp = 3
    eblq = 4
    eblr = 5
    ebls = 6

# .igd
class igd(IntFlag):
    eboi = 0
    eboj = 1
    ebok = 2

# .igm
class igm(IntFlag):
    ebpy = 0
    ebpz = 1
    ebqa = 2
    ebqb = 3

# .igz
class igz(IntFlag):
    ebtb = 0
    ebtc = 1
    ebtd = 2
    ebte = 3
    ebtf = 4
    ebtg = 5
    ebth = 6

# .ihd
class ihd(IntFlag):
    ebtq = 0
    ebtr = 1

# .ihs
class ihs(IntFlag):
    ebvl = 0
    ebvm = 1
    ebvn = 2

# .ihy
class ihy(IntFlag):
    ebwc = 0
    ebwd = 1
    ebwe = 2

# .iit
class iit(IntFlag):
    ebzz = 0
    ecaa = 1
    ecab = 2
    ecac = 3

# .ijc
class ijc(IntFlag):
    ecdb = 0
    ecdc = 1
    ecdd = 2
    ecde = 3
    ecdf = 4
    ecdg = 5
    ecdh = 6
    ecdi = 7

# .ijk
class ijk(IntFlag):
    ecfg = 0
    ecfh = 1

# .ijo
class ijo(IntFlag):
    ecfs = 0
    ecft = 1
    ecfu = 2
    ecfv = 3
    ecfw = 4

# .ili
class ili(IntFlag):
    ecoh = 0
    ecoi = 1
    ecoj = 2

# .ili
class ili(IntFlag):
    ecou = 0
    ecov = 1
    ecow = 2
    ecox = 3
    ecoy = 4
    ecoz = 5
    ecpa = 6
    ecpb = 7
    ecpc = 8

# .ili
class ili(IntFlag):
    ecpj = 0
    ecpk = 1
    ecpl = 2
    ecpm = 3
    ecpn = 4
    ecpo = 5

# .ilu
class ilu(IntFlag):
    ecrp = 0
    ecrq = 1
    ecrr = 3

# .ilu
class ilu(IntFlag):
    ecrs = 0
    ecrt = 1
    ecru = 2
    ecrv = 3
    ecrw = 4

# .imb
class imb(IntFlag):
    ectm = 0
    ectn = 1
    ecto = 2
    ectp = 3
    ectq = 4
    ectr = 5
    ects = 6
    ectt = 7

# .imp
class imp(IntFlag):
    ecvr = 0
    ecvs = 1
    ecvt = 2
    ecvu = 3
    ecvv = 4

# .ims
class ims(IntFlag):
    ecwe = 0
    ecwf = 1
    ecwg = 2
    ecwh = 3
    ecwi = 4
    ecwj = 5
    ecwk = 6
    ecwl = 7

# .imx
class imx(IntFlag):
    ecxr = 0
    ecxs = 1

# .ini
class ini(IntFlag):
    edai = 0
    edaj = 1
    edak = 2
    edal = 3
    edam = 4

# .inm
class inm(IntFlag):
    edbf = 0

# .inw
class inw(IntFlag):
    edcw = 0
    edcx = 1
    edcy = 2
    edcz = 3
    edda = 4
    eddb = 5
    eddc = 6

# .ioa
class ioa(IntFlag):
    eddp = 0
    eddq = 1
    eddr = 3

# .iod
class iod(IntFlag):
    edek = 0
    edel = 1
    edem = 2
    eden = 3

# .iou
class iou(IntFlag):
    edig = 0
    edih = 7
    edii = 9
    edij = 13
    edik = 14
    edil = 15

# .ioz
class ioz(IntFlag):
    edkh = 0
    edki = 1

# .ipg
class ipg(IntFlag):
    edlk = 0
    edll = 1
    edlm = 2
    edln = 3
    edlo = 4
    edlp = 5
    edlq = 6
    edlr = 7

# .ipz
class ipz(IntFlag):
    edqf = 0
    edqg = 1
    edqh = 2
    edqi = 3
    edqj = 4
    edqk = 5
    edql = 6
    edqm = 7
    edqn = 8

# .iqe
class iqe(IntFlag):
    edra = 0
    edrb = 1
    edrc = 4

# .iqg
class iqg(IntFlag):
    edsr = 0
    edss = 1
    edst = 2

# .iqh
class iqh(IntFlag):
    edsu = 0
    edsv = 1
    edsw = 2
    edsx = 3
    edsy = 4
    edsz = 5
    edta = 6
    edtb = 7
    edtc = 8
    edtd = 9
    edte = 10

# .ir
class ir(IntFlag):
    cuwh = 0
    cuwi = 1
    cuwj = 2

# .irg
class irg(IntFlag):
    edxr = 0
    edxs = 1
    edxt = 3
    edxu = 4

# .irg
class irg(IntFlag):
    edxv = 0
    edxw = 1
    edxx = 2

# .is
class is(IntFlag):
    cuwk = 4
    cuwl = 5
    cuwm = 6

# .iue
class iue(IntFlag):
    edzf = 0
    edzg = 1
    edzh = 2
    edzi = 5
    edzj = 6
    edzk = 7
    edzl = 8
    edzm = 9
    edzn = 10
    edzo = 11
    edzp = 12
    edzq = 13
    edzr = 14
    edzs = 15
    edzt = 17
    edzu = 18
    edzv = 19
    edzw = 20
    edzx = 21
    edzy = 22
    edzz = 23
    eeaa = 24
    eeab = 25
    eeac = 26
    eead = 27
    eeae = 28
    eeaf = 29
    eeag = 30
    eeah = 31
    eeai = 32
    eeaj = 33
    eeak = 34
    eeal = 35
    eeam = 36
    eean = 37
    eeao = 38
    eeap = 39
    eeaq = 40

# .iue
class iue(IntFlag):
    eebl = 0
    eebm = 1
    eebn = 2
    eebo = 3
    eebp = 4

# .iue
class iue(IntFlag):
    eees = 0
    eeet = 1
    eeeu = 2

# .iue
class iue(IntFlag):
    eege = 0
    eegf = 1
    eegg = 2
    eegh = 3
    eegi = 4

# .iue
class iue(IntFlag):
    eegr = 0
    eegs = 1
    eegt = 2
    eegu = 3
    eegv = 4
    eegw = 5
    eegx = 6

# .iue
class iue(IntFlag):
    eeiv = 0
    eeiw = 1
    eeix = 3

# .iue
class iue(IntFlag):
    eelu = 0
    eelv = 5
    eelw = 7

# .iue
class iue(IntFlag):
    eenc = 0
    eend = 1
    eene = 2
    eenf = 3
    eeng = 4
    eenh = 5

# .iue
class iue(IntFlag):
    eetg = 0
    eeth = 1

# .iue
class iue(IntFlag):
    eevi = 0
    eevj = 1
    eevk = 2
    eevl = 3
    eevm = 4
    eevn = 5
    eevo = 6
    eevp = 7

# .iuq
class iuq(IntFlag):
    eeyv = 0
    eeyw = 1
    eeyx = 2
    eeyy = 3
    eeyz = 4
    eeza = 5
    eezb = 6
    eezc = 7
    eezd = 8
    eeze = 9
    eezf = 10
    eezg = 11
    eezh = 12
    eezi = 13
    eezj = 14
    eezk = 15
    eezl = 16
    eezm = 17
    eezn = 18
    eezo = 19
    eezp = 20
    eezq = 21
    eezr = 22
    eezs = 23

# .iuy
class iuy(IntFlag):
    efaf = 0
    efag = 2
    efah = 3
    efai = 4
    efaj = 5

# .ivy
class ivy(IntFlag):
    efim = 0
    efin = 1
    efio = 2
    efip = 3
    efiq = 4
    efir = 5
    efis = 6

# .iwi
class iwi(IntFlag):
    efmq = 0
    efmr = 1
    efms = 2
    efmt = 3
    efmu = 4
    efmv = 5
    efmw = 6
    efmx = 7

# .iye
class iye(IntFlag):
    egbo = 0
    egbp = 1
    egbq = 2
    egbr = 3
    egbs = 4
    egbt = 5
    egbu = 6

# .iyh
class iyh(IntFlag):
    egcb = 0

# .iyz
class iyz(IntFlag):
    eggb = 0
    eggc = 1
    eggd = 2
    egge = 3
    eggf = 4

# .izx
class izx(IntFlag):
    egnm = 0
    egnn = 1
    egno = 2
    egnp = 3
    egnq = 4
    egnr = 5

# .jak
class jak(IntFlag):
    egqr = 0
    egqs = 1
    egqt = 2
    egqu = 3
    egqv = 4
    egqw = 5
    egqx = 6
    egqy = 7
    egqz = 8
    egra = 9
    egrb = 10

# .jaq
class jaq(IntFlag):
    egsg = 0
    egsh = 1
    egsi = 2
    egsj = 3

# .jbg
class jbg(IntFlag):
    egwc = 0

# .jbk
class jbk(IntFlag):
    egww = 0
    egwx = 1
    egwy = 2
    egwz = 3

# .jbq
class jbq(IntFlag):
    egxm = 0
    egxn = 1
    egxo = 2
    egxp = 3
    egxq = 4

# .jcu
class jcu(IntFlag):
    ehev = 0
    ehew = 1
    ehex = 2
    ehey = 3
    ehez = 4

# .jdb
class jdb(IntFlag):
    ehgv = 0
    ehgw = 1
    ehgx = 2
    ehgy = 3
    ehgz = 4
    ehha = 5
    ehhb = 6
    ehhc = 7

# .jdt
class jdt(IntFlag):
    ehls = 0
    ehlt = 1
    ehlu = 2
    ehlv = 3
    ehlw = 4
    ehlx = 5
    ehly = 6
    ehlz = 7
    ehma = 8
    ehmb = 9
    ehmc = 10
    ehmd = 11
    ehme = 12
    ehmf = 13
    ehmg = 14
    ehmh = 15
    ehmi = 16
    ehmj = 17
    ehmk = 18

# .jeg
class jeg(IntFlag):
    ehoi = 0
    ehoj = 1
    ehok = 2

# .jeg
class jeg(IntFlag):
    ehol = 0
    ehom = 1
    ehon = 2
    ehoo = 3
    ehop = 4

# .jeg
class jeg(IntFlag):
    ehoq = 0
    ehor = 1
    ehos = 2

# .jeg
class jeg(IntFlag):
    ehot = 0
    ehou = 1
    ehov = 2
    ehow = 3
    ehox = 4
    ehoy = 5
    ehoz = 6
    ehpa = 7

# .jet
class jet(IntFlag):
    ehrw = 0

# .jff
class jff(IntFlag):
    ehue = 0
    ehuf = 1

# .jfp
class jfp(IntFlag):
    ehwd = 0
    ehwe = 1

# .jft
class jft(IntFlag):
    ehwv = 0
    ehww = 1

# .jfw
class jfw(IntFlag):
    ehxj = 0
    ehxk = 1
    ehxl = 2

# .jgc
class jgc(IntFlag):
    ehyc = 0
    ehyd = 1
    ehye = 2
    ehyf = 3
    ehyg = 4

# .jgf
class jgf(IntFlag):
    ehyh = 0
    ehyi = 1
    ehyj = 2
    ehyk = 3
    ehyl = 4

# .jgo
class jgo(IntFlag):
    ehys = 0
    ehyt = 2
    ehyu = 3

# .jgo
class jgo(IntFlag):
    ehzz = 0
    eiaa = 1
    eiab = 2
    eiac = 3

# .jgr
class jgr(IntFlag):
    eiby = 0
    eibz = 1
    eica = 2
    eicb = 3
    eicc = 4
    eicd = 5

# .jhd
class jhd(IntFlag):
    eido = 0
    eidp = 2
    eidq = 5

# .jhd
class jhd(IntFlag):
    eidy = 0
    eidz = 1
    eiea = 2
    eieb = 3
    eiec = 4

# .jhg
class jhg(IntFlag):
    eifz = 0
    eiga = 1
    eigb = 2
    eigc = 3
    eigd = 4
    eige = 5
    eigf = 6
    eigg = 7

# .jho
class jho(IntFlag):
    eigo = 0
    eigp = 1
    eigq = 2

# .jho
class jho(IntFlag):
    eigr = 0
    eigs = 1
    eigt = 2

# .jho
class jho(IntFlag):
    eigu = 0
    eigv = 1
    eigw = 2
    eigx = 3
    eigy = 4
    eigz = 5
    eiha = 6

# .jib
class jib(IntFlag):
    eimn = 0
    eimo = 1

# .jib
class jib(IntFlag):
    eimp = 0
    eimq = 1
    eimr = 2
    eims = 3
    eimt = 4

# .jik
class jik(IntFlag):
    eioy = 0
    eioz = 1
    eipa = 2

# .jik
class jik(IntFlag):
    eipb = 0
    eipc = 1
    eipd = 2

# .jio
class jio(IntFlag):
    eipm = 0
    eipn = 1
    eipo = 2
    eipp = 3

# .jiv
class jiv(IntFlag):
    eirf = 0
    eirg = 1
    eirh = 2
    eiri = 3
    eirj = 4
    eirk = 5

# .jiz
class jiz(IntFlag):
    eiru = 0
    eirv = 1
    eirw = 2
    eirx = 3

# .jjd
class jjd(IntFlag):
    eise = 0

# .jji
class jji(IntFlag):
    eisw = 0
    eisx = 1
    eisy = 2
    eisz = 3
    eita = 4
    eitb = 5

# .jjs
class jjs(IntFlag):
    eivc = 0
    eivd = 1
    eive = 2
    eivf = 3
    eivg = 4
    eivh = 5

# .jjx
class jjx(IntFlag):
    eiwf = 0
    eiwg = 1
    eiwh = 2
    eiwi = 3

# .jkb
class jkb(IntFlag):
    eixm = 0
    eixn = 1

# .jkm
class jkm(IntFlag):
    eizp = 0
    eizq = 1

# .jkr
class jkr(IntFlag):
    ejah = 0
    ejai = 1
    ejaj = 2
    ejak = 3
    ejal = 4
    ejam = 5
    ejan = 6

# .jkz
class jkz(IntFlag):
    ejce = 0
    ejcf = 1
    ejcg = 2
    ejch = 3
    ejci = 4
    ejcj = 5

# .jlg
class jlg(IntFlag):
    ejck = 0
    ejcl = 1
    ejcm = 2

# .jlg
class jlg(IntFlag):
    ejcn = 0
    ejco = 1
    ejcp = 2
    ejcq = 3
    ejcr = 4
    ejcs = 5
    ejct = 6
    ejcu = 7
    ejcv = 8

# .jll
class jll(IntFlag):
    ejdm = 0
    ejdn = 1
    ejdo = 2

# .jlv
class jlv(IntFlag):
    ejes = 0
    ejet = 1
    ejeu = 3

# .jly
class jly(IntFlag):
    ejge = 0
    ejgf = 1
    ejgg = 2
    ejgh = 3
    ejgi = 4
    ejgj = 5

# .jmj
class jmj(IntFlag):
    ejho = 0
    ejhp = 2
    ejhq = 3

# .jmj
class jmj(IntFlag):
    ejhv = 0
    ejhw = 1
    ejhx = 2

# .jmv
class jmv(IntFlag):
    ejky = 0
    ejkz = 1
    ejla = 2
    ejlb = 3
    ejlc = 4
    ejld = 5
    ejle = 6
    ejlf = 7

# .jn
class jn(IntFlag):
    cvam = -1
    cvan = 0
    cvao = 1

# .jni
class jni(IntFlag):
    ejnq = 0
    ejnr = 2
    ejns = 3

# .jni
class jni(IntFlag):
    ejnt = 0
    ejnu = 1
    ejnv = 2
    ejnw = 3
    ejnx = 4
    ejny = 5
    ejnz = 6
    ejoa = 7

# .jnt
class jnt(IntFlag):
    ejpv = 0

# .jow
class jow(IntFlag):
    ejxh = 0
    ejxi = 1
    ejxj = 2
    ejxk = 3
    ejxl = 4

# .joz
class joz(IntFlag):
    ejxw = 0
    ejxx = 1
    ejxy = 2
    ejxz = 3
    ejya = 4
    ejyb = 5
    ejyc = 6
    ejyd = 7
    ejye = 8

# .jpr
class jpr(IntFlag):
    ejzw = 0
    ejzx = 1
    ejzy = 2
    ejzz = 3

# .jqb
class jqb(IntFlag):
    ekcs = 0
    ekct = 1

# .jqg
class jqg(IntFlag):
    ekdp = 0
    ekdq = 1

# .jqm
class jqm(IntFlag):
    ekey = 0
    ekez = 1
    ekfa = 2
    ekfb = 3
    ekfc = 4
    ekfd = 5

# .jqp
class jqp(IntFlag):
    ekfz = 0
    ekga = 1
    ekgb = 2
    ekgc = 3
    ekgd = 4
    ekge = 5
    ekgf = 6
    ekgg = 7
    ekgh = 8
    ekgi = 9
    ekgj = 10
    ekgk = 11
    ekgl = 12
    ekgm = 13
    ekgn = 14
    ekgo = 15
    ekgp = 16
    ekgq = 17

# .jqu
class jqu(IntFlag):
    ekhl = 0
    ekhm = 1
    ekhn = 2
    ekho = 3
    ekhp = 4
    ekhq = 5
    ekhr = 6
    ekhs = 7
    ekht = 8
    ekhu = 9
    ekhv = 10
    ekhw = 11

# .jqx
class jqx(IntFlag):
    ekib = 0
    ekic = 1
    ekid = 2
    ekie = 3
    ekif = 4
    ekig = 5
    ekih = 6
    ekii = 7

# .jqz
class jqz(IntFlag):
    ekit = 0
    ekiu = 1
    ekiv = 4

# .jrf
class jrf(IntFlag):
    ekkm = 0
    ekkn = 1

# .jrp
class jrp(IntFlag):
    eknc = 0
    eknd = 1
    ekne = 2
    eknf = 3
    ekng = 4

# .jrv
class jrv(IntFlag):
    ekon = 0
    ekoo = 1
    ekop = 2
    ekoq = 3
    ekor = 4

# .jry
class jry(IntFlag):
    ekow = 0
    ekox = 1
    ekoy = 2

# .jsc
class jsc(IntFlag):
    ekpl = 0

# .jsk
class jsk(IntFlag):
    ekrs = 0
    ekrt = 1
    ekru = 2
    ekrv = 3
    ekrw = 4
    ekrx = 5
    ekry = 6
    ekrz = 7
    eksa = 8
    eksb = 9
    eksc = 10
    eksd = 11

# .jso
class jso(IntFlag):
    eksg = 0
    eksh = 1
    eksi = 2

# .jta
class jta(IntFlag):
    ekvm = 0
    ekvn = 1

# .jte
class jte(IntFlag):
    ekvw = 0
    ekvx = 1

# .jtk
class jtk(IntFlag):
    ekwt = 0
    ekwu = 1
    ekwv = 2
    ekww = 3
    ekwx = 4
    ekwy = 5

# .jtx
class jtx(IntFlag):
    ekzk = 0
    ekzl = 1
    ekzm = 3

# .jtx
class jtx(IntFlag):
    ekzn = 0

# .jug
class jug(IntFlag):
    elbr = 0
    elbs = 1

# .juk
class juk(IntFlag):
    elca = 0
    elcb = 1
    elcc = 2

# .jux
class jux(IntFlag):
    eley = 0
    elez = 1
    elfa = 2

# .jve
class jve(IntFlag):
    elga = 0
    elgb = 1
    elgc = 2
    elgd = 3
    elge = 4
    elgf = 5
    elgg = 6
    elgh = 7

# .jvi
class jvi(IntFlag):
    elgv = 0

# .jvp
class jvp(IntFlag):
    elhu = 0
    elhv = 1
    elhw = 2
    elhx = 3
    elhy = 4
    elhz = 5
    elia = 6
    elib = 7
    elic = 8
    elid = 9
    elie = 10
    elif = 11
    elig = 12
    elih = 13
    elii = 14
    elij = 15
    elik = 16
    elil = 17
    elim = 18
    elin = 19
    elio = 20
    elip = 21
    eliq = 22
    elir = 23
    elis = 24
    elit = 25
    eliu = 26
    eliv = 27
    eliw = 28
    elix = 29
    eliy = 30
    eliz = 31
    elja = 32
    eljb = 33
    eljc = 34

# .jvt
class jvt(IntFlag):
    eljk = 0
    eljl = 1
    eljm = 2

# .jvx
class jvx(IntFlag):
    elkh = 0
    elki = 1
    elkj = 2
    elkk = 3

# .jvy
class jvy(IntFlag):
    elkl = 0
    elkm = 1
    elkn = 2
    elko = 3
    elkp = 4
    elkq = 5
    elkr = 6

# .jvz
class jvz(IntFlag):
    elks = 0
    elkt = 1

# .jwa
class jwa(IntFlag):
    elku = 0
    elkv = 1

# .jwb
class jwb(IntFlag):
    elkw = 0
    elkx = 1
    elky = 2
    elkz = 3

# .jwc
class jwc(IntFlag):
    ella = 0
    ellb = 1
    ellc = 2
    elld = 3
    elle = 4

# .jwd
class jwd(IntFlag):
    ellf = 0
    ellg = 1

# .jwe
class jwe(IntFlag):
    ellh = 0
    elli = 1
    ellj = 2
    ellk = 3
    elll = 4
    ellm = 5
    elln = 6

# .jwf
class jwf(IntFlag):
    ello = 0
    ellp = 1
    ellq = 2
    ellr = 3
    ells = 4
    ellt = 5
    ellu = 6

# .jwg
class jwg(IntFlag):
    ellv = 0
    ellw = 1
    ellx = 2
    elly = 3
    ellz = 4
    elma = 5
    elmb = 6
    elmc = 7
    elmd = 8
    elme = 9
    elmf = 10
    elmg = 11
    elmh = 12
    elmi = 13
    elmj = 14
    elmk = 15
    elml = 16
    elmm = 17
    elmn = 18

# .jwh
class jwh(IntFlag):
    elmo = 0
    elmp = 1
    elmq = 2
    elmr = 3
    elms = 4
    elmt = 5
    elmu = 6
    elmv = 7
    elmw = 8
    elmx = 9
    elmy = 10
    elmz = 11
    elna = 12
    elnb = 13
    elnc = 14
    elnd = 15

# .jwi
class jwi(IntFlag):
    elne = 0
    elnf = 1
    elng = 2
    elnh = 3
    elni = 4
    elnj = 5
    elnk = 6
    elnl = 7
    elnm = 8
    elnn = 9
    elno = 10
    elnp = 11
    elnq = 12
    elnr = 13
    elns = 14
    elnt = 15
    elnu = 16
    elnv = 17
    elnw = 18
    elnx = 19
    elny = 20
    elnz = 21
    eloa = 22
    elob = 23
    eloc = 24
    elod = 25
    eloe = 26
    elof = 27
    elog = 28
    eloh = 29

# .jwj
class jwj(IntFlag):
    eloi = 0
    eloj = 1
    elok = 2
    elol = 3
    elom = 4
    elon = 5
    eloo = 6
    elop = 7
    eloq = 8
    elor = 9
    elos = 10

# .jwk
class jwk(IntFlag):
    elot = 0
    elou = 1
    elov = 2
    elow = 3
    elox = 4
    eloy = 5

# .jwl
class jwl(IntFlag):
    eloz = 0
    elpa = 1
    elpb = 2
    elpc = 3

# .jwm
class jwm(IntFlag):
    elpd = 0
    elpe = 1
    elpf = 2
    elpg = 3
    elph = 4

# .jwn
class jwn(IntFlag):
    elpi = 0
    elpj = 1
    elpk = 2

# .jwo
class jwo(IntFlag):
    elpl = 0
    elpm = 1
    elpn = 2
    elpo = 3

# .jwp
class jwp(IntFlag):
    elpp = 0
    elpq = 1

# .jwq
class jwq(IntFlag):
    elpr = 0
    elps = 1

# .jwr
class jwr(IntFlag):
    elpt = 0
    elpu = 1
    elpv = 2
    elpw = 3
    elpx = 4
    elpy = 5
    elpz = 6
    elqa = 7

# .jws
class jws(IntFlag):
    elqb = 0
    elqc = 1
    elqd = 2
    elqe = 3

# .jwt
class jwt(IntFlag):
    elqf = 0
    elqg = 1
    elqh = 2
    elqi = 3
    elqj = 4
    elqk = 5
    elql = 6
    elqm = 7
    elqn = 8
    elqo = 9
    elqp = 10
    elqq = 11

# .jwu
class jwu(IntFlag):
    elqr = 0
    elqs = 1
    elqt = 2
    elqu = 3

# .jwv
class jwv(IntFlag):
    elqv = 0
    elqw = 1
    elqx = 2

# .jww
class jww(IntFlag):
    elqy = 0
    elqz = 1
    elra = 2

# .jwx
class jwx(IntFlag):
    elrb = 0
    elrc = 1
    elrd = 2
    elre = 3
    elrf = 4
    elrg = 5

# .jwy
class jwy(IntFlag):
    elrh = 0
    elri = 1
    elrj = 2
    elrk = 3
    elrl = 4
    elrm = 5
    elrn = 6
    elro = 7
    elrp = 8
    elrq = 9
    elrr = 10

# .jwz
class jwz(IntFlag):
    elrs = 0
    elrt = 1
    elru = 2

# .jxa
class jxa(IntFlag):
    elrv = 0
    elrw = 1
    elrx = 2
    elry = 3

# .jxb
class jxb(IntFlag):
    elrz = 0
    elsa = 1
    elsb = 2

# .jxc
class jxc(IntFlag):
    elsc = 0
    elsd = 1
    else = 2
    elsf = 3
    elsg = 4
    elsh = 5
    elsi = 6
    elsj = 7
    elsk = 8

# .jxd
class jxd(IntFlag):
    elsl = 0
    elsm = 1
    elsn = 2
    elso = 3

# .jxe
class jxe(IntFlag):
    elsp = 0
    elsq = 1
    elsr = 2
    elss = 3
    elst = 4
    elsu = 5
    elsv = 6
    elsw = 7
    elsx = 8
    elsy = 9
    elsz = 10
    elta = 11
    eltb = 12
    eltc = 13
    eltd = 14
    elte = 15
    eltf = 16
    eltg = 17
    elth = 18
    elti = 19
    eltj = 20

# .jxf
class jxf(IntFlag):
    eltk = 0
    eltl = 1

# .jxg
class jxg(IntFlag):
    eltm = 0
    eltn = 1
    elto = 2
    eltp = 3
    eltq = 4
    eltr = 5
    elts = 6

# .jxl
class jxl(IntFlag):
    eluu = 0

# .jxp
class jxp(IntFlag):
    elwf = 0
    elwg = 1
    elwh = 4
    elwi = 5

# .jye
class jye(IntFlag):
    elxp = 0
    elxq = 1
    elxr = 5

# .jye
class jye(IntFlag):
    elxs = 0
    elxt = 1
    elxu = 2
    elxv = 3

# .jym
class jym(IntFlag):
    embg = 0
    embh = 1
    embi = 2
    embj = 3
    embk = 4
    embl = 5
    embm = 6

# .jyt
class jyt(IntFlag):
    emdf = 0
    emdg = 1

# .jyx
class jyx(IntFlag):
    emdy = 0
    emdz = 1
    emea = 2

# .jzt
class jzt(IntFlag):
    emfw = 0
    emfx = 1
    emfy = 4
    emfz = 5

# .jzt
class jzt(IntFlag):
    emga = 0
    emgb = 2
    emgc = 3

# .jzt
class jzt(IntFlag):
    emih = 0
    emii = 1
    emij = 2
    emik = 3

# .jzw
class jzw(IntFlag):
    emjz = 0
    emka = 4
    emkb = 5
    emkc = 6
    emkd = 9

# .kac
class kac(IntFlag):
    emmh = 0
    emmi = 1

# .kai
class kai(IntFlag):
    emmr = 0
    emms = 1
    emmt = 3

# .kao
class kao(IntFlag):
    empx = 0
    empy = 1

# .kav
class kav(IntFlag):
    emrg = 0
    emrh = 1
    emri = 2
    emrj = 3
    emrk = 4
    emrl = 5

# .kbe
class kbe(IntFlag):
    emtp = 0
    emtq = 1
    emtr = 2

# .kbg
class kbg(IntFlag):
    emuk = 0
    emul = 1
    emum = 2

# .kdr
class kdr(IntFlag):
    emxs = 0
    emxt = 1
    emxu = 3

# .kdr
class kdr(IntFlag):
    emxv = 0
    emxw = 1
    emxx = 2
    emxy = 3
    emxz = 4
    emya = 5
    emyb = 6
    emyc = 7

# .kdr
class kdr(IntFlag):
    emyd = 0
    emye = 2
    emyf = 3

# .kdr
class kdr(IntFlag):
    emyg = 0
    emyh = 1
    emyi = 2
    emyj = 3
    emyk = 4
    emyl = 5
    emym = 6
    emyn = 7
    emyo = 8
    emyp = 9

# .kdr
class kdr(IntFlag):
    enae = 0
    enaf = 1
    enag = 2
    enah = 3
    enai = 4
    enaj = 5
    enak = 6

# .kdr
class kdr(IntFlag):
    enha = 0
    enhb = 2
    enhc = 5
    enhd = 8

# .kdr
class kdr(IntFlag):
    enhe = 0
    enhf = 2
    enhg = 4

# .kdr
class kdr(IntFlag):
    enhh = 0
    enhi = 1
    enhj = 2
    enhk = 3
    enhl = 4
    enhm = 5
    enhn = 6

# .kdr
class kdr(IntFlag):
    eniz = 0
    enja = 1
    enjb = 2

# .kdx
class kdx(IntFlag):
    ennq = 0
    ennr = 1
    enns = 2
    ennt = 5
    ennu = 6

# .ked
class ked(IntFlag):
    enoz = 0
    enpa = 1
    enpb = 2
    enpc = 3
    enpd = 4
    enpe = 5

# .kej
class kej(IntFlag):
    enqc = 0
    enqd = 1
    enqe = 3

# .kfl
class kfl(IntFlag):
    enro = 0
    enrp = 2
    enrq = 3

# .kfl
class kfl(IntFlag):
    enrr = 0
    enrs = 2
    enrt = 4
    enru = 5

# .kfl
class kfl(IntFlag):
    ento = 0
    entp = 2
    entq = 4
    entr = 6
    ents = 7

# .kfl
class kfl(IntFlag):
    entt = 0
    entu = 1
    entv = 2
    entw = 5

# .kfl
class kfl(IntFlag):
    entx = 0
    enty = 1
    entz = 2

# .kfp
class kfp(IntFlag):
    enyf = 0
    enyg = 1
    enyh = 2
    enyi = 3
    enyj = 4

# .kgb
class kgb(IntFlag):
    eoco = 0
    eocp = 1
    eocq = 2
    eocr = 3
    eocs = 4
    eoct = 5

# .kgf
class kgf(IntFlag):
    eoef = 0
    eoeg = 1
    eoeh = 2
    eoei = 3
    eoej = 4
    eoek = 5
    eoel = 6
    eoem = 7

# .kgf
class kgf(IntFlag):
    eoen = 0
    eoeo = 1
    eoep = 2
    eoeq = 3

# .kgh
class kgh(IntFlag):
    eofx = 0
    eofy = 2
    eofz = 6

# .kgp
class kgp(IntFlag):
    eoim = 0
    eoin = 1
    eoio = 2
    eoip = 3
    eoiq = 4
    eoir = 5

# .kgp
class kgp(IntFlag):
    eois = 0
    eoit = 1
    eoiu = 2

# .kgu
class kgu(IntFlag):
    eokz = 0
    eola = 1
    eolb = 2
    eolc = 3

# .khm
class khm(IntFlag):
    eooe = 0
    eoof = 2
    eoog = 3
    eooh = 4
    eooi = 6
    eooj = 7
    eook = 8
    eool = 9
    eoom = 10
    eoon = 11

# .khm
class khm(IntFlag):
    eopa = 0
    eopb = 1
    eopc = 2
    eopd = 3
    eope = 4

# .kho
class kho(IntFlag):
    eosd = 0
    eose = 1
    eosf = 2
    eosg = 3
    eosh = 4
    eosi = 5
    eosj = 7
    eosk = 8

# .khr
class khr(IntFlag):
    eosy = 0
    eosz = 1
    eota = 2
    eotb = 3
    eotc = 4
    eotd = 6
    eote = 7
    eotf = 9
    eotg = 10
    eoth = 11
    eoti = 12
    eotj = 13
    eotk = 14

# .ki
class ki(IntFlag):
    cvgy = 0
    cvgz = 1
    cvha = 2

# .kie
class kie(IntFlag):
    eotw = 0
    eotx = 1
    eoty = 2
    eotz = 5
    eoua = 6

# .kie
class kie(IntFlag):
    eouj = 0
    eouk = 1
    eoul = 2
    eoum = 3
    eoun = 4
    eouo = 5
    eoup = 6
    eouq = 7

# .kie
class kie(IntFlag):
    eove = 0
    eovf = 1
    eovg = 2
    eovh = 3
    eovi = 4
    eovj = 5
    eovk = 6
    eovl = 7
    eovm = 8

# .kjq
class kjq(IntFlag):
    epbd = 0
    epbe = 2
    epbf = 3
    epbg = 4
    epbh = 5
    epbi = 6
    epbj = 8
    epbk = 9
    epbl = 10
    epbm = 11
    epbn = 12
    epbo = 13
    epbp = 14

# .kjq
class kjq(IntFlag):
    epbq = 0
    epbr = 1
    epbs = 2

# .kjq
class kjq(IntFlag):
    epcj = 0
    epck = 1
    epcl = 2

# .kjq
class kjq(IntFlag):
    epcy = 0
    epcz = 1
    epda = 2

# .kjq
class kjq(IntFlag):
    epdb = 0

# .kjq
class kjq(IntFlag):
    epdu = 0
    epdv = 1
    epdw = 2

# .kjq
class kjq(IntFlag):
    epfb = 0
    epfc = 1
    epfd = 2
    epfe = 3
    epff = 4
    epfg = 5
    epfh = 6

# .kjq
class kjq(IntFlag):
    epge = 0
    epgf = 1
    epgg = 2
    epgh = 3
    epgi = 4
    epgj = 5
    epgk = 6
    epgl = 7
    epgm = 8

# .kkf
class kkf(IntFlag):
    eplz = 0
    epma = 1
    epmb = 4

# .kkf
class kkf(IntFlag):
    epmx = 0
    epmy = 1
    epmz = 2

# .kkv
class kkv(IntFlag):
    eprp = 0
    eprq = 1
    eprr = 2
    eprs = 3
    eprt = 4
    epru = 5
    eprv = 6
    eprw = 7
    eprx = 8

# .klb
class klb(IntFlag):
    epuh = 0
    epui = 2
    epuj = 4
    epuk = 5
    epul = 6

# .klf
class klf(IntFlag):
    epvt = 0
    epvu = 1
    epvv = 2
    epvw = 3
    epvx = 4

# .kly
class kly(IntFlag):
    eqcx = 0
    eqcy = 1
    eqcz = 2
    eqda = 3
    eqdb = 4
    eqdc = 5
    eqdd = 6

# .kme
class kme(IntFlag):
    eqeq = 0
    eqer = 1
    eqes = 2
    eqet = 3
    eqeu = 4
    eqev = 5
    eqew = 6
    eqex = 7
    eqey = 8
    eqez = 10
    eqfa = 11
    eqfb = 12
    eqfc = 13

# .kmk
class kmk(IntFlag):
    eqhm = 0
    eqhn = 1
    eqho = 2
    eqhp = 3
    eqhq = 4
    eqhr = 5
    eqhs = 6

# .kmq
class kmq(IntFlag):
    eqio = 0
    eqip = 1
    eqiq = 2
    eqir = 3
    eqis = 4
    eqit = 5
    eqiu = 6
    eqiv = 7
    eqiw = 8
    eqix = 9
    eqiy = 10
    eqiz = 11
    eqja = 12
    eqjb = 13
    eqjc = 14
    eqjd = 15

# .kmx
class kmx(IntFlag):
    eqku = 0
    eqkv = 1

# .knb
class knb(IntFlag):
    eqlh = 0
    eqli = 1
    eqlj = 2
    eqlk = 3
    eqll = 4
    eqlm = 5
    eqln = 6
    eqlo = 7
    eqlp = 8

# .kng
class kng(IntFlag):
    eqmg = 0
    eqmh = 1
    eqmi = 2

# .kni
class kni(IntFlag):
    eqmq = 0
    eqmr = 1
    eqms = 2
    eqmt = 3
    eqmu = 4

# .knn
class knn(IntFlag):
    eqmv = 0
    eqmw = 1
    eqmx = 2

# .knq
class knq(IntFlag):
    eqnz = 0
    eqoa = 1
    eqob = 2

# .kou
class kou(IntFlag):
    eqpy = 0
    eqpz = 1
    eqqa = 2
    eqqb = 3
    eqqc = 4

# .kou
class kou(IntFlag):
    eqsi = 0
    eqsj = 1
    eqsk = 2
    eqsl = 3
    eqsm = 4
    eqsn = 5

# .kou
class kou(IntFlag):
    eqsq = 0

# .kox
class kox(IntFlag):
    eque = 0
    equf = 1
    equg = 2
    equh = 3

# .kpx
class kpx(IntFlag):
    erba = 0
    erbb = 1
    erbc = 2
    erbd = 3
    erbe = 4
    erbf = 5
    erbg = 6
    erbh = 7
    erbi = 8

# .kqc
class kqc(IntFlag):
    ercb = 0
    ercc = 1

# .kqn
class kqn(IntFlag):
    eref = 0
    ereg = 1
    ereh = 3

# .kqs
class kqs(IntFlag):
    erfm = 0
    erfn = 1
    erfo = 2

# .krj
class krj(IntFlag):
    erju = 0
    erjv = 1
    erjw = 2

# .krk
class krk(IntFlag):
    erjx = 0
    erjy = 1
    erjz = 2
    erka = 3
    erkb = 4
    erkc = 5
    erkd = 6
    erke = 7
    erkf = 8
    erkg = 9
    erkh = 10
    erki = 11
    erkj = 12
    erkk = 13
    erkl = 14
    erkm = 15
    erkn = 16
    erko = 17
    erkp = 18
    erkq = 19
    erkr = 20
    erks = 21
    erkt = 22
    erku = 23
    erkv = 24
    erkw = 25

# .krp
class krp(IntFlag):
    erlf = 0

# .ksv
class ksv(IntFlag):
    ervm = 0
    ervn = 1
    ervo = 2
    ervp = 3
    ervq = 4

# .ktc
class ktc(IntFlag):
    erxb = 0
    erxc = 1
    erxd = 2
    erxe = 3
    erxf = 4

# .ktv
class ktv(IntFlag):
    esbj = 0
    esbk = 1
    esbl = 2
    esbm = 3
    esbn = 4
    esbo = 5
    esbp = 6
    esbq = 7
    esbr = 8

# .ktz
class ktz(IntFlag):
    esch = 0
    esci = 1
    escj = 2
    esck = 3
    escl = 4
    escm = 5

# .ku
class ku(IntFlag):
    cvil = 1
    cvim = 2
    cvin = 4
    cvio = 8
    cvip = 16
    cviq = 32
    cvir = 64
    cvis = 128

# .kuc
class kuc(IntFlag):
    esda = 0
    esdb = 1
    esdc = 2
    esdd = 3
    esde = 4
    esdf = 5
    esdg = 6
    esdh = 7
    esdi = 8

# .kuy
class kuy(IntFlag):
    esie = 0
    esif = 1
    esig = 2
    esih = 3
    esii = 4
    esij = 5
    esik = 6

# .kwe
class kwe(IntFlag):
    esoj = 0
    esok = 1
    esol = 2
    esom = 3
    eson = 4

# .kxo
class kxo(IntFlag):
    esxd = 0
    esxe = 1
    esxf = 2

# .kxo
class kxo(IntFlag):
    esxg = 0
    esxh = 1
    esxi = 2
    esxj = 3

# .kxx
class kxx(IntFlag):
    etam = 0
    etan = 1
    etao = 2
    etap = 3
    etaq = 4
    etar = 5

# .kzd
class kzd(IntFlag):
    ethx = 0
    ethy = 1
    ethz = 2

# .kzg
class kzg(IntFlag):
    etjm = 0
    etjn = 1
    etjo = 2
    etjp = 3
    etjq = 4

# .kzo
class kzo(IntFlag):
    etkp = 0
    etkq = 1
    etkr = 2

# .kzo
class kzo(IntFlag):
    etks = 0

# .kzw
class kzw(IntFlag):
    etmb = 0
    etmc = 1

# .lbf
class lbf(IntFlag):
    ettt = 0
    ettu = 1
    ettv = 2
    ettw = 3
    ettx = 4
    etty = 5
    ettz = 6

# .lbf
class lbf(IntFlag):
    etua = 0
    etub = 1
    etuc = 2
    etud = 3
    etue = 4
    etuf = 5

# .lbj
class lbj(IntFlag):
    etuv = 0
    etuw = 1
    etux = 2
    etuy = 3
    etuz = 4
    etva = 5

# .lbj
class lbj(IntFlag):
    etvb = 0
    etvc = 1
    etvd = 2
    etve = 3
    etvf = 4
    etvg = 5
    etvh = 6
    etvi = 7
    etvj = 8

# .lbq
class lbq(IntFlag):
    etwl = 0
    etwm = 1
    etwn = 2
    etwo = 3
    etwp = 4
    etwq = 5
    etwr = 6

# .lbs
class lbs(IntFlag):
    etws = 0
    etwt = 1
    etwu = 2
    etwv = 3

# .lbu
class lbu(IntFlag):
    etxd = 0
    etxe = 2
    etxf = 3
    etxg = 4
    etxh = 5
    etxi = 6
    etxj = 7
    etxk = 8

# .lbw
class lbw(IntFlag):
    etxy = 0
    etxz = 2
    etya = 3
    etyb = 4
    etyc = 5
    etyd = 6
    etye = 7

# .lby
class lby(IntFlag):
    etyr = 0
    etys = 1

# .lcd
class lcd(IntFlag):
    etzg = 0
    etzh = 3
    etzi = 4

# .lcq
class lcq(IntFlag):
    euaj = 0
    euak = 1
    eual = 2

# .lcq
class lcq(IntFlag):
    eubs = 0
    eubt = 1
    eubu = 2
    eubv = 3
    eubw = 4
    eubx = 5
    euby = 6
    eubz = 7
    euca = 8
    eucb = 9
    eucc = 10
    eucd = 11
    euce = 12
    eucf = 13
    eucg = 14

# .lcw
class lcw(IntFlag):
    eudb = 0
    eudc = 1
    eudd = 2

# .lcw
class lcw(IntFlag):
    eude = 0
    eudf = 1
    eudg = 2
    eudh = 3

# .ldc
class ldc(IntFlag):
    euen = 0
    eueo = 1
    euep = 2
    eueq = 3

# .ldf
class ldf(IntFlag):
    eufa = 0
    eufb = 1

# .ldi
class ldi(IntFlag):
    eufo = 0
    eufp = 2
    eufq = 3

# .ldp
class ldp(IntFlag):
    eugn = 0
    eugo = 1

# .ldp
class ldp(IntFlag):
    eugp = 0
    eugq = 1
    eugr = 2
    eugs = 3
    eugt = 4
    eugu = 5
    eugv = 6
    eugw = 7
    eugx = 8
    eugy = 9
    eugz = 10
    euha = 11
    euhb = 12
    euhc = 13
    euhd = 14
    euhe = 15
    euhf = 16
    euhg = 17
    euhh = 18

# .ldx
class ldx(IntFlag):
    euhw = 0
    euhx = 1
    euhy = 2

# .ldx
class ldx(IntFlag):
    euhz = 0
    euia = 1

# .lef
class lef(IntFlag):
    eujb = 0
    eujc = 1
    eujd = 2

# .lef
class lef(IntFlag):
    eujj = 0
    eujk = 1
    eujl = 2
    eujm = 3

# .mc
class mc(IntFlag):
    cvta = 0
    cvtb = 1
    cvtc = 2
    cvtd = 3
    cvte = 4

# .mo
class mo(IntFlag):
    cvuw = 0
    cvux = 1
    cvuy = 2
    cvuz = 4
    cvva = 8
    cvvb = 16
    cvvc = 32
    cvvd = 64
    cvve = 128

# .of
class of(IntFlag):
    cvzw = -1
    cvzx = 2
    cvzy = 3
    cvzz = 4
    cwaa = 5
    cwab = 22
    cwac = 19
    cwad = 271
    cwae = 7
    cwaf = 8
    cwag = 6

# .pc
class pc(IntFlag):
    cwbp = 0
    cwbq = 1
    cwbr = 2
    cwbs = 3

# .pg
class pg(IntFlag):
    cwbw = -4
    cwbx = -3
    cwby = -2
    cwbz = -1
    cwca = 0
    cwcb = 1
    cwcc = 2
    cwcd = 3
    cwce = 4
    cwcf = 5
    cwcg = 6
    cwch = 7

# .qi
class qi(IntFlag):
    cxjy = 0
    cxjz = 1
    cxka = 2

# .qo
class qo(IntFlag):
    cxma = 0
    cxmb = 1
    cxmc = 2
    cxmd = 3

# .rb
class rb(IntFlag):
    cxra = 0
    cxrb = 1
    cxrc = 2
    cxrd = 3
    cxre = 4
    cxrf = 5
    cxrg = 6
    cxrh = 7

# .sa
class sa(IntFlag):
    cxyw = 0
    cxyx = 1

# .so
class so(IntFlag):
    cygj = 0
    cygk = 1
    cygl = 2
    cygm = 3
    cygn = 4
    cygo = 5
    cygp = 6
    cygq = 7
    cygr = -1

# .sq
class sq(IntFlag):
    cygz = 0
    cyha = 1
    cyhb = 2
    cyhc = 3
    cyhd = 4
    cyhe = 5
    cyhf = 6
    cyhg = 7
    cyhh = 8
    cyhi = 9
    cyhj = 10
    cyhk = 11
    cyhl = 12
    cyhm = 13
    cyhn = 14
    cyho = 15
    cyhp = 16
    cyhq = 17
    cyhr = 18
    cyhs = 19
    cyht = 20
    cyhu = 21
    cyhv = 22
    cyhw = 23
    cyhx = 24

# .ss
class ss(IntFlag):
    cyik = 0
    cyil = 1
    cyim = 2
    cyin = 3

# .string
class string(IntFlag):
    Head = 0
    Tail = 1
    Both = 2

# .tz
class tz(IntFlag):
    Bandeau_ = 0
    BandeauB_ = 1
    Barbe_ = 2
    Chapeau_ = 3
    ChapeauB_ = 4
    cheveux_ = 5
    Frange_ = 20
    Custo_ = 6
    Oreille_d_ = 7
    Oreille_g_ = 8
    Oreille_ = 9
    Oreille_b_ = 10
    Masque_ = 11
    MasqueB_ = 12
    NatteHaute_ = 13
    Natte_ = 16
    NatteB_ = 17
    Natte_Basse_ = 19
    Patte_d_ = 14
    Patte_g_ = 15
    Patte_0 = 18
    Tete_OL_ = 21

# .ua
class ua(IntFlag):
    cyoh = 0
    cyoi = 1
    cyoj = 2
    cyok = 4
    cyol = 8
    cyom = 16
    cyon = 32
    cyoo = 64
    cyop = 128
    cyoq = 256
    cyor = 512
    cyos = 1024
    cyot = 2048
    cyou = 4096
    cyov = 8192
    cyow = 16384
    cyox = 32768
    cyoy = 65536
    cyoz = 131072

# .ub
class ub(IntFlag):
    cypa = 0
    cypb = 5
    cypc = 65
    cypd = 32769
    cype = 32833

# .uo
class uo(IntFlag):
    cysd = 0
    cyse = 1
    cysf = 2
    cysg = 3
    cysh = 4
    cysi = 5
    cysj = 6
    cysk = 7
    cysl = 8

# .uu
class uu(IntFlag):
    cytp = 0
    cytq = 1
    cytr = 2

# .vj
class vj(IntFlag):
    cyvx = 0
    cyvy = 1
    cyvz = 2
    cywa = 4
    cywb = 8
    cywc = 16
    cywd = 32
    cywe = 255

# .vn
class vn(IntFlag):
    cywr = -1
    cyws = 0
    cywt = 1
    cywu = 2

# .vo
class vo(IntFlag):
    cywy = 0
    cywz = 1
    cyxa = 2
    cyxb = 3
    cyxc = 4

# .vt
class vt(IntFlag):
    cyzx = 0
    cyzy = 1
    cyzz = 2
    czaa = 3
    czab = 4
    czac = 5
    czad = 6
    czae = 7

# .vy
class vy(IntFlag):
    czar = 0
    czas = 1
    czat = 2
    czau = 3

# .wd
class wd(IntFlag):
    czei = 0
    czej = 1
    czek = 2
    czel = 3

# .we
class we(IntFlag):
    czeo = 0
    czep = 1
    czeq = 2
    czer = 3
    czes = 4
    czet = 5
    czeu = 6
    czev = 7
    czew = 8
    czex = 9
    czey = 10

# .xi
class xi(IntFlag):
    czjd = 0
    czje = 1
    czjf = 2
    czjg = 3

