import os

file = r'F:\BaiduNetdiskDownload\4k.ts'

print(os.system(fr'ffprobe -i {file}'))
print('*'*30)