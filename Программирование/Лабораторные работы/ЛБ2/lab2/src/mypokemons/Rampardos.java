package mypokemons;

import mymoves.rampardos.Focus_Blast;

public class Rampardos extends Cranidos{
    public Rampardos(String name, int level) {
        super(name, level);

        super.setStats(97,165,60,65,50,58);

        Focus_Blast focusBlast = new Focus_Blast(120,70);

        super.addMove(focusBlast);
    }
}
