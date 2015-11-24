# pintool

<p>This tool can be useful for solving some reversing challenges in CTFs events. Implements the technique described here:</p>

<p>&nbsp; http://shell-storm.org/blog/A-binary-analysis-count-me-if-you-can/<br />
&nbsp;&nbsp;<br />
&nbsp;&nbsp;<br />
&nbsp;&nbsp;<br />
# Configuration

You must configure your pin PATH inside of script

PIN = "./pin-2.13-62732-gcc.4.4.7-linux/pin"
INSCOUNT32 = "./pin-2.13-62732-gcc.4.4.7-linux/inscount0.so"
INSCOUNT64 = "./pin-2.13-62732-gcc.4.4.7-linux/source/tools/ManualExamples/obj-intel64/inscount0.so"
&nbsp;&nbsp;<br />
&nbsp;&nbsp;<br />
&nbsp;&nbsp;<br />
# Examples

$python pintool.py&nbsp;<br />
usage: pin_tool.py [-h] [-e] [-l LEN] [-c NUMBER] [-b CHARACTER] [-a ARCH]&nbsp;[-i INITPASS] [-s SIMBOL] [-d EXPRESSION]&nbsp; Filename</p>

<p>positional arguments:<br />
&nbsp; Filename &nbsp; &nbsp; &nbsp; Program for playing with Pin Tool</p>

