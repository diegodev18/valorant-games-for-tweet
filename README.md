# Valorant Games for Tweet

> Este es un script basico que te permite obtener los juegos de valorant competitivo y publicarlos de manera automatica a twitter.

## Instalacion y configuracion

### 1. Clona el repositorio
```bash	
git clone https://github.com/diego-dev018/ValorantGamesForTweet
```

### 2. Entra en el repositorio
```bash
cd ValorantGamesForTweet
```

### 3. Obten tus credenciales de twitter en [developer.twitter.com](https://developer.twitter.com/)

### 4. Selecciona los torneos que quieres publicar en X

#### - Abre el archivo `tournament.txt`
#### - Escribe el nombre del torneo que quieres publicar

### 5. Inicia el script

#### Windows
```cmd
py init.py
```

#### Linux
```bash
python3 init.py
```

### Docker
> El dockerfile ya esta configurado para ejecutar el script, solo necesitas construir la imagen y ejecutar el contenedor, sigue las instrucciones.

#### 1. Construye la imagen
```bash
docker build -t valorant-games-for-tweet .
```

#### 2. Ejecuta el contenedor
```bash
docker run valorant-games-for-tweet
```

## Uso

> El script se ejecutara a la hora que asignes en el script, y subira un tweet a tu cuenta de X con los juegos de valorant competitivo que selecciones.