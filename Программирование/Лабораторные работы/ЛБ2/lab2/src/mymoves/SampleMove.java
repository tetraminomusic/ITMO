package mymoves;

import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Type;

public class SampleMove extends PhysicalMove {
    public SampleMove(double pow, double acc) {
        super(Type.NORMAL,pow,acc);
    }

    @Override
    protected String describe() {
        // class.pokemon.SampleMove
        // Берём последний и делаем какую-то атаку
        String[] pieces = this.getClass().toString().split("\\.");
        return "использует атаку " + pieces[pieces.length-1];
    }
}
