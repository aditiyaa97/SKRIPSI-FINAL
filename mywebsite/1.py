from PIL import Image, ImageEnhance
import pytesseract
import datetime

im = Image.open('Proposal_Aditiya.jpeg')
print(im)

def kode1():
    kode1x1 = 2008.17
    kode1y1 = 99.9658
    kode1x2 = 2378.5
    kode1y2 = 158.305
    kode1 = im.crop((kode1x1,kode1y1,kode1x2,kode1y2))
    var1 = (pytesseract.image_to_string(kode1))
    print(var1)
    if(var1=="HW01"):
        print("Printed circuit boards")
    elif(var1=="HW02"):
        print("Communication hardware, interfaces and storage")
    elif(var1=="HW03"):
        print("Integrated circuits")
    elif(var1=="HW04"):
        print("Very large scale integration design")
    elif(var1=="HW05"):
        print("Power and energy")
    elif(var1=="HW06"):
        print("Electronic design automation")
    elif(var1=="HW07"):
        print("Hardware validation")
    elif(var1=="HW08"):
        print("Hardware test")
    elif(var1=="HW09"):
        print("Robustness")
    elif(var1=="HW10"):
        print("RobusEmerging technologiestness")
    elif(var1=="CO01"):
        print("Architectures")
    elif(var1=="CO02"):
        print("Embedded and cyber-physical systems")
    elif(var1=="CO03"):
        print("Real-time systems")
    elif(var1=="CO04"):
        print("Dependable and fault-tolerant systems and networks")
    elif(var1=="NW01"):
        print("Network architectures")
    elif(var1=="NW02"):
        print("Network protocols")
    elif(var1=="NW03"):
        print("Network components")
    elif(var1=="NW04"):
        print("Network algorithms")
    elif(var1=="NW05"):
        print("Network performance evaluation")
    elif(var1=="NW06"):
        print("Network properties")
    elif(var1=="NW07"):
        print("Network services")
    elif(var1=="NW08"):
        print("Network types")
    elif(var1=="SE01"):
        print("Software organization and properties")
    elif(var1=="SE02"):
        print("Software notations and tools")
    elif(var1=="SE03"):
        print("Software creation and management")
    elif(var1=="TC01"):
        print("Models of computation")
    elif(var1=="TC02"):
        print("Formal languages and automata theory")
    elif(var1=="TC03"):
        print("Computational complexity and cryptography")
    elif(var1=="TC04"):
        print("Logic")
    elif(var1=="TC05"):
        print("Design and analysis of algorithms")
    elif(var1=="TC06"):
        print("Randomness, geometry and discrete structures")
    elif(var1=="TC07"):
        print("Theory and algorithms for application domains")
    elif(var1=="TC08"):
        print("Semantics and reasoning")
    elif(var1=="MC01"):
        print("Discrete mathematics")
    elif(var1=="MC02"):
        print("Probability and statistics")
    elif(var1=="MC03"):
        print("Mathematical software")
    elif(var1=="MC04"):
        print("Information theory")
    elif(var1=="MC05"):
        print("Mathematical analysis")
    elif(var1=="MC06"):
        print("Continuous mathematics")
    elif(var1=="IS01"):
        print("Data management systems")
    elif(var1=="IS02"):
        print("Information storage systems")
    elif(var1=="IS03"):
        print("Information systems applications")
    elif(var1=="IS04"):
        print("World Wide Web")
    elif(var1=="IS05"):
        print("Information retrieval")
    elif(var1=="SP01"):
        print("Cryptography")
    elif(var1=="SP02"):
        print("Formal methods and theory of security")
    elif(var1=="SP03"):
        print("Security services")
    elif(var1=="SP04"):
        print("Intrusion/anomaly detection and malware mitigation")
    elif(var1=="SP05"):
        print("Security in hardware")
    elif(var1=="SP06"):
        print("Systems security")
    elif(var1=="SP07"):
        print("Network security")
    elif(var1=="SP08"):
        print("Database and storage security")
    elif(var1=="SP09"):
        print("Software and application security")
    elif(var1=="SP10"):
        print("Human and societal aspects of security and privacy")
    elif(var1=="HC01"):
        print("Human computer interaction")
    elif(var1=="HC02"):
        print("Interaction design")
    elif(var1=="HC03"):
        print("Collaborative and social computing")
    elif(var1=="HC04"):
        print("Ubiquitous and mobile computing")
    elif(var1=="HC05"):
        print("Visualization")
    elif(var1=="HC06"):
        print("Accessibility")
    elif(var1=="CM01"):
        print("Symbolic and algebraic manipulation")
    elif(var1=="CM02"):
        print("Parallel computing methodologies")
    elif(var1=="CM03"):
        print("Artificial intelligence")
    elif(var1=="CM04"):
        print("Machine learning")
    elif(var1=="CM05"):
        print("Modeling and simulation")
    elif(var1=="CM06"):
        print("Computer graphics")
    elif(var1=="CM07"):
        print("Distributed computing methodologies")
    elif(var1=="CM08"):
        print("Concurrent computing methodologies")
    elif(var1=="AC01"):
        print("Electronic commerce")
    elif(var1=="AC02"):
        print("Enterprise computing")
    elif(var1=="AC03"):
        print("Physical sciences and engineering")
    elif(var1=="AC04"):
        print("Life and medical sciences")
    elif(var1=="AC05"):
        print("Law, social and behavioral sciences")
    elif(var1=="AC06"):
        print("Computer forensics")
    elif(var1=="AC07"):
        print("Arts and humanities")
    elif(var1=="AC08"):
        print("Computers in other domains")
    elif(var1=="AC09"):
        print("Operations research")
    elif(var1=="AC10"):
        print("Education")
    elif(var1=="AC11"):
        print("Document management and text processing")
    else:
        print("Kode Penelitian tidak ditemukan")
    
