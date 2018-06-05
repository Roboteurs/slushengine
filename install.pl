#!/usr/bin/perl 
#----------------------------------------------------------------------------------
# Install script for the Slush library and all of its dependancies
# - script installs required packages with dpkg
# - script uses pip to install both python3 and python2 packages
# - clones the
#
#
#
use strict;
use warnings;
use autodie;

# declare all required packages
my $packages = "python3 python3-setuptools python3-pip git python3-rpi.gpio python-setuptools python-pip python-rpi.gpio python-dev";
my $pip_packages = "spidev inputs smbus2";

# git repos to install
my $slush_repo = qw(https://github.com/Roboteurs/slushengine); 

# system commands
my $apt_update_cmd="sudo apt-get update";
my $apt_install_cmd="sudo apt-get -y install $packages";
my $pip3_install_cmd="sudo pip3 install $pip_packages";
my $pip2_install_cmd="sudo pip install $pip_packages";
my $git_clone_cmd = "git clone ";
my $python_install_cmd = "sudo python3 setup.py install";
my $logit = "1>>log.txt 2>&1";


# update
open(my $outfile, '>', 'log.txt');
print "Updatng apt \r\n";
system "$apt_update_cmd $logit";
if ($? != 0){
    print "Aptitude failed to updateNo: $? \r\n";
    print "Check log.txt";
    die();
}

# install required packages with apt
open(my $outfile, '>', 'log.txt');
print "Installing required build packages \r\n";
system "$apt_install_cmd $logit";
if ($? != 0){
    print "Aptitude failed to install packages Error No: $? \r\n";
    print "Check log.txt";
    die();
}

# install pip3 packages
print "Installing pip3 packages \r\n";
system "$pip3_install_cmd $logit";
if ($? != 0){
    print "Failed to install pip packages Error No: $? \r\n";
    print "Check log.txt";
    die();
}

# install pip packages
print "Installing pip2 packages \r\n";
system "$pip2_install_cmd $logit";
if ($? != 0){
    print "Failed to install pip packages Error No: $? \r\n";
    print "Check log.txt";
    die();
}

#install slush
print "Installing slush \r\n";
system "$git_clone_cmd $slush_repo $logit";
if ($? != 0){
    print "Failed to clone slush repo Error No: $? Does directory already exist? \r\n";
    print "Check log.txt";
    die();
}
chdir 'slushengine';
system "$python_install_cmd $logit";
if ($? != 0){
    print "Failed to install slush Error No: $? \r\n";
    print "Check log.txt";
    die();
}
chdir '..';

#finish install
unlink "log.txt";
print "Slush Install Complete \r\n";
print "Happy Spinning! \r\n"


