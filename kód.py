def kalif(počet_ľudí, medzera):
    zoznam_živých = []
    zoznam_mŕtvych = []
    for človek in range(1, počet_ľudí + 1):
        zoznam_živých.append(str(človek))
    poradie = medzera - 1
    while len(zoznam_živých) > 1:
        if poradie <= len(zoznam_živých) - 1:
            zoznam_mŕtvych.append(zoznam_živých[poradie])
            poradie += medzera
        else:
            poradie = - 1 * (len(zoznam_živých) - poradie)
            for nečlovek in zoznam_mŕtvych:
                zoznam_živých.remove(str(nečlovek))
            zoznam_mŕtvych = []
    print("Prežije " + str(*zoznam_živých) + ". človek v poradí.")
kalif(10, 3)
