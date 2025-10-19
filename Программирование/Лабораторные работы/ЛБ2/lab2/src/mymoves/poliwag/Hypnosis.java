package mymoves.poliwag;
import ru.ifmo.se.pokemon.*;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

public class Hypnosis extends StatusMove {
    public Hypnosis(double pow, double acc) {
        super(Type.PSYCHIC,pow,acc);
    }

    @Override

    //отправляем оппонента спать
    protected void applyOppEffects(Pokemon opp) {
        Effect.sleep(opp);
    }

    @Override
    /*
    protected String describe() {
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует атаку " + pieces[pieces.length-1];
    }
     */
    protected String describe() {
        return "использует Hypnosis";
    }
}
