from transcoder import Transcoder


def main():
    trans1 = Transcoder('grc2lat.txt')
    trans2 = Transcoder('grc2latNgrams.txt')
    trans3 = Transcoder('grcNgrams2ita.txt')
    f = open('prova.txt', encoding='UTF-8')
    for line in f:
        line = line.strip()
        line = ''.join([' ',line,' '])
        t1 = trans1.transcode(line)
        t2 = trans2.transcode(line)
        t3 = trans3.transcode(t2)
        print(line.strip())
        print(t1.strip())
        print(t3.strip())
        print()


if __name__ == '__main__':
    main()