#!/usr/bin/perl 
use strict;
use warnings;
use autodie;

# declare all required packages
my $packages = "python3 python3-setuptools python3-pip git";
my $pip_packages = "spidev inputs";

# git repos to install
my $slush_repo = qw(https://github.com/Roboteurs/slushengine); 
my $quick2wire_repo = qw(https://github.com/quick2wire/quick2wire-python-api);

# system commands
my $apt_install_cmd="sudo apt-get install $packages";
my $pip_install_cmd="sudo pip install $pip_packages";
my $git_clone_cmd = "git clone ";
my $python_install_cmd = "sudo python3 setup.py install";
my $logit = "1>>log.txt 2>&1";


# install required packages with apt
open(my $outfile, '>', 'log.txt');
print "Installing required build packages \r\n";
system "$apt_install_cmd $logit";
if ($? != 0){
    print "Aptitude failed to install packages Error No: $? \r\n";
    print "Check log.txt";
    die();
}

# install pip packages
print "Installing pip packages \r\n";
system "$pip_install_cmd $logit";
if ($? != 0){
    print "Failed to install pip packages Error No: $? \r\n";
    print "Check log.txt";
    die();
}

# install quicktowire
print "Cloning and setting up quick2wire \r\n";
system "$git_clone_cmd $quick2wire_repo $logit";
if ($? != 0){
    print "Failed to clone quick2wire Error No: $? Does directory already exist? \r\n";
    print "Check log.txt";
    die();
}
chdir 'quick2wire-python-api';
system "$python_install_cmd $logit"; 
if ($? != 0){
    print "Failed to install quick2wire Error No: $? \r\n";
    print "Check log.txt";
    die();
}
chdir '..';


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
print "Slush Install Complete";

