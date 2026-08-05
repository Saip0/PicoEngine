# PicoEngine

Uma engine para Raspberry Pi Pico escrita em MicroPython.

## Sobre

Este projeto tem como objetivo criar uma engine modular para sistemas embarcados, focada em interfaces gráficas e no desenvolvimento de jogos.

Atualmente a engine possui:

- Gerenciamento de estados
- Sistema de navegação
- Renderer
- Sistema de UI
- Input
- Storage

⚠️ O projeto ainda está em desenvolvimento e novas funcionalidades serão adicionadas conforme a evolução da arquitetura.

Este projeto está licenciado sob a GNU General Public License v3.0 (GPL-3.0).

## Autor

**Samuel** (@Saip0)

GitHub: <https://github.com/Saip0>


# Dependencies

Este projeto utiliza algumas bibliotecas e recursos externos. 
Os créditos dos autores originais são mantidos abaixo.

## Fonts

As fontes VGA utilizadas no projeto foram obtidas do repositório:

- **Author:** Russ Hughes
- **Repository:** https://github.com/russhughes/st7789py_mpy
- **Location:** romfonts/

Fontes utilizadas:
- vga8x16
- vga16x16
- vga16x32


## Display Driver

O driver utilizado para o display ILI9341 foi baseado em:

- **Author:** rdagger
- **Repository:** https://github.com/rdagger/micropython-ili9341

O código do driver foi adaptado para este projeto, incluindo modificações e extensões próprias para atender às necessidades da aplicação.
