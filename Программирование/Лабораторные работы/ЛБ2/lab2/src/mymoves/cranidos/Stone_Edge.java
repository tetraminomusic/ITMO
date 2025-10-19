package mymoves.cranidos;

import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Stone_Edge extends PhysicalMove {
    public Stone_Edge(double pow, double acc) {
        super(Type.ROCK,pow,acc);
    }
    // Stone Edge deals damage and has an increased critical hit ratio (1⁄8 instead of 1⁄24).
    protected double calcCriticalHit(Pokemon att, Pokemon def) {
        return (double) 0.125;
    }
    @Override
//    protected String describe() {
//        String[] pieces = this.getClass().toString().split("\\.");
//        return "использует атаку " + pieces[pieces.length-1];
//    }
    protected String describe() {
        return "использует Stone Edge";
    }
}
