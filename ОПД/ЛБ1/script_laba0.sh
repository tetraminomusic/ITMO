#!/bin/bash
cd ~
chmod -R 777 lab0
rm -rf lab0

#252537 - номер варианта

##############################################################################################################

#Задание №1

##############################################################################################################

mkdir lab0
cd lab0

mkdir -p happiny5/staraptor/hariyama
mkdir -p happiny5/poliwrath/weepinbell
mkdir -p happiny5/seel/samurott
mkdir -p happiny5/seel/magmortar
mkdir -p happiny5/seel/igglybuff
mkdir -p happiny5/seel/bidoof
mkdir -p nidoranF8/persian/pidgey
mkdir -p nidoranF8/persian/stoutland
mkdir -p nidoranF8/persian/magnezone
mkdir -p nidoranF8/persian/feebas
mkdir -p roselia7/mightyena/marshtomp
mkdir -p roselia7/mightyena/lillipup
mkdir -p roselia7/klang/eelektross
mkdir -p roselia7/klang/venusaur
mkdir -p roselia7/klang/infernape
mkdir -p roselia7/rampardos/leavanny



touch happiny5/caterpie
touch happiny5/staraptor/cacnea
touch happiny5/staraptor/cubone
touch happiny5/staraptor/rattata
touch happiny5/poliwrath/mudkip
touch happiny5/seel/pidgeotto
touch happiny5/seel/golurk
touch happiny5/seel/masquerain
touch nidoranF8/froslass
touch nidoranF8/persian/chimchar
touch roselia7/mightyena/venusaur
touch roselia7/rampardos/roggenrola
touch roselia7/rampardos/amoonguss
touch roselia7/rampardos/metang
touch horsea0
touch kirlia2
touch nidoranF8/mareep
touch nidoranF8/tangela
touch nidoranF8/lampent
touch nidoranF8/foongus
touch roselia7/ninetales
touch roselia7/salamence
touch roselia7/swoobat
touch zigzagoon3

###########

echo "Живет Forest" > happiny5/caterpie

echo "Ходы Block Body Slam Bullet Seed Dark
Pulse Double-Edge Drain Punch Fury Cutter Focus Punch Giga Drain Low
Kick Magic Coat Mega Punch Mud-Stap Role Play Seismic Toss Seed Bomb
Sleep Talk Snore Spite Sucker Punch Synthesis Thunderpunch Morry
Seed" > happiny5/staraptor/cacnea

echo "Тип диеты Herbivore" > happiny5/staraptor/cubone

echo "satk=3 sdef=4
spd=7" > happiny5/staraptor/rattata

echo "Способности Growl Tackle Mud-Stap Water Gun Bide
Foresight Mud Sport Take Down Whirlpool Protect Hydro Pump
Endeavor" > happiny5/poliwrath/mudkip

echo "Тип покемона NORMAL FLYING" > happiny5/seel/pidgeotto

echo "Тип диеты
Terravore" > happiny5/seel/golurk

echo "Возможности Overland=6 Surface=1 Sky=8 Jump=2
Power1=0 Intelligence=4" > happiny5/seel/masquerain

echo "Тип покемона WATER
NONE" > horsea0

echo "weight=44.5 height=31.0 atk=4 def=4" > kirlia2

echo "Живет
Taiga Tundra" > nidoranF8/froslass

echo "Способности Blaze Flash Fire
Gluttony" > nidoranF8/persian/chimchar

echo "Способности Overcharge Static Cute
Charm" > nidoranF8/mareep

echo "Тип покемона GRASS NONE" > tangela

echo "Живет Cave
Urban" > nidoranF8/lampent

echo "Способности Overgrow Venom Effect Spore
Chlorophyll" > nidoranF8/foongus

echo "Развитые способности Leaf Guard Flower
Gift" > roselia7/mightyena/venusaur

echo "Способности This is dummy text when pokemon does not
contain something. It is better than NPE!" > roselia7/ninetales

echo "Развитые  
способности Sheer Force Moxie" > roselia7/salamence

echo "Тип диеты  
Herbivore" > roselia7/swoobat

echo "Способности Mountain Peak Sturdy Sand Rush" > roselia7/rampardos/roggenrola

echo "Tuп покемона GRASS POISON" > roselia7/rampardos/amoonguss

echo "Tuп диеты  
Omnivore" > roselia7/rampardos/metang

echo "weight=38.6 height=16.0 atk=3 def=4" > zigzagoon3

##############################################################################################################

