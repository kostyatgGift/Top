<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bot Ping Tester & TOP</title>
    <!-- Подключаем Tailwind CSS для крутого стиля -->
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <style>
        body {
            background: radial-gradient(circle at center, #1a1a2e 0%, #0f0f1a 100%);
        }
        .neon-border {
            box-shadow: 0 0 15px rgba(168, 85, 247, 0.4);
        }
    </style>
</head>
<body class="text-gray-100 font-sans min-h-screen p-4 flex flex-col items-center">

    <!-- Заголовок -->
    <div class="text-center my-6">
        <h1 class="text-3xl font-extrabold bg-gradient-to-r from-purple-400 to-pink-500 bg-clip-text text-transparent uppercase tracking-wider">
            ⚡ Bot Ping Monitor
        </h1>
        <p class="text-gray-400 text-sm mt-1">Узнай задержку бота и попади в мировой ТОП</p>
    </div>

    <!-- Форма проверки бота -->
    <div class="w-full max-w-md bg-[#16162a]/80 border border-purple-500/30 rounded-2xl p-5 mb-6 neon-border backdrop-blur-md">
        <h2 class="text-lg font-semibold mb-3 text-purple-300">Проверить скорость бота</h2>
        <div class="flex gap-2">
            <span class="flex items-center pl-3 text-gray-500 font-bold bg-[#0f0f1a] rounded-l-xl border-y border-l border-gray-700">@</span>
            <input id="botUsername" type="text" placeholder="username_bot" 
                   class="w-full bg-[#0f0f1a] p-3 pl-1 border-y border-r border-gray-700 rounded-r-xl focus:outline-none focus:border-purple-500 transition text-white">
        </div>
        <button onclick="checkBotPing()" 
                class="w-full mt-4 bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 font-bold p-3 rounded-xl transition transform active:scale-95 cursor-pointer shadow-lg shadow-purple-500/20">
            Запустить тест 🔥
        </button>
        <!-- Результат теста (скрыт по умолчанию) -->
        <div id="resultBlock" class="hidden mt-4 p-3 bg-green-500/10 border border-green-500/30 rounded-xl text-center">
            <p class="text-gray-300">Результат <span id="checkedBotName" class="text-white font-bold"></span>:</p>
            <p class="text-2xl font-black text-green-400 mt-1"><span id="pingValue">0</span> ms</p>
        </div>
    </div>

    <!-- ТАБЛИЦА ЛИДЕРОВ (ТОП БОТОВ) -->
    <div class="w-full max-w-md bg-[#16162a]/80 border border-gray-800 rounded-2xl p-5 backdrop-blur-md">
        <h2 class="text-lg font-bold mb-4 text-pink-400 flex items-center gap-2">
            🏆 ТОП-5 Самых быстрых ботов
        </h2>
        <div class="space-y-3" id="topList">
            <!-- Сюда данные будут грузиться из API -->
            <div class="flex justify-between items-center bg-[#0f0f1a] p-3 rounded-xl border border-gray-800">
                <span class="font-medium text-gray-400">📊 Загрузка топа...</span>
            </div>
        </div>
    </div>

    <!-- Скрипт для связи с твоим Render API -->
    <script>
        // Замени на URL своего бэкенда на Render, когда обновишь его
        const BACKEND_URL = "https://ai-api-sonq.onrender.com"; 

        // Функция получения ТОПа при загрузке страницы
        async function loadTop() {
            try {
                const res = await fetch(`${BACKEND_URL}/v1/top`);
                const data = await res.json();
                const container = document.getElementById('topList');
                container.innerHTML = "";
                
                data.bots.forEach((bot, index) => {
                    let medal = index === 0 ? "🥇" : index === 1 ? "🥈" : index === 2 ? "🥉" : `${index + 1}.`;
                    container.innerHTML += `
                        <div class="flex justify-between items-center bg-[#0f0f1a] p-3 rounded-xl border border-gray-800 hover:border-purple-500/30 transition">
                            <span class="font-medium text-white">${medal} @${bot.username}</span>
                            <span class="font-bold text-green-400">${bot.ping} ms</span>
                        </div>
                    `;
                });
            } catch (e) {
                console.error("Ошибка загрузки ТОПа", e);
            }
        }

        // Функция отправки бота на проверку пинга
        async function checkBotPing() {
            const username = document.getElementById('botUsername').value.trim().replace('@', '');
            if(!username) return alert('Введите юзернейм бота!');

            // Показываем анимацию загрузки
            document.getElementById('resultBlock').classList.remove('hidden');
            document.getElementById('checkedBotName').innerText = `@${username}`;
            document.getElementById('pingValue').innerText = "Тестируем...";

            try {
                const res = await fetch(`${BACKEND_URL}/v1/ping`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ username: username })
                });
                const data = await res.json();
                
                // Выводим результат
                document.getElementById('pingValue').innerText = data.ping;
                loadTop(); // Обновляем ТОП
            } catch (e) {
                document.getElementById('pingValue').innerText = "Ошибка сервера";
            }
        }

        // Загружаем ТОП при открытии сайта
        loadTop();
    </script>
</body>
</html>
