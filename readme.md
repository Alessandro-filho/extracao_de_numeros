# Extração de Números de Telefone de Imagens

Este projeto é uma aplicação web simples construída com Flask, que utiliza OCR (Reconhecimento Óptico de Caracteres) para extrair números com padrão brasileiro de imagens. Utilizando a biblioteca pytesseract como interface para o Tesseract-OCR, o software de OCR mais popular e preciso disponível, este projeto simplifica a tarefa de digitalizar grandes quantidades de imagens para encontrar e catalogar números de telefone contidos nelas.

## Requisitos

Para executar este projeto, você precisará dos seguintes componentes instalados:

- Python 3.x
- Flask
- Pillow
- pytesseract
- Tesseract-OCR

## Instalação

Siga estes passos para configurar o projeto em seu ambiente local.

### Clonar o Repositório

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/Alessandro-filho/extracao_de_numeros.git
cd extracao_de_numeros
```

## Configurar o Ambiente Virtual
Crie e ative um ambiente virtual para isolar as dependências do projeto

```python -m venv venv```
### No Windows
```.\venv\Scripts\activate```
### No Unix ou MacOS
```source venv/bin/activate```

## Instalar Dependências

```pip install --upgrade pip setuptools wheel```

```pip install -r requirements.txt```

## Uso
Para iniciar a aplicação, execute

```python app.py```