#Задание №2

##############################################################################################################

chmod u=r,g=,o=r happiny5/caterpie
chmod u=rwx,g=rx,o=wx happiny5/staraptor
chmod u=r,g=,o= happiny5/staraptor/cacnea
chmod u=,g=rw,o=w happiny5/staraptor/cubone
chmod 550 happiny5/staraptor/hariyama
chmod u=r,g=r,o= happiny5/staraptor/rattata
chmod u=rwx,g=wx,o=wx happiny5/poliwrath
chmod ugo=rwx happiny5/poliwrath/weepinbell
chmod u=r,g=,o=r happiny5/poliwrath/mudkip
chmod u=rwx,g=wx,o=wx happiny5/seel
chmod 444 happiny5/seel/pidgeotto
chmod u=r,g=r,o= happiny5/seel/golurk
chmod u=rwx,g=wx,o=wx happiny5/seel/samurott
chmod u=rwx,g=rx,o=w happiny5/seel/magmortar
chmod 307 happiny5/seel/igglybuff
chmod 066 happiny5/seel/masquerain
chmod u=rx,g=rwx,o=rwx happiny5/seel/bidoof
chmod ugo=r horsea0
chmod u=r,g=,o= kirlia2
chmod 571 nidoranF8
chmod 044 nidoranF8/froslass
chmod u=rwx,g=rx,o=w nidoranF8/persian
chmod 330 nidoranF8/persian/pidgey
chmod 330 nidoranF8/persian/stoutland
chmod u=rw,g=w,o=w nidoranF8/persian/chimchar
chmod u=rx,g=rwx,o=rw nidoranF8/persian/magnezone
chmod 700 nidoranF8/persian/feebas
chmod u=,g=rw,o=w nidoranF8/mareep
chmod ugo=r nidoranF8/tangela
chmod 600 nidoranF8/lampent
chmod 006 nidoranF8/foongus
chmod u=wx,g=x,o=x roselia7/mightyena
chmod u=rx,g=,o=r roselia7/mightyena/venusaur
chmod u=rwx,g=wx,o=wx roselia7/mightyena/marshtomp
chmod 551 roselia7/mightyena/lillipup
chmod u=r,g=r,o= roselia7/ninetales
chmod u=wx,g=x,o=w roselia7/klang
chmod 700 roselia7/klang/eelektross
chmod u=rx,g=x,o=w roselia7/klang/venusaur
chmod u=rx,g=x,o=wx roselia7/klang/infernape
chmod u=rw,g=,o=r roselia7/salamence
chmod u=,g=,o=rw roselia7/swoobat
chmod u=rwx,g=rx,o=wx roselia7/rampardos
chmod u=rx,g=w,o=r roselia7/rampardos/leavanny
chmod u=rw,g=w,o=w roselia7/rampardos/roggenrola
chmod 664 roselia7/rampardos/amoonguss
chmod u=rw,g=w,o= roselia7/rampardos/metang
chmod 660 zigzagoon3

chmod u=rw,g=r,o=r happiny5
chmod u=rw,g=rw,o=r roselia7

##############################################################################################################

#Задание №3

##############################################################################################################

chmod 777 zigzagoon3
chmod 777 roselia7
chmod 777 roselia7/mightyena

ln zigzagoon3 roselia7/mightyena/venusaurzigzagoon

chmod u=wx,g=x,o=x roselia7/mightyena
chmod u=rw,g=rw,o=r roselia7
chmod 660 zigzagoon3


#############

chmod 777 kirlia2
chmod 777 roselia7
chmod 777 roselia7/klang
chmod 777 roselia7/klang/infernape

cp kirlia2 roselia7/klang/infernape/

chmod u=r,g=,o= roselia7/klang/infernape/kirlia2
chmod u=rx,g=x,o=wx roselia7/klang/infernape
chmod u=wx,g=x,o=w roselia7/klang
chmod u=rw,g=rw,o=r roselia7
chmod u=r,g=,o= kirlia2

#############

chmod 777 roselia7
chmod 777 nidoranF8
chmod 777 nidoranF8/persian
chmod 777 roselia7/mightyena
chmod 777 nidoranF8/persian/chimchar
chmod 777 roselia7/mightyena/venusaur
chmod 777 nidoranF8/lampent


cat nidoranF8/persian/chimchar roselia7/mightyena/venusaur nidoranF8/lampent > zigzagoon3_19

