adb shell rm -r /sdcard/capture.pcap
adb shell  /data/local/tcpdump -i any -p -s 0
pause
adb pull /sdcard/capture.pcap d:/
aasdasdad