# Vibe-coding-pupsiki-game
Готовый игра для телеграмм
1. Сборка проекта, команда для корневой папки:
   ```
   docker build -t ТВОЙ_НИК_ОТ_DockerHub/pupsiki:latest .
   ```
2. Запуск контейнераb и предворительно создал новый под домен для игры:
   ```
   docker run -d --name pupsiki --restart unless-stopped   -p 15080:15080   -e BOT_TOKEN=87****:AAF*****I   -e GAME_URL=https://game.site.ru/   ТВОЙ_НИК_ОТ_DockerHub/pupsiki:latest
   ```
## Изображение программы
![Image alt](https://raw.githubusercontent.com/Kirill-pixel/Vibe-coding-pupsiki-game/main/images/1.png)