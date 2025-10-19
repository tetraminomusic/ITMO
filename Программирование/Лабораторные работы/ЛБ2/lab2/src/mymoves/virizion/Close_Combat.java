package mymoves.virizion;

import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.Type;

public class Close_Combat extends PhysicalMove {
    public Close_Combat(double pow, double acc) {
        super(Type.FIGHTING,pow,acc);
    }


    // эффект атаки, снижение защиты и специальной защиты на 1 с каждой атакой
    @Override
    protected void applySelfEffects(Pokemon myself) {
        myself.setMod(Stat.DEFENSE, -1);
        myself.setMod(Stat.SPECIAL_DEFENSE, -1);
    }

    @Override
    /*
    protected String describe() {
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует атаку " + pieces[pieces.length-1];
    }
     */
    protected String describe() {
        return "использует Close Combat";
    }
}
