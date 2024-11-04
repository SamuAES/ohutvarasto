from varasto import Varasto

def lisaa_varastoon_mehua(mehua:Varasto, value):
    print(f"Mehuvarasto: {mehua}")
    print(f"mehua.lisaa_varastoon({value})")
    mehua.lisaa_varastoon(value)
    print(f"Mehuvarasto: {mehua}")

def lisaa_varastoon_olutta(olutta:Varasto, value):
    print(f"Olutvarasto: {olutta}")
    print(f"olutta.lisaa_varastoon({value})")
    olutta.lisaa_varastoon(value)
    print(f"Olutvarasto: {olutta}")

def ota_varastosta_olutta(olutta:Varasto, value):
    print(f"Olutvarasto: {olutta}")
    print(f"olutta.ota_varastosta({value})")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

def ota_varastosta_mehua(mehua:Varasto, value):
    print(f"Mehuvarasto: {mehua}")
    print(f"mehua.otaVarastosta({value})")
    saatiin = mehua.ota_varastosta(value)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

def olut_getterit(olutta:Varasto):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def mehu_setterit(mehua:Varasto, lisataan, otetaan):
    print("Mehu setterit:")
    print(f"Lisätään {lisataan}")
    mehua.lisaa_varastoon(lisataan)
    print(f"Mehuvarasto: {mehua}")
    print(f"Otetaan {otetaan}")
    mehua.ota_varastosta(otetaan)
    print(f"Mehuvarasto: {mehua}")

def virhetilanteita(tilavuus, alku_saldo=0):
    if alku_saldo != 0:
        print(f"Varasto({tilavuus}, {alku_saldo});")
    else:
        print(f"Varasto({tilavuus});")
    huono = Varasto(tilavuus=tilavuus, alku_saldo=alku_saldo)
    print(huono)

def luo_varastot(mehu_tilavuus, olut_tilavuus, mehu_saldo=0, olut_saldo=0):
    mehua = Varasto(mehu_tilavuus, mehu_saldo)
    olutta = Varasto(olut_tilavuus, olut_saldo)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")
    return mehua, olutta



def main():
    mehua, olutta = luo_varastot(mehu_tilavuus=100.0,
                                 olut_tilavuus=100.0,
                                 olut_saldo=20.2)

    olut_getterit(olutta)

    mehu_setterit(mehua=mehua, lisataan=50.7, otetaan=3.14)

    print("Virhetilanteita:")
    virhetilanteita(-100.0)
    virhetilanteita(100.0, -50.7)

    lisaa_varastoon_olutta(olutta, 1000.0)

    lisaa_varastoon_mehua(mehua, -666.0)

    ota_varastosta_olutta(olutta, 1000.0)

    ota_varastosta_mehua(mehua, -32.9)


if __name__ == "__main__":
    main()
