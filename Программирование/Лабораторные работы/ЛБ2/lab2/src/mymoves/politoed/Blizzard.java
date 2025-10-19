package mymoves.politoed;

import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;

public class Blizzard extends SpecialMove {
    public Blizzard(double pow, double acc) {
        super(Type.ICE,pow,acc);
    }

    @Override
    //Blizzard deals damage and has a 10% chance of freezing the target.
    protected void applyOppEffects(Pokemon opp) {
        if (Math.random() <= 0.1) {
            Effect.freeze(opp);
        }
    }
//    protected String describe() {
//        String[] pieces = this.getClass().toString().split("\\.");
//        return "использует атаку " + pieces[pieces.length-1];
//    }
    protected String describe() {
    return "использует Blizzard";
}
}
