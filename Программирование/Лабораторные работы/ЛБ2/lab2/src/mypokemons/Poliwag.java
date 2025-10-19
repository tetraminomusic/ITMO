package mypokemons;

import mymoves.poliwag.Hypnosis;
import mymoves.poliwag.Swagger;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Poliwag extends Pokemon {

    public Poliwag(String name, int level) {
        super(name, level); //надкласс сам определит, какой это покемон и уровень (инициализация)

        super.setType(Type.WATER, Type.FIGHTING);
        super.setStats(40,50,40,40,40,90);

        Hypnosis hypnosis = new Hypnosis(0, 60);
        Swagger swagger = new Swagger(0, 85);

        super.setMove(hypnosis,swagger);

    }
 }
