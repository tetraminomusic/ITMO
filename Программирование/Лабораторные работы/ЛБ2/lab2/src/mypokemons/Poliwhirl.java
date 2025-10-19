package mypokemons;

import mymoves.poliwhirl.Bubble;

public class Poliwhirl extends Poliwag{
    public Poliwhirl(String name, int level) {
        super(name, level);

        super.setStats(65, 65, 65, 50, 50, 90);

        Bubble bubble = new Bubble(40,100);

        //добавляем недостающие атаки
        super.addMove(bubble);
    }
}
