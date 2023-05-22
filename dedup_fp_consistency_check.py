pageFPfile = open("FPoutputtest/linux_fp_4KB.txt")
sectorFPfile = open("FPoutputtest/linux_fp_512B.txt")
sectorCRCfile = open("FPoutputtest/linux_crc_512B.txt")

sector_no_per_page = 8
FPchecker = dict()
sFPmode = 0
sCRCmode = 1

print("Checking...")
for FP in pageFPfile:
    sFPlist = []
    sCRClist = []
    for i in range(sector_no_per_page):
        sFPlist.append(sectorFPfile.readline())
        sCRClist.append(sectorCRCfile.readline())

    dupFP = FP in FPchecker
    if(dupFP == False):
        FPchecker[FP] = list()
        FPchecker[FP].append(sFPlist)
        FPchecker[FP].append(sCRClist)
    else:
        for i in range(sector_no_per_page):
            if(FPchecker[FP][sFPmode][i] != sFPlist[i] or FPchecker[FP][sCRCmode][i] != sCRClist[i]):
                print("ERROR: FP and sFP are unconsistent!")
                exit()
                
print("SUCCESS: FP and sFP are consistent")