def kode2():
    kode2x1 = 2155
    kode2y1 = 175
    kode2x2 = 2240
    kode2y2 = 220
    kode2 = im.crop((kode2x1,kode2y1,kode2x2,kode2y2))
    var_kode2 = (pytesseract.image_to_string(kode2))
    kode2_replace = (var_kode2.replace("O","0"))
    print(kode2_replace)
    if(kode2_replace=="HW01"):
        print("Printed circuit boards")
    elif(kode2_replace=="HW02"):
        print("Communication hardware, interfaces and storage")
    elif(kode2_replace=="HW03"):
        print("Integrated circuits")
    elif(kode2_replace=="HW04"):
        print("Very large scale integration design")
    elif(kode2_replace=="HW05"):
        print("Power and energy")
    elif(kode2_replace=="HW06"):
        print("Electronic design automation")
    elif(kode2_replace=="HW07"):
        print("Hardware validation")
    elif(kode2_replace=="HW08"):
        print("Hardware test")
    elif(kode2_replace=="HW09"):
        print("Robustness")
    elif(kode2_replace=="HW10"):
        print("RobusEmerging technologiestness")
    elif(kode2_replace=="CO01"):
        print("Architectures")
    elif(kode2_replace=="CO02"):
        print("Embedded and cyber-physical systems")
    elif(kode2_replace=="CO03"):
        print("Real-time systems")
    elif(kode2_replace=="CO04"):
        print("Dependable and fault-tolerant systems and networks")
    elif(kode2_replace=="NW01"):
        print("Network architectures")
    elif(kode2_replace=="NW02"):
        print("Network protocols")
    elif(kode2_replace=="NW03"):
        print("Network components")
    elif(kode2_replace=="NW04"):
        print("Network algorithms")
    elif(kode2_replace=="NW05"):
        print("Network performance evaluation")
    elif(kode2_replace=="NW06"):
        print("Network properties")
    elif(kode2_replace=="NW07"):
        print("Network services")
    elif(kode2_replace=="NW08"):
        print("Network types")
    elif(kode2_replace=="SE01"):
        print("Software organization and properties")
    elif(kode2_replace=="SE02"):
        print("Software notations and tools")
    elif(kode2_replace=="SE03"):
        print("Software creation and management")
    elif(kode2_replace=="TC01"):
        print("Models of computation")
    elif(kode2_replace=="TC02"):
        print("Formal languages and automata theory")
    elif(kode2_replace=="TC03"):
        print("Computational complexity and cryptography")
    elif(kode2_replace=="TC04"):
        print("Logic")
    elif(kode2_replace=="TC05"):
        print("Design and analysis of algorithms")
    elif(kode2_replace=="TC06"):
        print("Randomness, geometry and discrete structures")
    elif(kode2_replace=="TC07"):
        print("Theory and algorithms for application domains")
    elif(kode2_replace=="TC08"):
        print("Semantics and reasoning")
    elif(kode2_replace=="MC01"):
        print("Discrete mathematics")
    elif(kode2_replace=="MC02"):
        print("Probability and statistics")
    elif(kode2_replace=="MC03"):
        print("Mathematical software")
    elif(kode2_replace=="MC04"):
        print("Information theory")
    elif(kode2_replace=="MC05"):
        print("Mathematical analysis")
    elif(kode2_replace=="MC06"):
        print("Continuous mathematics")
    elif(kode2_replace=="IS01"):
        print("Data management systems")
    elif(kode2_replace=="IS02"):
        print("Information storage systems")
    elif(kode2_replace=="IS03"):
        print("Information systems applications")
    elif(kode2_replace=="IS04"):
        print("World Wide Web")
    elif(kode2_replace=="IS05"):
        print("Information retrieval")
    elif(kode2_replace=="SP01"):
        print("Cryptography")
    elif(kode2_replace=="SP02"):
        print("Formal methods and theory of security")
    elif(kode2_replace=="SP03"):
        print("Security services")
    elif(kode2_replace=="SP04"):
        print("Intrusion/anomaly detection and malware mitigation")
    elif(kode2_replace=="SP05"):
        print("Security in hardware")
    elif(kode2_replace=="SP06"):
        print("Systems security")
    elif(kode2_replace=="SP07"):
        print("Network security")
    elif(kode2_replace=="SP08"):
        print("Database and storage security")
    elif(kode2_replace=="SP09"):
        print("Software and application security")
    elif(kode2_replace=="SP10"):
        print("Human and societal aspects of security and privacy")
    elif(kode2_replace=="HC01"):
        print("Human computer interaction")
    elif(kode2_replace=="HC02"):
        print("Interaction design")
    elif(kode2_replace=="HC03"):
        print("Collaborative and social computing")
    elif(kode2_replace=="HC04"):
        print("Ubiquitous and mobile computing")
    elif(kode2_replace=="HC05"):
        print("Visualization")
    elif(kode2_replace=="HC06"):
        print("Accessibility")
    elif(kode2_replace=="CM01"):
        print("Symbolic and algebraic manipulation")
    elif(kode2_replace=="CM02"):
        print("Parallel computing methodologies")
    elif(kode2_replace=="CM03"):
        print("Artificial intelligence")
    elif(kode2_replace=="CM04"):
        print("Machine learning")
    elif(kode2_replace=="CM05"):
        print("Modeling and simulation")
    elif(kode2_replace=="CM06"):
        print("Computer graphics")
    elif(kode2_replace=="CM07"):
        print("Distributed computing methodologies")
    elif(kode2_replace=="CM08"):
        print("Concurrent computing methodologies")
    elif(kode2_replace=="AC01"):
        print("Electronic commerce")
    elif(kode2_replace=="AC02"):
        print("Enterprise computing")
    elif(kode2_replace=="AC03"):
        print("Physical sciences and engineering")
    elif(kode2_replace=="AC04"):
        print("Life and medical sciences")
    elif(kode2_replace=="AC05"):
        print("Law, social and behavioral sciences")
    elif(kode2_replace=="AC06"):
        print("Computer forensics")
    elif(kode2_replace=="AC07"):
        print("Arts and humanities")
    elif(kode2_replace=="AC08"):
        print("Computers in other domains")
    elif(kode2_replace=="AC09"):
        print("Operations research")
    elif(kode2_replace=="AC10"):
        print("Education")
    elif(kode2_replace=="AC11"):
        print("Document management and text processing")
    else:
        print("Kode Penelitian tidak ditemukan")

