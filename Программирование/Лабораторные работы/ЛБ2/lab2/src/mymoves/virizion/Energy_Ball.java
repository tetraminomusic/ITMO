package mymoves.virizion;

import ru.ifmo.se.pokemon.*;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;

public class Energy_Ball extends SpecialMove {
    public Energy_Ball(double pow, double acc) {
        super(Type.GRASS,pow,acc);
    }


    // Energy Ball deals damage and has a 10% chance of lowering the target's Special Defense by one stage.
    @Override
    protected void applyOppEffects(Pokemon opp) {
        if (Math.random() <= 0.1) {
            opp.setMod(Stat.SPECIAL_DEFENSE, -1);
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
        return "использует Energy Ball";
    }
}
