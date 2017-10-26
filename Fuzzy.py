class Fuzzy:
    def __init__(self, emosi, profokasi):
        self.nEmosi = []
        self.lEmosi = []
        self.nProvokasi = []
        self.lProvokasi = []
        self.hasilYa = []
        self.hasilTidak = []
        self.emosi = emosi
        self.profokasi = profokasi

    def cekEmosi(self):
        data = self.emosi
        if (data >= 0 and data <=36) :
            self.nEmosi.append(1.0)
            self.lEmosi.append("Rendah")
            self.nEmosi.append(1.0)
            self.lEmosi.append("Rendah")
        elif (data >= 37 and data <= 39) :
            self.nEmosi.append(-(data-40.0)/(40.0-36.0))
            self.lEmosi.append("Rendah")
            self.nEmosi.append((data-36.0)/(40.0-36.0))
            self.lEmosi.append("Sedang")
        elif (data >= 40 and data <= 63) :
            self.nEmosi.append(1.0)
            self.lEmosi.append("Sedang")
            self.nEmosi.append(1.0)
            self.lEmosi.append("Sedang")
        elif (data >= 64 and data <= 67) :
            self.nEmosi.append(-(data-68.0)/(68.0-63.0))
            self.lEmosi.append("Rendah")
            self.nEmosi.append((data-63.0)/(68.0-63.0))
            self.lEmosi.append("Sedang")
        elif (data >= 68 and data <= 100) :
            self.nEmosi.append(1.0)
            self.lEmosi.append("Tinggi")
            self.nEmosi.append(1.0)
            self.lEmosi.append("Tinggi")

    def cekProfokasi(self) :
        data = self.profokasi
        if (data >= 0 and data <= 25):
            self.nProvokasi.append(1.0)
            self.lProvokasi.append("Rendah")
            self.nProvokasi.append(1.0)
            self.lProvokasi.append("Rendah")
        elif (data >= 26 and data <= 31) :
            self.nProvokasi.append(-(data-32.0)/(32.0-25.0))
            self.lProvokasi.append("Rendah")
            self.nProvokasi.append((data-25.0)/(32.0-25.0))
            self.lProvokasi.append("Sedang")
        elif (data >= 32 and data <= 50) :
            self.nProvokasi.append(1.0)
            self.lProvokasi.append("Sedang")
            self.nProvokasi.append(1.0)
            self.lProvokasi.append("Sedang")
        elif (data >= 51 and data <= 61) :
            self.nProvokasi.append(-(data-62.0)/(62.0-50.0))
            self.lProvokasi.append("Sedang")
            self.nProvokasi.append((data-50.0)/(62.0-50.0))
            self.lProvokasi.append("Tinggi")
        elif (data >= 62 and data <= 85) :
            self.nProvokasi.append(1.0)
            self.lProvokasi.append("Tinggi")
            self.nProvokasi.append(1.0)
            self.lProvokasi.append("Tinggi")
        elif (data >= 86 and data <= 88) :
            self.nProvokasi.append(-(data-89.0)/(89.0-86.0))
            self.lProvokasi.append("Tinggi")
            self.nProvokasi.append((data-85.0)/(89.0-86.0))
            self.lProvokasi.append("Sangat Tinggi")
        elif (data >= 89 and data <= 100) :
            self.nProvokasi.append(1.0)
            self.lProvokasi.append("Sangat Tinggi")
            self.nProvokasi.append(1.0)
            self.lProvokasi.append("Sangat Tinggi")

    def inferensi (self):
        for iE in range(0,2):
            for iP in range(0,2):
                if (self.lEmosi[iE] == 'Rendah' and self.lProvokasi[iP] == 'Rendah'):
                    lHoax = 'Tidak'
                if (self.lEmosi[iE] == 'Rendah' and self.lProvokasi[iP] == 'Sedang'):
                    lHoax = 'Tidak'
                if (self.lEmosi[iE] == 'Rendah' and self.lProvokasi[iP] == 'Tinggi'):
                    lHoax = 'Ya'
                if (self.lEmosi[iE] == 'Rendah' and self.lProvokasi[iP] == 'Sangat Tinggi'):
                    lHoax = 'Ya'
                if (self.lEmosi[iE] == 'Sedang' and self.lProvokasi[iP] == 'Rendah'):
                    lHoax = 'Tidak'
                if (self.lEmosi[iE] == 'Sedang' and self.lProvokasi[iP] == 'Sedang'):
                    lHoax = 'Tidak'
                if (self.lEmosi[iE] == 'Sedang' and self.lProvokasi[iP] == 'Tinggi'):
                    lHoax = 'Tidak'
                if (self.lEmosi[iE] == 'Sedang' and self.lProvokasi[iP] == 'Sangat Tinggi'):
                    lHoax = 'Ya'
                if (self.lEmosi[iE] == 'Tinggi' and self.lProvokasi[iP] == 'Rendah'):
                    lHoax = 'Tidak'
                if (self.lEmosi[iE] == 'Tinggi' and self.lProvokasi[iP] == 'Sedang'):
                    lHoax = 'Tidak'
                if (self.lEmosi[iE] == 'Tinggi' and self.lProvokasi[iP] == 'Tinggi'):
                    lHoax = 'Ya'
                if (self.lEmosi[iE] == 'Tinggi' and self.lProvokasi[iP] == 'Sangat Tinggi'):
                    lHoax = 'Ya'
                nHoax = min(self.nEmosi[iE], self.nProvokasi[iP])
                if (lHoax == 'Tidak') :
                    self.hasilTidak.append([nHoax, lHoax])
                else :
                    self.hasilYa.append([nHoax, lHoax])
        if (len(self.hasilYa) == 0) :
            self.hasilYa.append([0.0, "Ya"])
        if (len(self.hasilTidak) == 0) :
            self.hasilTidak.append([0.0, "Tidak"])

    def defuzifikasi(self):
        self.hasilTidak.sort(reverse=True)
        self.hasilYa.sort(reverse=True)
        ya = self.hasilTidak[0][0]
        tidak = self.hasilYa[0][0]
        yStar = ((ya*50.0 + tidak*100.0)/(ya+tidak))
        return yStar

    def cekHoax(self):
        if (self.defuzifikasi() > 50) :
            return 'Ya'
        else :
            return 'Tidak'

    def main(self):
        self.cekEmosi()
        self.cekProfokasi()
        self.inferensi()
        self.defuzifikasi()
        return str(self.emosi) + ' | ' + str(self.profokasi) + ' | ' + str(self.defuzifikasi()) + ' | ' + str(
            self.cekHoax())

eT = [97, 36, 63, 82, 71, 79, 55, 57, 40, 57, 77, 68, 60, 82, 40, 80, 60, 50, 100, 11]
pT = [74, 85, 43, 90, 25, 81, 62, 45, 65, 45, 70, 75, 70, 90, 85, 68, 72, 95, 18, 99]
eTest = [58, 68, 64, 57, 77, 98, 91, 50, 95, 27]
pTest = [63, 70, 66, 77, 55, 64, 59, 95, 55, 79]

for data in range(len(eT)) :
    fuz = Fuzzy(eT[data], pT[data])
    print (str(data+1) + ' | ' + fuz.main())

for data in range(len(eTest)) :
    fuz = Fuzzy(eTest[data], pTest[data])
    print (str(data+21) + ' | ' + fuz.main())