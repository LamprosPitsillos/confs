# Edit this configuration file to define what should be installed on
# your system.  Help is available in the configuration.nix(5) man page
# and in the NixOS manual (accessible by running `nixos-help`).

{ config, pkgs, ... }:

{
    imports =
        [ # Include the results of the hardware scan.
        ./hardware-configuration.nix
        ];
# programs.home-manager.enable = true;

# Use the GRUB 2 boot loader.
    boot.loader.grub.enable = true;
# boot.loader.grub.efiSupport = true;
# boot.loader.grub.efiInstallAsRemovable = true;
# boot.loader.efi.efiSysMountPoint = "/boot/efi";
# Define on which hard drive you want to install Grub.
    boot.loader.grub.device = "/dev/sda"; # or "nodev" for efi only

        networking.hostName = "infernoPC"; # Define your hostname.
# Pick only one of the below networking options.
# networking.wireless.enable = true;  # Enables wireless support via wpa_supplicant.
        networking.networkmanager.enable = true;  # Easiest to use and most distros use this by default.

# Set your time zone.
        time.timeZone = "Europe/Athens";

# Configure network proxy if necessary
# networking.proxy.default = "http://user:password@proxy:port/";
# networking.proxy.noProxy = "127.0.0.1,localhost,internal.domain";

# Select internationalisation properties.
# i18n.defaultLocale = "en_US.UTF-8";
# console = {
#   font = "Lat2-Terminus16";
#   keyMap = "us";
#   useXkbConfig = true; # use xkbOptions in tty.
# };

# Enable the X11 windowing system.
    services.xserver.enable = true;

    environment.sessionVariables = {
        XDG_CACHE_HOME  = "$HOME/.cache";
        XDG_CONFIG_HOME = "$HOME/.config";
        XDG_DATA_HOME   = "$HOME/.local/share";
        XDG_STATE_HOME  = "$HOME/.local/state";
        ZDOTDIR         = "$HOME/.config/zsh";
        HISTFILE        = "$HOME/.config/zsh/.zsh_history";
        EDITOR          = "nvim";
        VISUAL          = "nvim";
        MANPAGER        = "nvim -c \"map q :quit<cr>\" +Man!";
    };



# Configure keymap in X11
    services.xserver.layout = "us";
    services.xserver.xkbOptions = "eurosign:e,caps:escape";
    services.xserver.windowManager.qtile.enable = true;

# Enable CUPS to print documents.
# services.printing.enable = true;

# Enable sound.
    sound.enable = true;
    hardware.pulseaudio.enable = true;

# Enable touchpad support (enabled default in most desktopManager).
    services.xserver.libinput.enable = true;

# Define a user account. Don't forget to set a password with ‘passwd’.
    users.users.inferno = {
        isNormalUser = true;
        extraGroups = [ "wheel" ]; # Enable ‘sudo’ for the user.
            packages = with pkgs; [
                nil
                qutebrowser
                tldr
                neofetch
            ];
    };

    qt = {
        enable = true;
        platformTheme = "qt5ct";
    };
    xdg.mime = {
        enable = true;
        defaultApplications = {

        };
    };
# List packages installed in system profile. To search, run:

# $ nix search wget
    environment.systemPackages = with pkgs; [
            home-manager
            qt5ct
            fzf
            xsel
            neovim
            gnumake
            xdg-user-dirs
            git
            qtile
            kitty
            vifm
            zsh
            zoxide
            clang
            gcc
            starship
    ];

# Some programs need SUID wrappers, can be configured further or are
# started in user sessions.
    programs.mtr.enable = true;
    programs.gnupg.agent = {
        enable = true;
        enableSSHSupport = true;
    };

# List services that you want to enable:

# Enable the OpenSSH daemon.
    services.openssh.enable = true;

    fonts = {
        fonts = with pkgs; [
            (nerdfonts.override {fonts = ["FiraCode"];}) 
        ];
    };
    programs.zsh= {
        enable = true ;
#   plugins = [ 
#
#   {
#  name = "fast-syntax-highlighting";
#  src = pkgs.fetchFromGitHub {
#    owner = "zdharma-continuum";
#    repo = "fast-syntax-highlighting";
#    rev = "cf318e0";
#    sha256 = "cf318e06a9b7c9f2219d78f41b46fa6e06011fd9" ;
#    };
# }
#   {
#  name = "fzf-zsh-plugin";
#  src = pkgs.fetchFromGitHub {
#    owner = "unixorn";
#    repo = "fzf-zsh-plugin";
#    rev = "5b07fb1";
#    sha256 = "5b07fb15e5be8a2fa7e1783aa80e4b7609772d63" ;
#  };
# }
#   ];
    };
    users.defaultUserShell = pkgs.zsh;
# Open ports in the firewall.
# networking.firewall.allowedTCPPorts = [ ... ];
# networking.firewall.allowedUDPPorts = [ ... ];
# Or disable the firewall altogether.
# networking.firewall.enable = false;

# Copy the NixOS configuration file and link it from the resulting system
# (/run/current-system/configuration.nix). This is useful in case you
# accidentally delete configuration.nix.
    system.copySystemConfiguration = true;

# This value determines the NixOS release from which the default
# settings for stateful data, like file locations and database versions
# on your system were taken. It's perfectly fine and recommended to leave
# this value at the release version of the first install of this system.
# Before changing this value read the documentation for this option
# (e.g. man configuration.nix or on https://nixos.org/nixos/options.html).
    system.stateVersion = "23.05"; # Did you read the comment?



}