<p>optional arguments:<br />
&nbsp; -h, --help &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;show this help message and exit<br />
&nbsp; -e &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Study the password length, for example -e -l 40, with 40&nbsp;characters<br />
&nbsp; -l LEN &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Length of password (Default: 10 )<br />
&nbsp; -c NUMBER &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Charset definition for brute force (1-Lowercase, 2-Uppecase,&nbsp;3-Numbers, 4-Hexadecimal, &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;5-Punctuation, 6-All)<br />
&nbsp; -b CHARACTER &nbsp; &nbsp; Add characters for the charset, example -b _-<br />
&nbsp; -a ARCH &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Program architecture 32 or 64 bits, -b 32 or -b 64<br />
&nbsp; -i INITPASS &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Inicial password characters, example -i CTF{<br />
&nbsp; -s SIMBOL &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Simbol for complete all password (Default: _ )<br />
&nbsp; -d EXPRESSION &nbsp; &nbsp;Difference between instructions that are successful or not&nbsp;&nbsp;(Default: != 0, example -d &#39;== &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;-12&#39;, -d &#39;=&gt; 900&#39;, -d &#39;&lt;= 17&#39;&nbsp;&nbsp;or -d &#39;!= 32&#39;)<br />
&nbsp;&nbsp;</p>

<p>&nbsp;</p>



<p><strong>Baleful - picoCTF 2014</strong></p>

<p>$python pintool.py -l 30 -c 1,2,3 -b _{} -s - baleful<br />
p----------------------------- = 763799 difference -12 instructions<br />
pa---------------------------- = 763787 difference -12 instructions<br />
pac--------------------------- = 763775 difference -12 instructions<br />
pack-------------------------- = 763763 difference -12 instructions<br />
packe------------------------- = 763751 difference -12 instructions<br />
packer------------------------ = 763739 difference -12 instructions<br />
packers----------------------- = 763727 difference -12 instructions<br />
packers_---------------------- = 763715 difference -12 instructions<br />
packers_a--------------------- = 763703 difference -12 instructions<br />
packers_an-------------------- = 763691 difference -12 instructions<br />
packers_and------------------- = 763679 difference -12 instructions<br />
packers_and_------------------ = 763667 difference -12 instructions<br />
packers_and_v----------------- = 763655 difference -12 instructions<br />
packers_and_vm---------------- = 763643 difference -12 instructions<br />
packers_and_vms--------------- = 763631 difference -12 instructions<br />
packers_and_vms_-------------- = 763619 difference -12 instructions<br />
packers_and_vms_a------------- = 763607 difference -12 instructions<br />
packers_and_vms_an------------ = 763595 difference -12 instructions<br />
packers_and_vms_and----------- = 763583 difference -12 instructions<br />
packers_and_vms_and_---------- = 763571 difference -12 instructions<br />
packers_and_vms_and_x--------- = 763559 difference -12 instructions<br />
packers_and_vms_and_xo-------- = 763547 difference -12 instructions<br />
packers_and_vms_and_xor------- = 763535 difference -12 instructions<br />
packers_and_vms_and_xors------ = 763523 difference -12 instructions<br />
packers_and_vms_and_xors_----- = 763511 difference -12 instructions<br />
packers_and_vms_and_xors_o---- = 763499 difference -12 instructions<br />
packers_and_vms_and_xors_oh--- = 763487 difference -12 instructions<br />
packers_and_vms_and_xors_oh_--&nbsp;= 763475 difference -12 instructions<br />
packers_and_vms_and_xors_oh_m- = 763463 difference -12 instructions</p>

<p><br />
<strong>Reverse 400 - Hack You 2014</strong></p>

<p>$python pintool.py -l 37 -c 4 -i CTF{ -b }_ -s - -d &#39;=&gt; 651&#39; reverse400<br />
CTF{c________________________________ = 1057174 difference 1300 instructions<br />
CTF{c9_______________________________ = 1058474 difference 1300 instructions<br />
CTF{c9f______________________________ = 1059774 difference 1300 instructions<br />
CTF{c9fd_____________________________ = 1061074 difference 1300 instructions<br />
CTF{c9fd9____________________________ = 1062374 difference 1300 instructions<br />
CTF{c9fd99___________________________ = 1063674 difference 1300 instructions<br />
CTF{c9fd99d__________________________ = 1064974 difference 1300 instructions<br />
CTF{c9fd99de_________________________ = 1066274 difference 1300 instructions<br />
CTF{c9fd99de8________________________ = 1067574 difference 1300 instructions<br />
CTF{c9fd99de8e_______________________ = 1068874 difference 1300 instructions<br />
CTF{c9fd99de8eb______________________ = 1070174 difference 1300 instructions<br />
CTF{c9fd99de8eb0_____________________ = 1071474 difference 1300 instructions<br />
CTF{c9fd99de8eb08____________________ = 1072774 difference 1300 instructions<br />
CTF{c9fd99de8eb082___________________ = 1074074 difference 1300 instructions<br />
CTF{c9fd99de8eb082c__________________ = 1075374 difference 1300 instructions<br />
CTF{c9fd99de8eb082c6_________________ = 1076674 difference 1300 instructions<br />
CTF{c9fd99de8eb082c66________________ = 1077974 difference 1300 instructions<br />
CTF{c9fd99de8eb082c66c_______________ = 1079274 difference 1300 instructions<br />
CTF{c9fd99de8eb082c66c4______________ = 1080574 difference 1300 instructions<br />
CTF{c9fd99de8eb082c66c4c_____________ = 1081874 difference 1300 instructions<br />
CTF{c9fd99de8eb082c66c4ce____________ = 1083174 difference 1300 instructions<br />
CTF{c9fd99de8eb082c66c4ce4___________ = 1084474 difference 1300 instructions<br />
CTF{c9fd99de8eb082c66c4ce40__________ = 1085774 difference 1300 instructions<br />
CTF{c9fd99de8eb082c66c4ce403_________ = 1087074 difference 1300 instructions<br />
CTF{c9fd99de8eb082c66c4ce4039________ = 1088374 difference 1300 instructions<br />
CTF{c9fd99de8eb082c66c4ce4039f19c____ = 1093574 difference 1300 instructions<br />
CTF{c9fd99de8eb082c66c4ce4039f19c4___ = 1094874 difference 1300 instructions<br />
CTF{c9fd99de8eb082c66c4ce4039f19c4f__ = 1096174 difference 1300 instructions<br />
CTF{c9fd99de8eb082c66c4ce4039f19c4fc_ = 1097474 difference 1300 instructions<br />
CTF{c9fd99de8eb082c66c4ce4039f19c4fc} = 1098391 difference 917 instructions<br />
CTF{c9fd99de8eb082c66c4ce4039f19c4fc}</p>

<p><br />
<strong>wyvern 500 - CSAW CTF 2015</strong></p>

<p>$python test_pin.py -c 1,2,3 -b _ -s - -a 64 -l 28 wyvern<br />
d--------------------------- = 1505212 difference 10332 instructions<br />
dr-------------------------- = 1515830 difference 10618 instructions<br />
dr4------------------------- = 1521965 difference 6135 instructions<br />
dr4g------------------------ = 1533160 difference 11195 instructions<br />
dr4g0----------------------- = 1539867 difference 6707 instructions<br />
dr4g0n---------------------- = 1546952 difference 7085 instructions<br />
dr4g0n_--------------------- = 1554227 difference 7275 instructions<br />
dr4g0n_o-------------------- = 1566566 difference 12339 instructions<br />
dr4g0n_or------------------- = 1574413 difference 7847 instructions<br />
dr4g0n_or_------------------ = 1582638 difference 8225 instructions<br />
dr4g0n_or_p----------------- = 1591053 difference 8415 instructions<br />
dr4g0n_or_p4---------------- = 1599752 difference 8699 instructions<br />
dr4g0n_or_p4t--------------- = 1608735 difference 8983 instructions<br />
dr4g0n_or_p4tr-------------- = 1618098 difference 9363 instructions<br />
dr4g0n_or_p4tri------------- = 1627651 difference 9553 instructions<br />
dr4g0n_or_p4tric------------ = 1642776 difference 15125 instructions<br />
dr4g0n_or_p4tric1----------- = 1652899 difference 10123 instructions<br />
dr4g0n_or_p4tric1a---------- = 1663001 difference 10102 instructions<br />
dr4g0n_or_p4tric1an--------- = 1673709 difference 10708 instructions<br />
dr4g0n_or_p4tric1an_-------- = 1684701 difference 10992 instructions<br />
dr4g0n_or_p4tric1an_i------- = 1695977 difference 11276 instructions<br />
dr4g0n_or_p4tric1an_it------ = 1707626 difference 11649 instructions<br />
dr4g0n_or_p4tric1an_it5----- = 1719474 difference 11848 instructions<br />
dr4g0n_or_p4tric1an_it5_---- = 1731606 difference 12132 instructions<br />
dr4g0n_or_p4tric1an_it5_L--- = 1744022 difference 12416 instructions<br />
dr4g0n_or_p4tric1an_it5_LL-- = 1756811 difference 12789 instructions<br />
dr4g0n_or_p4tric1an_it5_LLV- = 1769799 difference 12988 instructions<br />
dr4g0n_or_p4tric1an_it5_LLVM = 1785242 difference 15443 instructions<br />
dr4g0n_or_p4tric1an_it5_LLVM</p>

<p>For bugs please email me.</p>
