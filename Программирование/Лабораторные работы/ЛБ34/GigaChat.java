package menu_ui;

import asciiPictures.IntroHeadersPictures;
import muzlo_vidosi.Music;
import interfaces.clearConsoleSpace;

public class StartupAnimation implements clearConsoleSpace {

    IntroHeadersPictures introHeaders = new IntroHeadersPictures();
    Music intro = new Music("unitaz.mp3", false);

    public void showStartupAnimation() {
        try {
            // Запускаем саундтрек и очищаем сцену
            intro.playSound();
            clearConsoleSpace.clearConsole();

            // Рисуем логотип студии как искусство
            String[] studioArt = introHeaders.GetStudioHeader();
            for (int i = 0; i < studioArt.length; i++) {
                System.out.println(studioArt[i]);
                // Плавное ускорение анимации
                Thread.sleep(i < 3 ? 150 : 100);
            }

            // Момент истины - любуемся результатом
            Thread.sleep(2300);
            clearConsoleSpace.clearConsole();

            // Главный герой выходит на сцену
            String mainTitle = introHeaders.GetFunchozaHeader();
            System.out.println(mainTitle);
            
            // Финальная пауза перед началом приключения
            Thread.sleep(4000);
            clearConsoleSpace.clearConsole();

        } catch (InterruptedException e) {
            // Экстренное завершение шоу
            Thread.currentThread().interrupt();
            System.out.println("Шоу прервано!");
        }
    }

    // Секретный режим для разработчиков
    void debugAnimation() {
        try {
            clearConsoleSpace.clearConsole();
            System.out.println("=== ДЕБАГ РЕЖИМ ===");
            
            String[] studioArt = introHeaders.GetStudioHeader();
            for (String line : studioArt) {
                System.out.println("▶ " + line);
                Thread.sleep(30);
            }
            
            Thread.sleep(500);
            clearConsoleSpace.clearConsole();
            System.out.println("⚡ " + introHeaders.GetFunchozaHeader());
            Thread.sleep(1000);
            clearConsoleSpace.clearConsole();
            
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
