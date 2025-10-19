package mymoves.cranidos;

import ru.ifmo.se.pokemon.*;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

public class Sword_Dance extends StatusMove {
    public Sword_Dance(double pow, double acc) {
        super(Type.NORMAL,pow,acc);
    }

    //Swords Dance raises the user's Attack by two stages.
    @Override
    protected void applySelfEffects(Pokemon var1) {
        Effect effect = new Effect().stat(Stat.ATTACK, 2);
        var1.addEffect(effect);
    }

    @Override
//    protected String describe() {
//        String[] pieces = this.getClass().toString().split("\\.");
//        return "использует атаку " + pieces[pieces.length-1];
//    }
    protected String describe() {
        return "использует Sword Dance";
    }
}
