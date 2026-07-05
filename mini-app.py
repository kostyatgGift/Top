<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>TeamTop Leaderboard</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <style>
        /* Отключаем выделение текста для ощущения нативного приложения */
        * {
            user-select: none;
            -webkit-tap-highlight-color: transparent;
        }
        
        /* Сложный дизайнерский фон с глубокими неоновыми переливами */
        body {
            background-color: #080810;
            background-image: 
                radial-gradient(at 0% 0%, rgba(139, 92, 246, 0.15) 0px, transparent 55%),
                radial-gradient(at 100% 0%, rgba(236, 72, 153, 0.15) 0px, transparent 55%),
                radial-gradient(at 50% 100%, rgba(20, 184, 166, 0.1) 0px, transparent 60%);
            background-attachment: fixed;
        }

        /* Премиальный эффект матового стекла (Glassmorphism) */
        .glass-card {
            background: rgba(22, 22, 43, 0.7);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.06);
        }

        .neon-text-glow {
            text-shadow: 0 0 20px rgba(168, 85, 247, 0.5);
        }
    </style>
</head>
<body class="text-gray-100 font-sans min-h-screen p-4 flex flex-col items-center justify-start antialiased selection:bg-purple-500/30">

    <div class="text-center my-7 animate-fade-in">
        <div class="inline-block bg-purple-500/10 border border-purple-500/20 px-3 py-1 rounded-full text-[10px] font-black tracking-widest text-purple-400 uppercase mb-3">
            ⚡ SPEED MONITOR ⚡
        </div>
        <h1 class="text-4xl font-black bg-gradient-to-r from-white via-slate-200 to-gray-400 bg-clip-text text-transparent uppercase tracking-wider font-mono">
            TEAM<span class="bg-gradient-to-r from-purple-400 to-pink-500 bg-clip-text text-transparent neon-text-glow">TOP</span>
        </h1>
        <p class="text-gray-400 text-xs mt-1.5 tracking-wide font-medium opacity-80">Глобальный рейтинг отклика ботов</p>
    </div>

    <div class="w-full max-w-md glass-card rounded-3xl p-5 shadow-2xl shadow-black/40">
        
        <div class="flex justify-between items-center mb-5 border-b border-white/5 pb-4">
            <div class="flex flex-col">
                <h2 class="text-xs font-black uppercase tracking-widest text-slate-400">Рейтинг Лидеров</h2>
                <span class="text-[10px] text-gray-500 font-medium mt-0.5">Меньше ms — выше позиция</span>
            </div>
            <div class="flex items-center gap-1.5 bg-emerald-500/10 border border-emerald-500/20 px-2.5 py-1 rounded-full">
                <span class="w-1.5 h-1.5 bg-emerald-400 rounded-full animate-ping"></span>
                <span class="text-[9px] text-emerald-400 font-black tracking-widest font-mono">LIVE</span>
            </div>
        </div>
        
        <div class="space-y-3" id="topContainer">
            <div class="text-center py-8 text-gray-500 text-sm">
                ⏳ Загрузка результатов...
            </div>
        </div>
        
        <div class="mt-6 pt-4 border-t border-white/5 flex items-center justify-center gap-2 text-center text-slate-500 text-[11px] font-medium opacity-70">
            <span>🤖 Добавить бота: отправь юзернейм в чат TeamTop</span>
        </div>
    </div>

    <script>
        function renderGlobalTop() {
            const container = document.getElementById('topContainer');
            const urlParams = new URLSearchParams(window.location.search);
            const topDataRaw = urlParams.get('top');
            
            let bots = [];
            
            if (topDataRaw) {
                try {
                    bots = JSON.parse(decodeURIComponent(topDataRaw));
                } catch (e) {
                    console.error("Ошибка парсинга:", e);
                }
            }

            if (bots.length === 0) {
                container.innerHTML = `
                    <div class="text-center py-10 text-slate-500 text-sm font-medium bg-white/2 rounded-2xl border border-white/5">
                        <span class="text-2xl block mb-2">📭</span>
                        Таблица пуста.<br>Отправь первого бота в наш чат!
                    </div>
                `;
                return;
            }

            container.innerHTML = "";

            bots.forEach((bot, index) => {
                let badge = `${index + 1}`;
                let rowStyle = "border-white/5 bg-white/2 hover:bg-white/5";
                let pingStyle = "text-emerald-400 bg-emerald-500/10 border-emerald-500/10";
                let nameStyle = "text-slate-200";
                
                // Премиальные стили для ТОП-3 мест
                if (index === 0) {
                    badge = "🥇";
                    rowStyle = "border-amber-500/20 bg-gradient-to-r from-amber-500/10 to-transparent shadow-lg shadow-amber-500/5";
                    pingStyle = "text-amber-400 bg-amber-500/20 border-amber-500/30 font-black";
                    nameStyle = "text-amber-100 font-extrabold";
                } else if (index === 1) {
                    badge = "🥈";
                    rowStyle = "border-slate-400/20 bg-gradient-to-r from-slate-400/10 to-transparent";
                    pingStyle = "text-slate-300 bg-slate-400/20 border-slate-400/30 font-bold";
                    nameStyle = "text-slate-100 font-bold";
                } else if (index === 2) {
                    badge = "🥉";
                    rowStyle = "border-orange-600/20 bg-gradient-to-r from-orange-600/10 to-transparent";
                    pingStyle = "text-orange-400 bg-orange-600/20 border-orange-600/30 font-bold";
                    nameStyle = "text-orange-100 font-bold";
                }

                container.innerHTML += `
                    <div class="flex justify-between items-center p-3 rounded-2xl border ${rowStyle} transition-all duration-300 transform active:scale-[0.99]">
                        <div class="flex items-center gap-3">
                            <span class="w-6 text-center text-xs font-black font-mono text-slate-400">${badge}</span>
                            <div class="flex flex-col">
                                <span class="font-bold text-sm ${nameStyle}">
                                    <span class="text-purple-400/70 font-medium">@</span>${bot.username}
                                </span>
                            </div>
                        </div>
                        <div class="font-mono text-xs px-2.5 py-1 rounded-xl border ${pingStyle}">
                            ${bot.ping} ms
                        </div>
                    </div>
                `;
            });
        }

        renderGlobalTop();
    </script>
</body>
</html>
