package mypokemons;

import mymoves.virizion.*;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Virizion extends Pokemon {
    public Virizion(String name, int level) {
        super(name, level); //надкласс сам определит, какой это покемон и уровень (инициализация)

        super.setType(Type.GRASS, Type.FIGHTING);
        super.setStats(91,90,72,90,129,108);


        // перечисляем все атаки, которые имеет данный покемон

        X_Scissor xScissor = new X_Scissor(80, 100);
        Take_Down takeDown = new Take_Down(90, 85);
        Energy_Ball energyBall = new Energy_Ball(90, 100);
        Close_Combat closeCombat = new Close_Combat(120, 100);


        super.setMove(xScissor,takeDown, energyBall, closeCombat);


    }
}
