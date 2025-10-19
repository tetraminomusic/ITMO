package mymoves.poliwhirl;

import ru.ifmo.se.pokemon.*;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;

public class Bubble extends SpecialMove {
    public Bubble(double pow, double acc) {
        super(Type.WATER,pow,acc);
    }
    @Override

    //Bubble deals damage and has a 10% chance of lowering the target's Speed by one stage.

    protected void applyOppEffects(Pokemon opp) {
        if (Math.random() <= 0.1) {
            opp.setMod(Stat.SPEED, -1);
        }
    }

    @Override
    /*
    protected String describe() {
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует атаку " + pieces[pieces.length-1];
    }
     */
    protected String describe() {
        return "использует Bubble";
    }
}
