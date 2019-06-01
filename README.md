# qo-100_pi
This Repository will have my Raspberry PI QO-100 Satellite ground Station files.
I am planning to create aremote QO-100 trancever that has a live SDR and Transmitter so I can connect to from my Shack and the raspberry pi is at my satliite dish. 
This is ideal as I don't have to run expensive Coaxial cables from shack to Antenna.
At 2.4Ghz the TX frequency the power loss is high in coaxial cable.

# General Information.
The Defult PI OS gqrx recever dont work and you need to install it from http://gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi
The Default gnuradio-companion seem to work ok.
you need to install hackrf_tools,and sdrplay drivers for msi



# Project Status
This grc file is a working ssb transmitter for QO-100.

# Planned enhancements
1) Gnuradio RX using sdrplay or msi SDR's for rx with waterfall and AM,SSB,FM.
2) Gnuradio TX with FFT and Scope view with digital modes.



 


