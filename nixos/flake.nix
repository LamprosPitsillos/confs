{
  description = "NixOS Config flake";
inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-23.05";
    # nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    # xremap-flake.url = "github:xremap/nix-flake";
};
  outputs = {  nixpkgs, ... } @inputs: 
      let 
      system = "x86_64-linux";
      pkgs = import nixpkgs {
          inherit system;
      };

      in
      {
          nixosConfigurations = {
              inferno = nixpkgs.lib.nixosSystem {
                  specialArgs = {
                      inherit system;
                      inherit inputs;
                      };
                  modules = [
                  ./configuration.nix
                  ];
              };
          };


  };
}
