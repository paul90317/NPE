#!/bin/python3

import os

def to_sample(path='.'):
    for child in os.listdir(path):
        subpath = os.path.join(path, child)
        if os.path.isdir(subpath):
            to_sample(subpath)
        elif os.path.isfile(subpath) and child == '.env':
            env_example = subpath + '.example'
            with open(subpath, 'r') as fi:
                with open(env_example, 'w') as fo:
                    for line in fi:
                        i = line.find('=')
                        if i == -1:
                            fo.write(line)
                        else:
                            fo.write(f'{line[:i + 1]}\n')
            
            os.system(f'git reset {subpath}')
            os.system(f'git add {env_example}')
            
if __name__=='__main__':
    to_sample()
                    
            