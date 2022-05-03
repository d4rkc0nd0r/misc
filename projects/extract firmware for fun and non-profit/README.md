# Extract firmware for fun and non-profit
**This talk is given at IOT Village CFP 2022.** <br>
**This talk aims at dumping firmware from embedded device such as router in 3 ways:**
* Dumping using SPI Flash, we are familiar with that
* Using TFTP, a UDP protocol, which is used to upload firmware
* Dumping from bootloader

<h4>These are the steps I've taken before doing it:</h4>

* [Information gathering](https://github.com/d4rkc0nd0r/misc/blob/main/projects/extract%20firmware%20for%20fun%20and%20non-profit/information_gathering.md)
* [Interacting with UART](https://github.com/d4rkc0nd0r/misc/blob/main/projects/extract%20firmware%20for%20fun%20and%20non-profit/interacting_with_uart.md)
* [Tried dumping firmware via TFTP](https://github.com/d4rkc0nd0r/misc/blob/main/projects/extract%20firmware%20for%20fun%20and%20non-profit/dumping_firmware_using_tftp.md), but couldn't do it
* [Dumping firmware from bootloader](https://github.com/d4rkc0nd0r/misc/blob/main/projects/extract%20firmware%20for%20fun%20and%20non-profit/dumping_firmware_from_bootloader.md), this worked for me after hours of frustration to figure out the correct offset
* [Dumping firmware from SPI flash](https://github.com/d4rkc0nd0r/misc/blob/main/projects/extract%20firmware%20for%20fun%20and%20non-profit/dumping_firmware_from_spi_flash.md), this method works like charm

You can find the dumped firmware [here](https://github.com/d4rkc0nd0r/misc/tree/main/projects/extract%20firmware%20for%20fun%20and%20non-profit/firmware) <br>

[Here](https://github.com/d4rkc0nd0r/misc/tree/main/projects/extract%20firmware%20for%20fun%20and%20non-profit/setup_images), you can find on how I setup my project.

**If interested, you can emulate it on QEMU**
* **clean_firmware.7z is the `LZMA` compressed binary**
* **router.bin is the unpacked binary, result of clean_firmware.7z**

**This is how extracting firmware from bootloader looks like** <br>

[![firmware_dump](https://asciinema.org/a/KXGfROoAlhwGssttdss7qkHf1.png)](https://asciinema.org/a/KXGfROoAlhwGssttdss7qkHf1)

[Here](https://github.com/d4rkc0nd0r/misc/tree/main/projects/extract%20firmware%20for%20fun%20and%20non-profit/presentation) is my presentation for IOT Village CFP 2022.

**Duration**: It took me 2-3 weeks to complete this project

**CFP Date**: 31 March, 2022
