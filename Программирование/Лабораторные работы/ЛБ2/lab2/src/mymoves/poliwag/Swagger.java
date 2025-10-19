package mymoves.poliwag;
import ru.ifmo.se.pokemon.*;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

public class Swagger extends StatusMove {
    public Swagger(double pow, double acc) {
        super(Type.NORMAL,pow,acc);
    }

    @Override

    // конфуз врага
    protected void applyOppEffects(Pokemon opp) {
        super.applyOppEffects(opp);
        Effect.confuse(opp);
    }

    @Override

    // увеличиваем себе силу атаки на 2 единицы
    protected void applySelfEffects(Pokemon myself) {
        Effect effect = new Effect().stat(Stat.ATTACK, 2);
        myself.addEffect(effect);
    }

    @Override
    /*
    protected String describe() {
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует атаку " + pieces[pieces.length-1];
    }
     */
    protected String describe() {
        return "использует Swagger";
    }
}
