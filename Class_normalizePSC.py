import numpy as np
class normalizePSC():
#=======================================================================================
    def _init_(self):
        pass
#=======================================================================================
    def process(self, a, file_Name, storage):
        header = 1
        column = 0
        mediator = 0
        f = open(file_Name,'r')
        processed_f = open(storage,'w')
        bulk_current = 0
        for line in f:
            if header == 1 and column == 0:
                processed_f.write('normalized Distance, normalized Current\n')
            elif line == '\n':
                pass
            else:
                num = line.strip('\n').split(',')
                if mediator == 0:
                    bulk_current = float(num[1])
                mediator = mediator + 1
                normDistance = float(num[0]) / a
                normCurrent = float(num[1]) / bulk_current
                processed_line = str(normDistance) + ',' + str(normCurrent) + '\n'
                processed_f.write(processed_line)
            column = column + 1
        f.close()
        processed_f.close()
        return 1

