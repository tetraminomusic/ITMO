package mymoves.cranidos;

import ru.ifmo.se.pokemon.*;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

public class Rest extends StatusMove {
    public Rest(double pow, double acc) {
        super(Type.PSYCHIC,pow,acc);
    }

    @Override

    //User sleeps for 2 turns, but user is fully healed.
    protected void applySelfEffects(Pokemon myself) {
        myself.setMod(Stat.HP, -((int)myself.getHP()) + (int)myself.getStat(Stat.HP));
        Effect e = new Effect().condition(Status.SLEEP).turns(2);
        myself.addEffect(e);
    }

    @Override
//    protected String describe() {
//        String[] pieces = this.getClass().toString().split("\\.");
//        return "использует атаку " + pieces[pieces.length-1];
//    }
    protected String describe() {
        return "использует Rest";
    }
}