chmod u=wx,g=x,o=x roselia7/mightyena
chmod u=rw,g=w,o=w nidoranF8/persian/chimchar
chmod u=rx,g=,o=r roselia7/mightyena/venusaur
chmod u=rwx,g=rx,o=w nidoranF8/persian
chmod 600 nidoranF8/lampent
chmod 571 nidoranF8
chmod u=rw,g=rw,o=r roselia7

#############

chmod -R 777 happiny5
chmod -R 777 roselia7


cp -R happiny5 roselia7/klang/venusaur/

chmod u=rw,g=r,o=r roselia7/klang/venusaur/happiny5
chmod u=r,g=,o=r happiny5/caterpie
chmod u=rwx,g=rx,o=wx happiny5/staraptor
chmod u=r,g=,o= happiny5/staraptor/cacnea
chmod u=,g=rw,o=w happiny5/staraptor/cubone
chmod 550 happiny5/staraptor/hariyama
chmod u=r,g=r,o= happiny5/staraptor/rattata
chmod u=rwx,g=wx,o=wx happiny5/poliwrath
chmod ugo=rwx happiny5/poliwrath/weepinbell
chmod u=r,g=,o=r happiny5/poliwrath/mudkip
chmod u=rwx,g=wx,o=wx happiny5/seel
chmod 444 happiny5/seel/pidgeotto
chmod u=r,g=r,o= happiny5/seel/golurk
chmod u=rwx,g=wx,o=wx happiny5/seel/samurott
chmod u=rwx,g=rx,o=w happiny5/seel/magmortar
chmod 307 happiny5/seel/igglybuff
chmod 066 happiny5/seel/masquerain
chmod u=rx,g=rwx,o=rwx happiny5/seel/bidoof
chmod u=wx,g=x,o=x roselia7/mightyena
chmod u=rx,g=,o=r roselia7/mightyena/venusaur
chmod u=rwx,g=wx,o=wx roselia7/mightyena/marshtomp
chmod 551 roselia7/mightyena/lillipup
chmod u=r,g=r,o= roselia7/ninetales
chmod u=wx,g=x,o=w roselia7/klang
chmod 700 roselia7/klang/eelektross
chmod u=rx,g=x,o=w roselia7/klang/venusaur
chmod u=rx,g=x,o=wx roselia7/klang/infernape
chmod u=rw,g=,o=r roselia7/salamence
chmod u=,g=,o=rw roselia7/swoobat
chmod u=rwx,g=rx,o=wx roselia7/rampardos
chmod u=rx,g=w,o=r roselia7/rampardos/leavanny
chmod u=rw,g=w,o=w roselia7/rampardos/roggenrola
chmod 664 roselia7/rampardos/amoonguss
chmod u=rw,g=w,o= roselia7/rampardos/metang

chmod u=rw,g=r,o=r happiny5
chmod u=rw,g=rw,o=r roselia7

#############

chmod -R 777 roselia7
chmod 777 roselia7/swoobat

cp -R roselia7 roselia7_copy
cp -R roselia7_copy roselia7/rampardos/roselia7
rm -R roselia7_copy

chmod u=wx,g=x,o=x roselia7/mightyena
chmod u=rx,g=,o=r roselia7/mightyena/venusaur
chmod u=rwx,g=wx,o=wx roselia7/mightyena/marshtomp
chmod 551 roselia7/mightyena/lillipup
chmod u=r,g=r,o= roselia7/ninetales
chmod u=wx,g=x,o=w roselia7/klang
chmod 700 roselia7/klang/eelektross
chmod u=rx,g=x,o=w roselia7/klang/venusaur
chmod u=rx,g=x,o=wx roselia7/klang/infernape
chmod u=rw,g=,o=r roselia7/salamence
chmod u=,g=,o=rw roselia7/swoobat
chmod u=rwx,g=rx,o=wx roselia7/rampardos
chmod u=rx,g=w,o=r roselia7/rampardos/leavanny
chmod u=rw,g=w,o=w roselia7/rampardos/roggenrola
chmod 664 roselia7/rampardos/amoonguss
chmod u=rw,g=w,o= roselia7/rampardos/metang

chmod u=rw,g=r,o=r happiny5
chmod u=rw,g=rw,o=r roselia7

#############

chmod 777 happiny5

ln -s happiny5 Copy_56

chmod u=rw,g=r,o=r happiny5

#############

chmod 777 zigzagoon3
chmod 777 nidoranF8
chmod 777 nidoranF8/persian
chmod 777 nidoranF8/persian/pidgey