def judul():
    judulx1 = 466.044
    juduly1 = 680.645
    judulx2 = 2135.36
    juduly2 = 1133.64
    judul = im.crop((judulx1,juduly1,judulx2,juduly2))
    jdl = (pytesseract.image_to_string(judul))
    words = jdl.split("(STUDI")[0]
    spasi = words.split()
    if(len(spasi)>14):
        print("Format Judul Tidak Sesuai")
    else:
        print("Format Judul Sesuai")


def fakultas():
    fakultasx1 = 628.898
    fakultasy1 = 2519.17
    fakultasx2 = 1945.13
    fakultasy2 = 2923.11
    fakultas = im.crop((fakultasx1,fakultasy1,fakultasx2,fakultasy2))
    val_fakultas = (pytesseract.image_to_string(fakultas))
    if('MULTIMEDIA' in val_fakultas):
        print("Penamaan Kampus Sesuai")
    else:
        print("Fakultas Tidak Sesuai")

def tahun():
    now = datetime.datetime.now()
    years = now.year
    tahun = str(years)
    tahunx1 = 1223.32
    tahuny1 = 2943.93
    tahunx2 = 1391.19
    tahuny2 = 3033.86
    tahun = im.crop((tahunx1,tahuny1,tahunx2,tahuny2))
    val_tahun = (pytesseract.image_to_string(tahun))
    if(val_tahun==tahun):
        print("Tahun Sesuai")
    else:
        print("Tahun Tidak Sesuai")



kode1()
kode2()
judul()
fakultas()
tahun()
