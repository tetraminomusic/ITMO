package mypokemons;

import mymoves.cranidos.Rest;
import mymoves.cranidos.Stone_Edge;
import mymoves.cranidos.Sword_Dance;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Cranidos extends Pokemon {
    public Cranidos(String name, int level) {
        super(name, level); //надкласс сам определит, какой это покемон и уровень (инициализация)

        super.setType(Type.ROCK, Type.FIGHTING);
        super.setStats(67, 125, 40, 30, 30, 58);

        //пишем атаки
        Rest rest = new Rest(0,0);
        Stone_Edge stoneEdge = new Stone_Edge(100,80);
        Sword_Dance swordDance = new Sword_Dance(0,0);

        super.setMove(rest,stoneEdge, swordDance);

    }
}
