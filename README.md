# CustomTkinter Themes
A simple Custom theme manager for customtkinter with themes created and sourced



# How To Use
Install via PyPi
```commandline
pip3 install CustomTkinterThemes
```
Import it
```python
from customtkinterthemes import theme_manager
```
Use it
```python
set_default_color_theme(theme_manager.get("themename"))
```
Note: If it shows that some fonts needs to be installed, go ahead and follow the instructions 

# Methods

`.get(theme_name: str) -> Path:`

Returns the path to the theme JSON file.

`.get_all_themes() -> list[str]:`

Returns a list of theme names.

`.get_font_path():`

Returns font directory

`.validate_theme_fonts():`

Checks if all fonts are installed and prints a warning message if not.

***

Themes sourced from
- https://github.com/a13xe/CTkThemesPack [midnight, rose, metal, cherry, lavender, red, rime, breeze, coffee, orange, blue, yellow, marsh, patina, pink, autumn, sky, carrot, violet] (Unlicense LICENSE)
- Original [flipperzero, hacked, extreme, orangish] (MIT LICENSE)

### Want to add your theme?
Submit an issue with your theme and screenshots. Professional ones will be added with credits!!!

***
# Themes



## FlipperZero

<div align="center">
  <img width=99% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/flipperzero.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("flipperzero"))
```

***
## Hacked

<div align="center">
  <img width=99% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/hacked.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("hacked"))
```
***

## Extreme

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/extreme-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/extreme-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("extreme"))
```

***

## Orangish

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/orangish-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/orangish-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("orangish"))
```

***

## Breeze

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/breeze-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/breeze-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("breeze"))
```

***

## Coffee

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/coffee-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/coffee-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("coffee"))
```
***

## Orange

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/orange-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/orange-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("orange"))
```

***

## Midnight

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/midnight-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/midnight-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("midnight"))
```

***

## Violet

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/violet-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/violet-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("violet"))
```

***

## Autumn

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/autumn-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/autumn-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("autumn"))
```

***

## Metal

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/metal-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/metal-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("metal"))
```

***

## Cherry

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/cherry-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/cherry-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("cherry"))
```

***

## Red

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/red-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/red-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("red"))
```
***

## Patina

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/patina-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/patina-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("patina"))
```
***

## Yellow

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/yellow-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/yellow-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("yellow"))
```
***

## Marsh

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/marsh-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/marsh-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("marsh"))
```
***

## Rose

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/rose-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/rose-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("rose"))
```
***

## Pink

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/pink-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/pink-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("pink"))
```

***

## Lavender

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/lavender-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/lavender-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("lavender"))
```

***

## Carrot

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/carrot-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/carrot-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("carrot"))
```

***

## Rime

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/rime-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/rime-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("rime"))
```

***

## Sky

<div align="center">
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/sky-light.png?raw=true"/> 
  <img width=49% src="https://github.com/rigvedmaanas/CustomTkinterThemes/blob/main/src/customtkinterthemes/images/sky-dark.png?raw=true"/> 
</div>

```python
set_default_color_theme(theme_manager.get("sky"))
```



