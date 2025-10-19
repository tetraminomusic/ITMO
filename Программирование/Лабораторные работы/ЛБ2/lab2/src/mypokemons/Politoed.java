package mypokemons;

import mymoves.politoed.Blizzard;

public class Politoed extends Poliwhirl{
    public Politoed(String name, int level) {
        super(name, level);


        super.setStats(90,75,75,90,100,70);

        //добавляем недостающие атаки
        Blizzard blizzard = new Blizzard(110,70);

        super.addMove(blizzard);
    }
}
