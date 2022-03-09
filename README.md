# FSH-family-tree
Fallout Shelter visual family tree generator from save file (Linux)

# Dependencies
- npm
- Python 3
- kingraph

To install run:

#### Fedora
    sudo dnf in npm

#### Debian / Ubuntu
    sudo apt install npm

To use `kingraph` you can either rely on the backed up version saved to this repo or use the one from the official repo from [here](https://github.com/AlexanderWillner/kingraph)

# Usage

1. Clone this repo
2. [Decrypt](https://rakion99.github.io/shelter-editor/SaveDecrypt.html) your `.sav` file
   - Usually located at `users/USERNAME/AppData/Local/FalloutShelter/Vault1.sav`
4. Run `python3 gentree.py Vault.json` inside the workdir
5. Generate image with `kingraph`
   - To use the provided version, run `node_modules/kingraph/bin/kingraph dwellerdb.yaml -F dot | dot -Tsvg -o dwellers.svg`
   - To use the official version, you can install it with `npm install -g alexanderwillner/kingraph`

# Example

![](https://github.com/swanux/FSH-family-tree/blob/master/example.svg?raw=true)