cp zigzagoon3 nidoranF8/persian/pidgey/

chmod 660 zigzagoon3
chmod 660 nidoranF8/persian/pidgey/zigzagoon3
chmod 330 nidoranF8/persian/pidgey
chmod u=rwx,g=rx,o=w nidoranF8/persian
chmod 571 nidoranF8


#############

chmod 777 horsea0
chmod 777 roselia7
chmod 777 roselia7/rampardos

ln horsea0 roselia7/rampardos/amoongusshorsea

chmod u=rwx,g=rx,o=wx roselia7/rampardos
chmod u=rw,g=rw,o=r roselia7
chmod ugo=r horsea0

#############

chmod 777 roselia7
chmod 777 zigzagoon3
chmod 777 roselia7/rampardos

ln -s zigzagoon3 roselia7/rampardos/roggenrolazigzagoon

chmod u=rwx,g=rx,o=wx roselia7/rampardos
chmod 660 zigzagoon3
chmod u=rw,g=rw,o=r roselia7

#############

chmod 777 happiny5
chmod 777 roselia7
chmod 777 happiny5/staraptor
chmod 777 roselia7/rampardos
chmod 777 roselia7/rampardos/roggenrola
chmod 777 happiny5/staraptor/rattata
chmod 777 roselia7/rampardos/amoonguss

cat roselia7/rampardos/roggenrola happiny5/staraptor/rattata roselia7/rampardos/amoonguss > zigzagoon3_13

chmod 664 roselia7/rampardos/amoonguss
chmod u=r,g=r,o= happiny5/staraptor/rattata
chmod u=rw,g=w,o=w roselia7/rampardos/roggenrola
chmod u=rwx,g=rx,o=wx roselia7/rampardos
chmod u=rwx,g=rx,o=wx happiny5/staraptor
chmod u=rw,g=rw,o=r roselia7
chmod u=rw,g=r,o=r happiny5

#############

chmod 777 roselia7
chmod 777 zigzagoon3

cp zigzagoon3 roselia7/ninetaleszigzagoon

chmod 660 roselia7/ninetaleszigzagoon
chmod u=rw,g=rw,o=r roselia7
chmod 660 zigzagoon3


#############

chmod 777 kirlia2
chmod 777 happiny5

ln -s kirlia2 happiny5/caterpiekirlia

chmod u=rw,g=r,o=r happiny5
chmod u=r,g=,o= kirlia2

#############

chmod 777 roselia7
chmod 777 zigzagoon3
chmod 777 roselia7/rampardos

cp zigzagoon3 roselia7/rampardos/metangzigzagoon

chmod 660 roselia7/rampardos/metangzigzagoon
chmod u=rwx,g=rx,o=wx roselia7/rampardos
chmod 660 zigzagoon3
chmod u=rw,g=rw,o=r roselia7

#############

chmod 777 nidoranF8

ln -s nidoranF8 Copy_37

chmod 571 nidoranF8
chmod 571 Copy_37

##############################################################################################################

#Задание №4

##############################################################################################################

cd ..
chmod -R 777 lab0
cd lab0

##

wc -l nidoranF8/mareep nidoranF8/tangela nidoranF8/lampent 2>&1 | tee /tmp/lines_count

##

ls roselia7/ | sort -r


##

find -name "v*" -type f 2>/dev/null -exec cat -n {} \; | sort -r

##

cat happiny5/poliwrath/mudkip happiny5/seel/pidgeotto happiny5/seel/golurk happiny5/seel/masquerain nidoranF8/froslass nidoranF8/persian/chimchar nidoranF8/mareep nidoranF8/tangela | sort -r

##

find -name "*ma*" -type f -printf "%f\t%M\t%u\t%g\t%s\t%Td-%Tm-%TY\t%TH:%TM\n" 2>/dev/null | sort -k1 | tail -2

##

find roselia7 -type f -printf "%f\t%M\t%u\t%g\t%s\t%Td-%Tm-%TY\t%TH:%TM\n" 2>/tmp/error | sort -rk1

##

find -type f -name "*le*" -printf "%f\t%M\t%u\t%g\t%s\t%Td-%Tm-%TY\t%TH:%TM\n" | sort -k1

##

find -type f -name "p*" -printf "%f\t%M\t%u\t%g\t%s\t%Td-%Tm-%TY\t%TH:%TM\n" 2>&1 | sort -rk6

##

find -type f -name "*p" -printf "%f\t%M\t%u\t%g\t%s\t%Td-%Tm-%TY\t%TH:%TM\n" | sort -k6 | tail -2

