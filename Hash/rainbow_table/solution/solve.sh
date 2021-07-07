./rtgen md5 loweralpha-numeric 6 7 0 3800 33445532 0
./rtsort .
./rcrack . -h $( echo "aaaaaaa"|head -c 6|md5sum|head -c 32 )