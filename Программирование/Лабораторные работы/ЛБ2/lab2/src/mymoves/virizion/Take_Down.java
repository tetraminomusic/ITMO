package mymoves.virizion;

import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.Type;

public class Take_Down extends PhysicalMove {
    public Take_Down(double pow, double acc) {
        super(Type.NORMAL,pow,acc);
    }
    @Override
    protected void applySelfDamage(Pokemon myself, double var2) {
        myself.setMod(Stat.HP, (int)Math.round(var2 / 4)); //  уменьшает хп при использованни данной атаки на четверть
    }

    @Override
    /*
    protected String describe() {
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует атаку " + pieces[pieces.length-1];
    }
     */
    protected String describe() {
        return "использует Take Down";
    }
}
