package menu_ui;

import asciiPictures.IntroHeadersPictures;
import muzlo_vidosi.Music;
import interfaces.clearConsoleSpace;

public class StartupAnimation implements clearConsoleSpace {

    IntroHeadersPictures introHeaders = new IntroHeadersPictures();
    Music intro = new Music("unitaz.mp3", false);

    // Делаем задержки константами - это красиво и удобно для изменения
    private final int LINE_DELAY = 130;
    private final int LOGO_DELAY = 2300;
    private final int TITLE_DELAY = 4000;

    public void showStartupAnimation() {
        try {
            // Запускаем всё по порядку - чисто и понятно
            playIntroSound();
            showStudioLogo();
            showGameTitle();
            
        } catch (InterruptedException e) {
            // Аккуратно обрабатываем прерывание
            Thread.currentThread().interrupt();
        }
    }

    private void playIntroSound() {
        intro.playSound();
    }

    private void showStudioLogo() throws InterruptedException {
        // Очищаем и показываем логотип построчно
        clearConsoleSpace.clearConsole();
        
        String[] logoLines = introHeaders.GetStudioHeader();
        for (String line : logoLines) {
            System.out.println(line);
            Thread.sleep(LINE_DELAY); // Плавное появление
        }
        
        // Даём время насладиться логотипом
        Thread.sleep(LOGO_DELAY);
    }

    private void showGameTitle() throws InterruptedException {
        // Переход к заголовку игры
        clearConsoleSpace.clearConsole();
        
        String gameTitle = introHeaders.GetFunchozaHeader();
        System.out.println(gameTitle);
        
        // Ждём перед завершением анимации
        Thread.sleep(TITLE_DELAY);
        clearConsoleSpace.clearConsole();
    }
}
