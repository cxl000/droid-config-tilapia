# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device tilapia
%define vendor asus
%define vendor_pretty ASUS
%define device_pretty Nexus 7 GSM (2012)
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 2.0
# We assume most devices will
%define have_modem 1
%include droid-configs-device/droid-configs.inc
