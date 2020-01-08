EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 3
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L MAX32650GWP:MAX32650GWQ+ U?
U 2 1 5E12E874
P 4800 1500
AR Path="/5E12E874" Ref="U?"  Part="2" 
AR Path="/5E117560/5E12E874" Ref="U?"  Part="2" 
F 0 "U?" H 5700 1887 60  0000 C CNN
F 1 "MAX32650GWQ+" H 5700 1781 60  0000 C CNN
F 2 "21-100240A_W964A4+1" H 5700 1740 60  0001 C CNN
F 3 "" H 4800 1500 60  0000 C CNN
	2    4800 1500
	1    0    0    -1  
$EndComp
Wire Wire Line
	6600 1700 7000 1700
Wire Wire Line
	7000 1700 7000 1300
Wire Wire Line
	6600 1600 6900 1600
Wire Wire Line
	6900 1600 6900 1300
Wire Wire Line
	6600 1500 6800 1500
Wire Wire Line
	6800 1500 6800 1300
Text HLabel 6800 1300 1    50   Input ~ 0
HRINT
Text HLabel 6900 1300 1    50   BiDi ~ 0
SDA_I2C
Text HLabel 7000 1300 1    50   Output ~ 0
SCL_I2C
$EndSCHEMATC
