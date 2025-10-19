package mymoves.virizion;

import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;

public class X_Scissor extends SpecialMove {
    public X_Scissor(double pow, double acc) {
        super(Type.BUG,pow,acc);
    }

    @Override
    /*
    protected String describe() {
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует атаку " + pieces[pieces.length - 1];
    }
     */
    protected String describe() {
        return "использует X-Scissor";
    }

}
