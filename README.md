# nlpreader

This is a speedreader terminal utility for linux that incorporates part-of-speech (only supports english texts).
You can customize its colors, default parameters and keybindings (vim-like defaults).

## Installation

To install `nlpreader` you can run the following commands in a terminal:

```sh
git clone https://github.com/juselara1/nlpreader.git
cd nlpreader
pip install .
```

You can create an alias for `nlpreader`.

1. You must copy the main file to your home:

    ```sh
    mkdir ~/.nlpreader
    cp main.py ~/.nlpreader
    ```

2. Edit your `.bashrc` or `.zshrc` (`nano ~/.bashrc` or `nano ~/.zshrc`), append the following line:

    ```sh
    alias nlpreader="python /home/$USER/.nlpreader/main.py"
    ```

3. Source your rc file:

    ```sh
    cd ~
    source .bashrc
    ```

## Usage

`nlpreader` has two operation modes.

1. You can copy any text, when you execute `nlpreader` without arguments, it will read your clipboard and prompt the words into the terminal.
    
    ![example1](https://github.com/juselara1/Resources/blob/master/nlpreader/ex2.gif?raw=true)

2. You can pass a text as an argument:

    ```sh
    nlpreader --text "hi, this is a sample text."
    ```

    ![example2](https://github.com/juselara1/Resources/blob/master/nlpreader/ex1.gif?raw=true)

## Keybindings

The default keybindings are shown in the following table (you must press `return` or `enter`) after a command:

<div style="width: 100%; text-align: center;">

|key|action|
|---|---|
|`l`|Go to next word, can use multipliers (e.g., `2l` `3l` `10l`) to navigate through multiple words.|
|`h`|Go to previous word, can use multipliers (e.g., `2h` `3h` `10h`) to navigate through multiple words.|
|`j`|Decrease the words per minute (WPM) by 8 units, can use multipliers (e.g., `2j` `3j` `10j`) to modify the magnitude.|
|`k`|Increase the words per minute (WPM) by 8 units, can use multipliers (e.g., `2j` `3j` `10j`) to modify the magnitude.| 
|`g`|Moves to a given word (goes to the first word by default), can use a word index (e.g., `10g` `100g` `53g`)|
|`p`|Pauses the reading.|
|`q`|Closes `nlpreader`.|

</div>

## Configuration

The default configs can be found in `~/.config/nlpreader`, you will find the `colors.json`, `bindings.json`, `defaults.json` (you must execute `nlpreader` once to generate the default files).
