


import argparse
import sys,os


parser = argparse.ArgumentParser(description = '', add_help = False)
parser = argparse.ArgumentParser()


parser.add_argument('-n','--name', action='store', dest='name', required = True,
                    help = "The storage name")


if len(sys.argv)==1:
  parser.print_help()
  sys.exit(1)

args = parser.parse_args()



if args.name == 'lps':
  path1 = '/home/asp-calo/jodafons/cern_data'
  path2 = '/home/asp-calo/jodafons/phd_data/analysis/run2/2018/update'
  path3 = '/home/asp-calo/jodafons/tuning_data'
elif args.name == 'castor':
  path1 = '/Volumes/castor/cern_data'
  path2 = '/Volumes/castor/phd_data/analysis/electron/run2/2018/update'
  path3 = '/Volumes/castor/tuning_data'
elif args.name == 'cern':
  path1 = '/eos/user/j/jodafons/cern_data'
  path2 = '/eos/user/j/jodafons/phd_data/analysis/electron/run2/2018/update'
  path3 = '/eos/user/j/jodafons/tuning_data'
else:
  print('Using default path')
  path1 = '/Volumes/castor/cern_data'
  path2 = '/Volumes/castor/phd_data/analysis/electron/run2/2018/update'
  path3 = '/Volumes/castor/tuning_data'


print(path1)
print(path2)
print(path3)
os.system( 'ln -sf ' + path1 + ' cern_data' )
os.system( 'ln -sf ' + path2 + ' phd_data' )
os.system( 'ln -sf ' + path3 + ' tuning_data' )

