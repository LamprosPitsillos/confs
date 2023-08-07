# Edit this configuration file to define what should be installed on
# your system.  Help is available in the configuration.nix(5) man page
# and in the NixOS manual (accessible by running `nixos-help`).

{ config, pkgs, ... }:

{

    nixpkgs.config.allowUnfree = true;
    imports =
        [ # Include the results of the hardware scan.
        ./hardware-configuration.nix
        ];
# programs.home-manager.enable = true;
 nix.settings.experimental-features = [ "nix-command" "flakes" ];
documentation.man.generateCaches = true;
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
    i18n = {
        defaultLocale = "en_US.UTF-8";
        supportedLocales = [
            "en_US.UTF-8/UTF-8"
            "el_GR.UTF-8/UTF-8"
        ];
    };

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
    # services.xserver.displayManager.lightdm.greeters.gtk.enable =true;
    services.xserver.displayManager.sddm.enable = true;
    services.xserver.displayManager.sddm.autoNumlock = true;
    services.xserver.xkbOptions = "caps:escape";
    services.xserver.windowManager.qtile.enable = true;

    programs.hyprland ={
enable = true;
nvidiaPatches = true;
xwayland.enable = true;
    };

# Enable CUPS to print documents.
# services.printing.enable = true;

# Enable sound.
    # sound.enable = true;
    # hardware.pulseaudio.enable = true;

security.rtkit.enable = true;
services.pipewire = {
  enable = true;
  alsa.enable = true;
  alsa.support32Bit = true;
  pulse.enable = true;
  # If you want to use JACK applications, uncomment this
  #jack.enable = true;
};

hardware = {
    opengl.enable=true;
    nvidia.modesetting.enable=true;

};
# Enable touchpad support (enabled default in most desktopManager).
    services.xserver.libinput.enable = true;
 nixpkgs.overlays = [
    (final: prev: { qutebrowser = prev.qutebrowser.override { enableWideVine = true; }; })
  ];
# Define a user account. Don't forget to set a password with ‘passwd’.
    users.users.inferno = {
        isNormalUser = true;
        extraGroups = [ "wheel" ]; # Enable ‘sudo’ for the user.

  packages =  with pkgs; [
# libreoffice
# thunderbird
  (writeShellApplication {
  name = "dmenu";

  runtimeInputs = [ rofi ];

  text = ''
      rofi -dmenu -i "$@"
  '';
})
libsForQt5.qtstyleplugins
graphite-cursors
ripdrag
xfce.thunar
nsxiv
 tectonic
texlab
lxappearance
                nil
                qutebrowser
                tldr
                neofetch
                exa
                rofi
                fd
                zathura
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
vimix-gtk-themes
vimix-icon-theme
    ripgrep
    hyprland
            qt5ct
            fzf
            xsel
            xdragon
xcb-util-cursor
            neovim
            gnumake
            xdg-user-dirs
            git
            qtile
            kitty
            vifm
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
programs.zsh.enable = true;
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
    system.stateVersion = "23.11"; # Did you read the comment?



}
