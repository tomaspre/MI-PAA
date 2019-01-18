#!/bin/bash
#I:ID
#n:pocet veci:20
#N:pocet instanci:50
#m:pomer kapacity ku vaze (real)
#W:max vaha
#C:max cena
#k:exponent
#d:-1,0,1

#./a.out -I -n 20 -N 50 -m -W -C -k -d
#Test pomer kapacita/vaha:
./a.out -I 1 -n 20 -N 50 -m 0.1 -W 100 -C 300 -k 1 -d 0
./a.out -I 51 -n 20 -N 50 -m 0.2 -W 100 -C 300 -k 1 -d 0
./a.out -I 101 -n 20 -N 50 -m 0.3 -W 100 -C 300 -k 1 -d 0
./a.out -I 151 -n 20 -N 50 -m 0.4 -W 100 -C 300 -k 1 -d 0
./a.out -I 201 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 1 -d 0
./a.out -I 251 -n 20 -N 50 -m 0.6 -W 100 -C 300 -k 1 -d 0
./a.out -I 301 -n 20 -N 50 -m 0.7 -W 100 -C 300 -k 1 -d 0
./a.out -I 351 -n 20 -N 50 -m 0.8 -W 100 -C 300 -k 1 -d 0
./a.out -I 401 -n 20 -N 50 -m 0.9 -W 100 -C 300 -k 1 -d 0

#Test granularity
./a.out -I 451 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.1 -d -1
./a.out -I 501 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.2 -d -1
./a.out -I 551 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.3 -d -1
./a.out -I 601 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.4 -d -1
./a.out -I 651 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.5 -d -1
./a.out -I 701 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.6 -d -1
./a.out -I 751 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.7 -d -1
./a.out -I 801 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.8 -d -1
./a.out -I 851 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.9 -d -1
./a.out -I 901 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.1 -d 0
./a.out -I 951 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.2 -d 0 
./a.out -I 1001 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.3 -d 0 
./a.out -I 1051 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.4 -d 0 
./a.out -I 1101 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.5 -d 0 
./a.out -I 1151 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.6 -d 0 
./a.out -I 1201 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.7 -d 0 
./a.out -I 1251 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.8 -d 0 
./a.out -I 1301 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.9 -d 0 
./a.out -I 1351 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.1 -d 1
./a.out -I 1401 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.2 -d 1
./a.out -I 1451 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.3 -d 1
./a.out -I 1501 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.4 -d 1
./a.out -I 1551 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.5 -d 1
./a.out -I 1601 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.6 -d 1
./a.out -I 1651 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.7 -d 1
./a.out -I 1701 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.8 -d 1
./a.out -I 1751 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 0.9 -d 1

#Test max ceny
./a.out -I 1801 -n 20 -N 50 -m 0.5 -W 100 -C 100 -k 1 -d 0
./a.out -I 1851 -n 20 -N 50 -m 0.5 -W 100 -C 500 -k 1 -d 0
./a.out -I 1901 -n 20 -N 50 -m 0.5 -W 100 -C 1000 -k 1 -d 0
./a.out -I 1951 -n 20 -N 50 -m 0.5 -W 100 -C 50000 -k 1 -d 0
./a.out -I 2001 -n 20 -N 50 -m 0.5 -W 100 -C 100000 -k 1 -d 0
./a.out -I 2051 -n 20 -N 50 -m 0.5 -W 100 -C 500000 -k 1 -d 0
./a.out -I 2101 -n 20 -N 50 -m 0.5 -W 100 -C 100000 -k 1 -d 0

#Test max vahy
#./a.out -I 2151 -n 20 -N 50 -m 0.5 -W 10 -C 300 -k 1 -d 0
./a.out -I 2201 -n 20 -N 50 -m 0.5 -W 50 -C 300 -k 1 -d 0
./a.out -I 2251 -n 20 -N 50 -m 0.5 -W 100 -C 300 -k 1 -d 0
./a.out -I 2301 -n 20 -N 50 -m 0.5 -W 500 -C 300 -k 1 -d 0
./a.out -I 2351 -n 20 -N 50 -m 0.5 -W 1000 -C 300 -k 1 -d 0
./a.out -I 2401 -n 20 -N 50 -m 0.5 -W 5000 -C 300 -k 1 -d 0
./a.out -I 2451 -n 20 -N 50 -m 0.5 -W 10000 -C 300 -k 1 -d 0
./a.out -I 2501 -n 20 -N 50 -m 0.5 -W 50000 -C 300 -k 1 -d 0
./a.out -I 2551 -n 20 -N 50 -m 0.5 -W 100000 -C 300 -k 1 -d 0
