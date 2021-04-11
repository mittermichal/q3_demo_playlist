import glob
import os
import argparse
import re



def main():
    parser = argparse.ArgumentParser(description='generates demo playlist cfg for q3/wolf:et/rtcw')
    parser.add_argument('--dir', metavar='<PATH>', required=True,
                        help='path to demos folder (C:/Program Files (x86)/ioquake3/baseq3/demos/quakecon2049)')
    #parser.add_argument('-r', required=False,
    #                    help='recursively search for demos')
    args = parser.parse_args()

    print(args.dir)

    #dir = os.path.dirname(__file__)
    #filename = os.path.join(dir, args.dir+'.dm*')
    #print(filename)
    #print(os.path.join(args.dir,'/../'))
    if args.dir.find('demos')!=-1:
        cfg_path=args.dir.split('demos')[0]
        cfg_path=os.path.abspath(os.path.join(cfg_path,'demos_playlist.cfg'))
    else:
        print("demos folder not in path, incorrect path")
        exit(1)

    print(cfg_path)
    out = open(cfg_path, "w")
    i = 1
    for name in glob.glob(args.dir+'/*.dm*'):
        #print(name)
        match = re.search('demos\\\(.*)', name)
        #print(match)
        if match!=None:
            out.write('set demo'+str(i)+' "demo "'+match.group(1)+'";set nextdemo vstr demo'+str(i+1)+'"\n')
            i=i+1

        base = os.path.basename(name)
        ffilename = os.path.splitext(base)[0]
    out.write('vstr demo1')
    out.close()
main()