##

wc -m horsea0 2>/dev/null | tee /tmp/n_symbols

##

find -type f -printf "%f\t%M\t%u\t%g\t%s\t%Td-%Tm-%TY\t%TH:%TM\n" | sort -rk5 | tail -2

##

find -type f -name "*e" -printf "%f\t%M\t%u\t%g\t%s\t%Td-%Tm-%TY\t%TH:%TM\n" | sort -rk5

##

chmod u=r,g=,o=r happiny5/caterpie
chmod u=rwx,g=rx,o=wx happiny5/staraptor
chmod u=r,g=,o= happiny5/staraptor/cacnea
chmod u=,g=rw,o=w happiny5/staraptor/cubone
chmod 550 happiny5/staraptor/hariyama
chmod u=r,g=r,o= happiny5/staraptor/rattata
chmod u=rwx,g=wx,o=wx happiny5/poliwrath
chmod ugo=rwx happiny5/poliwrath/weepinbell
chmod u=r,g=,o=r happiny5/poliwrath/mudkip
chmod u=rwx,g=wx,o=wx happiny5/seel
chmod 444 happiny5/seel/pidgeotto
chmod u=r,g=r,o= happiny5/seel/golurk
chmod u=rwx,g=wx,o=wx happiny5/seel/samurott
chmod u=rwx,g=rx,o=w happiny5/seel/magmortar
chmod 307 happiny5/seel/igglybuff
chmod 066 happiny5/seel/masquerain
chmod u=rx,g=rwx,o=rwx happiny5/seel/bidoof
chmod ugo=r horsea0
chmod u=r,g=,o= kirlia2
chmod 571 nidoranF8
chmod 044 nidoranF8/froslass
chmod u=rwx,g=rx,o=w nidoranF8/persian
chmod 330 nidoranF8/persian/pidgey
chmod 330 nidoranF8/persian/stoutland
chmod u=rw,g=w,o=w nidoranF8/persian/chimchar
chmod u=rx,g=rwx,o=rw nidoranF8/persian/magnezone
chmod 700 nidoranF8/persian/feebas
chmod u=,g=rw,o=w nidoranF8/mareep
chmod ugo=r nidoranF8/tangela
chmod 600 nidoranF8/lampent
chmod 006 nidoranF8/foongus
chmod u=wx,g=x,o=x roselia7/mightyena
chmod u=rx,g=,o=r roselia7/mightyena/venusaur
chmod u=rwx,g=wx,o=wx roselia7/mightyena/marshtomp
chmod 551 roselia7/mightyena/lillipup
chmod u=r,g=r,o= roselia7/ninetales
chmod u=wx,g=x,o=w roselia7/klang
chmod 700 roselia7/klang/eelektross
chmod u=rx,g=x,o=w roselia7/klang/venusaur
chmod u=rx,g=x,o=wx roselia7/klang/infernape
chmod u=rw,g=,o=r roselia7/salamence
chmod u=,g=,o=rw roselia7/swoobat
chmod u=rwx,g=rx,o=wx roselia7/rampardos
chmod u=rx,g=w,o=r roselia7/rampardos/leavanny
chmod u=rw,g=w,o=w roselia7/rampardos/roggenrola
chmod 664 roselia7/rampardos/amoonguss
chmod u=rw,g=w,o= roselia7/rampardos/metang
chmod 660 zigzagoon3

chmod u=rw,g=r,o=r happiny5
chmod u=rw,g=rw,o=r roselia7

##############################################################################################################

#Задание №5

##############################################################################################################

chmod 777 horsea0

rm horsea0

#############

chmod 777 nidoranF8
chmod 777 nidoranF8/lampent

rm nidoranF8/lampent

chmod 571 nidoranF8

#############

chmod 777 roselia7
chmod 777 roselia7/rampardos

rm roselia7/rampardos/amoongusshorsea
rm roselia7/rampardos/roggenrolazigzagoon
rm -r roselia7/rampardos/roselia7 #надо задать вопрос по поводу удаления этой директории!!

chmod u=rwx,g=rx,o=wx roselia7/rampardos
chmod u=rw,g=rw,o=r roselia7

#############

chmod 777 roselia7
chmod 777 roselia7/klang/infernape
chmod 777 roselia7/klang

rm -r roselia7/klang/infernape

chmod u=wx,g=x,o=w roselia7/klang
chmod u=rw,g=rw,o=r roselia7

#############